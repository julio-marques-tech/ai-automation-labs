# Roadmap — SQL & Data Modeling Track

A structured refresher, not a from-zero course. Prior exposure comes from
the business/functional side of data projects (ODI/ODS data integration,
QlikView/Qlik Sense BI) — strong on structure and concepts, rusty on
writing SQL hands-on. The goal is solid, interview-ready SQL for
functional analysis: modeling data, validating requirements, and
supporting development and QA teams.

## Execution order

1. **Lab 00 — Setup and querying basics** — PostgreSQL via Docker (reusing
   the Docker setup from the n8n track) and DBeaver as client; `SELECT`,
   `WHERE`, `ORDER BY`, `LIMIT`, `NULL` handling, basic functions.
2. **Lab 01 — Data modeling** — entities, keys, cardinality,
   normalization (1NF–3NF) and when to denormalize; DDL (`CREATE TABLE`,
   constraints). Domain: FHIR-inspired (Patient, Practitioner,
   Appointment, Encounter). Deliverable includes an ER diagram (Mermaid).
3. **Lab 02 — Joins and aggregation** — `INNER`/`LEFT`/`FULL` joins,
   `GROUP BY`/`HAVING`, subqueries, `CASE`; exercise: answering business
   questions written as acceptance criteria.
4. **Lab 03 — Analytical SQL and data validation** — CTEs, window
   functions, and the queries a functional analyst actually runs to
   validate requirements: orphan records, duplicates, reconciliation
   between source and target (the ODI/ODS pattern), data quality checks
   usable by QA.
5. **Lab 04 — SQL in practice (capstone)** — querying PostgreSQL from
   Python (`psycopg`), SQL as `Then` steps in BDD scenarios (bridge to the
   BDD track), and a first look at `pgvector` as a vector store (bridge to
   the RAG track). *Requires Python Fundamentals Lab 04.*

## Technical decisions

- **PostgreSQL over SQL Server/Oracle:** free, runs in Docker, standard
  SQL, and `pgvector` connects it directly to the RAG track. Dialect
  differences (e.g. `TOP` vs `LIMIT`) are noted as they appear.
- **DBeaver as client:** built on the Eclipse platform, so it also builds
  familiarity with the Eclipse IDE environment.

## Status

See [PROGRESS.md](PROGRESS.md) for the detailed log of each lab.
