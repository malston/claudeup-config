# Skill-Category Profiles Design

## Goal

Create a `category-profiles/` directory alongside the existing `profiles/` structure, organizing plugins by skill category for composable reuse. Categories are self-contained capability units (plugins, rules, MCP servers, agents, hooks). Stacks compose categories into common combos.

## Sources

- Anthropic's "Complete Guide to Building Skills for Claude" (PDF)
- @trq212's "Lessons from Building Claude Code: How We Use Skills" (Anthropic internal experience)
- Current plugin inventory across all profiles

## Design Decisions

1. **Parallel structure** -- `category-profiles/` coexists with `profiles/`. Originals stay intact.
2. **Composable atoms** -- Each category is an independent atom. Stacks in `profiles/stacks/` compose multiple categories via `includes`.
3. **Custom taxonomy** -- Categories derived from actual plugin inventory, informed by Anthropic's 9-category and 3-category taxonomies.
4. **Full bundles** -- Each category includes plugins, rules, skills, agents, hooks -- everything needed for that capability.
5. **Per-category scoping** -- Each category sets user or project scope based on the nature of its plugins.

## Categories

### code-quality (project scope)

Review, simplification, and style enforcement.

**Plugins:**

- `code-review@claude-plugins-official`
- `code-simplifier@claude-plugins-official`
- `pr-review-toolkit@claude-plugins-official`
- `feature-dev@claude-plugins-official`
- `comprehensive-review@claude-code-workflows`
- `code-refactoring@claude-code-workflows`
- `codebase-cleanup@claude-code-workflows`
- `elements-of-style@superpowers-marketplace`

**Skills:**

- `pr-comments`
- `pr-review-fix`
- `the-antislop`

**Rules:**

- `coding-standards.md`
- `naming-and-comments.md`

**@trq212 mapping:** Code Quality & Review

### testing (project scope)

TDD, verification, debugging, e2e, and performance testing.

**Plugins:**

- `playwright@claude-plugins-official`
- `tdd-workflows@claude-code-workflows`
- `unit-testing@claude-code-workflows`
- `performance-testing-review@claude-code-workflows`
- `testing-suite@claude-code-templates`
- `debugging-toolkit@claude-code-workflows`
- `error-debugging@claude-code-workflows`

**Skills:**

- `playwright-skill`

**Agents:**

- `test-runner/test-runner.md`

**@trq212 mapping:** Product Verification

### security (project scope)

SAST, hardening, threat modeling, auth patterns, and safety guardrails.

**Plugins:**

- `security-guidance@claude-plugins-official`
- `security-compliance@claude-code-workflows`
- `security-scanning@claude-code-workflows`
- `backend-api-security@claude-code-workflows`
- `safety-hooks@cctools-plugins`

**@trq212 mapping:** Cross-cutting (no direct equivalent)

### vcs (user scope)

Git workflows, commits, PRs, and branch management.

**Plugins:**

- `commit-commands@claude-plugins-official`
- `git-pr-workflows@claude-code-workflows`
- `github@claude-plugins-official`

**Commands:**

- `commit.md`
- `create-release.md`
- `make-local-issue.md`

**Rules:**

- `version-control.md`

**@trq212 mapping:** CI/CD & Deployment (partial)

### memory (user scope)

Persistence, vault, session continuity, and knowledge management.

**Plugins:**

- `claude-mem@thedotmack`
- `episodic-memory@superpowers-marketplace`

**Skills:**

- `session-notes`

**Commands:**

- `update-memory.md`
- `recovery-prompt.md`

**@trq212 mapping:** No direct equivalent (unique to this setup)

### reference (mixed scope)

Library docs, language-specific tooling, documentation generation.

Language LSPs and language-specific plugins go at project scope (activated by project detection). Documentation and reference skills go at user scope.

**Plugins (project scope):**

- `gopls-lsp@claude-plugins-official`
- `pyright-lsp@claude-plugins-official`
- `swift-lsp@claude-plugins-official`
- `document-skills@anthropic-agent-skills`
- `code-documentation@claude-code-workflows`
- `documentation-generation@claude-code-workflows`

**Skills (user scope):**

- `bash`
- `golang`
- `context7-mcp`
- `explain-code`

**Rules (user scope):**

- `context7.md`
- `documentation-guidelines.md`

**@trq212 mapping:** Library & API Reference

