# Lab 03 — Simple AI Agent

## What

Build a fully self-hosted AI agent in n8n — a local LLM (no cloud API,
no billing) that can answer natural-language questions using a real tool
connected to the Azure DevOps project from Lab 02.

## Why

This is the track's central milestone: moving from "workflows that call
static endpoints" to "an agent that decides, on its own, whether and when
to call a tool" based on the user's question. Running it fully locally
(Ollama) rather than a paid cloud API also matters for the portfolio
story — it shows the ability to evaluate and deploy LLMs in contexts
where data can't leave the premises (directly relevant to a healthcare/
FHIR background, where this is a common real constraint).

## Setup

- Installed [Ollama](https://ollama.com) natively on Windows (outside
  Docker) and pulled **Llama 3.1 8B** (`ollama pull llama3.1`) — chosen
  for its solid tool-calling support and because 32GB RAM comfortably
  handles an 8B model on CPU (~5-25s per response, no dedicated GPU)
- **Key architecture detail:** n8n runs inside a Docker container (Lab
  00), but Ollama runs natively on the Windows host. `localhost` inside
  the container refers to the container itself, not the host — so the
  Ollama credential's Base URL had to be
  `http://host.docker.internal:11434`, not `http://localhost:11434`
- Reused the `Azure DevOps PAT` credential from Lab 02 for the tool

## Workflow structure

`Chat Trigger → AI Agent (+ Ollama Chat Model, + HTTP Request Tool)`

- **Chat Trigger** ("When chat message received") — gives the workflow a
  built-in chat UI to converse with the agent
- **AI Agent** — the orchestrator: receives the user's message, decides
  whether it needs a tool to answer, calls it if so, and composes the
  final reply
- **Ollama Chat Model** — the "brain" (Llama 3.1 8B, running 100% locally)
- **HTTP Request Tool** — lets the agent query real Azure DevOps work
  items on demand

## Problem encountered: WIQL only returns IDs, not field values

First version of the tool used the same WIQL query from Lab 02. The agent
correctly called it and got 4 work item IDs — but reported all titles as
**"not available"**. Worth noting: **the model did not hallucinate fake
titles** — it accurately reported it didn't have that data, which says
something good about how it handled an incomplete tool result.

**Cause:** WIQL's `flat` query type returns only work item IDs and URLs,
not field values — same limitation documented in
[Lab 02's README](../lab-02-azure-devops-connection/README.md).

**Resolution:** switched the tool's endpoint to Azure DevOps'
**`workitemsbatch`** API, which returns IDs *and* requested field values
(`System.Title`, `System.State`) in a single call:
```
POST https://dev.azure.com/{org}/{project}/_apis/wit/workitemsbatch?api-version=7.1

{
  "ids": [1, 2, 3, 4],
  "fields": ["System.Id", "System.Title", "System.State"]
}
```
After the fix, the agent answered with the real titles for all 4 work
items.

## How to run

1. Install [Ollama](https://ollama.com), run `ollama pull llama3.1`
2. Open n8n at `localhost:5678`, import [`workflow.json`](workflow.json)
3. Create an Ollama credential: Base URL `http://host.docker.internal:11434`
   (if n8n runs in Docker) and select model `llama3.1:latest`
4. Create/reuse a Basic Auth credential for Azure DevOps (PAT as
   password, no username) and update the tool's URL to your own
   organization/project
5. Open the chat panel and ask something like *"How many work items are
   there and what are their titles?"*

## What I learned

- The **AI Agent** node pattern in n8n: Chat Model + Tools + Memory
  connectors, and how the agent decides on its own whether a tool call
  is needed
- Running an LLM **fully self-hosted** with Ollama — no API key, no
  billing, no data leaving the machine
- The Docker networking detail (`host.docker.internal`) needed to
  connect a containerized n8n to a host-native service
- Azure DevOps' `workitemsbatch` endpoint as a better fit than WIQL when
  you need field values, not just IDs, in one call
- A concrete, positive observation about model behavior: it reported
  missing data honestly instead of fabricating plausible-looking answers
