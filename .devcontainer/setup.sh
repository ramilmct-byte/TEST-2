#!/usr/bin/env bash
# Codespaces setup for the course project. UNTESTED as of 15 Nov 2026: rehearse
# in a fresh codespace before relying on it, then pin the versions that worked.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

# Codex's Linux sandbox uses bubblewrap.
sudo apt-get update -qq && sudo apt-get install -y -qq bubblewrap

# Project Python environment, the same layout as on a laptop.
python3 -m venv .venv
.venv/bin/python -m pip install -q -r requirements-tested.txt

# Agents. Pin versions here once a rehearsal has passed.
npm install --global @openai/codex @anthropic-ai/claude-code

git --version
codex --version || true
claude --version || true
.venv/bin/python scripts/00_check_environment.py
.venv/bin/python scripts/check_data.py
.venv/bin/python scripts/01_first_output.py

cat <<'MESSAGE'

Course setup complete. Open outputs/01-first-output/age_distribution.png.
Next: open the Codex (or Claude Code) panel in the left sidebar and sign in.
See CODESPACES.md.
MESSAGE
