# Lab 01 — Real RAG Pipeline

## What

A working RAG pipeline answering questions about the FHIR specification,
grounded in real, official HL7 FHIR R4 documentation — not the model's
training memory — with a citation for every claim.

## Why

This is the pipeline the [scoping note](../lab-00-scoping-fundamentals/scoping-note.md)
called for: traceable answers a healthcare analyst could actually verify,
built the way a consultant would validate the core technique works before
scaling it to the full specification.

## Corpus

Three real FHIR R4 resource pages, fetched from the official specification
(`hl7.org/fhir/R4`) and stored as markdown in [`corpus/`](corpus/):
`patient.md`, `observation.md`, `encounter.md`. Chosen as three of the
most commonly referenced clinical resources — enough to prove the
pattern without ingesting the entire (much larger) specification.

## How it's built

- **[`ingest.py`](ingest.py)** — splits each document into ~800-character
  chunks (grouped by paragraph, never splitting one mid-sentence), embeds
  them locally (`sentence-transformers`), and stores them in a
  **Chroma** vector database persisted to disk (`chroma_db/`)
- **[`query.py`](query.py)** — takes a question, embeds it, retrieves
  the 3 closest chunks from Chroma, and sends them to Claude with an
  explicit instruction: answer using *only* this context, cite the
  source for every claim, and say so explicitly if the context doesn't
  contain the answer

## Results

**Grounded, cited answer** — asked about `Patient.gender`:
> Cardinality: 0..1 [Source: patient]
> Allowed values: male | female | other | unknown, bound via the
> AdministrativeGender value set (Required binding) [Source: patient]

Matches the real specification text exactly, with the citation as
instructed.

**Honest refusal on missing data** — asked about `Condition.severity`
(the `Condition` resource was deliberately never ingested):
> The provided context does not contain any information about
> `Condition.severity`... I cannot answer this question from the
> provided material.

No fabrication. This is the scoping note's most important success
criterion, and it held on the first real test.

## How to run

```powershell
& "03-rag\.venv\Scripts\Activate.ps1"
python "03-rag\lab-01-fhir-rag-pipeline\ingest.py"
python "03-rag\lab-01-fhir-rag-pipeline\query.py" "What is the cardinality of Patient.gender?"
```

## What I learned

- An end-to-end RAG pipeline: chunk → embed → store → retrieve →
  augment → answer, each step built and verified individually before
  connecting them
- Chunking by paragraph groups (rather than arbitrary fixed-length
  cuts) keeps each chunk semantically coherent, which matters for
  retrieval quality
- Explicitly instructing the model to cite sources and refuse ungrounded
  answers is a prompt-level decision, not something RAG gives you for
  free just by retrieving relevant text
- Retrieval isn't perfect even when it works: for the `Patient.gender`
  question, the second-closest chunk was from `encounter`, not
  `patient` — a reminder that "top-k" retrieval can surface some
  irrelevant chunks alongside the right one, which the next lab's
  quality work addresses directly
