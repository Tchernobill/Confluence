# Novel Writing Vault in Obsidian

https://pdworkman.com/writing-a-novel-in-markdown/

This document is the guide / standard to respect when interacting with the local Obsidian vault

**The optimal Obsidian vault for novel series combines three foundational elements**: a hierarchical folder structure organized by project phase rather than content type, property-driven metadata that powers dynamic queries for tracking characters and plot threads across books, and strategic AI integration at specific workflow stages. Professional authors with 70+ published books report that this approach scales from single novels to 10-book series while maintaining continuity and preventing the organizational chaos that derails long-term projects. The key insight is treating your vault as a living database rather than a file cabinet, where relationships between notes matter more than their location.

This matters because **most writers lose track of critical details across long series**—character eye colors change between books, timelines become inconsistent, and plot threads get dropped. A well-structured Obsidian vault with proper metadata acts as a persistent memory system that prevents these continuity errors while accelerating your writing process. Writers using these systems report finding scenes 80% faster, catching contradictions before publication, and reducing revision time by tracking character knowledge states across chapters.

The system emerged from analyzing workflows of published authors including P.D. Workman (70+ books), Vanessa Glau, and dozens of fantasy/sci-fi writers managing 400+ character databases. These practitioners discovered that **Obsidian's linking and query capabilities transform worldbuilding from a chore into an asset**, where each new note strengthens the foundation rather than adding complexity.

## Setting up your vault architecture for long-term success

Start with a single vault per series or standalone novel, creating a master folder structure organized by workflow phase rather than content type. Professional authors universally recommend **the one-vault-per-series approach** to prevent cross-contamination between fictional worlds, especially when managing multiple concurrent projects.

Your top-level structure should reflect the "degrees of doneness" principle, organizing content by where it sits in your creative pipeline. Create five primary folders: **Wiki** for all series-wide worldbuilding that persists across books, **Books** containing individual novel subfolders with their drafts and notes, **Templates** for reusable note structures, **Resources** for images and reference materials, and **Research-Series** as an alphabetical archive of all research conducted across books. This organization means you navigate by asking "what am I doing?" rather than "what type of thing is this?"

Within each book folder, implement P.D. Workman's battle-tested structure from 70+ published novels. Create **Drafts** (containing numbered draft folders—zip previous drafts immediately to prevent working on wrong versions), **Prep** (brainstorming, outlines, character sketches, Snowflake Method work), **Notes** (chapter summaries, continuity tracking, revision checklists), and **Research** (book-specific only—copy to series archive after completion). The Book folder also contains your Longform project index file that ties everything together.

The Wiki folder deserves special attention as your **series bible and worldbuilding repository**. Structure it with subfolders for Characters, Locations, Magic-Systems, History-Timeline, Organizations-Factions, Cultures, and Technology-Science. This becomes your single source of truth that prevents continuity errors across a 5-10 book series. When writing Book 3, you reference the Wiki to confirm that travel from City A to City B takes exactly 5 days by horse, just as it did in Book 1.

For the Templates folder, create master templates for every recurring note type. You'll need templates for novels, chapters, characters, locations, scenes, plot threads, research notes, daily writing logs, and book home pages. These templates should include comprehensive YAML frontmatter that powers your tracking queries. The time invested in crafting these templates pays dividends through hundreds of note creations.

Name your files with **numerical prefixes for chapters** to ensure proper sorting: "01 - Opening Scene" rather than "Opening Scene". This simple convention prevents frustration when viewing files outside Obsidian or in mobile apps where alphabetical sorting dominates. Include brief scene descriptions in titles so you can find "15 - Tavern Confrontation" without opening every file.

## Creating property-rich templates that power your tracking systems

YAML frontmatter properties transform static notes into queryable database records. The key is **designing property schemas that capture what you'll actually need to track** while avoiding property proliferation that clutters your notes.

Here's a complete scene template with comprehensive properties:

```markdown
---
type: scene
title: "The Midnight Confession"
chapter: 7
scene_number: 23
project: "[[Murder in the Mist]]"
status: draft-2
progress: 85
word_count: 2847
words_goal: 3000
pov: Elena Thornfield
pov_type: first-person
characters_present:
  - "[[Elena Thornfield]]"
  - "[[Marcus Vale]]"
  - "[[The Witness]]"
location: "[[The Crimson Lantern]]"
time_of_day: midnight
weather: stormy
date_in_story: 1889-03-15
timeline_position: "Act 2, Rising Action"
plot_threads:
  - "[[Main Investigation]]"
  - "[[Marcus's Secret]]"
emotional_tone: tense, suspenseful
scene_goal: "Elena learns crucial information about the murder"
conflict: "The witness fears for their life"
outcome: "Elena gets a lead but loses the witness"
synopsis: "Elena meets an informant at the Crimson Lantern who reveals the murder victim's secret connection to the city's underworld. Before they can get more information, an assassin attacks."
notes: "Need to add more sensory details about the storm. Check timeline consistency."
tags:
  - scene/action
  - scene/investigation
  - plot/main-mystery
created: 2024-02-10
modified: 2024-03-19
---

## Scene Content

[Actual scene text goes here]

## Scene Beats

1. Elena and Marcus arrive at the tavern
2. Witness reveals key evidence
3. Assassin attempts to kill witness
4. Chase scene through the streets
5. Witness escapes, leaving cryptic message

## Notes & Ideas

- Research Victorian-era weapons for next scene
- Develop the cryptic message further

---

**Word Count:** `$= this.word_count`  
**Status:** `$= this.status`  
**Progress:** `$= round((this.word_count / this.words_goal) * 100)`%
```

