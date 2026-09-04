"""Lab 02 - an agent with two independent tools: one calling real
external data (Azure DevOps work items), one providing a fact the model
genuinely cannot know on its own (the current real-world date/time).

Unlike Lab 01's calculator, neither of these can be reasoned out by the
model - so tool-use decisions here are a more honest test of
orchestration.
"""

import asyncio
import os
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

from claude_agent_sdk import (
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


@tool("get_current_datetime", "Get the current real-world date and time (UTC)", {})
async def get_current_datetime(args: dict) -> dict:
    now = datetime.now(timezone.utc)
    return {"content": [{"type": "text", "text": now.strftime("%Y-%m-%d %H:%M UTC")}]}


tools_server = create_sdk_mcp_server(
    name="lab02-tools",
    version="1.0.0",
    tools=[get_work_items, get_current_datetime],
)

options = ClaudeAgentOptions(
    mcp_servers={"lab02": tools_server},
    allowed_tools=[
        "mcp__lab02__get_work_items",
        "mcp__lab02__get_current_datetime",
    ],
)


async def main():
    async with ClaudeSDKClient(options=options) as client:
        await client.query(
            "Que dia e hoje, e quantos work items existem no projeto? "
            "Lista os titulos."
        )
        async for message in client.receive_response():
            print(message)


if __name__ == "__main__":
    asyncio.run(main())
