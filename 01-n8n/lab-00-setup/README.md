# Lab 00 — Setup (Docker + WSL2 + n8n)

## What

Prepare the local Windows environment to run n8n self-hosted via Docker,
and connect Claude Code to VSCode as the working environment for this track.

## Why

n8n runs best as a Docker container — it isolates dependencies, is easy to
update/remove, and mirrors how it would run in production (self-hosted on
a server). On Windows, Docker Desktop needs WSL2 as its underlying
virtualization engine.

## What was installed

- **WSL2** (Windows Subsystem for Linux) — the virtualization engine
  required by Docker Desktop on Windows
- **Docker Desktop** — via `winget install -e --id Docker.DockerDesktop`
- **"Claude Code for VS Code" extension** (publisher Anthropic) — Claude
  Code integrated directly into the editor, authenticated via Claude.ai
  Subscription
- **n8n** — running as a Docker container, with a persistent volume

## Problems encountered and how they were solved

### Corrupted WSL2 (`REGDB_E_CLASSNOTREG`)

Running `wsl --version` for the first time returned:
```
wsl: WSL installation appears to be corrupted (Error code: Wsl/CallMsi/Install/REGDB_E_CLASSNOTREG)
```

**Cause:** a misregistered WSL COM component — common when the Windows
feature was never properly enabled.

**Resolution:**
1. Enable the two required Windows features (PowerShell as Administrator):
   ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```
2. Restart the PC (the features only take effect after a reboot)
3. Run `wsl --update` and, when the "Press any key to repair WSL" prompt
   appears, let the self-repair run (instead of cancelling)

After this, `wsl --version` returned the version with no error.

### Docker: command not recognized right after installing

After installing Docker Desktop via `winget`, the `docker` command wasn't
recognized in PowerShell. **Cause:** the terminal window was already open
before the installation finished, and Windows only refreshes `PATH` in new
windows. **Resolution:** open a new terminal.

## How to run

```powershell
# Start n8n with persistent data
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n

# Confirm it's running
docker ps
```

Then visit [http://localhost:5678](http://localhost:5678).

To stop/resume without losing data:
```powershell
docker stop n8n
docker start n8n
```

## What I learned

- The difference between WSL1/WSL2 and why Docker Desktop on Windows
  depends on WSL2 as its virtualization engine
- How to diagnose and repair a corrupted WSL installation via DISM
  (enabling Windows features) instead of reinstalling everything from
  scratch
- The difference between a Docker image, container, and volume — and why
  a volume is needed so n8n data isn't lost between restarts
- How to install and authenticate the official "Claude Code for VS Code"
  extension, distinguishing it from unofficial extensions with similar
  names in the Marketplace
- There are alternative backends for running Claude in an enterprise
  context (AWS Bedrock, Azure AI Foundry, Google Vertex) — to explore
  later in the AI Agents track
