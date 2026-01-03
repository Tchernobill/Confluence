```dataviewjs
const eras = [1,2,3,4,5,6];
const basePath = "06_Scenes";

function fileCell(folder, name) {
    const path = `${folder}/${name}.md`;
    const file = dv.page(path);
    if (file) {
        return `✅ [[${path}|${name}]]`;
    } else {
        return `☐ [[${path}|${name}]]`;
    }
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

    dv.table(
        ["Date Time", "Title", "Summary", "Draft", "Revised", "Final", "Published"],
        pages.map(p => {
            const folder = p.file.folder;

            const titleWithTooltip =
                `<span title="${p.description ?? ""}">${p.title}</span>`;

            return [
                p.story_date ?? "",
                titleWithTooltip,
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
