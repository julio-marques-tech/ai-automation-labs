# Progress — AI Agents Track

Log of completed labs, technical decisions, and problems solved along the track.

## Lab 00 — Fundamentals and Setup

**Status:** completed (2026-09-04)

**Done:**
- Installed the Claude Code CLI globally (npm) and the `claude-agent-sdk`
  Python package inside a virtual environment
- Confirmed the SDK authenticates via the existing Claude Code session
  (no separate API key or billing)
- Ran a smoke-test script confirming end-to-end connectivity

**Technical decisions:**
- Used the Claude Agent SDK (subscription-based auth via CLI) instead of
  the raw Anthropic API, specifically to avoid pay-per-token billing for
  this portfolio project

**Problems and resolution:** PowerShell execution policy blocking npm/
claude scripts, a virtual environment created in the wrong directory, and
a path-parsing error with a leading-digit folder name — see detail in
[lab-00-fundamentals-setup/README.md](lab-00-fundamentals-setup/README.md#problems-encountered)

## Lab 01 — Agent From Scratch

**Status:** completed (2026-09-04)

**Done:**
- Built a minimal agent in Python (Claude Agent SDK) with one custom
  tool (`calculate`), defined via `@tool` + an in-process MCP server
  (`create_sdk_mcp_server`)
- Ran three experiments to test whether the agent decides on its own
  whether to call the tool

**Technical decisions:**
- Implemented the calculator tool with Python's `ast` module instead of
  `eval()`, to avoid executing arbitrary code from a tool argument

**Finding:** arithmetic is a weak test case for autonomous tool-use
decisions — Claude's own reasoning (especially with extended thinking)
is strong enough that it only used the tool when explicitly told to,
even on a genuinely harder calculation. Reliable autonomous tool choice
needs a tool providing information the model can't produce itself (e.g.
live external data) — planned for Lab 02. Full detail in
[lab-01-agent-from-scratch/README.md](lab-01-agent-from-scratch/README.md#finding-arithmetic-is-a-poor-test-case-for-autonomous-tool-use)

## Lab 02 — Multiple Tools and Orchestration

**Status:** completed (2026-09-04)

**Done:**
- Built an agent with two tools: real Azure DevOps work item data
  (reusing the org/project from the n8n track) and the current
  real-world date/time
- Moved credentials to a gitignored `.env` file (`python-dotenv`)
  instead of hardcoding them
- Confirmed genuine orchestration: the agent chose to call both tools,
  in a sensible order, and stated its plan in plain text before acting

**Technical decisions:**
- Picked tools that provide information the model cannot reason its way
  to (live data, real time) — directly addressing the Lab 01 finding
  that arithmetic is a weak test case
- Implemented the Azure DevOps WIQL + `workitemsbatch` two-step call
  inside the tool itself, so the agent only sees one clean tool call

**Result:** the agent called both tools autonomously and combined their
results correctly — full detail in
[lab-02-multi-tool-orchestration/README.md](lab-02-multi-tool-orchestration/README.md#result)

## Lab 03 — Multi-Agent Coordination

**Status:** completed (2026-09-04)

**Done:**
- Built a lead agent delegating to two specialized subagents
  (`work-item-analyst`, `report-writer`) via `AgentDefinition` +
  `ClaudeAgentOptions(agents=...)`
- Confirmed sequential delegation with a data dependency (report needs
  the work item data first) works correctly

**Technical decisions:**
- Gave `report-writer` zero tools, forcing it to work only from data it's
  handed — a deliberate test of whether it would invent data (it didn't)

**Problem and resolution:** the lead agent ran the second subagent in the
background on its own initiative; the script didn't wait for it, so the
result was lost on the first run. Fixed by explicitly instructing both
subagents to run in the foreground. Full detail in
[lab-03-multi-agent-coordination/README.md](lab-03-multi-agent-coordination/README.md#problem-encountered-a-subagent-ran-in-the-background-and-its-result-was-lost)

**AI Agents track status:** core labs (00-03) complete.