This template enables powerful tracking queries. You can instantly find all scenes featuring specific characters, verify timeline consistency, track which plot threads appear where, and monitor completion progress across your manuscript.

For character sheets, implement this property schema:

```yaml
---
type: character
name: Elena Thornfield
aliases:
  - The Shadow Weaver
  - Ellie
age: 32
gender: female
species: human
role: protagonist
occupation: detective
status: alive
traits:
  - intelligent
  - cynical
  - determined
relationships:
  - "[[Marcus Vale]] - partner"
  - "[[Sarah Chen]] - mentor"
  - "[[Victor Crane]] - antagonist"
character_arc: redemption
motivation: "To solve her sister's murder and expose corruption"
internal_conflict: "Trust vs. self-reliance"
external_conflict: "Fighting a powerful criminal syndicate"
backstory: "Former FBI agent turned private investigator after her sister's unsolved death"
strengths:
  - analytical thinking
  - hand-to-hand combat
  - photographic memory
weaknesses:
  - alcoholism
  - trust issues
  - impulsive decisions
appearance: "Tall, athletic build, dark curly hair, scar above left eyebrow"
personality: INTJ
voice: "Sharp, sarcastic, uses detective jargon"
first_appearance: "[[Chapter 1 - The Call]]"
tags:
  - character/protagonist
  - character/detective
created: 2024-01-15
modified: 2024-03-20
---
```

The **relationships field using wiki-links** is crucial—it enables you to query which characters are connected and trace relationship networks across your cast. For series work, add book-specific age fields (age-b1, age-b2, age-b3) to track aging across installments.

Location notes should capture sensory details and track which scenes occur there:

```yaml
---
type: location
name: The Crimson Lantern
location_type: tavern
region: "[[Waterfront District]]"
city: "[[Port Meridian]]"
atmosphere: "Dimly lit, smoky, bustling with sailors and merchants"
description: "A three-story tavern with brass fixtures and gaslight chandeliers"
history: "Built by retired pirate captain, now run by his granddaughter"
inhabitants:
  - "[[Marina Blackwood]] - proprietor"
  - "[[Old Tom]] - regular patron"
notable_features:
  - "Secret meeting room in basement"
  - "Wall covered in navigation maps"
secrets: "Hidden smuggling tunnel connects to the docks"
senses:
  smell: "Salt air, pipe smoke, roasted meat"
  sound: "Sea shanties, clinking glasses, hushed conversations"
  sight: "Warm amber lighting, polished brass, worn wooden floors"
tags:
  - location/tavern
  - location/important
created: 2024-01-20
modified: 2024-03-18
---
```

Follow **ISO 8601 date format (YYYY-MM-DD)** for all date properties to ensure proper sorting in queries. Use **snake_case for property names** (word_count, not wordCount or word-count) for consistency. Keep status values limited to a defined set: draft-1, draft-2, revision, editing, complete, cut. This consistency makes Dataview queries reliable.

The golden rule for properties: **capture data you'll actually query, not aspirational tracking**. Start minimal and add properties when you discover you need them, rather than front-loading every possible field.

## Implementing a hierarchical tagging system that scales to epic series

Tags provide categorical organization while properties handle structured data. The key is **using hierarchical tags with forward slashes** that scale from trilogy to 10-book series without becoming unwieldy.

Your core tag hierarchy should look like this:

```
#character
  #character/protagonist
  #character/antagonist
  #character/supporting
  #character/minor

#location
  #location/continent
  #location/city
  #location/landmark

#magic-system
  #magic-system/elemental
  #magic-system/divine
  #magic-system/blood

#plot
  #plot/main
  #plot/subplot
  #plot/backstory
  #plot/foreshadowing

#scene
  #scene/action
  #scene/dialogue
  #scene/introspection

#status
  #status/idea
  #status/draft
  #status/complete
  #status/needs-expansion
```

