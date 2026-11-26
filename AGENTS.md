# Work, care and wellbeing

A descriptive study of how work, care and wellbeing relate, using a **simulated** survey of 2,000 adults. Nothing here is evidence about real people.

## How to work here

- Run Python with the project's own environment: `.venv/bin/python` (on Windows: `.venv\Scripts\python.exe`). If `.venv` does not exist yet, follow the setup prompt in `README.md`.
- Never change anything in `data/raw/`. Save scripts in `scripts/` and outputs in `outputs/`. Use relative paths.
- Do not use the internet, install packages or change settings outside this folder unless I ask.
- Research choices are mine: who is in the sample, how variables are defined, how missing values are treated, which model to use. Ask me; do not decide for me.
- Where there is a standard convention (for example, dividing by n − 1 for a standard deviation), use it without asking and tell me which one you used.
- Explain what you changed in plain words. Keep command output short. Use British spelling.
- For a piece of analysis with a spec, use the `spec-driven-research` skill (`.agents/skills/spec-driven-research/SKILL.md`). If the skill is not found automatically, read that file.

## Scripts

- `scripts/00_check_environment.py` checks that Python 3.10+ and numpy, pandas, matplotlib and scipy are installed. It reads no data.
- `scripts/check_data.py` checks the raw CSV: 2,000 rows, unique IDs, documented ranges and codes. It changes nothing.
- `scripts/01_first_output.py` makes the age histogram: `outputs/01-first-output/age_distribution.png` and `summary.csv`.
- `scripts/02_inherited.py` makes mean life satisfaction by employment status in `outputs/02-life-satisfaction/`. It came from a previous research assistant and **has not been checked**. Do not trust its numbers or copy its approach until it has been.
- `scripts/03_plot_inputs.py` draws two plain plots from the small tables in `data/fixtures/` into `outputs/03-plain-plots/`.
- Run order for a fresh copy: `00_check_environment.py`, then `check_data.py`, then `01_first_output.py`. The others can run in any order.
- Each script writes only to its own folder under `outputs/`, and creates that folder if needed.
- Figures: save PNG at 180 dpi.

## Data notes

- The main file is `data/raw/work_care_wellbeing.csv`. Its codebook is `data/README.md`.
- −8 means don't know, −9 means refused, −7 means not applicable (only in `commute_minutes`, for people not in paid work). None of these is zero.
- Zero is a real value for life satisfaction, care hours and social contact, and for the commute of a fully remote worker.
