# Lab 01 — Core Concepts

## What

Build a first n8n workflow from scratch to learn the platform's four core
building blocks: nodes, triggers, connections, and executions.

## Why

Before connecting n8n to any real system (Azure DevOps in Lab 02), it's
worth understanding how data actually flows between nodes and how to
inspect it — this is the foundation every later workflow builds on.

## Workflow structure

`Manual Trigger → Edit Fields → HTTP Request`

1. **Manual Trigger** ("When clicking 'Execute workflow'") — starts the
   workflow on demand, by clicking the Execute button in the editor.
2. **Edit Fields** (Set node) — creates a static field (`message: "Hello
   by n8n!"`) to demonstrate how a node produces output data that the next
   node receives as input.
3. **HTTP Request** — calls a public test API
   (`https://jsonplaceholder.typicode.com/todos/1`, GET, no auth) and
   returns real JSON data (`userId`, `id`, `title`, `completed`), showing
   how a node consumes external data mid-workflow.

## How to run

1. Open n8n at `localhost:5678`
2. Create a new workflow → menu (`...`) → **Import from File** → select
   [`workflow.json`](workflow.json)
3. Click **Execute workflow**
4. Click on each node to inspect its **Input** and **Output** panels
5. Check the **Executions** tab to see the run log

## What I learned

- **Node** — a single step in a workflow; each one does one thing
  (transform data, call an API, etc.)
- **Trigger** — the special node that starts a workflow; every workflow
  needs at least one
- **Connection** — the line between nodes that defines execution order and
  passes data forward (each node's output becomes the next node's input)
- **Execution** — a full run of the workflow, logged with duration, size,
  and per-node success/failure — the equivalent of a pipeline run log in
  Azure DevOps
- The **HTTP Request** node is the same building block that will later
  connect to the Azure DevOps API in Lab 02 — just without authentication
  for now, to isolate the concept first