### productivity (user scope)

Orchestration, planning, parallel dispatch, and developer experience.

**Plugins:**

- `superpowers@superpowers-marketplace`
- `superpowers-lab@superpowers-marketplace`
- `developer-essentials@claude-code-workflows`
- `full-stack-orchestration@claude-code-workflows`
- `team-collaboration@claude-code-workflows`
- `shell-scripting@claude-code-workflows`

**Agents:**

- `developer-experience`

**@trq212 mapping:** Business Process & Automation

### migration (project scope)

Framework upgrades, dependency management, and legacy modernization.

**Plugins:**

- `framework-migration@claude-code-workflows`
- `dependency-management@claude-code-workflows`

**@trq212 mapping:** Spans Code Scaffolding & Infrastructure Operations

### tooling (user scope)

Claude Code configuration, plugin development, HUD, and meta-tooling.

**Plugins:**

- `claude-hud@claude-hud`
- `claude-code-setup@claude-plugins-official`
- `claude-md-management@claude-plugins-official`
- `hookify@claude-plugins-official`
- `superpowers-developing-for-claude-code@superpowers-marketplace`

**Output Styles:**

- `technical-evangelist.md`

**@trq212 mapping:** No direct equivalent (meta-tooling)

## What stays in `profiles/`

- `languages/` -- Language-specific plugins remain orthogonal to skill categories
- `platforms/` -- Platform-specific plugins (frontend, backend, mobile) remain orthogonal
- `stacks/` -- Updated to compose from category-profiles
- `orchestrators/` -- Opinionated meta-configurations, kept as-is
- Root profiles (base.json, bare.json, etc.) -- Unchanged
- `extensions/common.json` -- Shared hooks stay in base infrastructure

## Shared infrastructure (stays in base.json)

Hooks that are cross-cutting infrastructure, not category-specific:

- `block-dangerous-commands.sh`
- `format-on-save.sh`
- `log-bash-commands.sh`
- `markdown_formatter.py`
- `protect-sensitive-files.sh`

These remain in `base.json` or `extensions/common.json`.

## Composition model

### Category profile schema

```json
{
  "name": "code-quality",
  "description": "Code review, simplification, and style enforcement",
  "perScope": {
    "project": {
      "plugins": ["..."],
      "extensions": {
        "skills": ["..."],
        "rules": ["..."]
      }
    }
  }
}
```

### Stack composition

Stacks use `includes` to compose categories with language/platform profiles:

```json
{
  "name": "go-backend",
  "includes": [
    "../../category-profiles/code-quality",
    "../../category-profiles/testing",
    "../../category-profiles/vcs",
    "../../category-profiles/memory",
    "../../category-profiles/reference",
    "../../category-profiles/productivity",
    "languages/go",
    "platforms/backend"
  ]
}
```

### CLI usage

Single category: `--base-profile base --profile ../../category-profiles/code-quality`

Via stack: `--base-profile base --profile stacks/go-backend`

## Plugins not categorized

These plugins exist in current profiles but don't fit the skill-category model cleanly. They remain accessible via language/platform profiles or orchestrators:

- `frontend-design@claude-plugins-official` -- Stays in `platforms/frontend`
- `ui-design@claude-code-workflows` -- Stays in `platforms/frontend`
- `vercel@claude-plugins-official` -- Stays in `platforms/frontend`
- `nextjs-vercel-pro@claude-code-templates` -- Stays in `platforms/frontend`
- `backend-development@claude-code-workflows` -- Stays in `platforms/backend`
- `frontend-mobile-development@claude-code-workflows` -- Stays in `platforms/mobile`
- `frontend-mobile-security@claude-code-workflows` -- Stays in `platforms/mobile`
- `conductor@claude-code-workflows` -- Stays in `orchestrators/`
- AI/experimental tools (`aichat`, `langroid`, `tmux-cli`, `voice`, `workflow` from cctools) -- Stays in `tools/ai-tools`
- `everything-claude-code@everything-claude-code` -- Standalone, not categorized

## Future categories

Can be added when plugins are installed:

- **data** -- Data fetching, analysis, dashboards (@trq212: Data Fetching & Analysis)
- **runbooks** -- Incident response, debugging playbooks (@trq212: Runbooks)
- **infrastructure** -- Cloud ops, resource management (@trq212: Infrastructure Operations)
