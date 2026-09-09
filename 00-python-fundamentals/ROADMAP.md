# Roadmap — Python Fundamentals Track

Programming fundamentals from zero, built specifically to support the
other tracks in this repository (RAG, AI Agents, Prompt Engineering,
Fine-tuning) rather than as a standalone CS course. Every lab closes with
a small exercise tied to a concrete AI-track use case instead of a
generic textbook exercise.

## Execution order

1. **Lab 00 — Setup** — installing Python, a virtual environment, an
   editor, running a first script from the command line
2. **Lab 01 — Core syntax and data types** — variables, numbers, strings,
   booleans, type conversion; exercise: parsing a FHIR-like patient
   record represented as a Python dict
3. **Lab 02 — Control flow and functions** — `if`/`elif`/`else`, loops,
   functions, exceptions; exercise: validating and filtering a list of
   FHIR-like resources
4. **Lab 03 — Data structures in depth** — lists, dicts, sets, tuples,
   comprehensions; exercise: transforming a small JSON dataset
5. **Lab 04 — Files, modules, venv and packages** — reading/writing
   files, the `json` module, `pip`, `requirements.txt`, organizing a
   project into modules; exercise: persist and reload structured data as
   JSON
6. **Lab 05 — OOP basics** — classes, objects, methods, inheritance;
   exercise: modeling a simple `Agent`/`Tool`-style class, foreshadowing
   the patterns used in the AI Agents track
7. **Lab 06 — APIs and capstone** — the `requests` library, calling a
   real REST API, parsing a JSON response; capstone exercise that
   connects directly to the skills needed in the RAG and AI Agents tracks

## Status

See [PROGRESS.md](PROGRESS.md) for the detailed log of each lab.
