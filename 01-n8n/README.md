# n8n Track

Workflow automation with n8n, self-hosted via Docker on Windows (WSL2).

## Overview

Four labs, each building on the last: from a working local environment to
a self-hosted AI agent that reads real data from an external system.

| Lab | What it demonstrates |
|---|---|
| [00 — Setup](lab-00-setup/) | Diagnosing and repairing a corrupted WSL2 install via DISM; Docker Desktop on WSL2; installing and authenticating the Claude Code VS Code extension |
| [01 — Core Concepts](lab-01-core-concepts/) | n8n fundamentals: nodes, triggers, connections, executions; calling an external API with the HTTP Request node |
| [02 — Azure DevOps Connection](lab-02-azure-devops-connection/) | Authenticating to a real system with no native n8n connector (PAT + Basic Auth over the REST API); diagnosing and fixing a PAT scope/401 error; querying real data with WIQL |
| [03 — Simple AI Agent](lab-03-simple-ai-agent/) | A fully self-hosted AI agent (n8n's AI Agent node + Ollama/Llama 3.1, no cloud API) that decides on its own when to call a tool — reusing the Lab 02 connection to answer natural-language questions about real Azure DevOps work items |

See [PROGRESS.md](PROGRESS.md) for the detailed log (technical decisions,
problems encountered, and how they were resolved) and
[ROADMAP.md](ROADMAP.md) for how the track was planned.

## Why this progression

Each lab was scoped to isolate one concept before combining it with the
next: learn the tool (01) → connect it to a real system (02) → give an AI
agent access to that same connection (03). By Lab 03, the workflow is no
longer a tutorial exercise — it's a small but genuine integration between
a local LLM and a real Azure DevOps project.

## Skills demonstrated

- Self-hosted infrastructure: Docker, WSL2, and a locally-run LLM (Ollama)
  with zero cloud dependency or billing
- Integrating a system with no native connector via generic HTTP Request +
  REST API authentication (a transferable pattern, not Azure DevOps-specific)
- Debugging real errors (WSL corruption, PAT scope mismatches) by
  diagnosing root cause rather than trial-and-error
- AI agent orchestration: tool calling, and recognizing/fixing a case
  where the agent had incomplete data rather than accepting a hallucinated
  answer

## What's next

The n8n track's core labs are complete. A **"Content Factory"** capstone
— combining n8n with the AI Agents track (and possibly RAG) into an
end-to-end automated content pipeline — is noted as a future cross-track
project once those tracks are further along. See `CLAUDE.md` for the
overall portfolio roadmap.