The critical practice from published authors: **limit yourself to 5 tags maximum per note**. Tag proliferation destroys findability. Don't tag what's already captured in folders (no #character tag if the note is already in the Characters folder), don't tag physical descriptions that belong in note content, and don't duplicate information from properties.

Use the **#openloops tag** for unresolved plot threads that need future attention. P.D. Workman, with 70+ published books, searches for #openloops during brainstorming sessions to find storylines left dangling in previous books. This simple tag prevents dropped plot threads that frustrate readers.

For series work, add book-specific tags:

```
#series/book1
#series/book2
#series/book3
```

This enables queries showing which characters appear in which books, essential when managing a cast of 50+ across multiple installments.

**Avoid these common tagging mistakes**: Creating tags like #protagonist-female-magic-user-northern-kingdoms when #character/protagonist and #northern-kingdoms suffice. Using tags for data that belongs in properties (don't tag #age-32, put age: 32 in frontmatter). Creating single-use tags that will never query usefully.

The test for whether something deserves a tag: "Will I ever want to query all notes with this tag?" If no, don't create it.

## Building dynamic dashboards with Dataview queries

Dataview transforms your vault from static notes into a living database. These queries create automatically updating views that would require hours of manual maintenance.

Create a master writing dashboard at your vault root:

```markdown
# Current Project Dashboard

## Scenes by Status

```dataview
TABLE 
  chapter as "Ch",
  word_count as "Words",
  round((word_count / words_goal) * 100) + "%" as "Progress",
  pov as "POV",
  location as "Location"
FROM "Book-03-Title/Drafts/Draft-1"
WHERE type = "scene"
SORT status ASC, chapter ASC
```

## Open Plot Threads

```dataview
TASK
FROM #openloops OR #plot/unresolved
WHERE !completed
```

## Characters Needing Development

```dataview
LIST
FROM #character
WHERE contains(tags, "#needs-expansion")
SORT file.name
```

## Timeline Verification

```dataview
TABLE 
  date_in_story as "Date",
  time_of_day as "Time",
  location as "Location",
  synopsis as "What Happens"
FROM "Book-03-Title"
WHERE type = "scene" AND date_in_story
SORT date_in_story ASC
```
```

This dashboard shows your project status at a glance: which scenes need work, which plot threads are unresolved, which characters need development, and whether your timeline is consistent.

For character tracking across scenes:

```markdown
## Character Appearance Tracker

```dataview
TABLE 
  pov as "POV",
  location as "Location",
  timeline as "When"
FROM #scene
WHERE contains(characters_present, "Kira")
SORT file.name
```
```

This query instantly shows every scene featuring Kira, essential for ensuring major characters don't disappear for too long.

**Track POV distribution** to ensure balanced multi-POV narratives:

```markdown
## POV Breakdown

```dataview
TABLE
  rows.file.link as "Scenes",
  sum(rows.word_count) as "Total Words"
FROM "Drafts/Draft-1"
WHERE type = "scene"
GROUP BY pov
SORT pov ASC
```
```

For series work, create a continuity checker:

```markdown
## Character Ages Across Series

```dataview
TABLE age-b1, age-b2, age-b3
FROM #character
WHERE age-b1
```
```

The power of Dataview is **automatic updates**—when you change a scene's status from draft to complete, your dashboard updates instantly without manual list editing. This saves hours across a 90,000-word novel.

For word count tracking, use DataviewJS for calculations:

```markdown
```dataviewjs
const project = dv.current();
const scenesPath = '"Book-03-Title/Drafts/Draft-1"';
const scenes = dv.pages(scenesPath).where(p => p.type == "scene");

const totalWords = scenes.word_count.sum() || 0;
const goalWords = project.words_goal || 100000;
const progress = Math.round((totalWords / goalWords) * 100);

dv.header(4, "Writing Progress");
dv.paragraph("**Total Words:** " + totalWords.toLocaleString());
dv.paragraph("**Goal:** " + goalWords.toLocaleString());
dv.paragraph("<progress max=100 value=" + progress + "></progress> " + progress + "%");
```
```

## Integrating AI tools into your creative workflow

AI integration works best when applied strategically at specific workflow stages rather than during drafting. **The 80/20 rule applies**: AI provides 80% rough content, you add the 20% that makes it yours.

Install the Text Generator plugin for versatile AI integration supporting ChatGPT, Claude, Gemini, and local models. For local privacy-focused work, set up LM Studio with models like Llama 3.2 3B (fast) or Gemma 2 27B (quality). Configure the plugin with your API key or local endpoint at `http://localhost:1234/v1/chat/completions`.

Alternatively, install the Copilot plugin for polished inline editing and custom prompt management. This costs around $10-20/month with built-in models or $1-5/month using your own API keys with spending limits.

**For brainstorming**, use Canvas for visual mind-mapping combined with AI expansion:

1. Create Canvas with random story thoughts, character concepts, plot possibilities
2. Document "State of the Union" - where characters and plot threads stand
3. Search vault for #openloops to find unresolved storylines
4. Use AI prompt: "Given these elements [paste canvas contents], suggest 10 plot directions that create maximum conflict"
5. Create visual connections until storyline gels

Store this comprehensive prompt library in your Templates folder:

```markdown
# Character Development Prompts

## Core Identity
For {{character_type}} in {{genre}}, generate:
1. Three conflicting motivations
2. One deep-seated fear driving behavior
3. Moral boundary they might cross under pressure
4. Two relationships complicating their journey
5. Character arc from beginning to end showing transformation

## Voice Development
Develop distinctive speech for {{character}}:
Education: {{level}}, Class: {{class}}, Region: {{region}}
Generate 5 dialogue examples showing:
1. Greeting a friend
2. Arguing with enemy
3. Lying convincingly
4. Expressing vulnerability
5. Commanding authority

Make each voice identifiable without dialogue tags through sentence length, vocabulary, verbal tics, and what they avoid saying.

## Plot Development Prompts

## Scene Structure
For scene: {{description}}

Break down:
1. Goal: What does POV character want?
2. Conflict: What prevents them?
3. Disaster: How does it go wrong?
4. Reaction: Emotional response
5. Dilemma: Impossible choice
6. Decision: What they choose next

## Plot Hole Detection
Analyze this outline for:
- Motivation gaps (why would they do this?)
- Timeline impossibilities
- Unearned resolutions (deus ex machina)
- Dropped plot threads
- Contradictions in worldbuilding
- Stakes that don't escalate properly

Be specific about which scene has each problem.

## Worldbuilding Prompts

## Culture Builder
Develop {{society_name}}:

SOCIAL STRUCTURE: Class system, gender roles, coming-of-age rituals, family structures

VALUES: Core values, religious practices, taboos, gap between heroic ideals and reality

DAILY LIFE: Typical day, food/clothing/housing, entertainment, education systems

Make culture feel lived-in with internal contradictions and competing viewpoints.
```

**For plot feedback**, compile your outline or completed chapters with Longform and prompt:

"Analyze this outline for structural weaknesses using the Save the Cat beat sheet. Identify where beats are missing or mis-timed. Note any motivation gaps, unearned character moments, or stakes that don't escalate properly. Be specific about which scenes need revision."

**For worldbuilding assistance**, create systematic prompts:

```
Phase 1 - Foundation: Create 3 defining features making {{world}} unique from typical fantasy
Phase 2 - Cultures: Develop {{culture}} with social structure, traditions, taboos, internal contradictions
Phase 3 - Magic/Tech: Design system with clear costs and limitations that create story conflict
Phase 4 - History: Create timeline with unresolved historical grievance driving current conflict
```

**For dialogue refinement**, select rough dialogue and use:

"Rewrite this dialogue with subtext—characters can't say what they really mean. Add physical actions showing power dynamics. Include interrupted thoughts and half-finished sentences. Make it feel natural while maintaining tension."

**For consistency checking**, after drafting use:

"Review chapters 1-10 for timeline inconsistencies, contradictions in character descriptions, and logical impossibilities. List specific issues with chapter and line references."

Organize AI conversations in a dedicated folder:

```
AI-Conversations/
├── Brainstorming/
│   └── Character-Ideas-2024-01-15.md
├── Research/
│   └── Forensics-QA-2024-01-18.md
└── Feedback/
    └── Chapter-5-Critique.md
```

Use this template for AI conversation notes:

```markdown
---
date: {{date}}
topic: {{topic}}
ai_model: ChatGPT-4
tags: [ai-conversation, brainstorming]
---

# AI: Character Development for Elena

## Context
Working on protagonist backstory for Book 1, need motivation that justifies extreme actions in climax.

## Prompt
{{exact_prompt_used}}

## Response
{{ai_output}}

## Actions
- [ ] Add betrayal by former partner to backstory
- [ ] Foreshadow trust issues in Chapter 3
- [ ] Reference this trauma at climax decision point

## Insights
The betrayal motivation connects internal and external conflicts better than revenge alone.
```

**Maintain creative control** by always heavily editing AI output. Red flags include: using AI prose without revision, generic plot developments that could apply to any story, losing your distinctive voice, not understanding why story decisions make sense. AI should clarify and generate options, never make final decisions about your story.

Document AI usage ethically:

```yaml
---
ai_assisted: true
ai_involvement: [brainstorming, critique, research]
ai_percentage: <10%
---

<!-- AI used for:
- Plot outline brainstorming (generated options, I selected and developed)
- Dialect research (verified with primary sources)
- Timeline consistency checking
All final prose is original -->
```

P.D. Workman's workflow from 70+ books: Draft without AI to maintain flow. After 30-day "seasoning" period, run each chapter through AI for awkward phrasing, inconsistencies, and missing sensory descriptions. Copy to Grammarly for grammar. Paste corrected version back. This keeps AI as editor rather than co-author.

## Essential plugins for novel writing

The plugin ecosystem makes Obsidian a complete novel-writing environment. **Start with these six essential plugins**: Longform for manuscript compilation, Dataview for tracking queries, Pandoc or Enhancing Export for Word conversion, Templater for dynamic templates, QuickAdd for rapid note creation, and your chosen sync solution.

**Longform plugin transforms Obsidian into a novel-writing IDE**. Install from Community Plugins, then right-click your book folder and select "Create Longform Project". Choose Multi-scene for novels (each chapter is a separate file) or Single-scene for short stories. This creates an Index.md file with project metadata.

Configure Longform to compile chapters into single manuscript, stripping frontmatter. Each chapter should be a numbered file: "01 - Opening Scene.md". The plugin's sidebar shows your scene hierarchy with drag-and-drop reordering. Create multiple drafts (Draft 1, Draft 2, Draft 3) within the same project to track revision stages.

Critical practice: **Immediately zip previous draft folders** after creating new draft. This prevents accidentally working on the wrong version and excludes old drafts from searches. Your drafts folder should look like: Draft-1.zip, Draft-2.zip, Draft-3/ (current).

Set up Longform workflows: "Default" for basic compilation, "Export to Word" that combines compilation with Pandoc conversion, "Final" that does full cleanup. The session tracker shows word count goals and daily progress.

**Dataview plugin enables all your tracking queries**. Install and enable JavaScript queries in settings for advanced features. Every template with YAML properties becomes queryable. The learning curve is moderate—SQL-like syntax but simpler. Use the Dataview Query Wizard (Custom GPT) to generate queries if stuck.

**Pandoc plugin (or Enhancing Export) handles final manuscript export**. Install Pandoc application system-wide first (Homebrew on Mac: `brew install pandoc`). Then install the Obsidian plugin. The original Pandoc plugin hasn't updated in 2+ years, so prefer the actively maintained "Enhancing Export" plugin.

Configure export to DOCX with standard manuscript format: body text with 1.5 line spacing and first-line indent, proper heading styles, header/footer fields. After export, open in Word for final spelling/grammar check and any manual formatting adjustments before sending to editors.

**Templater plugin adds dynamic templating with JavaScript**. Create templates that prompt for input and auto-generate content:

```markdown
---
chapter: null
title: "null"
characters_present: []
location: 
date_in_story: 
status: draft-1
word_count: 0
words_goal: 3000
created: 2025-11-18
---

# null - null

[Start writing here]


```

This template prompts for chapter number and title, renames the file, fills in frontmatter, and moves the file to the correct location—all automatically.

**QuickAdd plugin enables rapid note capture**. Set up Choices for different note types with assigned hotkeys:

- Alt+C: Create character sheet (prompts for name, creates from template, moves to Characters folder)
- Alt+L: Create location note
- Alt+I: Capture idea to "Story Ideas.md" with timestamp
- Alt+W: Create daily writing log

Configure each Choice with template path, file naming format, and destination folder. This eliminates friction when inspiration strikes.

**Notes Refactor plugin splits large notes**. P.D. Workman's workflow: write multiple chapters in a single daily file with H2 headers for each chapter. At end of day, use "Split note by heading level 2" command. This creates separate chapter files automatically, perfect for writers who prefer uninterrupted daily writing sessions.

For visual planning, enable the **Canvas core plugin**. Canvas excels at brainstorming and relationship mapping. Create story structure canvases connecting plot beats with arrows, character relationship webs showing conflicts and alliances, and worldbuilding maps linking locations, cultures, and historical events.

**Kanban plugin provides visual plot boards**. Create boards with columns like "Ideas → Outlined → Drafted → Revised → Complete" or "Act 1 → Act 2 → Act 3". Each card can link to actual scene notes. This works well for plotters who think visually. The plugin stores everything in plain Markdown, so boards remain future-proof.

For timeline visualization, install **April's Automatic Timelines** or **Easy Timeline**. Tag scene notes with timeline metadata, and these plugins generate visual chronologies showing story events in order. Essential for catching timeline inconsistencies in complex narratives with flashbacks or parallel plotlines.

**Better Word Count plugin** provides enhanced statistics beyond core Obsidian: selected text counts, character counts, better metadata handling. **Novel Word Count** shows stats directly in the file explorer and calculates folder-level word counts for entire drafts.

**Tag Wrangler** enables bulk tag operations. Right-click any tag in the Tags pane to rename (updates all files), merge duplicate tags, or create tag pages. This prevents tag drift where similar concepts accumulate different tags (#worldbuilding vs #world-building vs #world_building).

**Smart Typography** auto-converts straight quotes to curly quotes and fixes em-dashes—professional typography without manual formatting. Note: disable "Auto pair brackets" in editor settings when using this plugin to prevent conflicts.

For mobile writing, **Obsidian Sync ($4-8/month) is the premium solution** with seamless integration, end-to-end encryption, version history, and reliable cross-platform syncing. For free alternatives, Android users should use **Syncthing** (peer-to-peer sync with desktop) while iOS users can use iCloud Drive (simpler but occasional sync issues reported).

The optimal beginner setup: Longform, Dataview, Templater, QuickAdd, Pandoc, Better Word Count, Smart Typography, Tag Wrangler, and sync solution. That's 9 plugins total—enough power without overwhelming complexity. Add more only when you identify specific needs.

Advanced users like P.D. Workman add: Note Refactor, Kanban, Advanced Tables, Periodic Notes, Autolink Title, Todoist Sync, Whisper (audio transcription), and Text Generator (AI integration). The key principle: **plugins should enhance your writing process, not become a distraction from actually writing**.

## Managing drafts and story variations

Effective draft management prevents the nightmare of accidentally working on an old version for hours before realizing your mistake. The battle-tested system from 70+ published books: **create separate draft folders, compress old drafts immediately, and use status properties to track current work**.

Structure your Drafts folder like this:

```
Drafts/
├── Draft-1.zip (compressed immediately after starting Draft 2)
├── Draft-2.zip (compressed after starting Draft 3)
└── Draft-3/ (current working draft)
    ├── 01 - Opening Scene.md
    ├── 02 - Meet the Villain.md
    └── ...
```

When starting a new draft: 1) Zip the previous draft folder, 2) Duplicate it, 3) Rename the duplicate to next draft number, 4) Begin revisions. The compressed archive stays searchable but won't appear in general vault searches, preventing confusion.

