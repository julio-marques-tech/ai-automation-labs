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
