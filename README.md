# CU-URC-2027 rover project

Project context for the University Rover Challenge capstone: authoritative
competition sources, the team’s traceable requirements, architecture decisions,
and evidence-backed research.

## Layout

```text
AGENTS.md                         Codex project instructions
docs/source/                      Immutable source material and source index
docs/requirements/                Testable, traceable team requirements
docs/architecture/                Architecture decisions and diagrams
docs/research/                    Research briefs and evidence
```

## First setup

1. Add the current official rulebook as `docs/source/URC-rulebook.pdf`.
2. Add official URC pages and their retrieval dates to
   `docs/source/urc-website-sources.md`.
3. Translate rules into testable entries in
   `docs/requirements/master-requirements.md`; retain rulebook references.
4. Start Codex from this repository root when researching or making rover
   design decisions, so it loads `AGENTS.md`.

The agent package is maintained separately in the sibling
[`agents`](../agents) repository. Install/update it through the team marketplace;
do not copy its skills or dependencies into this repository.

## Publishing this repository

Create a **private** GitHub repository named `CU-URC-2027/rover-project`, then
from this directory run:

```text
git remote add origin https://github.com/CU-URC-2027/rover-project.git
git push -u origin main
```

Use feature branches and pull requests after the initial publication.
