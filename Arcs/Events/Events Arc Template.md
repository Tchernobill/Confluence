---
type: arc
arc_type: event
name: DarkNight Outbreak
status: active
theme: corruption_and_survival
summary: Chronicles the outbreak and spread of the DarkNight infection across Proxima District and the characters’ responses.
locations:
  - "[[Proxima District]]"
  - "[[Phoenix Recovery]]"
focus_characters:
  - "[[03.Hobbies/Writing/Confluence_bak/Characters/Kyr4n]]"
  - "[[03.Hobbies/Writing/Confluence_bak/Characters/Mira]]"
scenes:
  - "[[2111-02-17_lab_raid]]"
  - "[[2111-02-20_quarantine_scene]]"
related_arcs:
  - "[[Era: The Boss]]"
progress: 0
---
# Event Arc: {{name}}

## Scope
- **Location(s):** `=this.locations`
- **Duration:** [Estimated time span in story]

## Purpose
[Why this event matters in the grand narrative: stakes, moral tension, impact on characters.]

## Related Scenes
```dataview
TABLE story_date AS "Date", title AS "Scene", pov AS "POV", status
FROM "03.Hobbies/Writing/Confluence/Scenes"
WHERE contains(plot_threads, this.file.link) OR contains(character_arcs, this.file.link)
SORT story_date ASC
```
