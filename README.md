# Agentic coding for social scientists: course project

This is the project you will work in during the course (Heriot-Watt, Thursday 26 November 2026). It holds a **simulated** survey of 2,000 adults covering work, care and wellbeing, and a few small scripts.

You won't need to type commands. You ask the agent, it proposes what to run, and you approve or decline.

## Before the course (about 20 minutes)

### 1. Get the project

On the course's GitHub page choose **Code → Download ZIP**, then unzip it somewhere you can find, such as `Documents`. Keep it apart from your real research files.

(Can't install software on your laptop? Use [the browser-only route](CODESPACES.md) instead.)

### 2. Install VS Code

Download **VS Code** from [code.visualstudio.com](https://code.visualstudio.com), install it and open it. It's a free editor: your files and the agent sit side by side in one window.

### 3. Add an agent to VS Code

1. Open the Extensions view: click the icon of four squares in the left-hand bar, or choose **View → Extensions**.
2. Search for **Codex** and install *Codex – OpenAI's coding agent* (publisher: OpenAI).
3. Click the Codex icon that appears in the left-hand bar and sign in with your ChatGPT account. A free account is enough.

If you already use Claude, you can install the **Claude Code** extension (publisher: Anthropic) instead.

Prefer a dedicated app? The ChatGPT desktop app (which includes Codex) or the Claude desktop app work too. In step 4, open the folder from inside the app instead.

### 4. Open the project

In VS Code choose **File → Open Folder…** and pick this folder (the one containing this README). When VS Code asks whether you **trust** the authors of the files, say yes. Then open the agent's panel from the left-hand bar; if the agent also asks whether to trust the folder, say yes again.

### 5. Paste the setup prompt

Copy this into the chat:

> Set up this project for the course. Find a Python 3.10 or newer on this computer. Create a Python environment called `.venv` inside this folder and install `requirements.txt` into it. Then use that environment to run `scripts/00_check_environment.py`, `scripts/check_data.py` and `scripts/01_first_output.py`. Also check whether git is installed. Tell me in plain words what worked, what didn't, and what I need to do.

The agent will ask, in its panel, to use the internet to download packages. Read the request, then approve it.

If Python or git is missing, ask the agent to explain how to install it on your computer, then follow its steps. It can't install system software for you without your approval.

### 6. Check it worked

You're ready when:

- `outputs/01-first-output/age_distribution.png` exists. Open it: it's a histogram of ages.
- The agent reports that the environment check and the data check passed.
- The agent reports a git version.

If you get stuck, copy the agent's last message and email it to us before the course. Please don't spend your free allowance asking it to retry the same thing over and over.

## What's in here

| Path | What it is |
|---|---|
| `AGENTS.md` | Instructions the agent reads at the start of every chat (`CLAUDE.md` points to it) |
| `data/raw/work_care_wellbeing.csv` | The survey. Never edit it. |
| `data/README.md` | The codebook. Read it before trusting any number. |
| `data/fixtures/` | Small tables for plotting and hand checks |
| `scripts/` | Small analysis scripts |
| `permissions/ask-first.toml` | Strict permission settings. They do nothing until you switch them on. |
| `.agents/skills/` | Skills for Codex (`.claude/skills/` is the same, for Claude Code) |
| `specs/`, `notes/` | Where your specs and notes go |

All the data are invented. Don't bring real or confidential research data to the course.
