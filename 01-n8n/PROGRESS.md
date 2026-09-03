# Progress — n8n Track

Log of completed labs, technical decisions, and problems solved along the track.

## Lab 00 — Setup (Docker + WSL2)

**Status:** completed (2026-09-02)

**Done:**
- WSL2 repaired and functional (was necessary — corrupted installation)
- Docker Desktop installed (via `winget`), WSL2-based engine confirmed
- Official "Claude Code for VS Code" extension installed and authenticated
- n8n running as a Docker container, with a persistent volume (`n8n_data`),
  accessible at `localhost:5678`

**Technical decisions:**
- n8n local-only for now (no network exposure) — enough for learning,
  revisit if access from another device is needed
- Logged into Claude Code via Claude.ai Subscription (not Anthropic
  Console/API billing) — simpler for interactive use

**Problems and resolution:** see detail in
[lab-00-setup/README.md](lab-00-setup/README.md#problems-encountered-and-how-they-were-solved)

**Note for future tracks:** explore AWS Bedrock / Azure AI Foundry as
alternative backends to Claude (relevant given the Azure background) —
logged in `CLAUDE.md`, AI Agents track.

## Lab 01 — Core Concepts

**Status:** completed (2026-09-02)

**Done:**
- Built a first workflow: `Manual Trigger → Edit Fields → HTTP Request`
- Learned nodes, triggers, connections, and executions hands-on in the
  n8n editor
- Called a public API (JSONPlaceholder) with the HTTP Request node, the
  same node type that will connect to Azure DevOps in Lab 02
- Exported the workflow as JSON — see
  [lab-01-core-concepts/workflow.json](lab-01-core-concepts/workflow.json)

**Details:** see [lab-01-core-concepts/README.md](lab-01-core-concepts/README.md)

## Lab 02 — Azure DevOps Connection

**Status:** completed (2026-09-02)

**Done:**
- Created a free, personal Azure DevOps organization and project (kept
  separate from any employer's tenant)
- Authenticated n8n to the Azure DevOps REST API via PAT (Basic Auth,
  generic credential)
- Built a workflow that queries real work items via WIQL
  (`Manual Trigger → HTTP Request POST`)
- Exported the workflow as JSON — see
  [lab-02-azure-devops-connection/workflow.json](lab-02-azure-devops-connection/workflow.json)

**Technical decisions:**
- Used the generic HTTP Request node (n8n has no native Azure DevOps
  connector) — same pattern reusable for any unsupported API
- PAT scoped to least privilege needed (Work Items: Read, Project and
  Team: Read)

**Problems and resolution:** PAT scope mismatch caused a 401 on the work
items endpoint even though a simpler endpoint worked — see detail in
[lab-02-azure-devops-connection/README.md](lab-02-azure-devops-connection/README.md#problem-encountered-pat-scope-mismatch-401-error)

## Lab 03 — Simple AI Agent

**Status:** completed (2026-09-03)

**Done:**
- Installed Ollama on Windows, running Llama 3.1 8B fully locally (no
  cloud API, no billing)
- Built an AI Agent workflow in n8n: Chat Trigger → AI Agent (Ollama
  Chat Model + HTTP Request Tool)
- Tool connects to the real Azure DevOps project from Lab 02 — agent
  answers natural-language questions about real work items
- Exported the workflow as JSON — see
  [lab-03-simple-ai-agent/workflow.json](lab-03-simple-ai-agent/workflow.json)

**Technical decisions:**
- Chose Ollama (self-hosted) over a cloud LLM API (Gemini free tier
  considered) to avoid billing entirely and to build self-hosted LLM
  deployment experience, relevant given the FHIR/healthcare background
  (data residency constraints)
- Llama 3.1 8B chosen for tool-calling support, sized to run acceptably
  on CPU with 32GB RAM (no dedicated GPU)

**Problems and resolution:** WIQL only returns work item IDs, not field
values, so the agent initially reported titles as "not available" (did
not hallucinate) — switched the tool to the `workitemsbatch` endpoint to
get full field values in one call. See detail in
[lab-03-simple-ai-agent/README.md](lab-03-simple-ai-agent/README.md#problem-encountered-wiql-only-returns-ids-not-field-values)

## Lab 04 — Export and Documentation

**Status:** completed (2026-09-03)

**Done:**
- Wrote [01-n8n/README.md](README.md), a track-level overview tying
  together Labs 00-03 (what each demonstrates, why the progression was
  scoped that way, skills demonstrated)
- Updated [ROADMAP.md](ROADMAP.md) to reflect the core track as complete
- Reframed the early "Content Factory" idea as a future **cross-track
  capstone** (n8n + AI Agents, possibly RAG) instead of a step within
  this track — logged in `CLAUDE.md`

**n8n track status:** core labs (00-03) complete. Next active track:
**AI Agents**.
