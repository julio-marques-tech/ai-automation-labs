# Lab 00 — Fundamentals and Setup

## What

Set up a Python environment to build AI agents in code, and confirm the
Claude Agent SDK can authenticate using the existing Claude Code session
— no separate, pay-per-token API key needed.

## Why

The n8n track's Lab 03 used a pre-built "AI Agent" node that handled the
reasoning loop, tool calling, and model connection internally. This track
strips that abstraction away: writing the agent loop in code to see
exactly what a framework like that is doing under the hood.

## Agent fundamentals

A single LLM call is: prompt in, response out, once. An **agent** runs
that in a loop — the model can decide to call a tool, observe the result,
and decide the next step, repeating until it considers the task done.
This is often called the **ReAct** pattern (Reason + Act), or an "agentic
loop": Think → Act → Observe → repeat.

The core pieces:
- **The LLM** — the reasoning engine
- **Tools** — functions the agent can call (e.g. the Azure DevOps query
  from the n8n track)
- **Memory** — conversation/state carried across loop iterations
- **The orchestration loop** — the code driving all of the above

## Setup

- Installed the **Claude Code CLI** globally via npm
  (`npm install -g @anthropic-ai/claude-code`) — the Claude Agent SDK
  drives this CLI under the hood, so it needed to exist on the system
- Installed the **`claude-agent-sdk`** Python package inside a virtual
  environment (`02-ai-agents/.venv`)
- Confirmed the SDK authenticates via the CLI's existing session (same
  Claude.ai subscription used elsewhere) — no `ANTHROPIC_API_KEY` needed,
  and no separate pay-per-token billing

## Problems encountered

### PowerShell blocked npm/claude scripts by default

Both `npm` and the newly installed `claude` command are PowerShell (`.ps1`)
wrapper scripts on Windows, and PowerShell's default execution policy
blocks running scripts. **Resolution:**
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
A safe, standard fix for Node.js development on Windows (current-user
scope, no admin rights needed).

### Virtual environment created in the wrong directory

Ran `python -m venv "02-ai-agents\.venv"` from the parent folder instead
of the repository root, creating the environment one level above the
git repo. **Resolution:** `cd` into the correct directory first, delete
the misplaced folder, and recreate it in the right place — a reminder to
always check the shell prompt's current path before running relative-path
commands.

### PowerShell misparsed a path starting with digits

`02-ai-agents\.venv\Scripts\Activate.ps1`, unquoted, was parsed as an
expression (`02` followed by an unexpected `-ai-agents` token) instead of
a path. **Resolution:** invoke it with the call operator and quotes:
`& "02-ai-agents\.venv\Scripts\Activate.ps1"`.

### Virtual environments don't inherit user-level pip packages

`claude-agent-sdk` was already installed at the user level (from an
earlier step), but a fresh venv doesn't see it by default — `pip show`
came back empty until it was installed again inside the activated venv.

## How to run

```powershell
cd ai-automation-labs
& "02-ai-agents\.venv\Scripts\Activate.ps1"
python "02-ai-agents\lab-00-fundamentals-setup\test_setup.py"
```

## What I learned

- The **agentic loop** concept (Think → Act → Observe) as the actual
  distinction between "an agent" and "a single LLM call"
- The Claude Agent SDK drives the Claude Code CLI as a subprocess, so it
  can reuse an existing subscription-based login instead of requiring API
  billing — a genuinely useful cost-avoidance path for personal projects
- `total_cost_usd` in the SDK's result output is an *informational*
  list-price estimate, not an actual charge, when there's no API key
  attached (`apiKeySource: 'none'`) — usage instead counts against the
  subscription's rate limits
- Windows-specific friction points (execution policy, path quoting,
  venv package isolation) that are easy to hit and worth recognizing
  quickly rather than debugging from scratch each time
