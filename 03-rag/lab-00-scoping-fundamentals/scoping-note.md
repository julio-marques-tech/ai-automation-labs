# Scoping Note — FHIR Documentation Assistant

*A requirements note, written the way a consultant would frame a real
engagement before writing any code. The client below is fictional; the
knowledge domain (FHIR) and the problem it describes are real.*

## Client situation (fictional, but realistic)

A healthcare organization's interoperability team (analysts, developers)
spends significant time manually searching the FHIR specification —
hundreds of pages across resources, profiles, and implementation
guidance — to answer implementation questions ("what cardinality does
this field have," "which resource models this concept," "is this field
required or optional").

## The ask

An internal assistant that answers FHIR implementation questions in
natural language, **grounded in the actual specification text**, with a
citation back to the source section for every answer — so an analyst
can verify it, not just trust it blindly.

## Why this isn't "just ask an LLM directly"

1. **Version precision matters.** FHIR has multiple versions (R4, R4B,
   R5) with real differences. A model's general training knowledge can't
   reliably tell you which version a specific detail applies to, or may
   blend versions.
2. **Traceability is a hard requirement, not a nice-to-have.** In a
   regulated healthcare context, "the AI said so" is not an acceptable
   answer — every claim needs to point to a specific spec section a
   human can check.
3. **Confident wrong answers are the actual risk**, not "the AI doesn't
   know something." A model that hallucinates a plausible-sounding but
   incorrect cardinality or resource name is worse than one that says "I
   don't know."

This is precisely the shape of problem RAG is built for: grounding
answers in a specific, current, verifiable document set, rather than
depending on the model's own (unverifiable, potentially stale or
blended) training knowledge.

## Success criteria for this track

- Answers are grounded in real, official FHIR specification text (not
  paraphrased from the model's memory)
- Every answer can point back to the source chunk it came from
- Honest handling of "the docs don't cover this" rather than a
  fabricated answer
- A clear, defensible recommendation at the end on RAG vs. fine-tuning
  for this kind of problem, and what it would take to run this for real

## Non-goals for this track

- Not a production-grade system (no auth, no scaling, no multi-tenant
  data isolation)
- Not covering every FHIR version — one version, scoped deliberately, is
  enough to prove the pattern
- Not a replacement for a human's clinical/implementation judgment — an
  assistant that speeds up lookup, not a decision-maker
