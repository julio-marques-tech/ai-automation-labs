# Lab 00 — Setup

## What

Confirmed a working Python setup for this track: interpreter installed,
an isolated virtual environment, and a first script run end-to-end from
the VS Code integrated terminal.

## Why

Every later lab in this track (and the scripts in RAG/AI Agents) depends
on a working Python + venv setup. Getting this right once, and
understanding *why* each piece exists, avoids silent "works on my
machine" issues later.

## How to run

```bash
cd 00-python-fundamentals
python -m venv .venv
.venv\Scripts\Activate.ps1
python lab-00-setup\hello.py
```

Expected output:

```
Hello, Python!
Python version: 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)]
```

(exact version string will match whatever Python is installed locally)

## What I learned

- Python 3.14.7 is installed on this machine
- `python -m venv .venv` creates an isolated interpreter copy per track,
  so dependencies installed later (`pip install ...`) don't leak into
  other tracks — same pattern already used in `03-rag/.venv`
- Activation (`.venv\Scripts\Activate.ps1` on Windows PowerShell) is what
  makes `python`/`pip` in that terminal point at the venv instead of the
  system Python; the `(.venv)` prefix in the prompt is the visual
  confirmation
- `.venv/` is already covered by the repo's root `.gitignore` — no extra
  setup needed per track
- `import sys` loads a standard-library module (no install needed) that
  exposes interpreter info like `sys.version`
- f-strings (`f"...{expr}..."`) embed expressions directly in a string
  without manual concatenation
