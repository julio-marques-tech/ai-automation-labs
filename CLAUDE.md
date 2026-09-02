# AI & Automation Labs — Julio Marques

## About this project

A hands-on learning portfolio in applied AI and automation, structured as
guided labs. Each lab produces a working project, documented and versioned
in this repository, serving as evidence of competence for interviews and
career progression.

Methodology: learn by doing. Claude guides step by step, the work runs on
the user's local machine (self-hosted where applicable), and each lab is
closed with portfolio-ready documentation.

## Planned tracks

1. **n8n** — workflow automation, self-hosted via Docker (IN PROGRESS)
2. **AI Agents** — agent architecture, orchestration (future note: explore Azure AI Foundry / AWS Bedrock as alternative backends to Claude, relevant given the Azure background)
3. **RAG** (Retrieval-Augmented Generation) — theory and practical application
4. **Skills** — building and integrating reusable skills
5. **Advanced FHIR** — deepening existing professional expertise from SPMS
6. **Salesforce** — fundamentals + Trailhead track
7. **Slack** — integrations and automations
8. **Fine-tuning** — future exploration, after solid foundations

Execution order within the n8n track: Azure DevOps → Simple AI Agent → Content Factory.

## User profile

Business/Functional Analyst with ~17 years of experience, a solid background
in FHIR and healthcare interoperability (SPMS, Portugal), agile/BDD, and MCP
(Azure DevOps, Confluence). Transitioning into AI consulting.

**Important:** zero prior experience with n8n, AI agents, RAG, Salesforce,
or the Slack API. Treat every new track as an absolute starting point — do
not assume implicit knowledge, even where the user already masters adjacent
concepts (e.g. already knows Azure DevOps via MCP, but not via n8n).

Prefers structured, ready-to-use deliverables with explicit reasoning, and
direct correction when something is wrong or misunderstood.

## HOW TO WORK WITH ME ON THIS PROJECT (fixed rule, always active)

This is a space for **guided learning**, not "just code it and solve it
yourself." Always follow this mode, unless explicitly told otherwise within
a session:

1. **Explain before executing.** Before running any command or writing any
   code, explain in 2-3 sentences what is about to happen and why.
2. **One step at a time.** Do not chain several steps together. Wait for
   confirmation that the previous step worked before moving on.
3. **Prefer guiding over doing it for me.** When it makes pedagogical sense
   (e.g. running a simple command, filling in a field in the n8n UI), ask
   ME to run the command and bring back the result, instead of running it
   yourself. When it's repetitive/mechanical (e.g. creating folder
   structures, writing documentation files), you can do it directly.
4. **Never assume it worked.** Always ask for explicit confirmation
   ("did it work?", "what result did you get?") before marking a step as
   done.
5. **Log progress.** At the end of each lab, update the corresponding
   track's PROGRESS.md with: what was done, technical decisions made,
   problems encountered, and how they were solved.
6. **Close with a commit.** At the end of each completed lab, propose the
   commit (clear message, e.g. "Lab 00: Docker + WSL2 installation") and
   only run `git add/commit/push` with my confirmation.

## Style

- Working conversation language: **Portuguese**. All written deliverables
  in this repository (READMEs, roadmaps, progress logs, lab docs) are in
  **English**, since this portfolio targets global teams — but Claude and
  the user keep talking to each other in Portuguese.
- Direct, no fluff. Exact, copy-paste-ready commands when I'm meant to run
  them.
- Correct me bluntly if something is technically or conceptually wrong.
- Honest trade-off assessments (e.g. n8n vs. plain code, RAG vs.
  fine-tuning) — never sell the trendy tool without critique.
- Whenever it makes sense, connect the lab to how it would translate into
  an interview conversation ("this shows you know X, Y").

## Repository structure

```
/01-n8n/
  ROADMAP.md              → phases of the n8n track
  PROGRESS.md             → log of completed labs
  lab-00-setup/
  lab-01-core-concepts/
  lab-02-azure-devops-connection/
  lab-03-real-workflow/
  lab-04-export-documentation/

/02-ai-agents/
  ROADMAP.md

/03-rag/
  ROADMAP.md

/04-skills/
  ROADMAP.md

/05-advanced-fhir/
  ROADMAP.md

/06-salesforce/
  ROADMAP.md

/07-slack/
  ROADMAP.md

/08-fine-tuning/
  ROADMAP.md
```

Each lab folder, once finished, should contain:
- Exported file/workflow (JSON, script, etc.)
- Lab-specific README.md (what, why, how to run, what I learned)

## Current status

Active track: **n8n**. Lab 00 (Docker + WSL2 + n8n setup) and Lab 01 (core
concepts) completed on 2026-09-02. Next up: Lab 02 (Azure DevOps connection).
See `/01-n8n/PROGRESS.md` for the detailed history.
