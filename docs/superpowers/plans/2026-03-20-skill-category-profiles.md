# Skill-Category Profiles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create 9 category profile JSON files in `profiles/categories/`, slim `extensions/common.json` to hooks only, update `stacks/essentials.json` to compose from categories, and add a new `stacks/go-backend.json` stack.

**Architecture:** Each category profile is a standalone JSON file following the existing profile schema (`name`, `description`, `marketplaces`, `perScope`, `extensions`). Stacks compose categories via `includes`. The existing `profiles/` structure is preserved -- categories are additive.

**Tech Stack:** JSON profile files, claudeup CLI for validation

**Spec:** `docs/superpowers/specs/2026-03-20-skill-category-profiles-design.md`

---

### Task 1: Create categories directory

**Files:**

- Create: `profiles/categories/` (directory)

- [ ] **Step 1: Create the directory**

```bash
mkdir -p profiles/categories
```

- [ ] **Step 2: Commit**

```bash
git add profiles/categories
git commit -m "Add profiles/categories directory for skill-category profiles"
```

Note: git won't track an empty directory. If needed, the first category file commit will create it.

---

### Task 2: Create code-quality category profile

**Files:**

- Create: `profiles/categories/code-quality.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/code-quality.json`:

```json
{
  "name": "code-quality",
  "description": "Code review, simplification, and style enforcement",
  "marketplaces": [
    { "source": "github", "repo": "anthropics/claude-plugins-official" },
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

- [ ] **Step 2: Validate JSON is well-formed**

```bash
python3 -c "import json; json.load(open('profiles/categories/code-quality.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/code-quality.json
git commit -m "Add code-quality category profile"
```

---

### Task 3: Create testing category profile

**Files:**

- Create: `profiles/categories/testing.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/testing.json`:

```json
{
  "name": "testing",
  "description": "TDD, verification, debugging, e2e, and performance testing",
  "marketplaces": [
    { "source": "github", "repo": "anthropics/claude-plugins-official" },
    { "source": "github", "repo": "wshobson/agents" },
    { "source": "github", "repo": "davila7/claude-code-templates" }
  ],
  "perScope": {
    "project": {
      "plugins": [
        "playwright@claude-plugins-official",
        "tdd-workflows@claude-code-workflows",
        "unit-testing@claude-code-workflows",
        "performance-testing-review@claude-code-workflows",
        "testing-suite@claude-code-templates",
        "debugging-toolkit@claude-code-workflows",
        "error-debugging@claude-code-workflows"
      ]
    }
  },
  "extensions": {
    "skills": ["playwright-skill"],
    "agents": ["test-runner/test-runner.md"]
  }
}
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/categories/testing.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/testing.json
git commit -m "Add testing category profile"
```

---

### Task 4: Create security category profile

**Files:**

- Create: `profiles/categories/security.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/security.json`:

```json
{
  "name": "security",
  "description": "SAST, hardening, threat modeling, auth patterns, and safety guardrails",
  "marketplaces": [
    { "source": "github", "repo": "anthropics/claude-plugins-official" },
    { "source": "github", "repo": "wshobson/agents" },
    { "source": "github", "repo": "pchalasani/claude-code-tools" }
  ],
  "perScope": {
    "user": {
      "plugins": [
        "security-guidance@claude-plugins-official",
        "security-compliance@claude-code-workflows",
        "security-scanning@claude-code-workflows",
        "backend-api-security@claude-code-workflows",
        "safety-hooks@cctools-plugins"
      ]
    }
  }
}
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/categories/security.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/security.json
git commit -m "Add security category profile"
```

---

### Task 5: Create vcs category profile

**Files:**

- Create: `profiles/categories/vcs.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/vcs.json`:

```json
{
  "name": "vcs",
  "description": "Git workflows, commits, PRs, and branch management",
  "marketplaces": [
    { "source": "github", "repo": "anthropics/claude-plugins-official" },
    { "source": "github", "repo": "wshobson/agents" }
  ],
  "perScope": {
    "user": {
      "plugins": [
        "commit-commands@claude-plugins-official",
        "git-pr-workflows@claude-code-workflows",
        "github@claude-plugins-official"
      ]
    }
  },
  "extensions": {
    "commands": ["commit.md", "create-release.md", "make-local-issue.md"],
    "rules": ["version-control.md"]
  }
}
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/categories/vcs.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/vcs.json
git commit -m "Add vcs category profile"
```

---

### Task 6: Create memory category profile

**Files:**

- Create: `profiles/categories/memory.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/memory.json`:

```json
{
  "name": "memory",
  "description": "Persistence, vault, session continuity, and knowledge management",
  "marketplaces": [
    { "source": "github", "repo": "obra/superpowers-marketplace" },
    { "source": "github", "repo": "thedotmack/claude-mem" }
  ],
  "perScope": {
    "user": {
      "plugins": [
        "claude-mem@thedotmack",
        "episodic-memory@superpowers-marketplace"
      ]
    }
  },
  "extensions": {
    "skills": ["session-notes"],
    "commands": ["update-memory.md", "recovery-prompt.md"]
  }
}
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/categories/memory.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/memory.json
git commit -m "Add memory category profile"
```

---

### Task 7: Create reference category profile

**Files:**

- Create: `profiles/categories/reference.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/reference.json`:

```json
{
  "name": "reference",
  "description": "Library docs, documentation generation, and reference skills",
  "marketplaces": [
    { "source": "github", "repo": "wshobson/agents" },
    { "source": "github", "repo": "anthropics/skills" }
  ],
  "perScope": {
    "user": {
      "plugins": [
        "document-skills@anthropic-agent-skills",
        "code-documentation@claude-code-workflows",
        "documentation-generation@claude-code-workflows"
      ],
      "mcpServers": [
        {
          "name": "context7",
          "command": "npx",
          "args": ["-y", "@upstash/context7-mcp"],
          "scope": "user"
        }
      ]
    }
  },
  "extensions": {
    "skills": ["bash", "golang", "context7-mcp", "explain-code"],
    "rules": ["context7.md", "documentation-guidelines.md"]
  }
}
```

Note: The context7 MCP server requires an API key. The key is configured in base.json. If this category is used without base, the MCP server args will need the `--api-key` flag added. When used with `--base-profile base`, the base MCP server config takes precedence.

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/categories/reference.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/reference.json
git commit -m "Add reference category profile"
```

