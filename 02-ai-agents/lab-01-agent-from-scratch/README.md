# Lab 01 — Agent From Scratch

## What

Build a minimal agent directly in code (Claude Agent SDK, Python), with
one custom tool, to observe the reasoning loop that a no-code tool like
n8n's AI Agent node hides.

## Why

Understanding the mechanics — not just using a pre-built node — matters
for being able to explain *why* an agent behaves the way it does, debug
it, and make informed build-vs-buy calls later (code vs. no-code).

## How it's built

- `@tool(...)` — a decorator that marks a plain Python function as
  something the model can choose to call, with a name, description, and
  expected arguments (the description is what the model actually reads
  to decide when the tool is relevant — there's no hardcoded rule for
  "when to use it")
- `create_sdk_mcp_server(...)` — bundles one or more `@tool`-decorated
  functions into an **in-process MCP server**: it runs inside the same
  Python program, no separate process. This is the simplest form of MCP
  (Model Context Protocol, originally built by Anthropic, now an open
  standard) — a "real" external MCP server runs as its own process and
  can be written in any language
- `ClaudeAgentOptions(mcp_servers=..., allowed_tools=...)` — tells the
  agent which tools it's allowed to use
- `ClaudeSDKClient` — sends the query and streams back the agent's
  messages (thinking, tool calls, tool results, final answer)

The custom tool built here (`calculate`) evaluates arithmetic safely
using Python's `ast` module rather than `eval()`, to avoid executing
arbitrary code from a tool argument.

## Experiment: does the agent decide to use the tool on its own?

Three tests, same tool available throughout:

1. **Simple calculation, no instruction about the tool.** The agent
   answered directly, without calling `calculate` — it solved
   `847 × 392 − 1500` in its own reasoning.
2. **Same-ish calculation, explicitly told "you MUST use the tool."**
   The agent complied: it first had to look up the tool (a `ToolSearch`
   call — tools aren't all loaded upfront, they're fetched on demand),
   then called `mcp__calculator__calculate` with the right expression,
   read back the result, and used it in the final answer. This confirmed
   the *mechanism* works correctly end to end, but forcing the tool
   defeats the point of testing autonomous decision-making.
3. **A genuinely harder calculation, no instruction at all.** The agent
   *still* chose not to use the tool — instead it used substantially more
   "thinking" (1317 thinking tokens vs. ~50-100 for the simple case) to
   work through the multi-step arithmetic itself, correctly.

## Finding: arithmetic is a poor test case for autonomous tool use

Claude's own arithmetic capability (especially with extended thinking) is
strong enough that it rarely judges an external calculator necessary —
it only used the tool when explicitly instructed to. This isn't a bug in
the lab; it's a real, useful finding: **to reliably observe an agent
autonomously choosing a tool, the tool needs to provide something the
model genuinely cannot produce itself** — live/external data (like the
Azure DevOps queries from the n8n track), not something it can reason
its way to. Lab 02 will use that kind of tool instead.

## How to run

```powershell
& "02-ai-agents\.venv\Scripts\Activate.ps1"
python "02-ai-agents\lab-01-agent-from-scratch\agent.py"
```

## What I learned

- The mechanical difference between a **tool definition** (a Python
  function + description) and the **decision to call it** (made by the
  model itself, based on the description text, not a coded rule)
- MCP servers can be **in-process** (same program, simplest case) or
  **external processes** (any language) — both talk to the model the
  same way
- A concrete example of why picking the right test case matters when
  evaluating agent behavior — a "hard for a human" problem isn't
  necessarily "hard for the model," and arithmetic specifically is a
  weak probe for tool-use decisions with Claude
- How to defend this project without having memorized the code: the
  interview-relevant skill is explaining the architecture and defending
  each decision, not reciting syntax — consistent with how the code was
  actually built (directed and reviewed, not hand-typed from memory)
