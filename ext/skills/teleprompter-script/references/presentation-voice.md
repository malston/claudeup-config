---
modified: 2026-05-15T22:50:00-06:00
---

# Presentation Voice Style

Comprehensive voice/style guide for Mark's spoken / presentation content -- workshops, lunch-and-learns, demos, walkthroughs, teleprompter drafts. Use this as the canonical reference when drafting or auditing slide narration.

This guide combines:

- The original style rules
- New patterns and banned phrases identified across multiple slide-rewrite sessions
- Concrete before/after examples from real edits
- Pointers to calibration sources

---

## Calibration Sources

These are the ground truth for Mark's actual speaking voice. Read them before drafting:

- **Cowork transcript** -- `example-transcript.md`. This is Mark presenting live; it's the canonical reference for cadence and idiom.
- **Calibration slides** -- Slides 20, 21, 22 of `Intapp_Session_1_Slide_Teleprompter.md`. These are reference examples of Mark's voice in the short-line teleprompter format.

If a draft doesn't sound like the cowork transcript or those three slides, it's wrong.

---

## Audience and Register

- Coworkers / peers, not customers. Casual workshop energy, not pitch energy.
- Verbose, full-sentence speech. Mark uses a lot of words when he speaks. Do not abbreviate his sentences.
- Conversational discourse markers are welcome: "Alright", "OK, so", "Now", "Anyway", "honestly".
- First-person ownership of the work: "I built", "what I do is", "the thing I most need help with".

---

## Sentence-Level Patterns to Match

### Conversational openers

Match these cadences:

- "OK so..." / "OK so before we go any further..."
- "Alright..." / "Alright, so what I want to walk through..."
- "Let me walk you through..."
- "What I do is..."
- "The way I think about it is..."
- "The way I tend to use these together is..."
- "Now in practice..." / "Anyway..."

### Honest hedging (anti-pitch)

Mark names limits directly. Don't oversell.

- "I'd assume..."
- "honestly..."
- "It helps, but it's not a guarantee."
- "It helps, but it's not deterministic."
- "I'm pretty sure this is not enabled for [team]."
- "I haven't validated..."
- "Usually. Not deterministically." (a deliberately kept punchy form -- see "Sometimes-allowed punchy reveals" below)

### First-person ownership

- "I want you to..."
- "I'm going to..."
- "What I do is..."
- "The way I think about it is..."
- "The way I tend to use these together is..."

### Q&A framing

Mark loops in audience-style questions:

- "the next question is..."
- "The natural question here is..."
- "The question that usually comes up here is..."
- "I get this question a lot."

### Concrete grounding

Mark uses specific numbers, file paths, function names, time spans. Lean into these.

- "thirty seconds vs two hours"
- "in around twenty-five lines of Python"
- "the original author left two years ago"
- "reverted from DFS to BFS three commits ago because they hit a stack overflow on deeply nested data"
- "an awkward conversation"
- "six months from now when somebody looks at the section and asks..."

### Numbered enumeration -- weave it, don't bark it

GOOD: `First, [full sentence]. Second, [full sentence]. Third, [full sentence].`

GOOD: `The first one is X. The second one is Y. And the third one is Z.`

BAD: `First. / [content on next line] / Second. / [content on next line]` (clipped fragment headers; reads as translated bullets)

### Sentence shape

- Long flowing sentences with subordinate clauses
- Lists weave with "and" rather than naked enumeration ("X, Y, Z" with em-dash and no connective)
- Full sentences with subjects and verbs
- The teleprompter short-line format breaks long sentences into reading chunks; the underlying writing should still be conversational prose

---

## Banned Phrases

Mark hears these by ear and will flag them.