---

### Task 8: Create productivity category profile

**Files:**

- Create: `profiles/categories/productivity.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/productivity.json`:

```json
{
  "name": "productivity",
  "description": "Orchestration, planning, parallel dispatch, and developer experience",
  "marketplaces": [
    { "source": "github", "repo": "obra/superpowers-marketplace" },
    { "source": "github", "repo": "wshobson/agents" }
  ],
  "perScope": {
    "user": {
      "plugins": [
        "superpowers@superpowers-marketplace",
        "superpowers-lab@superpowers-marketplace",
        "developer-essentials@claude-code-workflows",
        "full-stack-orchestration@claude-code-workflows",
        "team-collaboration@claude-code-workflows",
        "shell-scripting@claude-code-workflows"
      ]
    }
  },
  "extensions": {
    "agents": ["developer-experience"]
  }
}
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/categories/productivity.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/productivity.json
git commit -m "Add productivity category profile"
```

---

### Task 9: Create migration category profile

**Files:**

- Create: `profiles/categories/migration.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/migration.json`:

```json
{
  "name": "migration",
  "description": "Framework upgrades, dependency management, and legacy modernization",
  "marketplaces": [{ "source": "github", "repo": "wshobson/agents" }],
  "perScope": {
    "project": {
      "plugins": [
        "framework-migration@claude-code-workflows",
        "dependency-management@claude-code-workflows"
      ]
    }
  }
}
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/categories/migration.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/migration.json
git commit -m "Add migration category profile"
```

---

### Task 10: Create tooling category profile

**Files:**

- Create: `profiles/categories/tooling.json`

- [ ] **Step 1: Create the profile**

Write `profiles/categories/tooling.json`:

```json
{
  "name": "tooling",
  "description": "Claude Code configuration, plugin development, HUD, and meta-tooling",
  "marketplaces": [
    { "source": "github", "repo": "anthropics/claude-plugins-official" },
    { "source": "github", "repo": "anthropics/claude-code" },
    { "source": "github", "repo": "jarrodwatts/claude-hud" },
    { "source": "github", "repo": "obra/superpowers-marketplace" }
  ],
  "perScope": {
    "user": {
      "plugins": [
        "claude-hud@claude-hud",
        "claude-code-setup@claude-plugins-official",
        "claude-md-management@claude-plugins-official",
        "hookify@claude-plugins-official",
        "plugin-dev@claude-code-plugins",
        "superpowers-developing-for-claude-code@superpowers-marketplace"
      ]
    }
  },
  "extensions": {
    "output-styles": ["technical-evangelist.md", "thinking-jester.md"]
  }
}
```

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/categories/tooling.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/categories/tooling.json
git commit -m "Add tooling category profile"
```

---

### Task 11: Slim extensions/common.json to hooks only

**Files:**

- Modify: `profiles/extensions/common.json`

The current file contains agents, commands, skills, hooks, output-styles, and rules. After this change, only hooks remain. Skills, rules, commands, and output styles from common.json are redistributed to category profiles. Some category profiles also include extensions not previously in common.json (e.g., `the-antislop`, `session-notes`, `explain-code`) -- these are additions from other profiles or newly included.

- [ ] **Step 1: Read the current file to confirm contents**

```bash
cat profiles/extensions/common.json
```

Verify it contains the skills, rules, commands, output-styles, and agents that are now in category profiles.

- [ ] **Step 2: Update to hooks only**

Replace the contents of `profiles/extensions/common.json` with:

```json
{
  "name": "common",
  "description": "Shared hooks used across multiple profiles",
  "extensions": {
    "hooks": [
      "block-dangerous-commands.sh",
      "format-on-save.sh",
      "log-bash-commands.sh",
      "markdown_formatter.py",
      "protect-sensitive-files.sh"
    ]
  }
}
```

- [ ] **Step 3: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/extensions/common.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add profiles/extensions/common.json
git commit -m "Slim extensions/common.json to hooks only

Skills, rules, commands, and output styles are now provided
by category profiles in profiles/categories/."
```

