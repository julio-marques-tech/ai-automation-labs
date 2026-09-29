# Roadmap — BDD & Test Automation Track

Taking Gherkin feature files beyond documentation: from well-written
specifications to executable scenarios, browser automation, and living
documentation in CI. Built to close a concrete gap observed in practice —
scenarios written inside Use Cases that were never executed, integrated,
or automated.

**Starting point:** intermediate on the *writing* side (already authors
Gherkin scenarios, assisted by Atlassian Rovo, inside Use Case
documentation); zero on the *execution* side (step definitions, test
runners, Cucumber, Playwright, CI).

## Execution order

1. **Lab 00 — Feature file craft** — no code. Refactoring and critiquing
   scenarios rather than learning syntax from zero: declarative vs
   imperative style, `Background`, `Rule`, `Scenario Outline`/`Examples`,
   tags, common anti-patterns. Includes a structured review of
   AI-generated (Rovo-style) Gherkin against a quality checklist, and
   traceability user story → acceptance criteria → scenario. Domain:
   FHIR-inspired appointment scheduling. *Can start now.*
2. **Lab 01 — Executable specifications in Python** — `pytest-bdd`: step
   definitions, fixtures, running a `.feature` file, red → green cycle,
   test reports. *Requires Python Fundamentals Lab 04.*
3. **Lab 02 — Browser automation with Playwright** — Gherkin steps
   driving a real web UI through Playwright (`pytest-playwright`):
   locators, assertions, screenshots/traces on failure. The "Playwright
   in the middle" step that turns a scenario into an end-to-end test.
4. **Lab 03 — Cucumber-JVM in Eclipse on Linux** — the same feature file
   executed with Cucumber (Java + Maven) inside Eclipse, running on
   Linux via WSL2. Minimal Java, guided — the goal is hands-on
   familiarity with the actual Cucumber toolchain, not Java proficiency.
5. **Lab 04 — BDD for AI systems** — Gherkin acceptance criteria for the
   RAG pipeline (e.g. out-of-corpus questions must be refused, answers
   must cite a source), executed against the real system; includes SQL
   `Then` steps for data validation (bridge to the SQL track).
   *Requires RAG Lab 02 and SQL Lab 03.*
6. **Lab 05 — Living documentation in CI (capstone)** — features run
   automatically in GitHub Actions on every push, publishing an HTML
   report readable by business stakeholders. Closes the full loop:
   Use Case → feature file → automation → CI report.

## Technical decisions

- **`pytest-bdd` over `behave` for Python:** `behave` feels closer to
  Cucumber, but `pytest-bdd` plugs directly into the `pytest` ecosystem
  (`pytest-playwright`, fixtures, reporting plugins), which is what the
  Playwright and CI labs need. Cucumber proper is covered in Lab 03.
- **Cucumber-JVM kept small on purpose:** Java is not a target skill of
  this portfolio; one working Eclipse + Maven + Cucumber project is
  enough to speak credibly about the toolchain.

## Status

See [PROGRESS.md](PROGRESS.md) for the detailed log of each lab.
