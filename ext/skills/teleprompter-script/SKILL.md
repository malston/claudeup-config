---
name: teleprompter-script
description: >-
  Generate teleprompter speaker scripts in Mark's voice from a deck (.pptx file
  or Google Slides URL). Produces slide-by-slide narration in short-line
  breath-group teleprompter format, with optional companion demo scripts.
  Writes both files to Forgd/<client> in the private Obsidian vault via the
  obsidian-private MCP server.
when_to_use: >-
  Use when Mark asks to write teleprompter notes, create speaker scripts,
  narrate slides, generate slide narration, draft delivery copy from a deck,
  or produce a reading copy of a presentation. Triggers on requests like
  "write teleprompter notes for <deck>", "narrate the slides in <deck>",
  "create speaker scripts from this Google Slides URL", "draft a teleprompter
  for the <Client> deck", or "turn this pptx into reading copy". Also covers
  follow-ups like adding companion demo scripts to an existing teleprompter
  file.
argument-hint: "[deck-path-or-url] [client?] [product?]"
arguments:
  - deck
  - client
  - product
  - demos
---

# Teleprompter Script Generator

Generates slide-by-slide narration in Mark's actual presenting voice and writes it to Mark's Obsidian vault in teleprompter format.

## Arguments

| Argument  | Required | Description                                                                                   |
| --------- | -------- | --------------------------------------------------------------------------------------------- |
| `deck`    | Yes      | Path to a `.pptx` file OR a Google Slides URL                                                 |
| `client`  | No       | Client name (e.g., "Intapp", "Sonos", "Innovaccer"). Extract from the title slide if omitted. |
| `product` | No       | Product or session name. Extract from the title slide if omitted.                             |
| `demos`   | No       | Generate companion demo script. Skill scans the deck and asks if unspecified.                 |

**Only `$deck` is substituted directly into this skill content.** `client` and `product` are positional overrides — when not provided, you (the agent) must extract them from the title slide before using them. Treat `<client>` and `<product>` in this doc as placeholders for the values you derive at runtime, not literal `$name` substitutions.

**Extracting client and product from the title slide (slide 1):** Read the title slide's text content. The client is typically the audience name that appears after "for" (e.g., "Session 1 -- for Intapp" → client is `Intapp`). The product is typically the deck's primary title (e.g., "Advanced Claude Code" → product is `Advanced_Claude_Code`). Spaces become underscores in the output filename. If the title slide doesn't make the client/product obvious, ask Mark before proceeding -- don't guess from the filename.

## Reference assets (read these BEFORE drafting)

- **`references/presentation-voice.md`** -- Mark's voice/style guide. Banned phrases, sentence patterns, structural AI-tells, concrete before/after examples. The narration MUST conform.
- **`references/example-transcript.md`** -- Transcript of Mark delivering a Claude Cowork deepdive. The canonical source of his actual cadence and idiom. Skim before drafting to calibrate.

If a draft doesn't sound like the transcript or the voice guide's calibration slides, it's wrong.

## Process

### 1. Read the deck

The deck path or URL is `$deck` (the first positional argument).

For `.pptx`:

```bash
python -m markitdown $deck
```

For Google Slides URLs (`$deck` starts with `https://docs.google.com/`): use `mcp__claude_ai_Google_Drive__download_file_content` or `read_file_content` to fetch the slide content. If Drive access isn't available, ask Mark to export to `.pptx` and supply the local path.

Each slide is delimited by `<!-- Slide number: N -->`. Extract the slide title and visible content for each.

### 2. Extract client and product (if not provided)

If Mark didn't pass `client` and `product` as arguments, extract them from slide 1 (the title slide). See the rule under "Arguments" above. Confirm with Mark using `AskUserQuestion` if the title slide is ambiguous.

These values become `<client>` and `<product>` everywhere in this doc — used in output paths, frontmatter, and demo wikilinks.

### 3. Scan for demo candidates

