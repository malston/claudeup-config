# Skill-Category Profiles Design

## Goal

Create a `profiles/categories/` directory within the existing profile structure, organizing plugins by skill category for composable reuse. Categories are self-contained capability units (plugins, rules, MCP servers, agents, hooks). Stacks compose categories into common combos.

## Sources

- Anthropic's "Complete Guide to Building Skills for Claude" (PDF)
- @trq212's "Lessons from Building Claude Code: How We Use Skills" (Anthropic internal experience)
- Current plugin inventory across all profiles

## Design Decisions

1. **Nested structure** -- `profiles/categories/` lives inside the existing profile directory so that `includes` resolution works without path hacks. Originals stay intact.
2. **Composable atoms** -- Each category is an independent atom. Stacks in `profiles/stacks/` compose multiple categories via `includes`.
3. **Custom taxonomy** -- Categories derived from actual plugin inventory, informed by Anthropic's 9-category and 3-category taxonomies.
4. **Full bundles** -- Each category includes plugins, rules, skills, agents, hooks -- everything needed for that capability.
5. **Per-category scoping** -- Each category sets user or project scope based on the nature of its plugins.

## Categories

### code-quality (user scope)

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

### security (user scope)

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

### reference (user scope, with project-scope plugins)

Library docs, documentation generation, and reference skills. LSPs stay in `languages/` profiles.

**Plugins (user scope):**

- `document-skills@anthropic-agent-skills`
- `code-documentation@claude-code-workflows`
- `documentation-generation@claude-code-workflows`

**Skills:**

- `bash`
- `golang`
- `context7-mcp`
- `explain-code`

**Rules:**

- `context7.md`
- `documentation-guidelines.md`

**MCP Servers:**

- `context7` (npx @upstash/context7-mcp)

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
- `plugin-dev@claude-code-plugins`
- `superpowers-developing-for-claude-code@superpowers-marketplace`

**Output Styles:**

- `technical-evangelist.md`
- `thinking-jester.md`

**@trq212 mapping:** No direct equivalent (meta-tooling)

## What stays in `profiles/`

- `languages/` -- Language-specific plugins remain orthogonal to skill categories
- `platforms/` -- Platform-specific plugins (frontend, backend, mobile) remain orthogonal
- `stacks/` -- Updated to compose from category-profiles
- `orchestrators/` -- Opinionated meta-configurations, kept as-is
- Root profiles (base.json, bare.json, etc.) -- Unchanged

## Fate of `extensions/common.json`

`extensions/common.json` currently bundles skills, rules, hooks, commands, and output styles used by `stacks/essentials.json` and others. With categories, its contents are distributed:

- **Hooks** stay in `extensions/common.json` (cross-cutting infrastructure)
- **Skills** move to their respective categories (bash/golang to reference, playwright-skill to testing, etc.)
- **Rules** move to their respective categories (coding-standards to code-quality, version-control to vcs, etc.)
- **Commands** move to their respective categories (commit.md to vcs, update-memory.md to memory, etc.)
- **Output Styles** move to tooling category

`extensions/common.json` is retained but slimmed down to hooks only.

## Shared infrastructure (stays in base.json)

Hooks that are cross-cutting infrastructure, not category-specific:

- `block-dangerous-commands.sh`
- `format-on-save.sh`
- `log-bash-commands.sh`
- `markdown_formatter.py`
- `protect-sensitive-files.sh`

These remain in `base.json` and `extensions/common.json`.

## Composition model

### Include resolution

Includes resolve relative to the `profiles/` directory. Existing examples:

- From `stacks/essentials.json`: `"extensions/common"` resolves to `profiles/extensions/common.json`
- From `stacks/fullstack-go.json`: `"essentials"` resolves to `profiles/stacks/essentials.json` (name-based lookup within stacks)

By placing categories in `profiles/categories/`, includes like `"categories/code-quality"` resolve correctly from any profile.

**Explicit paths required:** Several category profiles share `name` values with existing workflow/tools profiles (e.g., `testing`, `security`, `memory`). To avoid ambiguity in name-based resolution, all includes must use explicit directory-prefixed paths (e.g., `"workflow/testing"` not `"testing"`, `"categories/testing"` not `"testing"`). Existing stacks have been updated to follow this convention.

### Marketplace inheritance

Category profiles that reference plugins from marketplaces not in `base.json` must declare their own `marketplaces` array. Base provides: `claude-plugins-official`, `claude-hud`, `superpowers-marketplace`, `thedotmack`.

Categories needing additional marketplaces:

- **code-quality** needs `claude-code-workflows`, `superpowers-marketplace`
- **testing** needs `claude-code-workflows`, `claude-code-templates`
- **security** needs `claude-code-workflows`, `cctools-plugins`
- **productivity** needs `claude-code-workflows`
- **migration** needs `claude-code-workflows`
- **reference** needs `claude-code-workflows`, `anthropic-agent-skills`
- **tooling** needs `claude-code-plugins`
- **vcs** needs `claude-code-workflows`
- **memory** -- covered by base marketplaces

### Category profile schema

Extensions are top-level (not nested under `perScope`), matching the existing schema:

```json
{
  "name": "code-quality",
  "description": "Code review, simplification, and style enforcement",
  "marketplaces": [
    { "source": "github", "repo": "wshobson/agents" },
    { "source": "github", "repo": "obra/superpowers-marketplace" }
  ],
  "perScope": {
    "user": {
      "plugins": [
        "code-review@claude-plugins-official",
        "code-simplifier@claude-plugins-official",
        "pr-review-toolkit@claude-plugins-official",
        "feature-dev@claude-plugins-official",
        "comprehensive-review@claude-code-workflows",
        "code-refactoring@claude-code-workflows",
        "codebase-cleanup@claude-code-workflows",
        "elements-of-style@superpowers-marketplace"
      ]
    }
  },
  "extensions": {
    "skills": ["pr-comments", "pr-review-fix", "the-antislop"],
    "rules": ["coding-standards.md", "naming-and-comments.md"]
  }
}
```

### Stack composition

Stacks use `includes` to compose categories with language/platform profiles:

```json
{
  "name": "go-backend",
  "description": "Go backend: code quality, testing, security, vcs, memory, reference, productivity",
  "includes": [
    "extensions/common",
    "categories/code-quality",
    "categories/testing",
    "categories/security",
    "categories/vcs",
    "categories/memory",
    "categories/reference",
    "categories/productivity",
    "languages/go",
    "platforms/backend"
  ]
}
```

### CLI usage

Single category: `--base-profile base --profile categories/code-quality`

Via stack: `--base-profile base --profile stacks/go-backend`

## Notable categorization decisions

- **`feature-dev`** lives in code-quality only (was in both productivity and code-quality). Its skills (code-reviewer, code-explorer, code-architect) are review/analysis focused.
- **`playwright`** lives in testing (was in productivity). Its primary use is browser-based verification.
- **`dependency-management` and `framework-migration`** live in migration (were in productivity). They're project-scoped concerns, not general productivity.
- **`backend-api-security`** lives in security (was in platforms/backend). Security concerns should travel with the security category, not be tied to a platform.
- **LSPs** (gopls, pyright, swift) stay in `languages/` profiles, not in reference. They're language-specific tooling that should activate per-project via detection, not as a general reference capability.

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
