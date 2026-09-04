# Lab 02 — Multiple Tools and Orchestration

## What

Give the agent two independent tools — real Azure DevOps work item data,
and the current real-world date/time — and observe genuine orchestration:
deciding which tools to call, in what order, and how to combine results.

## Why

Lab 01 found that arithmetic is a weak test for autonomous tool use,
because Claude can usually reason its way to the answer without a tool.
This lab fixes that by using tools that provide information the model
**cannot** produce on its own — neither live external data nor the actual
current date are things an LLM can know without a tool call.

## How it's built

- **`get_work_items`** — calls the Azure DevOps REST API (same
  organization/project as the n8n track's Lab 02), doing the WIQL query
  + `workitemsbatch` two-step internally so the agent sees one clean
  tool that returns id, title, and state directly
- **`get_current_datetime`** — pure Python, no external call, returns the
  real UTC date/time
- Credentials moved to a **`.env`** file (via `python-dotenv`), gitignored
  — not hardcoded in the script and never pasted into chat. See
  [`.env.example`](.env.example) for the required variables

## Result

Asked *"What day is it, and how many work items are there? List the
titles"* — with no instructions about which tools to use — the agent:

1. **Stated its plan first**, in its own words: *"I'll check the current
   date and query the project's work items using the available MCP
   tools — these are simple, side-effect-free queries, so I'll bring
   back both results."* This is visible planning: it reasoned about
   *why* it was safe to call both tools without asking permission
   (read-only, no side effects)
2. Called `get_current_datetime` first, then `get_work_items`
3. Combined both results into one structured answer

Unlike Lab 01, neither tool call was optional here — both pieces of
information were genuinely unavailable to the model otherwise, so this
is a clean demonstration of orchestration rather than a coin flip.

## How to run

```powershell
& "02-ai-agents\.venv\Scripts\Activate.ps1"
```

1. Copy `.env.example` to `.env` and fill in your own Azure DevOps org,
   project, and a PAT scoped to Work Items: Read
2. `python "02-ai-agents\lab-02-multi-tool-orchestration\agent.py"`

## What I learned

- How to give an agent multiple tools and see it choose autonomously
  between them, rather than testing with just one
- The agent doesn't just call tools silently — it can (and here, did)
  state its reasoning in plain text before acting, which is directly
  useful for building trust/transparency in a production agent
- Keeping secrets in a gitignored `.env` file (loaded via
  `python-dotenv`) instead of hardcoding them — the same pattern used in
  any real backend project, not something specific to AI agents
- Reusing the Azure DevOps REST API knowledge from the n8n track,
  confirming that the WIQL + `workitemsbatch` two-step pattern is a
  reusable piece of knowledge, not a one-off for n8n specifically