| Banned                                                                                                          | Reason                                             | Use instead                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "land", "land in", "to land this", "land it"                                                                    | Presentation jargon                                | "wrap up", "close out", "match", "fit"                                                                                                                                                       |
| "shape", "structural shapes", "structurally"                                                                    | AI tic                                             | Plain description: "the two have to be written differently"                                                                                                                                  |
| "grounds", "grounds itself on"                                                                                  | AI tic borrowed from RAG/LLM literature            | "the prompt uses", "the prompt references"                                                                                                                                                   |
| "the canonical docs"                                                                                            | AI flavor                                          | "the reference documents", "the source documents"                                                                                                                                            |
| "compounds", "compound" (in the value-grows-over-time sense)                                                    | Aphoristic AI vocabulary                           | "adds up", "builds up", "stacks up"                                                                                                                                                          |
| "seed", "seeded", "gets seeded from"                                                                            | Abstract managerial vocabulary                     | "comes from", "starts as", "originates in"                                                                                                                                                   |
| "converge"                                                                                                      | Abstract managerial vocabulary                     | "agree", "settle on", "line up"                                                                                                                                                              |
| "boundary chart"                                                                                                | Abstract managerial vocabulary                     | Describe the diagram concretely                                                                                                                                                              |
| "same building block", "same building blocks"                                                                   | Aphoristic                                         | Name the actual thing being reused: "we use sub-agents again in..."                                                                                                                          |
| "in someone's head" (POLISHED form)                                                                             | The polished version is corporate AI-speak         | Use the colloquial form Mark actually uses: "the stuff that used to live in someone's head" -- but never the polished "context that lives in engineers' heads gets codified" version         |
| "in the loop" (as in "with the right people in the loop")                                                       | Corporate                                          | "where the right teams know about it"                                                                                                                                                        |
| "playbook" (as in "your refactor playbook")                                                                     | Mild corporate                                     | "your refactor notes"                                                                                                                                                                        |
| "recipe" (as a metaphor for a procedure)                                                                        | Mild AI metaphor                                   | "It's pretty simple." / "Here's how it works."                                                                                                                                               |
| "the right tradeoff", "the balanced everyday model", "the right pairing"                                        | Polished marketing-speak                           | "the right call", "the everyday model", "the right combination"                                                                                                                              |
| "looking at the same picture"                                                                                   | Mild metaphor                                      | "on the same page", "agree on what we're doing"                                                                                                                                              |
| "the details that matter"                                                                                       | Mildly aphoristic                                  | "the actual details", "the details you actually need"                                                                                                                                        |
| "Reuse is real --" and other slogan openers                                                                     | Reads like a tagline                               | "In practice you reuse a lot of this..."                                                                                                                                                     |
| "Quick frame:", "Two numbers.", "Polish.", "Tooling." (clipped fragment headers)                                | Translated-from-bullet-points speech               | Full sentences. "OK, so let me start with the problem this is trying to solve."                                                                                                              |
| "Here's the pain", "Here's the thing", "The truth is", "Let me be honest", "the most honest thing I can say is" | Pitch jargon                                       | Just say the thing                                                                                                                                                                           |
| "the exercises file reads the workshop file as its only input"                                                  | File-level mechanics; sounds clinical              | Skill-level framing: "the generate-exercises skill relies on the workshop produced by the generate-workshop skill"                                                                           |
| Time estimates ("two hours", "six hours", "X minutes per Y") for hand-author work                               | Mark does not quote times for his own writing work | Describe scope (artifacts, segments, what gets written) without quoting hours. EXCEPTION: time-comparison contrasts like "thirty seconds vs two hours" are good when grounding a value claim |

---

## Aphoristic Phrasing to Avoid

These are slogan-style sentences -- punchy, quotable, presentation-deck-flavored. Mark hears them as AI-generated.

Examples seen and rejected:

- "Same pattern, fraction of the cost"
- "Once you understand the mechanism, the use cases compound"
- "same building block, applied to a specific problem"
- "one engineer's hard-won pattern becomes the whole team's standard"
- "the same convention is showing up at two different enforcement points in the workflow"
- "It's how a fix you make today ends up benefiting everyone on the team going forward"
- "to systems that survive peer review"
- "Y, made concrete"

Pattern to recognize: a clean, balanced sentence that could fit on a slide as a bullet header. If it could be a tagline, it's wrong.

Replacement strategy: rewrite as a flowing claim with concrete machinery, not a slogan.

---

## Structural AI-Tells to Avoid

### "Not X / it's Y" reversals (rhetorical move)

The rhetorical move where you negate the wrong thing to set up the right thing. Sometimes substantive (model decision vs CLI block); sometimes pure flourish.

Substantive contrast = OK.

Pure flourish or punchline reveal = NOT OK.

BAD example (rejected):

> It's not running in a sandbox / pretending to be your laptop. / It's actually on your laptop.

Replacement:

> All of that runs on your actual machine, against your real codebase -- not in a sandbox pretending to be your laptop.

### Punchy two-line "X. Y." reveals

The pattern where you split a contrast across two short lines for dramatic emphasis.

BAD example (rejected):

> Today is setup and partial mitigation.
> Session 2 is the full solution.

Replacement:

> Today is the setup and the partial mitigation, and Session 2 is where we build the actual fix.

