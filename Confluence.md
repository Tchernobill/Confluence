---
title: Confluence Master Dashboard
tags:
  - dashboard
  - Confluence
---

# 🌌 Confluence Master Dashboard
> Six-tome cyberpunk saga spanning 2086-2165
## 📊 Project Overview

```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene");

const tomes = [1, 2, 3, 4, 5, 6];
let tomeStats = {};

for (let tome of tomes) {
  let tomeScenes = scenes.where(s => s.tome === tome);
  tomeStats[tome] = {
    sceneCount: tomeScenes.length,
    totalWords: tomeScenes.array().reduce((sum, s) => sum + (Number(s.words_count) || 0), 0),
    complete: tomeScenes.where(s => s.status === "final").length,
    draft: tomeScenes.where(s => s.status === "draft").length,
    inProgress: tomeScenes.where(s => s.status === "in progress").length
  };
}

let totalScenes = scenes.length;
let totalWords = scenes.array().reduce((sum, s) => sum + (Number(s.words_count) || 0), 0);
let totalComplete = scenes.where(s => s.status === "final").length;

dv.header(3, `📈 Series-Wide Statistics`);
dv.paragraph(`**Total Word Count**: ${totalWords.toLocaleString()} words`);
dv.paragraph(`**Total Scenes**: ${totalScenes} | **Complete**: ${totalComplete} (${Math.round(totalComplete/totalScenes*100)}%)`);

dv.header(4, "Per-Tome Breakdown");
let tomeTable = tomes.map(t => {
  let stats = tomeStats[t];
  let pct = stats.sceneCount > 0 ? Math.round(stats.complete/stats.sceneCount*100) : 0;
  return [
    `**Tome ${t}**`,
    stats.totalWords.toLocaleString(),
    stats.sceneCount,
    `${stats.complete}/${stats.sceneCount}`,
    `${pct}%`,
    `✏️${stats.inProgress} | 📝${stats.draft}`
  ];
});

dv.table(
  ["Tome", "Words", "Scenes", "Complete", "Progress", "Status"],
  tomeTable
);
````


---

## 📝 Current Writing Focus

```dataview
TABLE WITHOUT ID
  tome + "." + chapter + "." + scene_number as "Scene ID",
  file.link as "Title",
  pov as "POV",
  words_count as "Words",
  status as "Status"
FROM "03.Hobbies/Writing/Confluence/Story"
WHERE type = "scene" AND (status = "in progress" OR status = "draft")
SORT file.mtime DESC
LIMIT 10
```

---

## 🎭 Character Appearances by Tome

```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene" && p.characters_present);

// Get all unique characters
let characterSet = new Set();
for (let scene of scenes) {
  if (scene.characters_present) {
    for (let char of scene.characters_present) {
      let charName = char.path ? char.path.split("/").pop().replace(".md", "") : char;
      characterSet.add(charName);
    }
  }
}

// Count appearances per tome for major characters
let characters = Array.from(characterSet);
let majorCharacters = ["Kyr4n", "Isa", "Sedh", "Mira", "Aurelio"]; // Adjust based on your main cast

dv.header(3, "Main Cast Scene Count");

let charTable = majorCharacters.map(char => {
  let row = [char];
  for (let tome = 1; tome <= 6; tome++) {
    let count = scenes.where(s => 
      s.tome === tome && 
      s.characters_present && 
      s.characters_present.some(c => {
        let name = c.path ? c.path.split("/").pop().replace(".md", "") : c;
        return name === char;
      })
    ).length;
    row.push(count || "-");
  }
  return row;
});

dv.table(
  ["Character", "T1", "T2", "T3", "T4", "T5", "T6"],
  charTable
);
```

---

## 📅 Timeline Tracker

```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene" && p.story_date)
  .sort(p => p.story_date, 'asc');

dv.header(3, "Chronological Scene Distribution");

// Group by year
let yearGroups = {};
for (let scene of scenes) {
  if (scene.story_date && scene.story_date !== "TBD") {
    try {
      let year = scene.story_date.toString().substring(0, 4);
      if (!yearGroups[year]) yearGroups[year] = [];
      yearGroups[year].push(scene);
    } catch (e) {
      // Skip invalid dates
    }
  }
}

let yearTable = Object.keys(yearGroups).sort().map(year => {
  let sceneCount = yearGroups[year].length;
  let tomes = [...new Set(yearGroups[year].map(s => s.tome))].sort().join(", ");
  return [year, sceneCount, tomes];
});

dv.table(
  ["Year", "Scenes", "Tomes"],
  yearTable
);

dv.header(4, "Scenes with TBD Dates");
let tbdScenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene" && (!p.story_date || p.story_date === "TBD"));
dv.paragraph(`⚠️ ${tbdScenes.length} scenes need timeline placement`);
```

---

## 🧵 Plot Thread Tracker

```dataview
TABLE WITHOUT ID
  file.link as "Thread",
  status as "Status",
  introduced as "Introduced",
  resolved as "Resolved"
