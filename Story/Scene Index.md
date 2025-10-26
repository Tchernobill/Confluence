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

// Convert to array and sort
let items = Object.values(grouped).sort((a, b) => {
  if (a.tome !== b.tome) return a.tome - b.tome;
  if (a.chapter !== b.chapter) return String(a.chapter).localeCompare(String(b.chapter));
  return String(a.scene_number).localeCompare(String(b.scene_number));
});

let lastTome = null;
let lastChapter = null;

let rows = items.map(item => {
  let p = item.scene || item.summary; // Use scene data, fallback to summary
  
  let tome = (p.tome !== lastTome) ? p.tome : "";
  let chapter = (p.tome !== lastTome || p.chapter !== lastChapter) ? 
    String(p.chapter).padStart(2, '0') : "";
  
  lastTome = p.tome;
  lastChapter = p.chapter;
  
  let scene = String(p.scene_number).padStart(3, '0');
  
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
  
  return [tome, chapter, scene, date, titleLink, summaryLink, pov, chars];
});

dv.table(["Tome", "Chapter", "Scene", "Date", "Title", "Summary", "POV", "Characters"], rows);
```

