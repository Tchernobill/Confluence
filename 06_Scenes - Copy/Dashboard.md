---
cssclass: full-width
---
```dataviewjs
const eras = [1,2,3,4,5,6];
const basePath = "06_Scenes";
const stages = ["Summary", "Draft", "Revised", "Final", "Published"];

function fileExists(path) {
    return dv.page(path) !== undefined;
}

const stageIcons = {
    Summary: "🧾",
    Draft: "✏️",
    Revised: "🔁",
    Final: "🏁",
    Published: "📤"
};

function formatDate(dt) {
    if (!dt) return "";
    return dt.toFormat("dd-MMM-yyyy HH:mm");
}

function fileCell(folder, stage) {
    const path = `${folder}/${stage}.md`;
    const icon = stageIcons[stage] ?? "📄";
    return dv.page(path)
        ? `✅ [[${path}|${icon}]]`
        : `☐ [[${path}|${icon}]]`;
}

function sceneStatus(folder) {
    if (fileExists(`${folder}/Published.md`)) return "Published";
    if (fileExists(`${folder}/Final.md`)) return "Final";
    if (fileExists(`${folder}/Revised.md`)) return "Revised";
    if (fileExists(`${folder}/Draft.md`)) return "Draft";
    return "Summary";
}

function sceneProgress(folder) {
    let count = 0;
    for (const stage of stages) {
        if (fileExists(`${folder}/${stage}.md`)) count++;
    }
    return Math.round((count / stages.length) * 100);
}

function progressBar(percent) {
    return `
<div style="width:100%; background:#333; border-radius:4px;">
  <div style="width:${percent}%; background:#4caf50; padding:2px 0; border-radius:4px; text-align:center; color:black; font-size:0.8em;">
    ${percent}%
  </div>
</div>`;
}

for (const era of eras) {
    dv.header(2, `Era ${era}`);

    const pages = dv.pages(`"${basePath}/Era ${era}"`)
        .where(p => p.type === "scene_summary")
        .sort(p => p.story_date, "asc");

    if (pages.length === 0) {
        dv.paragraph("_No scenes found._");
        continue;
    }

    // ERA PROGRESS
    let totalProgress = 0;
    pages.forEach(p => totalProgress += sceneProgress(p.file.folder));
    const eraProgress = Math.round(totalProgress / pages.length);

    dv.paragraph("**Era Progress**");
    dv.el("div", progressBar(eraProgress), { cls: "progress-bar" });

    // TABLE
    dv.table(
        ["Date Time", "Title", "POV", "Status", "🧾", "✏️", "🔁", "✅","📤" ],
        pages.map(p => {
            const folder = p.file.folder;
            const titleTooltip =
                `<span title="${p.description ?? ""}">${p.title}</span>`;

            return [
				formatDate(p.story_date),
				titleTooltip,
				p.pov ?? "",
				sceneStatus(folder),
				fileCell(folder, "Summary"),
				fileCell(folder, "Draft"),
				fileCell(folder, "Revised"),
				fileCell(folder, "Final"),
				fileCell(folder, "Published")
			];
        })
    );
}

```
