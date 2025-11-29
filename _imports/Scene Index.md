
```dataviewjs
let allPages = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
  .where(p => p.type === "scene" || p.type === "summary");

// Group by tome, chapter, scene_number
let grouped = {};
for (let p of allPages) {
  let key = `${p.tome}-${p.chapter}-${p.scene_number}`;
  if (!grouped[key]) {
    grouped[key] = { scene: null, summary: null, tome: p.tome, chapter: p.chapter, scene_number: p.scene_number };
  }
  if (p.type === "scene") {
    grouped[key].scene = p;
  } else if (p.type === "summary") {
    grouped[key].summary = p;
  }
}

// Convert to array and sort numerically
let items = Object.values(grouped).sort((a, b) => {
  if (a.tome !== b.tome) return Number(a.tome) - Number(b.tome);
  if (a.chapter !== b.chapter) return Number(a.chapter) - Number(b.chapter);
  return Number(a.scene_number) - Number(b.scene_number);
});

// Calculate chapter word counts
let chapterWords = {};
for (let item of items) {
  let chapterKey = `${item.tome}-${item.chapter}`;
  if (!chapterWords[chapterKey]) {
    chapterWords[chapterKey] = 0;
  }
  let words = item.scene?.words_count || 0;
  chapterWords[chapterKey] += Number(words) || 0;
}

let lastTome = null;
let lastChapter = null;
const BUDGET = 8000;

let rows = items.map(item => {
  let p = item.scene || item.summary; // Use scene data, fallback to summary
  
  // Format as X.XX.XXX
  let sceneId = `${p.tome}.${String(p.chapter).padStart(2, '0')}.${String(p.scene_number).padStart(3, '0')}`;
  
  // Handle date with fallback for non-date values like "TBD"
  let date = "";
  if (p.story_date) {
    try {
      date = dv.date(p.story_date).toFormat("yyyy-MM-dd");
    } catch {
      date = p.story_date;
    }
  }
  
  // Title - only if scene file exists
  let titleLink = "";
  if (item.scene) {
    let titleText = Array.isArray(item.scene.title) ? item.scene.title[0] : item.scene.title;
    let tooltip = item.scene.description || item.scene.summary || "";
    titleLink = tooltip 
      ? dv.el("a", titleText, {attr: {href: item.scene.file.path, title: tooltip}, cls: "internal-link"})
      : dv.fileLink(item.scene.file.path, false, titleText);
  }
  
  // Summary - link to summary file if it exists
  let summaryLink = "";
  if (item.summary) {
    summaryLink = dv.fileLink(item.summary.file.path, false, "summary");
  }
  
  // Get POV
  let pov = p.pov || "";
  
  let chars = p.characters_present
    ?.map(c => dv.fileLink(c).display || c.path.split("/").pop().replace(".md", ""))
    .join(", ") || "";
  
  // Get word count (from scene file if it exists, otherwise from summary)
  let words = item.scene?.words_count || item.summary?.words_count || "";
  
  // Chapter word count - only show on first scene of chapter
  let chapterWordCount = "";
  if (p.tome !== lastTome || p.chapter !== lastChapter) {
    let chapterKey = `${p.tome}-${p.chapter}`;
    let total = chapterWords[chapterKey];
    chapterWordCount = `${total}`;
  }
  
  lastTome = p.tome;
  lastChapter = p.chapter;
  
  return [sceneId, date, titleLink, summaryLink, pov, chars, words, chapterWordCount];
});

dv.table(["Scene", "Date", "Title", "Summary", "POV", "Characters", "Words", "Total"], rows);

```
