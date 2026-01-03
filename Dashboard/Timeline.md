```dataview
TABLE
  scene_date AS "Date",
  scene_time AS "Time",
  scene_title AS "Scene",
  pov AS "POV",
  status AS "Status"
FROM "Scenes"
WHERE stage = null
SORT scene_date ASC, scene_time ASC

```



POV-Specific Timeline - Kyr4n
```dataview
TABLE
  scene_date,
  scene_time,
  scene_title,
  status
FROM "Scenes"
WHERE pov = "Kyr4n"
AND stage = null
SORT scene_date, scene_time

```

Scene Progress Tracker
```dataview
TABLE
  scene_title,
  status,
  file.mtime AS "Last touched"
FROM "Scenes"
WHERE stage = null
SORT file.mtime DESC

```