Mark each scene with draft version in frontmatter:

```yaml
draft: 3
status: current
version-date: 2024-10-10
```

For story branching and alternate endings, create a dedicated structure:

```
Novel-Project/
├── main-timeline/
├── alternate-branches/
│   ├── branch-A-romance-ending/
│   │   ├── 15-divergence-point.md
│   │   ├── 16-alternate-scene.md
│   │   └── metadata.md
│   ├── branch-B-tragedy-ending/
│   └── branch-C-what-if-villain-wins/
└── decision-tree.canvas
```

Use Canvas to create visual decision trees showing branching points with arrows connecting cause and effect. Color-code different timeline branches for quick identification.

Tag variations with metadata:

```yaml
timeline: main
branch: alternate-A
divergence-point: chapter-15
scenario: what-if-hero-refuses
belongs-to: timeline-A
status: exploratory
```

Create hub notes for major divergence points:

```markdown
# Chapter 12 - The Choice (Divergence Point)

## Canon Version
[[12-choice-main-timeline]]

## Alternate Branches
- [[12-choice-branch-A-refuses-call]] #alternate #branch-A
- [[12-choice-branch-B-accepts-quest]] #alternate #branch-B
- [[12-choice-branch-C-betrays-mentor]] #alternate #branch-C

## Decision Consequences
Branch A leads to: [[15-living-with-regret]]
Branch B leads to: [[15-heroic-journey-begins]]
Branch C leads to: [[15-villain-origin-arc]]
```

