---
name: spec-driven-research
description: Plan, carry out and check one piece of research work through written specs. Use when the researcher wants to set up project files (mission, tech stack, roadmap), plan a roadmap item, implement an agreed spec, validate finished work, or pick up the next task in a new session.
---

# Spec-driven research

Work through files, not chat history. A new session must be able to continue from the files alone.

## Files

```
specs/
  mission.md        what the project is for, who it is for, its rules
  tech-stack.md     language, packages, data locations, commands that run things
  roadmap.md        numbered list of small tasks, ticked when done
  log.md            one line per finished task (date, task, result), append only
  YYYY-MM-DD-short-name/      one folder per task
    requirements.md goal, scope, sample and definitions, what done looks like; Status line
    plan.md         the approach and the steps, in small groups that can each be checked
    validation.md   checks that could fail, with expected values where known
    decisions.md    choices made along the way, who made them, and why
    artifacts/      working files: scratch scripts, tests, intermediate outputs
```

## Templates

Every file above has a starting template in this skill's `templates/` folder (`templates/project/` and `templates/task/`, next to this file).

- Start each new spec file by copying its template into `specs/`. Never edit the templates themselves.
- Keep the headings. Fill each section, then delete its guidance comment.
- If a section has nothing in it, write `None`, or `Open:` and the question. Do not delete it.
- The comments say who decides each section: *you* means the researcher, *agent* means you fill it in yourself from the files.

## What to ask, and what to decide yourself

Sort each choice into one of three kinds before you ask anything.

**Research decisions: ask.** Choices where researchers could reasonably differ, and where the answer changes what the result means:

- who is in the sample and who is left out;
- how each variable is defined: its groups, categories and units;
- how missing codes, special codes and zeros are treated;
- which comparison or model answers the question;
- what the output should show, if the roadmap item does not already say.

**Conventions: do not ask.** Where there is a standard choice that most researchers would make without discussion, make it yourself. List each one under "Defaults the agent chose" in `requirements.md`, one line each, so the researcher can overrule it when they review the spec. Examples: dividing by n − 1 for a sample variance or standard deviation, 95% confidence intervals, a t interval for a mean, how numbers are rounded, the order of rows, the styling of a chart, file names and formats.

**Facts: look them up.** Column names, codes, units and ranges are in the codebook. Check them yourself.

## How to ask

- Ask **one question at a time** and wait for the answer.
- Use plain words, with no formulas or statistical shorthand. The researcher may not be a statistician.
- Ask open questions. **Do not suggest answers, list options or give a recommendation**, unless the researcher explicitly asks for help with that question. If they do, label it as a suggestion and wait for their choice.
- Do not ask for anything the researcher has already told you, in the chat or in the spec files.
- A task rarely needs more than five questions. If you have more, ask the ones that would change the result most and write the rest under "Open questions".
- Record only what the researcher actually decided. If a decision is still open, write it down as open.

## 0. Find the spec, or start one

At the start of every session:

1. If `specs/mission.md`, `tech-stack.md` or `roadmap.md` does not exist, go to step 1.
2. Otherwise read `specs/mission.md`, `roadmap.md` and `log.md`, and the `Status:` line of each `specs/*/requirements.md`.
3. If a task folder's status is not `done`, that task is in progress: read its files (ticked steps in `plan.md` show where it got to) and carry on from there.
4. Otherwise the next task is the first unticked roadmap item. Confirm it with the researcher, then go to step 2.

## 1. Project files (once per project)

Do this first if `specs/mission.md`, `tech-stack.md` or `roadmap.md` does not exist yet. Write only the missing files.

Interview the researcher for `mission.md` and `roadmap.md`. Use what they have already told you, and ask only for what is still missing. Fill in `tech-stack.md` yourself from `AGENTS.md` and the project files. Copy an empty `log.md`. Keep each file short. The roadmap is a list of small tasks; each should be doable and checkable in one sitting. Show the files and stop for review.

## 2. Plan one task

1. Read `specs/mission.md`, `tech-stack.md`, `roadmap.md`, `log.md`, and the `requirements.md` and `decisions.md` of any finished task this one depends on.
2. Confirm which roadmap item this is. Create `specs/YYYY-MM-DD-short-name/` (today's date) and copy the four task templates into it.
3. Interview the researcher about the research decisions, as above.
4. Fill in `requirements.md`, `plan.md` and `validation.md`. List the conventions you chose under "Defaults the agent chose". Every check in `validation.md` must be able to fail. Prefer checks with a number you can compare against, such as a count from the raw file or one value worked out by hand.
5. Show the three files and stop. Point out the defaults you chose and ask whether any should change. **Do not write or run analysis code until the researcher has approved the spec.** When they approve, set `Status: approved`.

## 3. Implement

1. Read the task's files. If `Status:` is still `draft`, ask once whether the researcher has approved the spec. If yes, set it to `approved` and carry on.
2. Follow `plan.md`, one group of steps at a time if asked. Tick each step as it is done.
3. If something comes up that would change the research design, stop and ask. Do not decide it yourself.
4. Record any choices in `decisions.md`, with who made them.
5. Run the code from a clean start and report what you ran and what it produced.

## 4. Validate

1. Go through `validation.md` check by check. Fill in the `## Completed` table: each check, its result (pass / fail / not checked) and the evidence (a number, a file, a line of output).
2. Never mark a check as passed without evidence.
3. If the researcher asks for a change, change the spec files **and** the code together, so they stay in step.

## 5. Close out

1. Set `Status: done` in `requirements.md`.
2. Add one line to `specs/log.md`.
3. Tick the task in `specs/roadmap.md`, and add anything learned that affects later tasks under "Learned along the way".
4. Check whether the project files need updating in light of this task:
   - `mission.md`: a new rule, or a change to the question or the audience;
   - `roadmap.md`: a later task that should change, split, move, be dropped or be added;
   - `tech-stack.md`: a new package, command or data location.
   Update `tech-stack.md` yourself, since it holds facts. Changes to the mission or the roadmap are the researcher's: say what you noticed and why it matters, ask, and change them only as they decide. If nothing needs changing, say so.
5. Ask the researcher whether the next roadmap item still looks right.
