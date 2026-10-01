# Progress — BDD & Test Automation Track

Log of completed labs, technical decisions, and problems solved along the track.

## Warm-up — First executable feature file with `behave`

**Status:** completed (2026-09-30) — off-roadmap, done ahead of Lab 00

**Done:**
- Wrote a Portuguese-language feature file (`# language: pt`) with tags,
  user-story narrative, `Contexto` (Background) and two scenarios (happy
  and negative path) in declarative style
- Saw the full cycle: undefined steps → step definitions (with a
  parameter and reused steps) → green → deliberately red → execution
  filtered by tags (`--tags=@smoke`)
- System under test is simulated (a plain Python function) — a proof of
  concept, not automation against a real application

**Technical decisions:**
- `behave` instead of the roadmap's `pytest-bdd` for this warm-up only:
  most direct first run, and console output closest to Cucumber. The
  roadmap is unchanged
- Run as `python -m behave` instead of the `behave.exe` launcher (see
  problems)

**Problems and fixes:**
- `ConfigError: No steps directory` — `behave` requires `features/steps`
  to exist before the first run
- Windows Application Control (Smart App Control) blocked the unsigned
  `behave.exe` launcher created by pip in the venv — solved by running it
  as a module through the signed `python.exe`; security policy left
  untouched
- Step text must match the step definition exactly — a wording fix in the
  feature ("informado de que") had to be applied to the code as well

**Details:** see [warmup-behave/README.md](warmup-behave/README.md)
(in Portuguese for now; English version pending)

Next up: Lab 00 (feature file craft).
