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