EXCEPTION (Sometimes-allowed punchy reveals): "Usually. / Not deterministically." was kept on slide 18 because the punch carries an honest hedge. Use this exception sparingly, only when the punch is doing real anti-pitch work.

### Rule-of-three / four parallels for cadence

Banned examples:

- "your actual shell, your actual tests, your actual git"
- "reasoning, tool-calling, observation, looping"
- "rope... map... scaffold..."
- "Claude does X, you do Y, the next engineer does Z"

These read as too clean. Functional 3-item lists naming concrete things (steps in a process, model names) are fine; rhetorical triplets stacking adjectives or metaphors are not.

### Triplet "exact same X / exact same Y / exact same Z" drumbeat

Same flag as rule-of-three.

BAD:

> the exact same logic / against the exact same diff / reading the exact same CLAUDE.md rules

GOOD:

> the exact same logic / against the same diff / reading the same CLAUDE.md rules

(Keep one "exact" for emphasis; drop the rest.)

### Meta-narration about the slide layout

BAD:

- "This slide covers both halves."
- "On the left side of this slide..."
- "Mechanically," (slightly clinical opener)

GOOD:

- "Let me walk through each one."
- "On the left here..."
- "Under the hood..." / "What's happening underneath is..." / "What's actually going on here is..."

### Circular subject-object framings

When the subject and object are effectively the same entity, the sentence reads as confusing or AI-flavored.

BAD: `Claude's private memory biases the model.` (Claude IS the model -- circular.)

GOOD: `Every Claude session builds up its own private context, and that context biases what Claude says toward whoever it's been talking with.` (Names the SESSION as the subject and what Claude SAYS as the affected output.)

### Polished metaphors and corporate-abstract phrasing

- "context that lives in people's heads gets codified" -- corporate-abstract
- "in the original engineers' heads" -- corporate-abstract
- "the right tradeoff", "the right pairing" -- polished marketing-speak
- "looking at the same picture" -- soft metaphor

Mark's colloquial forms are fine ("the stuff that used to live in someone's head"); the polished/corporate variants are not.

---

## Concrete Before/After Examples from Real Edits

### 1. Numbered enumeration

BEFORE:

```
First.
The shift I want you to make today...

Second.
I want you to leave knowing...

Third.
I want you ready...
```

AFTER:

```
The first one is
the shift from one-off prompts...

The second one is
I want you to leave knowing...

And the third one is
I want you ready...
```

### 2. Aphoristic capstone

BEFORE:

```
The reason
is that one engineer's hard-won pattern
becomes the whole team's standard
once it's in version control.
```

AFTER:

```
The reason
is that putting it in git
means every other engineer on the team
picks up the same rule
on their next Claude session,
without having to learn it the hard way themselves.
```

### 3. Banned word "seeded"

BEFORE: `your requirements docs / get seeded from Jira / and from your PMs`

AFTER: `your requirements docs / come from Jira / or from your PMs`

### 4. Banned phrase "same building block"

BEFORE:

```
sub-agents
are the same building block
we come back to in Session 2
for the reviewer-bias problem --
it's a sub-agent there too,
it just happens to be reading
different inputs
and doing a different job.
```

AFTER:

```
sub-agents come back in Session 2 --
the context-isolated reviewer
we build for the reviewer-bias problem
is just another sub-agent,
reading different inputs
and doing a different job.
```

### 5. Banned phrase "in engineers' heads" (corporate form)

BEFORE:

```
That gets the context
that's currently sitting
in the original engineers' heads
down into files in the repo,
so Claude has somewhere to read it from
instead of trying to re-derive it
every session.
```

AFTER:

```
That gets all the stuff that nobody wrote down
written down in the repo,
so Claude can read it
instead of having to re-derive it
every session.
```

### 6. Punchy two-line reveal

BEFORE: `Today is setup and partial mitigation. / Session 2 is the full solution.`

AFTER: `Today is the setup and the partial mitigation, and Session 2 is where we build the actual fix.`

### 7. Rule-of-three drumbeat

BEFORE: `all against your real environment, / your real tests, / your real git history. / It's not running in a sandbox / pretending to be your laptop. / It's actually on your laptop.`

AFTER: `All of that runs on your actual machine, / against your real codebase -- / not in a sandbox / pretending to be your laptop.`

### 8. Circular subject-object

BEFORE: `Claude's private memory / biases the model / toward whoever it talked with first.`

AFTER: `Every Claude session / builds up its own private context -- / and that context biases what Claude says / toward whoever it's been talking with.`

