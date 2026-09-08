# Progress — RAG Track

Log of completed labs, technical decisions, and problems solved along the track.

## Lab 00 — Scoping and Fundamentals

**Status:** completed (2026-09-06)

**Done:**
- Wrote a consultant-style [scoping note](lab-00-scoping-fundamentals/scoping-note.md)
  framing the track around a realistic engagement: a healthcare
  interoperability team needing a traceable FHIR documentation assistant
- Set up a local, zero-cost embedding pipeline (`sentence-transformers`,
  `all-MiniLM-L6-v2`) in its own virtual environment (`03-rag/.venv`)
- Confirmed embeddings capture meaning, not just shared vocabulary:
  0.799 similarity between paraphrased FHIR sentences vs. -0.099 for an
  unrelated sentence

**Technical decisions:**
- Local embeddings + (in Lab 01) ChromaDB instead of a paid embeddings
  API — keeps the self-hosted, zero-ongoing-cost pattern from the
  Ollama setup in the AI Agents track
- Scoped the engagement around one FHIR version and a lookup assistant,
  not a production system — deliberately, per the scoping note's
  non-goals

**Details:** see [lab-00-scoping-fundamentals/README.md](lab-00-scoping-fundamentals/README.md)

## Lab 01 — Real RAG Pipeline

**Status:** completed (2026-09-08)

**Done:**
- Fetched 3 real HL7 FHIR R4 resource pages (Patient, Observation,
  Encounter) as the corpus
- Built `ingest.py` (chunk + embed + store in Chroma) and `query.py`
  (retrieve + ask Claude, grounded, with citations)
- Verified grounded, cited answers on an in-corpus question
  (`Patient.gender`) and an honest refusal on an out-of-corpus question
  (`Condition.severity` — that resource was never ingested)

**Technical decisions:**
- Paragraph-grouped chunking (~800 chars) instead of arbitrary
  fixed-length cuts, to keep chunks semantically coherent
- Explicit prompt instruction to cite sources and refuse ungrounded
  answers — not automatic just from retrieving relevant text

**Result:** both scoping-note success criteria (traceable citations,
honest "don't know") held on first real test. Full detail in
[lab-01-fhir-rag-pipeline/README.md](lab-01-fhir-rag-pipeline/README.md#results)