If Mark didn't explicitly say "demos yes" or "demos no," scan the deck for demo candidates and confirm. A slide is a demo candidate if any of these apply:

- Slide title or text contains `live demo`, `[DEMO]`, `demo:`, or similar
- Speaker notes mention `demo this live`, `show this live`, `if there's time, demo`
- Slide is a section divider that introduces a hands-on exercise (e.g., "Live practice", "Walk this codebase")

Present the candidate list to Mark and confirm which (if any) to generate. Use `AskUserQuestion` with a multi-select question, or list the candidates and ask for confirmation. Don't guess.

If Mark says no demos, skip Step 7 entirely.

### 4. Calibrate the voice

Read `references/presentation-voice.md` cover-to-cover. Particularly:

- The **Banned Phrases** table -- never use them
- **Structural AI-Tells to Avoid** -- "not X / it's Y" reversals, punchy two-line reveals, rule-of-three drumbeats, meta-narration, circular subject-object framings
- Mark's actual openers: "Alright", "OK so", "What I do is", "The way I think about it is", "Let me walk you through"
- Honest hedging patterns: "It helps, but it's not deterministic", "Usually. Not deterministically."

Skim `references/example-transcript.md` to absorb the cadence.

### 5. Generate per-slide narration

For each slide, write narration that:

