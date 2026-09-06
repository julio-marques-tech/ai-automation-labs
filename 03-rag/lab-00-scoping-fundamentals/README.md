# Lab 00 — Scoping and Fundamentals

## What

Frame the RAG track as a real AI consulting engagement (not a generic
tech demo), explain the core RAG concepts, and set up a local,
zero-cost embedding + vector store environment.

## Why

Before writing any code, a consultant scopes the actual problem and why
the proposed approach fits it. See
[scoping-note.md](scoping-note.md) for the full requirements note: a
fictional healthcare interoperability team needs an internal assistant
that answers FHIR specification questions with traceable citations —
a problem where "confidently wrong" is worse than "doesn't know," which
is exactly what RAG (grounding answers in real documents) is built to
address, as opposed to relying on a model's own training knowledge.

## RAG fundamentals

- **Embedding** — converts a piece of text into a vector of numbers that
  captures its *meaning*, not its exact wording. Semantically similar
  texts end up with mathematically similar vectors.
- **Vector store** — a database specialized in finding the closest
  vectors to a new query, fast.
- **Chunking** — splitting long documents (like the FHIR spec) into
  smaller pieces, since retrieval works better over focused chunks than
  one giant document.
- **Retrieval + augmentation** — find the most relevant chunks for a
  question, then paste them into the prompt before asking the model to
  answer — grounding the answer in retrieved facts rather than the
  model's memory alone.

## Setup

- Own virtual environment for this track (`03-rag/.venv`), isolated from
  the AI Agents track's
- **`sentence-transformers`** (model: `all-MiniLM-L6-v2`) — generates
  embeddings locally, no API key, runs on CPU
- **`chromadb`** — local, file-based vector store (added in Lab 01)

Both chosen to keep the "self-hosted, zero ongoing cost" pattern from
earlier tracks (Ollama for AI Agents) rather than depending on a paid
embeddings API.

## Smoke test

Embedded three sentences: two paraphrases of the same FHIR concept
("Patient resource represents a person receiving healthcare") and one
unrelated sentence (stock market). Result:
- Related sentences: **0.799** cosine similarity
- Unrelated sentences: **-0.099** cosine similarity

Clear separation — confirms the embedding model correctly captures
meaning, not just shared words (the two related sentences share almost
no vocabulary).

## How to run

```powershell
& "03-rag\.venv\Scripts\Activate.ps1"
python "03-rag\lab-00-scoping-fundamentals\test_setup.py"
```

## What I learned

- How to scope an AI project the way a consultant would: define the
  client problem, why the proposed technique fits it, success criteria,
  and explicit non-goals — before touching code
- The four building blocks of RAG (embedding, vector store, chunking,
  retrieval+augmentation) and what each one is actually for
- Why RAG specifically fits problems where traceability and avoiding
  confident-but-wrong answers matter more than raw fluency — a concrete
  answer to "why not just ask the LLM directly"
- Local embeddings (`sentence-transformers`) as a zero-cost alternative
  to a paid embeddings API, consistent with this portfolio's self-hosted
  approach elsewhere
