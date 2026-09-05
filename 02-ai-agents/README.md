# AI Agents Track

Agent architecture and orchestration, built directly in code with the
Claude Agent SDK (Python) — no no-code tool involved, unlike the n8n
track's Lab 03.

## Overview

| Lab | What it demonstrates |
|---|---|
| [00 — Fundamentals and Setup](lab-00-fundamentals-setup/) | The agentic loop concept (Think → Act → Observe); Python + Claude Agent SDK authenticating via the existing Claude Code session, no separate API billing |
| [01 — Agent From Scratch](lab-01-agent-from-scratch/) | Defining a custom tool (`@tool`, in-process MCP server); a real experiment on whether the model autonomously chooses to use a tool, and why arithmetic is a poor test case for that |
| [02 — Multiple Tools and Orchestration](lab-02-multi-tool-orchestration/) | An agent choosing between multiple tools providing genuinely external information (real Azure DevOps data, real time) rather than something it can reason its way to; credentials moved to a gitignored `.env` |
| [03 — Multi-Agent Coordination](lab-03-multi-agent-coordination/) | A lead agent delegating to two specialized subagents with a data dependency between them; a real bug found and fixed around foreground vs. background delegation |

See [PROGRESS.md](PROGRESS.md) for the detailed log and
[ROADMAP.md](ROADMAP.md) for how the track was planned.

## No-code vs. code: an honest comparison

The n8n track's Lab 03 built an AI agent using n8n's pre-built "AI Agent"
node. This track rebuilt the same underlying concepts directly in code.
Having done both, here's the actual trade-off, not a sales pitch for
either:

**No-code (n8n's AI Agent node) is better when:**
- Speed matters more than control — a working agent in minutes, visually
- Non-programmers need to build or maintain the workflow
- The use case is a single agent with a handful of tools and no need for
  custom orchestration logic
- The tool/credential setup is simple point-and-click (HTTP Request node
  + a saved credential)

**Code (Claude Agent SDK) is better when:**
- You need **multi-agent coordination** — n8n's AI Agent node doesn't
  expose an equivalent to defining specialized subagents with their own
  restricted toolsets; that pattern only showed up once this track moved
  to code (Lab 03)
- You need full visibility into the reasoning loop for debugging — the
  message stream (thinking, tool calls, tool results) is far more
  granular than what n8n's node surfaces
- The logic needs to be version-controlled, tested, and reviewed like
  normal software, not stored as one workflow JSON blob
- You need precise control over execution details that matter in
  practice — e.g. the foreground/background delegation bug found in
  Lab 03 would have been invisible and unfixable inside a no-code node

**What stayed genuinely the same either way:** the core concepts —
trigger → agent → tool call → result → response — and the reusable
Azure DevOps REST API knowledge (WIQL, `workitemsbatch`, PAT scopes)
carried directly from the n8n track into this one's Python tools with no
relearning needed.

## What's next

This track's core labs are complete. Noted for the future: exploring
**Azure AI Foundry / AWS Bedrock** as alternative backends for running
Claude in an enterprise context — relevant given the Azure background —
and the cross-track **"Content Factory"** capstone combining this track
with n8n (and possibly RAG). See `CLAUDE.md` for the overall roadmap.