FROM "03.Hobbies/Writing/Confluence/Wiki/Plot-Threads"
SORT status ASC, file.name ASC
```

---

## 👁️ POV Distribution

```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene" && p.pov);

let povCounts = {};
for (let scene of scenes) {
  let pov = scene.pov;
  if (!povCounts[pov]) povCounts[pov] = { total: 0, byTome: {} };
  povCounts[pov].total++;
  if (!povCounts[pov].byTome[scene.tome]) povCounts[pov].byTome[scene.tome] = 0;
  povCounts[pov].byTome[scene.tome]++;
}

let povTable = Object.keys(povCounts)
  .sort((a, b) => povCounts[b].total - povCounts[a].total)
  .map(pov => {
    let row = [pov, povCounts[pov].total];
    for (let tome = 1; tome <= 6; tome++) {
      row.push(povCounts[pov].byTome[tome] || "-");
    }
    return row;
  });

dv.table(
  ["POV Character", "Total", "T1", "T2", "T3", "T4", "T5", "T6"],
  povTable
);
```

---

## 📍 Location Usage

```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene" && p.location);

let locationCounts = {};
for (let scene of scenes) {
  let loc = scene.location;
  let locName = loc.path ? loc.path.split("/").pop().replace(".md", "") : loc;
  if (!locationCounts[locName]) locationCounts[locName] = 0;
  locationCounts[locName]++;
}

let topLocations = Object.entries(locationCounts)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 10)
  .map(([loc, count]) => [loc, count]);

dv.header(3, "Top 10 Most Used Locations");
dv.table(["Location", "Scene Count"], topLocations);
```

---

## 🎯 Word Count Goals

```dataviewjs
const SCENE_BUDGET = 3000; // Average words per scene target
const TOME_BUDGET = 8000; // Words per chapter budget (adjust as needed)

const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene");

dv.header(3, "Writing Progress vs Goals");

for (let tome = 1; tome <= 6; tome++) {
  let tomeScenes = scenes.where(s => s.tome === tome);
  if (tomeScenes.length === 0) continue;
  
  let actualWords = tomeScenes.array().reduce((sum, s) => sum + (Number(s.words_count) || 0), 0);
  let chapters = new Set(tomeScenes.array().map(s => s.chapter)).size;
  let estimatedGoal = chapters * TOME_BUDGET;
  let progress = Math.round((actualWords / estimatedGoal) * 100);
  
  dv.paragraph(`**Tome ${tome}**: ${actualWords.toLocaleString()} / ${estimatedGoal.toLocaleString()} words (${progress}%)`);
}
```

---

## 🚨 Continuity Alerts

```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene");

let alerts = [];

// Check for scenes without dates
let noDateCount = scenes.where(s => !s.story_date || s.story_date === "TBD").length;
if (noDateCount > 0) {
  alerts.push(`⚠️ ${noDateCount} scenes missing timeline dates`);
}

// Check for scenes without POV
let noPOVCount = scenes.where(s => !s.pov).length;
if (noPOVCount > 0) {
  alerts.push(`⚠️ ${noPOVCount} scenes missing POV designation`);
}

// Check for scenes without locations
let noLocationCount = scenes.where(s => !s.location).length;
if (noLocationCount > 0) {
  alerts.push(`⚠️ ${noLocationCount} scenes missing location`);
}

// Check for scenes without characters
let noCharCount = scenes.where(s => !s.characters_present || s.characters_present.length === 0).length;
if (noCharCount > 0) {
  alerts.push(`⚠️ ${noCharCount} scenes without characters listed`);
}

if (alerts.length > 0) {
  dv.header(3, "⚠️ Issues Requiring Attention");
  dv.list(alerts);
} else {
  dv.paragraph("✅ No major continuity issues detected!");
}
```

---

## 📚 Recent Modifications

```dataview
TABLE WITHOUT ID
  file.link as "File",
  tome as "Tome",
  chapter as "Ch",
  status as "Status",
  file.mtime as "Modified"
FROM "03.Hobbies/Writing/Confluence"
WHERE type = "scene" OR type = "character" OR type = "location"
SORT file.mtime DESC
LIMIT 15
```

---

## 🔍 Quick Links

### Core Reference

- [[Confluence_Character_Bible]] - Character profiles and arcs
- [[Confluence_Story_Continuity_Tracker]] - Plot threads and timeline
- [[Confluence_Writing_Workflow_Guide]] - Daily workflow

### By Tome

- [[Tome 1 Hub]] | [[Tome 2 Hub]] | [[Tome 3 Hub]]
- [[Tome 4 Hub]] | [[Tome 5 Hub]] | [[Tome 6 Hub]]

### Character Quick Access

```dataview
LIST
FROM "03.Hobbies/Writing/Confluence/Characters"
WHERE type = "character"
SORT file.name
```

---

## 📋 Weekly Checklist

- [ ] Review continuity tracker for unresolved threads
- [ ] Check timeline coherence across week's scenes
- [ ] Verify character voice consistency
- [ ] Update character ages if timeline advanced
- [ ] Check for open loops (#openloops tag)
- [ ] Update word count goals
- [ ] Review POV balance across tomes

---

_Last Dashboard Update: `= date(now)`_

## Additional Specialized Dashboards

### Character-Specific Dashboard

# Character Deep-Dive Dashboard

```dataviewjs
// Set your character name here
const CHARACTER_NAME = "Kyr4n";

