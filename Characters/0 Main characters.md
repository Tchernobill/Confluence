---
title:
tags:
  - Characters
  - Inner_Circle
version: "0.6"
status: in progress
last_updated: 2025-09-28 17:15
type: Reference
---
```dataview
table character_name as "Character", character_core as "Core", tome as "Tome", role_in_story as "Role"
from "Characters"
where type = "character-tome"
sort character_name asc, tome asc

```