For revision tracking, use the checkbox system (Cmd/Ctrl-L) to insert task checkboxes inline:

```markdown
The detective examined the scene. - [ ] Add more sensory details here

"We need to find the weapon," Marcus said. - [ ] Make dialogue sound more natural
```

Query incomplete revision tasks:

```dataview
TASK
WHERE !completed
FROM "drafts/draft-3"
```

The marker system for critical notes: insert **999** for editor notes that need to persist through export to Word. Search for "999" before final submission to catch all marked issues.

For beta reader feedback, create organized folders:

```
feedback/
├── beta-readers/
│   ├── reader-1-sarah/
│   │   ├── general-feedback.md
│   │   └── chapter-notes.md
│   ├── reader-2-john/
│   └── reader-3-maria/
├── consolidated-feedback.md
└── action-items.md
```

Consolidate feedback into actionable tasks:

```markdown
# Beta Reader Feedback Summary

## Chapter 5 - The Revelation

### Issues Raised (Multiple Readers)
- [ ] Pacing too slow (Sarah, John) #pacing
- [ ] Character motivation unclear (Sarah, Maria) #character

### Positive Feedback
- Dialogue feels natural (all readers)
- Twist was surprising but earned (John, Maria)

### Individual Observations
- [[Reader-Sarah-Chapter-5]] - Suggested cutting opening paragraph
- [[Reader-John-Chapter-5]] - Loved the metaphor about storms
```

