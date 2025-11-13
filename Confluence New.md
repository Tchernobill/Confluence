## ⚙️ Structure of the Dashboard Note

## 📈 Global Statistics
```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Scenes"')
  .where(p => p.title && p.status);

let totalScenes = scenes.length;
let totalWords = scenes.array().reduce((sum, s) => sum + (Number(s.words_count) || 0), 0);
let completed = scenes.where(s => s.status && s.status.includes("final")).length;
let drafted = scenes.where(s => s.status && s.status.includes("drafted")).length;
let revised = scenes.where(s => s.status && s.status.includes("revised")).length;
let planning = scenes.where(s => s.status && s.status.includes("planning")).length;

dv.paragraph(`**Total Scenes:** ${totalScenes}`);
dv.paragraph(`**Word Count:** ${totalWords.toLocaleString()} words`);
dv.paragraph(`**Completion:** ${completed}/${totalScenes} (${Math.round(completed/totalScenes*100)}%)`);
dv.paragraph(`**Status Breakdown:** 🧠 ${planning} | ✏️ ${drafted} | 🔁 ${revised} | ✅ ${completed}`);
```

---

## 🎬 Scene Index
```dataview
TABLE 
	story_date + " " + story_time AS "Date", 
	title AS "Scene", 
	pov AS "POV", 
	emotional_tone AS "Tone", 
	status AS "Status", 
	words_count AS "Words"
FROM "03.Hobbies/Writing/Confluence/Scenes"
SORT story_date + " " + story_time ASC
```

```dataview
TABLE
  story_date + " " + story_time AS "📅 Date",
  title AS "🎬 Title",
  pov AS "👁️ POV",
  emotional_tone AS "🎭 Tone",
  status AS "📋 Status",
  word_count AS "✍️ Words"
FROM "03.Hobbies/Writing/Confluence/Scenes"
WHERE type = "scene"
SORT story_date + " " + story_time ASC
```
---

## 👥 Character Tracker

```dataviewjs
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Scenes"');
let characters = {};

for (let s of scenes) {
  if (Array.isArray(s.characters_present)) {
    for (let c of s.characters_present) {
      const name = (typeof c === "string")
        ? c.replace(/\[\[|\]\]/g, "")
        : c.path || c.display || String(c);

      if (!characters[name]) characters[name] = { scenes: 0, words: 0, final: 0 };
      characters[name].scenes++;
      characters[name].words += Number(s.words_count) || 0;
      if (s.status && s.status.includes("final")) characters[name].final++;
    }
  }
}

let charTable = Object.entries(characters).map(([name, data]) => [
  `[[${name}]]`,
  data.scenes,
  data.words.toLocaleString(),
  `${data.final}/${data.scenes}`,
  `${Math.round((data.final / data.scenes) * 100)}%`
]);

dv.table(["Character", "Scenes", "Words", "Complete", "Progress"], charTable.sort((a,b)=>b[1]-a[1]));

```

---

## 🌌 Arcs & Threads Overview

```dataviewjs
const arcs = dv.pages('"03.Hobbies/Writing/Confluence/Arcs"')
  .where(p => p.type === "arc");

const grouped = {
  era: arcs.where(a => a.arc_type === "era"),
  character: arcs.where(a => a.arc_type === "character"),
  event: arcs.where(a => a.arc_type === "event")
};

function makeTable(collection) {
  return collection.array().map(a => {
    const scenes = Array.isArray(a.scenes) ? a.scenes.length : 0;
    const pct = a.progress || 0;
    return [
      `[[${a.file.name}]]`,
      a.status,
      scenes,
      `${pct}%`,
      a.theme || ""
    ];
  });
}

dv.header(3, "🌍 Era Arcs");
dv.table(["Arc", "Status", "Scenes", "Progress", "Theme"], makeTable(grouped.era));

dv.header(3, "👤 Character Arcs");
dv.table(["Arc", "Status", "Scenes", "Progress", "Theme"], makeTable(grouped.character));

dv.header(3, "🏙️ Localized Events");
dv.table(["Arc", "Status", "Scenes", "Progress", "Theme"], makeTable(grouped.event));
```

---

## 🕒 Timeline View

```dataview
TABLE story_date + " " + story_time AS "Chronology", title AS "Scene", pov AS "POV", status AS "Status"
FROM "03.Hobbies/Writing/Confluence/Scenes"
SORT story_date + " " + story_time ASC
```

---

## 🧭 Optional Future Ideas

- Integrate **progress bars** using inline HTML + CSS (to visualize arc or scene completion)
- Add a **“Scenes needing revision”** filter table
- Add a **chart** using DataviewJS + Chart.js (e.g. word count by month or by arc)
- Add **interactive toggles** (for filtering by character or arc dynamically)

---
