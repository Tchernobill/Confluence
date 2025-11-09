TABLE story_date, title, narrative_arc, pov
FROM "Confluence/Scenes"
SORT story_date ASC
WHERE narrative_arc = "foundation_and_isolation"


TABLE story_date, pov, narrative_arc, status
FROM "Confluence/Scenes"
WHERE contains(plot_threads, "Sedh's Awakening")
SORT story_date ASC

