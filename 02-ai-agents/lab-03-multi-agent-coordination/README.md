# Lab 03 — Multi-Agent Coordination

## What

A lead agent that delegates to two specialized subagents — a
`work-item-analyst` (reads real Azure DevOps data) and a `report-writer`
(drafts a report from data it's given, with no tools of its own) — and
combines their results into one final answer.

## Why

Lab 02 showed one agent orchestrating multiple *tools*. This lab is the
next level up: one agent orchestrating multiple *other agents*, each
specialized and isolated. This is the same delegation pattern Claude Code
itself uses with its own subagents (Explore, general-purpose, Plan) —
here it's applied to a small, custom, two-agent pipeline instead.

## How it's built

- **`AgentDefinition`** — defines a subagent: a `description` (helps the
  lead agent decide when to delegate to it), a `prompt` (its system
  prompt / specialization), and `tools` (what it's allowed to use —
  `work-item-analyst` gets `get_work_items`, `report-writer` gets none)
- **`ClaudeAgentOptions(agents={...})`** — registers both subagents with
  the lead agent
- The lead agent gets access to a `Task` tool automatically once
  subagents are defined, and uses it to invoke a named subagent with its
  own prompt — that subagent runs in an isolated context and returns its
  result to the lead agent

## Problem encountered: a subagent ran in the background and its result was lost

First run: the lead agent delegated to `work-item-analyst` **in the
foreground** (it waited for the result, since `report-writer` depends on
it) — that part worked correctly. But it delegated to `report-writer`
**in the background** (`is_backgrounded: True`), on its own initiative,
saying it would "let me know when ready." The script's `receive_response()`
loop, however, ends once the lead agent's own turn completes — it never
listens for a background subagent's later completion. The script exited
successfully, but the actual report was never surfaced.

**Cause:** background delegation is asynchronous by design — useful for
long independent tasks, but it means the calling code has to explicitly
wait for or poll the result, which this simple script didn't do.

**Resolution:** added an explicit instruction to the prompt telling the
agent to run **both** subagents in the foreground and show the final
report before finishing. On the next run, both subagents ran
sequentially in the foreground, and the full report came back correctly.

## Result

Asked to "write a project status report," the lead agent:
1. Delegated to `work-item-analyst`, which read the 4 real work items
   from Azure DevOps and returned a factual summary
2. Passed that summary to `report-writer`, which drafted a full,
   structured report (executive summary, table, data limitations,
   observations)
3. **Notably**, `report-writer` explicitly flagged that these 4 work
   items are test data from the n8n track's Lab 02, and do *not*
   represent the portfolio's actual progress — pointing instead to the
   real `PROGRESS.md` files. It followed the "don't invent conclusions
   the data doesn't support" instruction correctly, unprompted for that
   specific caveat.

## How to explain this in an interview

*"I define subagents with a description, a system prompt, and a
restricted toolset. The lead agent picks which subagent to delegate to
based on the description — it's the same mechanism Claude Code itself
uses internally with its own subagents. Delegation can run in the
foreground (the caller waits) or in the background (async, fire-and-
forget) — I actually hit a bug where the lead agent chose background for
one subagent, and my simple script didn't know how to wait for the
result, so I lost it. Fixing it meant being explicit in the prompt about
execution mode — a real lesson about the difference between what an
agent *can* decide and what the surrounding code needs to be built to
handle."*

## How to run

```powershell
& "02-ai-agents\.venv\Scripts\Activate.ps1"
```

1. Copy `.env.example` to `.env` and fill in your own Azure DevOps org,
   project, and PAT
2. `python "02-ai-agents\lab-03-multi-agent-coordination\agent.py"`

## What I learned

- How to define specialized subagents (`AgentDefinition`) with their own
  prompt and restricted toolset, rather than one agent with every tool
- The foreground/background distinction in agent delegation, and that
  it's a real design decision with consequences for the calling code —
  not just an implementation detail
- A concrete example of a subagent correctly caveating its output based
  on context it was given, instead of overclaiming what the data showed
- The interview-ready explanation above — the goal isn't reciting code,
  it's being able to explain the mechanism and defend the debugging
  decisions