For version control power users, integrate Git with the **Obsidian Git plugin**. Initialize repository, configure auto-commits every 30-60 minutes, and push after each writing session. This creates complete revision history you can revert to if needed. Tag major milestones: "v1.0-draft-complete", "v2.0-revision-complete", "v3.0-final".

The comprehensive backup strategy:
- **Layer 1**: Obsidian File Recovery (automatic, built-in)
- **Layer 2**: Manual compressed archives of draft folders
- **Layer 3**: Git with GitHub/GitLab (complete history)
- **Layer 4**: Cloud sync (Obsidian Sync or Dropbox)
- **Layer 5**: Export backups at milestones (compiled Word/PDF)

## Organizing worldbuilding for epic fantasy and sci-fi series

Worldbuilding organization determines whether your series maintains consistency across 10 books or accumulates contradictions that force awkward retcons. **The Wiki folder serves as your immutable series bible**—once something is established here, it becomes canon for all books.

Structure your Wiki with these subfolders:

**Characters** contains profiles for all characters who appear in multiple books. Track age progression across series:

```yaml
age-b1: 24
age-b2: 25  
age-b3: 27
```

**Copy exact physical descriptions from published books** into character notes to lock them:

```markdown
## Physical Description (LOCKED)
*From Book 1, Chapter 2:*
"Auburn hair past her shoulders, green eyes with gold flecks, standing 5'6" with an athletic build"

DO NOT CHANGE without series-wide revision.
```

**Locations** contains your geography hierarchy. Create continent notes linking to regions, region notes linking to cities, city notes linking to landmarks. Each location note tracks travel times to other locations:

```markdown
## Travel Times
- From [[Capital City]]: 3 days horse, 5 days walking
- From [[Port Town]]: 2 days ship (favorable winds)

LOCKED SINCE BOOK 1 - Do not change without continuity check
```

**Magic-Systems** documents your magic's absolute rules—what it can do, cannot do, and costs for using it:

```markdown
# Aethermancy

## CORE RULES (NEVER VIOLATE)
✓ CAN: Manipulate energy, create light/heat, levitation
✗ CANNOT: Resurrect the dead, time travel, true mind control
⚠️ COSTS: Mental exhaustion, addiction risk, years of training required

## Power Levels (Training Time)
Novice (1 year): Small sparks, basic levitation
Adept (5 years): Energy blasts, sustained flight  
Master (15 years): Weather manipulation, teleportation
Grand Master (30+ years): Time dilation, mass transformation

## Practitioners Database
```dataview
TABLE skill-level, specialization, location
FROM #character AND #magic-user
SORT skill-level DESC
```
```

**History-Timeline** contains your complete chronology from world creation to current book events:

```markdown
# Complete Series Timeline

## Ancient History (1000+ years ago)
- ~2000 ya: World created by [[Divine Beings]]
- 1500 ya: [[First Empire]] established
- 1000 ya: [[The Cataclysm]] - magic emerged

## Recent History (Last 100 years)
- 50 ya: [[Discovery of Aether]]
- 25 ya: [[Protagonist]] born

## Book 1: Shadow Rising (Spring-Summer Year 0, 3 months)
| Day | Event | Location | Chapter |
|-----|-------|----------|---------|
| 1 | Inciting Incident | [[Village]] | Ch 1 |
| 45 | Midpoint Twist | [[Capital]] | Ch 13 |
| 90 | Climax | [[Mountain]] | Ch 25 |

## Book 2: (Autumn Y0-Winter Y1, 6 months)
Gap from B1: 2 weeks
Starts: Day 104

## Book 3: CURRENT (Summer Y1-Y2, 1 year)
Gap from B2: 3 months  
Starts: Day 370
```

