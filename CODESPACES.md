# The browser-only route: GitHub Codespaces

Use this if you can't install software on your laptop. Codespaces gives you VS Code in the browser, running on a cloud computer with Python, git, Codex and Claude Code already installed.

**What you need**

- A free GitHub account.
- A ChatGPT account for Codex (a free one is enough), or a paid Claude plan for Claude Code.

## Set it up (about 15 minutes, before the course)

1. On the course's GitHub page choose **Use this template → Create a new repository**. Make it **private**.
2. In your new repository choose **Code → Codespaces → Create codespace**. Wait while it builds; the first time takes a few minutes.
3. When the build log says **Course setup complete**, open `outputs/01-first-output/age_distribution.png` in the file list.
4. Click the **Codex** or **Claude Code** icon in the left sidebar and sign in.
   For Codex, first turn on device-code sign-in: at chatgpt.com go to **Settings → Security & login** and enable *device code sign-in*. Then choose that option in VS Code and enter the code it shows you.
5. Ask the agent: *"Read AGENTS.md and tell me how to run Python in this project."*

If something fails, copy the error and email it to us.

## Keep your work

- Ask the agent to **commit and push** your changes; your repository is where your work lives.
- Figures in `outputs/` are not saved to git. To keep them, right-click a file and choose **Download**.
- Stop the codespace when you're done (github.com/codespaces). You can reopen the same one later.

## On the day

Everything works the same as on a laptop, because it is the same VS Code. Where an exercise says "your app", use the VS Code instructions.
