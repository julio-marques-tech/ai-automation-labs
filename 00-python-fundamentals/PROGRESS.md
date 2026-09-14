# Progress — Python Fundamentals Track

Log of completed labs, technical decisions, and problems solved along the track.

## Lab 00 — Setup

**Status:** completed (2026-09-14)

**Done:**
- Confirmed Python 3.14.7 already installed
- Created and activated an isolated virtual environment (`.venv`), same
  pattern already used in `03-rag/.venv`
- Wrote and ran `hello.py` from the VS Code integrated terminal — first
  contact with `import`, `print`, and f-strings

**Technical decisions:**
- Per-track `.venv` instead of one shared environment for the whole
  repo, to keep dependency versions isolated between tracks
- No new `.gitignore` entry needed — `.venv/` is already covered by the
  repo's root `.gitignore`

**Details:** see [lab-00-setup/README.md](lab-00-setup/README.md)