**Organizations-Factions** documents political structures, guilds, secret societies. Track leadership succession and internal conflicts:

```markdown
# The Mage Guild

## Leadership
Current Guildmaster: [[Character Name]] (since Year 245)
Previous: [[Character Name]] (died Book 2, Chapter 18)

## Structure
Council of Nine Masters → Regional Chapters → Apprentices

## Political Position (Book 3)
Allied with [[Faction A]], conflict with [[Faction B]]
Neutral on [[Political Crisis]]

## Appearances
```dataview
TABLE chapter, event
FROM "Books"
WHERE contains(organizations, "Mage Guild")
SORT file.name
```
```

**Cultures** contains ethnography—social structures, beliefs, customs, daily life, values. Make cultures feel lived-in with **internal contradictions** rather than monolithic uniformity:

```markdown
# Northern Kingdom Culture

## Core Values (Official)
Honor, duty, loyalty to clan

## Core Values (Actual)
Honor when convenient, self-preservation, family first

## Social Structure
Clan-based hierarchy with contested leadership succession

## Taboos
- Breaking guest-right (death penalty)
- Showing weakness publicly (loss of status)
- Marrying outside clan (varies by clan)

## Daily Life
Cold climate influences everything: architecture (thick walls, small windows), clothing (layered furs), food (preserved meats, root vegetables), entertainment (indoor storytelling traditions)
```

Create a **Master Series Bible** document linking everything:

```markdown
# SERIES BIBLE - Chronicles of Aethermoor

## QUICK REFERENCE
- [[Character Index]]
- [[Location Index]]  
- [[Complete Timeline]]
- [[Plot Threads Tracker]]
- [[Magic System Rules]]

## CONSISTENCY RULES (LOCKED)

### Magic - IRON RULES
✓ CAN: [specific locked list from Book 1]
✗ CANNOT: No resurrection, no time travel, no mind control
⚠️ COSTS: Mental exhaustion, addiction risk

### Geography - FIXED SINCE BOOK 1
Travel times are locked canon. Changes require series-wide continuity check.
[[City A]] to [[City B]]: 5 days horse (DO NOT CHANGE)

### Style Guide
- grey (not gray)
- towards (not toward)
- Aethermancy always capitalized
- Character titles lowercase unless part of name

## CONTINUITY CHECKLIST
Before starting each new book:
- [ ] Verify timeline gaps and character ages
- [ ] Check magic rules never violated
- [ ] Confirm geography/distances match
- [ ] Lock physical descriptions from published books
- [ ] Review unresolved plot threads from previous book
```

For **cross-book plot thread tracking**, maintain this database:

```markdown
# Plot Threads MOC

## Active Series-Spanning Threads

### [[Ancient Prophecy]] - Books 1-5
- B1: Introduced cryptically [[B1-Ch7]]
- B2: Part fulfilled [[B2-Ch20]], reinterpreted
- B3: Major revelation planned
- B4-5: Full resolution planned
Status: Active, 60% complete

### [[Political Crisis]] - Books 1-3
- B1: King dies [[B1-Ch2]]
- B2: Civil war begins [[B2-Ch8]]
- B3: Resolution planned for climax
Status: Active, will resolve

## Resolved Threads ✓

### [[Mystery Artifact]] - Resolved B2-Ch18
Setup B1-Ch12, resolved B2-Ch18
Consequence: Triggered [[Event in B3]]
```

The **foreshadowing tracker** prevents dropped setups:

```markdown
# Foreshadowing Database

| Setup | Location | Payoff | Payoff Location | Status |
|-------|----------|--------|-----------------|--------|
| Strange dreams | B1-Ch2 | B3-Ch20 | [[Revelation Scene]] | ✓ Resolved |
| Mentor's warning | B1-Ch8 | B2-Ch15 | [[Betrayal]] | ✓ Resolved |
| Ancient artifact mention | B1-Ch12 | B5 (planned) | TBD | ⏳ Pending |
```

Create Map of Content (MOC) hub notes for major topics:

```markdown
# Worldbuilding MOC

## Geography
- [[Continents Overview]]
- [[Northern Kingdoms]]
- [[Southern Realms]]
- [[Complete World Map]]

## Systems
- [[Magic System]]
- [[Technology Level]]
- [[Economy & Trade]]

## Cultures
- [[Culture A Ethnography]]
- [[Culture B Ethnography]]
- [[Religion Overview]]

## History
- [[Ancient History]]
- [[Classical Period]]
- [[Modern Era]]
- [[Complete Timeline]]
```

For **managing large character casts (50-400+ characters)**, use hierarchical organization with Dataview queries:

