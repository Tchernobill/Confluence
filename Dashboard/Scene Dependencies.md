```dataviewjs
const scenes = dv.pages('"Scenes"')
  .where(p => !p.stage);

let graph = [];

for (let s of scenes) {
  if (s.previous_scene) {
    graph.push(`"${s.previous_scene}" --> "${s.scene_id}"`);
  }
  if (s.next_scene) {
    graph.push(`"${s.scene_id}" --> "${s.next_scene}"`);
  }
}

dv.paragraph(`
\`\`\`mermaid
graph LR
${graph.join("\n")}
\`\`\`
`);

```