---

### Task 12: Update stacks/essentials.json to use categories

**Files:**

- Modify: `profiles/stacks/essentials.json`

The current essentials stack includes: `extensions/common`, `languages/go`, `orchestrators/superpowers`, `tools/memory`, `tools/claude-hud`, `workflow/code-quality`, `workflow/git`, `workflow/productivity`, `workflow/security`.

Replace workflow/ and tools/ references with category/ references. Keep `extensions/common` (for hooks), `languages/go`, and `orchestrators/superpowers` since those are orthogonal to categories.

- [ ] **Step 1: Read the current file**

```bash
cat profiles/stacks/essentials.json
```

Verify it matches the expected includes list.

- [ ] **Step 2: Update to use categories**

Replace the contents of `profiles/stacks/essentials.json` with:

```json
{
  "name": "essentials",
  "description": "Core tools and extensions via skill categories",
  "includes": [
    "extensions/common",
    "categories/code-quality",
    "categories/testing",
    "categories/security",
    "categories/vcs",
    "categories/memory",
    "categories/reference",
    "categories/productivity",
    "categories/tooling",
    "languages/go",
    "orchestrators/superpowers"
  ]
}
```

- [ ] **Step 3: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/stacks/essentials.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add profiles/stacks/essentials.json
git commit -m "Update essentials stack to compose from category profiles"
```

---

### Task 13: Add stacks/go-backend.json

**Files:**

- Create: `profiles/stacks/go-backend.json`

- [ ] **Step 1: Create the stack**

Write `profiles/stacks/go-backend.json`:

```json
{
  "name": "go-backend",
  "description": "Go backend: code quality, testing, vcs, memory, reference, productivity",
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

- [ ] **Step 2: Validate JSON**

```bash
python3 -c "import json; json.load(open('profiles/stacks/go-backend.json')); print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add profiles/stacks/go-backend.json
git commit -m "Add go-backend stack composing categories with Go and backend"
```

---

### Task 14: Add categories CLAUDE.md

**Files:**

- Create: `profiles/categories/CLAUDE.md`

- [ ] **Step 1: Create the documentation**

Write `profiles/categories/CLAUDE.md`:

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add profiles/categories/CLAUDE.md
git commit -m "Add categories CLAUDE.md documentation"
```

---

### Task 15: Validate end-to-end

- [ ] **Step 1: Verify all 9 category files exist and are valid JSON**

```bash
for f in profiles/categories/*.json; do
  python3 -c "import json; json.load(open('$f')); print('OK: $f')"
done
```

Expected: 9 lines, all `OK`

- [ ] **Step 2: Verify stacks reference valid category paths**

```bash
python3 -c "
import json, os
for stack in ['profiles/stacks/essentials.json', 'profiles/stacks/go-backend.json']:
    data = json.load(open(stack))
    for inc in data.get('includes', []):
        path = f'profiles/{inc}.json'
        exists = os.path.exists(path)
        status = 'OK' if exists else 'MISSING'
        print(f'{status}: {path} (from {stack})')
"
```

Expected: All `OK`, no `MISSING`

- [ ] **Step 3: Verify extensions/common.json has only hooks**

```bash
python3 -c "
import json
data = json.load(open('profiles/extensions/common.json'))
exts = data.get('extensions', {})
keys = set(exts.keys())
assert keys == {'hooks'}, f'Expected only hooks, got: {keys}'
print('OK: extensions/common.json has hooks only')
"
```

Expected: `OK: extensions/common.json has hooks only`

- [ ] **Step 4: Commit validation (no changes expected)**

If any fixes were needed, commit them. Otherwise, no action needed.