```markdown
# Character Directory

## Protagonists (5)
[[Character A]], [[Character B]], [[Character C]]...

## Main Supporting (20)
```dataview
LIST role
FROM #character AND #supporting AND #major
SORT file.name
```

## By Region
```dataview
LIST role
FROM #character AND #active
GROUP BY region
SORT region
```

## By First Appearance
```dataview
TABLE role, current-status
FROM #character
WHERE first-book = "Book 1"
```

## Deceased (Track for continuity)
```dataview
TABLE death-date, death-location, cause
FROM #character AND #deceased
SORT death-date DESC
```

The key organizational principle: **Wiki = immutable series canon, Book folders = mutable drafts**. Never change Wiki content without checking every book for contradictions. This separation prevents the cascading continuity errors that plague long series.

## Turning your vault into a productivity engine

The difference between a vault that accelerates writing and one that creates busywork lies in workflow integration. **Your vault should fade into the background, enabling flow rather than demanding attention**.

P.D. Workman's complete novel workflow from 70+ books demonstrates integration:

**Week 1: Brainstorming**. Create Canvas with random thoughts. Document series "State of Union" noting character positions and unresolved plots. Search #openloops for dangling threads. Use AI prompts for plot direction suggestions. Create visual connections until storyline gels. Produce short outline.

**Week 2: Plot Development**. Snowflake Method in Prep folder—develop logline, 5-line summary, back cover copy. Create character sheets with names, pictures, basic traits. Research key topics in Research folder. Build detailed outline or Kanban board (broad strokes, not chapter-by-chapter).

**Week 3: Cover and Marketing** (parallel track). Brainstorm titles, check Goodreads for conflicts. Create mockup cover. Draft marketing metadata—taglines, tropes, keywords, comp titles.

**Weeks 4-12: First Draft**. Set up Longform project. Write in daily file or directly in chapter files numbered with descriptions. Track metadata in YAML properties. Use Cmd/Ctrl-L for inline checkboxes marking revision needs. Insert 999 markers for editor notes. End each day: write chapter summaries, adjust outline, conduct additional research.

**Weeks 13-15: Draft 2**. Zip Draft 1, create Draft 2 copy. Address all checkboxes and 999 markers. Read chapter by chapter. Run AI critique for awkward sentences, inconsistencies, sensory descriptions. Copy to Grammarly, paste corrections back.

**30-day Seasoning Period**. Don't touch manuscript. Work on next book. Let your brain reset.

**Weeks 19-20: Final Revisions**. High-speed read catching inconsistencies, plot holes, continuity errors. Polish first and last chapters (read aloud). Run spelling/grammar check in Word. Send to editor.

**Weeks 21-22: Post-Editor**. Review editor changes. Format in Vellum or formatting software. Send to ARC readers. Implement final feedback. Upload.

Throughout this workflow, the vault provides: **Longform for scene organization, Dataview dashboards showing progress, Templates generating consistent note structures, QuickAdd capturing inspiration instantly, Pandoc exporting to Word, Canvas visualizing plot connections, and Git backing up everything automatically**.

The key plugins work together: QuickAdd creates notes from templates, Templater makes those templates dynamic, Dataview queries show project status, Longform compiles the manuscript, and Pandoc exports to Word. Each plugin handles one job well rather than trying to be an all-in-one solution.

**Set up workspace layouts** for different phases. Writing Workspace: Longform sidebar, main editor, properties panel on right. Planning Workspace: Canvas, Kanban board, outline notes in tabs. Research Workspace: Split panes with multiple reference documents. Editing Workspace: Manuscript with Grammarly checking, Track Changes simulation.

Create keyboard shortcuts for common actions: Cmd/Ctrl-E for QuickAdd scene creation, Cmd/Ctrl-D for daily log, Cmd/Ctrl-T for inserting timestamps. Reduce friction for repetitive tasks.

The vault becomes a **productivity engine when it provides three things**: instant capture (QuickAdd), reliable retrieval (Dataview queries), and comprehensive context (linked notes). When you can capture a character idea in 10 seconds, find all scenes featuring that character in 5 seconds, and see their entire relationship web instantly, you spend time writing rather than managing.

## Conclusion: From organized vault to finished novels

The truly transformative aspect of a well-structured Obsidian vault isn't organization for its own sake—it's **how organization enables creative emergence**. When you can instantly find the scene where a character's eye color was established, trace plot threads across three books, verify timeline consistency with a single query, and see relationship webs at a glance, your brain shifts from administrative overhead to creative problem-solving.

The authors successfully using these systems report **a qualitative shift in their writing process**. Instead of dreading continuity checks or avoiding complex multi-POV narratives due to tracking difficulty, they embrace complexity because their vault handles the cognitive load. Character casts expand from 20 to 200 without proportional management burden. Series extend from trilogies to 10-book epics while maintaining consistency.

The critical insight: **your vault should be a second brain, not a filing cabinet**. Filing cabinets organize by location—this document goes in that folder. Second brains organize by connection—this concept relates to these seventeen other concepts in non-obvious ways. The difference is Dataview queries that show you things you didn't remember, Graph view revealing thematic connections you didn't consciously create, and linked references surfacing relevant context exactly when needed.

The path forward starts with one practice: **implement the folder structure and one template today**. Not the entire system—just the basic folder hierarchy and scene template with YAML properties. Write three scenes using that template. Then add one Dataview query to show your scenes. That's sufficient to experience the shift from file management to knowledge management.

As your vault grows organically—accumulating characters, locations, plot threads, worldbuilding notes—the network effects compound. The 200th note is exponentially more valuable than the 20th because it connects to 199 other context nodes. This is when the system transitions from overhead to asset, when checking continuity becomes faster than writing from memory, when the vault generates story ideas through unexpected connections.

The ultimate goal isn't a perfectly organized vault. It's finishing your novel series with confidence that every detail aligns, every thread resolves, and every character remains consistent—while enjoying the writing process enough to start the next project.