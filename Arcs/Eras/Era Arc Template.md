---
type: arc
arc_type: era
name: The Scavenger
status: active
timeline_start: 2108-04-01
timeline_end: 2111-03-12
theme: survival_vs_identity
summary: Kyr4n’s early years as a scavenger, surviving the underbelly of South Shore and building the foundation of his identity.
locations:
  - "[[South Shore Slums]]"
  - "[[The Stacks]]"
focus_characters:
  - "[[Kyr4n]]"
  - "[[Isa]]"
scenes:
  - "[[2108-04-30_evening_scene]]"
  - "[[2108-05-01_afternoon_scene]]"
related_arcs:
  - "[[Arc: Kyr4n Learning Connection]]"
progress: 0
---
# Era: {{name}}

## Overview
A general summary of this era’s role in the story’s macro-timeline.

## Narrative Function
- **Primary Conflict:** [Core struggle defining the era]
- **Transformation Focus:** [What changes over this time]
- **Tone Evolution:** [How the emotional texture shifts]

## Timeline Coverage
| From | To | Duration |
|------|----|-----------|
| `=this.timeline_start` | `=this.timeline_end` | `=date(this.timeline_end).diff(date(this.timeline_start), "days")` days |

## Contained Scenes
```dataview
TABLE story_date AS "Date", title AS "Scene", status
FROM "03.Hobbies/Writing/Confluence/Scenes"
WHERE contains(character_arcs, this.file.link) OR contains(plot_threads, this.file.link)
SORT story_date ASC
