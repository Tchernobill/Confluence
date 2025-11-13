---
type: arc
arc_type: character
name: Kyr4n Learning Connection
status: active
theme: isolation_vs_connection
focus_characters:
  - "[[Kyr4n]]"
related_arcs:
  - "[[Isa Finding Safety]]"
scenes:
  - "[[2108-05-01_afternoon_scene]]"
progress: 0
summary: "Tracks Kyr4n’s growth from detached survivalist to someone capable of trust and emotional intimacy."
---
# Character Arc: {{name}}

## Emotional Journey
- **Starting State:** [Emotionally numb, survival-focused]
- **Challenges:** [Internal and external barriers to connection]
- **Climax:** [Turning point of vulnerability]
- **Resolution:** [Moment of earned emotional openness]

## Development Beats
| Phase | Description |
|--------|-------------|
| Setup | [Initial condition] |
| Conflict | [Growing tension] |
| Crisis | [Emotional collapse] |
| Resolution | [New perspective] |

## Involved Scenes
```dataview
TABLE story_date AS "Date", title AS "Scene", status
FROM "03.Hobbies/Writing/Confluence/Scenes"
WHERE contains(character_arcs, this.file.link)
SORT story_date ASC
```
