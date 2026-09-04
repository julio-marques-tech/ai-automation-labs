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
