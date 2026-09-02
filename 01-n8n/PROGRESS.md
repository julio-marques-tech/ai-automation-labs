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
