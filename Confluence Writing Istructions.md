I'll search the project knowledge to map out the current file and folder structure for the Confluence novel.Based on the project knowledge search results, I can see references to a comprehensive file structure that exists in your full project repository, but the current GitHub project files only contain a single template file. Let me create a comprehensive map based on the information found in the search results:

# Confluence Novel - GitHub File Structure Map

## Full Project Structure (Referenced in Documents)

### 📁 Root Level

```
Root/
├── Confluence Story Bible.md          # Master reference document
├── Confluence Writing Instructions.md      # (This document - writing protocols)
└── [Additional root-level docs]
```

### 📁 Story/ (Main narrative content)

```
Story/
├── Dev/
│   └── 2108-00-00_12-00 - Scene Template.md (Scene summary template for new scenes)
│
├── Era 1 - The Scavenger/
│   ├── 2108-05-31_14-00 - The Enforcer Incident.md
│   ├── 2108-07-02_22-00 - The Riot Night.md
│   └── [Other Era 1 scenes]
│
├── Era 4 - The Boss/
│   ├── Era 4 - The Boss.md (Era overview)
│   ├── 2109-07-13_21-30 - The Takeover.md
│   ├── 2109-07-30_16-00 - The Behemoth Incident.md
│   ├── 2109-08-15_00-00 - King Of The Mat.md
│   └── [Other Era 4 scenes]
│
└── [Eras 2, 3, 5, 6 - similar structure]
```

### 📁 Arcs/Eras/ (Structural planning)

```
Arcs/Eras/
└── Era 5 Arc - Bismarckian Strategy for South Shore Slum Consolidation.md
└── [Other era arc documents]
```

### 📁 Characters/ (Character documentation)

```
Characters/
├── Characters Base.base (Database view configuration)
└── Dev/
    └── [Character files with #cast tag]
```

### 📁 Additional Structure (Inferred)

```
Locations/
├── South Shore Slum.md
├── Market Square.md
├── Kyr4n's Utility Room Hideout.md
└── Main Gym - Organization Headquarters.md

Plot Threads/
├── Thread: Kyr4n's Hidden Abilities.md
├── Thread: Territory Consolidation.md
├── Thread: Zara Integration.md
└── [Other plot threads]

Themes/
├── Theme: Violence as Protection.md
├── Theme: Hidden Power.md
└── [Other themes]

World-Building/
├── Enhancement Technology.md
├── Criminal Territory Structure.md
└── South Shore Culture.md

Timelines/
├── Chronos Timeline (main)
└── Tome-specific timelines
```

## File Naming Convention

**Scene Files:**

```
YYYY-MM-DD_HH-MM - Scene Title.md
```

- Example: `2108-05-31_14-00 - The Enforcer Incident.md`
- Date/time reflects in-story timeline
- Allows chronological sorting

**Character Files:**

```
[Character Name] - [Type].md
```

- Types: Summary, Details, Evolution
- Example: `Kyr4n - Evolution.md`

**Era/Arc Files:**

```
Era [Number] - [Era Name].md
Era [Number] Arc - [Description].md
```

## Scene File Structure

Each scene file contains comprehensive YAML frontmatter including:

- Story date/time
- Location
- POV character
- Narrative arc
- Scene type
- Characters present
- Plot threads
- Thematic elements
- Status and word count
- Previous/next scene links
- Foreshadowing elements

## Key Organization Features

1. **Date-based scene naming** enables chronological navigation
2. **Era folders** group scenes by major story phases
3. **Characters** maintain detailed character documentation
4. **Dataview queries** in overview files auto-generate scene lists
5. **Wiki-links** [[like this]] connect related documents
6. **Tags** enable filtering (#cast, #location, etc.)
7. **YAML frontmatter** provides rich metadata for querying