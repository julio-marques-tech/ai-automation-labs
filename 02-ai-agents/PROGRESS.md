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
