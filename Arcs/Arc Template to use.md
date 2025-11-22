---
type: arc
name: Kyr4n Learning Connection
arc_type: character
status: active
theme: isolation_vs_connection
focus_character: "[[03.Hobbies/Writing/Confluence_bak/Characters/Kyr4n]]"
related_arcs:
  - "[[Isa Finding Safety]]"
related_threads:
  - "[[Thread: Kyr4n's Isolation]]"
scenes:
  - "[[2108-04-30_evening_scene]]"
  - "[[2108-05-01_afternoon_scene]]"
progress: 0
notes: ""
---
# {{name}}

## Overview
[What this arc is about emotionally and narratively.]

## Transformation Stages
1. **Setup:** [Initial state]
2. **Conflict:** [Obstacle preventing growth]
3. **Crisis:** [Moment of collapse or revelation]
4. **Resolution:** [How character changes]

## Related Scenes
```dataview
TABLE story_date AS "Date", title AS "Scene", status AS "Status"
FROM "03.Hobbies/Writing/Confluence/Scenes"
WHERE contains(character_arcs, this.file.link)
SORT story_date ASC