- Tells the slide's story in Mark's voice (full conversational sentences, NOT bullet readouts)
- Uses concrete grounding (numbers, file paths, function names, time spans) when the slide content supports it
- Includes stage directions in brackets where natural:
  - `[pause, 2 seconds]` -- longest pause, used at session openings
  - `[PAUSE]` -- structural transition between concept blocks
  - `[beat]` -- brief mid-thought pause
  - `[advance to slide N]` -- end of each slide
  - `` `[DEMO -- description]` → [[<client>_<product>_Demo_Teleprompter#Demo N -- Slide M -- Title]] `` -- only on slides Mark confirmed in Step 3
- Each phrase on its own line (a single eye-fixation chunk, typically 2-7 words)
- Lines tight within a breath group, blank line between breath groups

Tag each slide at the top with `` `[NEW]` `` (or `` `[REUSED from ...]` `` if the slide carries over from another deck).

### 6. Apply teleprompter formatting

Once raw narration is written for all slides, run the reflow helper:

```bash
python scripts/reflow.py <path-to-draft.md>
```

The script:

- Tightens lines within a thought (no blank between)
- Inserts a blank line after `.`, `!`, `?`, `:`, `;`, or `--` (and their quote-trailing variants like `."`)
- Preserves stage directions and headers with proper padding

After the script, manually add blank-line breaks at **parallel structures** the script can't detect:

- "one is X / and the other is Y"
- "First X / and second Y"
- "X / but Y" with substantive Y
- 3-4 item parallel lists where each item is substantive

### 7. Add Table of Contents

After the intro paragraph and before the first slide:

```markdown
## Table of Contents

- [[#Slide 1 -- Title (timing)]]
- [[#Slide 2 -- Title (timing)]]
- ...
```

Use Obsidian's same-file wikilink syntax (`[[#Heading]]`).

### 8. Demo script (only if Mark confirmed demos in Step 3)

Generate a companion file with one section per demo Mark confirmed:

```markdown
## Demo N -- Slide M -- Slide Title

**Setup:** [terminal state, repo state, prior session context]

**The task / prompt:** [what to actually type or do]

**What to narrate:** [in teleprompter format -- short lines, breath groups]

**If it goes sideways:** [recovery moves -- name what to do when each likely failure happens]

**Key beats to land:** [bulleted list of takeaways for the live narration]
```

Wikilinks in the main file reference these sections:

```
`[DEMO -- description]` → [[<client>_<product>_Demo_Teleprompter#Demo N -- Slide M -- Slide Title]]
```

Format the "What to narrate" section in the same teleprompter style as the main file (short lines, breath groups).

### 9. Voice audit (automated + manual)

**Automated pass first.** Run the banned-phrase scanner against the draft:

```bash
python scripts/audit_voice.py <path-to-draft.md>
```

Output sections:

- **BANNED PHRASES** -- hard hits. Rewrite each before continuing. Exit code 1.
- **CONTEXT-DEPENDENT WARNINGS** -- review case-by-case. Some are valid (e.g., "shape of a session" is OK; "structural shapes" is not). Mark uses "recipe" idiomatically in `references/example-transcript.md`; banned only when used as a metaphor for a procedure.

Also run the audit on the demo file if it exists.

**Manual pass second.** The scanner catches lexical hits. It can't catch structural AI-tells. Read the draft against `references/presentation-voice.md` section "How to Audit a Slide Draft":

1. **Aphoristic capstones** -- sentences that could fit on a slide as a bullet header
2. **"Not X / it's Y" reversals** -- judge substantive vs flourish
3. **Punchy two-line "X. Y." reveals** -- collapse into flowing thoughts (rare exceptions when the punch carries an honest hedge)
4. **Rule-of-three or four parallels** -- distinguish functional lists from rhetorical triplets
5. **Meta-narration** -- "This slide covers...", "On the left side of this slide...", "Mechanically,"
6. **Circular subject-object framings** -- Claude/the-model/the-session conflated
7. **Time estimates for hand-author work** -- keep concrete value comparisons like "thirty seconds vs two hours" only

Rewrite anything that doesn't sound like Mark's transcript.

### 10. Write to Obsidian

Use the `obsidian-private` MCP server's `write_note` tool. Vault paths (substituting the `<client>` and `<product>` you derived in Step 2):

- Main: `Forgd/<client>/<client>_<product>_Teleprompter.md`
- Demos: `Forgd/<client>/<client>_<product>_Demo_Teleprompter.md` (only if demos confirmed)

Frontmatter for the main file (substitute `<client>`, `<product>`, `<client-lowercase>`):

```yaml
---
title: <client> <product> -- Slides Teleprompter (Reading Copy)
purpose: Reading-optimized teleprompter for <product> slides. Short lines, generous spacing, minimal eye movement. Demo scripts (if any) are in <client>_<product>_Demo_Teleprompter.md.
tags:
  - presentation
  - teleprompter
  - <client-lowercase>
  - forgd
status: draft
---
```

Frontmatter for the demo file:

```yaml
---
title: <client> <product> -- Demos Teleprompter (Reading Copy)
purpose: Demo scripts referenced by <client>_<product>_Teleprompter.md.
tags:
  - presentation
  - teleprompter
  - demo
  - <client-lowercase>
  - forgd
status: draft
---
```

## Output structure example

```markdown
---
title: <client> <product> -- Slides Teleprompter (Reading Copy)
purpose: ...
tags: [presentation, teleprompter, <client-lowercase>, forgd]
status: draft
---

# Reading Copy -- <product>

Short lines, big spacing.

Scroll slowly.

The demo scripts are in `<client>_<product>_Demo_Teleprompter.md`.

When a slide has a `[DEMO]` marker, click the `→ [[...]]` wikilink to jump to the matching demo section.

---

## Table of Contents

- [[#Slide 1 -- Title (1m)]]
- [[#Slide 2 -- Title (1m)]]
- ...

---

## Slide 1 -- Title (1m)

`[NEW]`

[narration in teleprompter format]

[advance to slide 2]

---

## Slide 2 -- ...
```

## Notes

- Headers use `## Slide N -- Title (timing)` format. The `(timing)` parenthetical is optional but helpful when Mark has a time budget per slide.
- Use `--` (double hyphen), never em-dash `—`. This is a hard rule from Mark's voice guide.
- Don't reference slide numbers in narration. Use "earlier in the deck", "the previous slide", "the next slide" instead.
- For sessions where Session 2 isn't scheduled yet, don't say "tomorrow". "Session 2" by name is fine.
- The audit script (`scripts/audit_voice.py`) exits 1 if hard-ban hits are found. Treat exit-1 as a blocker before writing to Obsidian.
