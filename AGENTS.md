# CU-URC-2027 rover project instructions

## Purpose

This repository contains the team’s project context: competition sources,
derived requirements, architecture decisions, and research. The reusable Codex
agents live in the sibling `../agents` repository and must not be copied here.

## Read before advising or changing engineering work

1. Read `docs/requirements/master-requirements.md`.
2. Read the relevant section of `docs/source/URC-rulebook.pdf` when it is
   available locally.
3. Read relevant architecture decisions and research notes before proposing a
   design change.

Do not treat a web search result, an old note, or a model inference as a
competition rule.

## Authority and traceability

- The current URC rulebook is authoritative for competition rules.
- `master-requirements.md` records team-derived, testable requirements. Every
  requirement should cite its rulebook section or other source.
- Architecture documents record decisions and their rationale; they do not
  override rules or approved requirements.
- Research documents record evidence and uncertainty; they are not approved
  requirements unless explicitly promoted into the requirements document.
- Clearly label statements as a **rule**, **derived requirement**,
  **assumption**, or **recommendation**.
- When rules conflict with an existing document, report the conflict and update
  the derived document only after team direction.

## Document practices

- Keep source files unchanged under `docs/source/`; use Markdown notes to
  summarize or interpret them.
- Give requirements stable IDs such as `REQ-MOB-001` and preserve them when
  editing.
- Cite rulebook sections, source URLs, and retrieval dates where applicable.
- Put architecture decisions in `docs/architecture/` and research briefs in
  `docs/research/`.
- Do not commit passwords, API keys, access tokens, private personal data, or
  virtual environments.

## Before completing work

State what sources were used, list affected requirement IDs or architecture
documents, and call out unresolved assumptions or rule interpretations that
need team review.
