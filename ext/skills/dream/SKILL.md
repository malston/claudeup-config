---
name: dream
description: Use when memory files need consolidation, at session boundaries, before context compaction, or when the user says "dream" or "consolidate memory". Performs a structured reflective pass over the auto-memory directory to merge duplicates, prune stale facts, and rebuild the index.
---

# Dream

A structured reflective pass over your memory files. Synthesize recent learnings into durable, well-organized memories so future sessions orient quickly.

## When to Use

- User says "dream", "consolidate memory", or "clean up memory"
- Before context compaction when you have significant new knowledge
- At session end when multiple memories were created or updated
- When MEMORY.md exceeds 150 lines

## When NOT to Use

- Mid-task when you should be working (save dreaming for boundaries)
- When no memory files exist yet

## The Four Phases

```dot
digraph dream {
  rankdir=LR;
  node [shape=box];
  orient [label="Phase 1\nOrient"];
  gather [label="Phase 2\nGather Signal"];
  consolidate [label="Phase 3\nConsolidate"];
  prune [label="Phase 4\nPrune & Index"];
  orient -> gather -> consolidate -> prune;
}
```

### Phase 1 -- Orient

Read the memory directory to understand current state.

1. `ls` the memory directory
2. Read `MEMORY.md` (the index)
3. Skim each topic file -- read frontmatter and first few lines
4. Note file count, approximate total size, last-modified dates

**Output:** Mental inventory of what exists and how old it is.

### Phase 2 -- Gather Recent Signal

Check for new information that should update memories.

1. `git log --oneline -20` in the project directory -- what shipped recently?
2. Check if any memory files reference things that have changed (merged PRs, deleted branches, renamed files)
3. Grep narrowly for specific facts only when a memory claim seems stale
4. Check the conversation context for decisions or feedback not yet captured

**Rules:**

- Do NOT read entire transcripts or do broad searches
- Grep only when you have a specific fact to verify
- Focus on what CHANGED, not on re-reading everything

**Output:** List of stale facts, new facts to add, and contradictions found.

### Phase 3 -- Consolidate

Merge, update, and correct memory files.

1. **Merge duplicates:** If two files cover the same topic, combine into one
2. **Convert relative dates:** "last week" becomes "2026-03-19", "Thursday" becomes the actual date
3. **Delete contradicted facts:** If a memory says X but reality is Y, update to Y
4. **Promote ephemeral to durable:** Session-specific notes with lasting value get rewritten as general knowledge
5. **Update frontmatter:** Ensure name, description, and type fields match current content
6. **Delete dead files:** Remove files whose entire content is now stale or captured elsewhere

**Rules:**

- When deleting a file, first check if any lasting insight should be preserved in another file
- When merging, keep the better-organized file and fold the other into it
- Update the file, don't append -- memories should read as current truth, not a changelog

### Phase 4 -- Prune and Index

Rebuild MEMORY.md as a clean, scannable index.

1. Rebuild MEMORY.md from scratch based on current files
2. Each entry: `- [Title](file.md) -- one-line hook` (under 150 chars)
3. Group entries by topic, not chronologically
4. Total index must stay under 200 lines (truncated beyond that)
5. Remove pointers to deleted files
6. Add pointers for any new files created during consolidation

**Output:** Clean MEMORY.md that a fresh session can scan in seconds.

## Return a Summary

After all four phases, report to the user:

- Files read / created / updated / deleted
- Key changes made (2-5 bullet points)
- Current memory file count and MEMORY.md line count
- Any unresolved items that need human input

## Common Mistakes

| Mistake                                          | Fix                                                 |
| ------------------------------------------------ | --------------------------------------------------- |
| Broad transcript grep in Phase 2                 | Grep only for specific facts you need to verify     |
| Appending to files instead of rewriting          | Memories should read as current truth               |
| Keeping dead PR/branch references                | If the work shipped, the tracking note is stale     |
| Leaving relative dates in files                  | Always convert to absolute dates                    |
| Rebuilding MEMORY.md without reading files first | Phase 1 exists for a reason -- orient before acting |
