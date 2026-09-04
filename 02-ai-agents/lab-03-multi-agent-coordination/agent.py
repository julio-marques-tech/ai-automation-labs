"""Lab 03 - a lead agent that delegates to two specialized subagents:
`work-item-analyst` (reads real Azure DevOps data) and `report-writer`
(drafts a report from data it's given, with no tools of its own).

This is the same delegation pattern Claude Code itself uses with its
own subagents (Explore, general-purpose, Plan, ...) - here we define
our own.
"""

import asyncio
import os

import requests
from dotenv import load_dotenv

from claude_agent_sdk import (
    AgentDefinition,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    create_sdk_mcp_server,
    tool,
)

load_dotenv()

AZURE_DEVOPS_ORG = os.environ["AZURE_DEVOPS_ORG"]
AZURE_DEVOPS_PROJECT = os.environ["AZURE_DEVOPS_PROJECT"]
AZURE_DEVOPS_PAT = os.environ["AZURE_DEVOPS_PAT"]


@tool(
    "get_work_items",
    "Get the current Azure DevOps work items for this project, with id, title, and state",
    {},
)
async def get_work_items(args: dict) -> dict:
    base = f"https://dev.azure.com/{AZURE_DEVOPS_ORG}/{AZURE_DEVOPS_PROJECT}/_apis/wit"
    auth = ("", AZURE_DEVOPS_PAT)

    wiql_resp = requests.post(
        f"{base}/wiql?api-version=7.1",
        auth=auth,
        json={"query": "Select [System.Id] From WorkItems"},
    )
    wiql_resp.raise_for_status()
    ids = [item["id"] for item in wiql_resp.json()["workItems"]]

    if not ids:
        return {"content": [{"type": "text", "text": "No work items found."}]}

    batch_resp = requests.post(
        f"{base}/workitemsbatch?api-version=7.1",
        auth=auth,
        json={"ids": ids, "fields": ["System.Id", "System.Title", "System.State"]},
    )
    batch_resp.raise_for_status()
    items = batch_resp.json()["value"]

    lines = [
        f"#{item['fields']['System.Id']}: {item['fields']['System.Title']} "
        f"({item['fields']['System.State']})"
        for item in items
    ]
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


tools_server = create_sdk_mcp_server(
    name="lab03-tools",
    version="1.0.0",
    tools=[get_work_items],
)

options = ClaudeAgentOptions(
    mcp_servers={"lab03": tools_server},
    allowed_tools=["mcp__lab03__get_work_items"],
    agents={
        "work-item-analyst": AgentDefinition(
            description="Reads Azure DevOps work items and produces a factual summary",
            prompt=(
                "You are a specialist in reading Azure DevOps work item data. "
                "Use the get_work_items tool and produce a clear, factual "
                "summary: total count, and counts by state. No opinions, "
                "no recommendations - just the facts."
            ),
            tools=["mcp__lab03__get_work_items"],
        ),
        "report-writer": AgentDefinition(
            description="Writes a polished status report from data it is given",
            prompt=(
                "You are a specialist in writing clear, professional status "
                "reports in Portuguese. You have no tools - work only from "
                "the information given to you in the prompt. Do not invent "
                "data."
            ),
            tools=[],
        ),
    },
)


async def main():
    async with ClaudeSDKClient(options=options) as client:
        await client.query(
            "Escreve um relatorio de estado do projeto. Delega a recolha "
            "de dados ao work-item-analyst, depois passa esses dados ao "
            "report-writer para redigir o relatorio final. IMPORTANTE: "
            "corre AMBOS os subagentes em primeiro plano (nao uses "
            "background) e mostra-me o relatorio final completo do "
            "report-writer antes de terminares."
        )
        async for message in client.receive_response():
            print(message)


if __name__ == "__main__":
    asyncio.run(main())