const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene" && p.characters_present)
  .where(s => s.characters_present.some(c => {
    let name = c.path ? c.path.split("/").pop().replace(".md", "") : c;
    return name === CHARACTER_NAME;
  }));

dv.header(2, `${CHARACTER_NAME} Appearances`);
dv.paragraph(`**Total Scenes**: ${scenes.length}`);

// POV vs Appears-In
let povScenes = scenes.where(s => s.pov === CHARACTER_NAME).length;
let appearanceScenes = scenes.length - povScenes;

dv.paragraph(`**POV Scenes**: ${povScenes} | **Appears In**: ${appearanceScenes}`);

// Timeline of appearances
dv.header(3, "Chronological Appearances");
let charTable = scenes
  .sort(s => s.story_date, 'asc')
  .array()
  .map(s => [
    `${s.tome}.${String(s.chapter).padStart(2, '0')}`,
    s.story_date || "TBD",
    dv.fileLink(s.file.path, false, s.title),
    s.pov === CHARACTER_NAME ? "POV" : "Appears",
    s.location || "-"
  ]);

dv.table(
  ["Scene", "Date", "Title", "Role", "Location"],
  charTable
);
````

### Timeline Gaps Dashboard

# Timeline Continuity Dashboard

```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene" && p.story_date && p.story_date !== "TBD")
  .sort(p => p.story_date, 'asc');

dv.header(2, "Timeline Gaps Analysis");

let previousDate = null;
let gaps = [];

for (let scene of scenes) {
  if (previousDate) {
    let prev = new Date(previousDate);
    let curr = new Date(scene.story_date);
    let diffDays = Math.floor((curr - prev) / (1000 * 60 * 60 * 24));
    
    if (diffDays > 30) { // Flag gaps longer than 30 days
      gaps.push({
        from: previousDate,
        to: scene.story_date,
        days: diffDays,
        fromScene: `${scene.tome}.${scene.chapter}`,
        years: Math.floor(diffDays / 365)
      });
    }
  }
  previousDate = scene.story_date;
}

if (gaps.length > 0) {
  dv.header(3, "⏰ Significant Time Jumps (30+ days)");
  let gapTable = gaps.map(g => [
    g.from,
    g.to,
    `${g.days} days (${g.years} years)`,
    g.fromScene
  ]);
  
  dv.table(
    ["From", "To", "Gap", "Scene"],
    gapTable
  );
} else {
  dv.paragraph("✅ No significant timeline gaps detected");
}
````

### Plot Thread Status Board

# Plot Thread Status Board

## 🔴 Unresolved Major Threads
```dataview
TABLE WITHOUT ID
  file.link as "Thread",
  introduced_tome as "Introduced (Tome)",
  expected_resolution as "Expected Resolution"
FROM "03.Hobbies/Writing/Confluence/Wiki/Plot-Threads"
WHERE status = "active" AND importance = "major"
SORT introduced_tome ASC
````

## 🟡 Subplots in Progress

```dataview
TABLE WITHOUT ID
  file.link as "Thread",
  related_characters as "Characters",
  last_appearance_tome as "Last Seen"
FROM "03.Hobbies/Writing/Confluence/Wiki/Plot-Threads"
WHERE status = "active" AND importance = "subplot"
```

## 🟢 Resolved Threads

```dataview
TABLE WITHOUT ID
  file.link as "Thread",
  introduced_tome as "Intro",
  resolved_tome as "Resolved"
FROM "03.Hobbies/Writing/Confluence/Wiki/Plot-Threads"
WHERE status = "resolved"
SORT resolved_tome DESC
```


These dashboards will:

1. **Auto-update** as you write - no manual maintenance needed
2. **Visualize progress** across all six tomes
3. **Track character appearances** to ensure no one disappears too long
4. **Monitor timeline** for the century-spanning narrative
5. **Flag continuity issues** before they become problems
6. **Show POV distribution** to maintain balance
7. **Track locations** to ensure world-building consistency
8. **Calculate word count progress** against goals

The modular design lets you place these on separate dashboard pages or combine them into one master dashboard. The DataviewJS queries handle complex calculations your project needs for managing an epic-scale narrative.