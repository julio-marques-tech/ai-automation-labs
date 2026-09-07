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

1. **n8n** — workflow automation, self-hosted via Docker (COMPLETE)
2. **AI Agents** — agent architecture, orchestration (COMPLETE)
3. **RAG** (Retrieval-Augmented Generation) — theory and practical application (IN PROGRESS)
4. **Prompt Engineering** — advanced prompting strategies, evaluation/
   benchmarking, lifecycle/governance (added after analyzing 3 real job
   postings the user is targeting — see note below)
5. **Fine-tuning** — functional understanding of the AI model lifecycle
   (training, fine-tuning, inference), with a light hands-on fine-tune of
   a small local model. Moved up in priority (was originally last) since
   it appears explicitly in 2 of the 3 target job postings
6. **Skills** — building and integrating reusable skills
7. **Advanced FHIR** — deepening existing professional expertise from SPMS
8. **Salesforce** — fundamentals + Trailhead track
9. **Slack** — integrations and automations

Execution order within the n8n track: Azure DevOps → Simple AI Agent (both
done). **Future cross-track capstone:** "Content Factory" — an end-to-end
automated content pipeline combining n8n with the AI Agents track (and
possibly RAG), to be tackled once those tracks are further along.

### Job-posting-driven scope (2026-09-07)

The user shared 3 real job postings they're targeting (Prompt Engineer @
Hitachi Energy — industrial/GenAI; Prompt/Agent role @ eXperience IT
Solutions, Spain, remote; Analista Funcional GenAI @ Soltel Group). Cross-
referencing them against the existing roadmap led to:
- Adding the **Prompt Engineering** track (zero-shot/few-shot/Chain-of-
  Thought/ReAct, prompt chaining, context injection, evaluation &
  benchmarking, prompt lifecycle/versioning/governance, Responsible AI)
- Reprioritizing **Fine-tuning** to come right after Prompt Engineering
- Explicit low-effort additions decided to close remaining gaps:
  - Actually use **MLflow** (not just describe it) in Prompt Engineering's
    benchmarking lab
  - Produce at least one **UML/BPMN-style architecture diagram** somewhere
    in the upcoming tracks
  - Pull and try **Mistral or Gemma via Ollama** (in addition to Llama) for
    model variety in benchmarking
  - Touch **Azure AI Foundry** hands-on (even minimally), not leave it as
    just a note

**Honest gaps flagged and accepted as out of scope:** Kubernetes, OAuth2/
Keycloak/LDAP, Jira, Confluence (specific tools, not AI skills — learnable
on the job) and the Hitachi posting's electrical-engineering/transformer-
industry domain requirement (a hard mismatch no portfolio project can
close).

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

- All written deliverables in this repository (READMEs, roadmaps, progress logs, lab docs)
  are in  **English**, since this portfolio targets global teams — but Claude and
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
  README.md                → track overview (complete)
  ROADMAP.md               → phases of the n8n track
  PROGRESS.md              → log of completed labs
  lab-00-setup/
  lab-01-core-concepts/
  lab-02-azure-devops-connection/
  lab-03-simple-ai-agent/

/02-ai-agents/
  README.md                → track overview (complete)
  ROADMAP.md               → phases of the AI Agents track
  PROGRESS.md              → log of completed labs
  lab-00-fundamentals-setup/
  lab-01-agent-from-scratch/
  lab-02-multi-tool-orchestration/
  lab-03-multi-agent-coordination/

/03-rag/
  ROADMAP.md

/04-prompt-engineering/
  ROADMAP.md

/05-fine-tuning/
  ROADMAP.md

/06-skills/
  ROADMAP.md

/07-advanced-fhir/
  ROADMAP.md

/08-salesforce/
  ROADMAP.md

/09-slack/
  ROADMAP.md
```

Each lab folder, once finished, should contain:
- Exported file/workflow (JSON, script, etc.)
- Lab-specific README.md (what, why, how to run, what I learned)

## Current status

**n8n track complete** (Labs 00-04: setup, core concepts, Azure DevOps
connection, self-hosted AI agent, export/documentation). See
`/01-n8n/README.md` for the track overview and `/01-n8n/PROGRESS.md` for
the detailed history.

**AI Agents track complete** (Labs 00-04: fundamentals/setup, agent from
scratch, multi-tool orchestration, multi-agent coordination, comparison
and documentation). See `/02-ai-agents/README.md` for the track overview
and `/02-ai-agents/PROGRESS.md` for the detailed history.

Active track: **RAG** — Lab 00 (scoping and fundamentals) completed on
2026-09-06. Next up: Lab 01 (real RAG pipeline over FHIR documentation).
See `/03-rag/PROGRESS.md` for the detailed history.