### 9. Meta-narration

BEFORE: `This slide covers both halves. / Let me walk through each one.`

AFTER: `Let me walk through each one.`

### 10. Polished metaphor

BEFORE: `you and Claude / are looking at the same picture / before any code changes.`

AFTER: `you and Claude / are on the same page / before any code changes.`

### 11. "the right tradeoff" and "balanced everyday model"

BEFORE: `Sonnet is the balanced everyday model... Sonnet is usually / the right tradeoff.`

AFTER: `Sonnet is the everyday model... Sonnet is usually / the right call.`

---

## Honest Framing Pattern

For unfinished or unproven projects, frame as recruiting feedback, not asking for adoption.

- Lead with a candid caveat about state: "I've put a lot of time into this, but the output isn't equally good across all six teams, and I haven't manually tested it end-to-end on a real activation yet."
- Frame as "show-and-tell + recruiting help" instead of "use this thing".
- Acknowledge unknowns explicitly: "the validation I haven't done myself yet", "gaps I haven't even seen yet".
- Do not oversell. Mark hears overselling immediately.

---

## Skill-Level vs File-Level Framing

When describing how skills relate to each other, talk about skills depending on each other, not about files reading other files.

- Avoid: "the exercises file reads the workshop file as its only input"
- Prefer: "the generate-exercises skill relies on the workshop produced by the generate-workshop skill"

---

## Cross-Slide Threading

When a slide references content from another slide, use these phrases:

- "earlier in the deck" (allowed)
- "the last slide" / "the previous slide" (allowed)
- "the next slide" (allowed -- no explicit slide numbers)

NEVER use explicit slide numbers in narration.

---

## Session Scheduling References

- Don't say "tomorrow" -- Session 2 isn't always scheduled yet
- "Session 2" by name is fine
- "Coming up..." / "We'll cover that in Session 2" is fine

---

## Punctuation

- NEVER use em dashes (—) in documentation. Use `--` or rewrite the sentence to avoid the need for either.
- Apostrophes for contractions are fine ("don't", "it's", "you've").

---

## Teleprompter Format Notes

For the short-line reading format used in `Intapp_Session_*_Slide_Teleprompter.md`:

- Each phrase on its own line, blank line between phrases
- Sentences flow naturally but get broken into reading chunks
- Format is for layout (eye movement); voice is the underlying content
- Long flowing sentences are correct -- they just get broken across multiple lines

Stage directions stay in `[brackets]` and don't follow the short-line format:

- `[pause, 2 seconds]`
- `[beat]`
- `[PAUSE]`
- `[advance to slide N]`
- `[DEMO -- description]` followed by wikilink

---

## Cross-Reference: CLAUDE.md Anti-Patterns

Everything in `CLAUDE.md` "Writing Style" still applies:

- No contrastive reframes ("not X, but Y") as the rhetorical move
- No superlatives (powerful, seamless, robust, elegant, cutting-edge)
- No triplet lists for rhetorical cadence
- No hedged bold sandwiches
- `--` not `—`
- "Task" not "workflow" in Sessions 1-3
- No relative product-timeline phrasing (new, recently added, improved, legacy)

---

## How to Audit a Slide Draft

When auditing a draft, scan for:

1. **Banned phrases** -- table above (compounds, seed, building block, in people's heads, in the loop, playbook, recipe, right tradeoff, etc.)
2. **Aphoristic capstones** -- the sentences that could fit on a slide as a bullet header
3. **"Not X / it's Y" reversals** -- judge whether substantive or flourish
4. **Punchy two-line "X. Y." reveals** -- collapse into flowing thoughts
5. **Rule-of-three or four parallels** -- distinguish functional lists from rhetorical triplets
6. **Meta-narration** -- "This slide covers...", "On the left side of this slide...", "Mechanically,"
7. **Circular subject-object framings** -- where Claude/the-model/the-session get conflated
8. **Polished metaphors** -- looking at the same picture, the right tradeoff, etc.
9. **Corporate-abstract phrasing** -- in people's heads (polished form), institutional knowledge gets codified
10. **Time estimates for hand-author work** -- but keep concrete value comparisons like "thirty seconds vs two hours"

For each flagged spot, propose a replacement that:

- Is a full sentence with subject and verb
- Uses Mark's actual idiom (matched against the cowork transcript and slides 20-22)
- Names concrete things (file paths, numbers, time spans, function names) where possible
- Preserves the technical substance and the slide's purpose
