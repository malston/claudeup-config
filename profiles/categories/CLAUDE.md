# Category Profiles

Skill-category profiles organize plugins by what you're trying to accomplish.
Each category is a self-contained capability unit (plugins, rules, skills, agents, hooks).

## Categories

| Category     | Scope   | Purpose                                       |
| ------------ | ------- | --------------------------------------------- |
| code-quality | user    | Review, simplification, style enforcement     |
| testing      | project | TDD, verification, debugging, e2e             |
| security     | user    | SAST, hardening, threat modeling              |
| vcs          | user    | Git workflows, commits, PRs                   |
| memory       | user    | Persistence, vault, session continuity        |
| reference    | user    | Library docs, documentation, reference skills |
| productivity | user    | Orchestration, planning, parallel dispatch    |
| migration    | project | Framework upgrades, legacy modernization      |
| tooling      | user    | Claude Code config, plugin dev, HUD           |

## Usage

Single category: `--base-profile base --profile categories/code-quality`

Via stack: `--base-profile base --profile stacks/go-backend`

## Design

See `docs/superpowers/specs/2026-03-20-skill-category-profiles-design.md`
