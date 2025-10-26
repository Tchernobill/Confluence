---
cssclasses:
  - full-width
---
```chronos
> DEFAULTVIEW 2086|2170
> 
# Characters

@ [2078~2170] {Kyr4n}

- [2078-08-28] {Kyr4n} Birth (0)
- [2093-07-03] {Kyr4n} Mother dies (15)

@ [2093~2099] #cyan {Kyr4n} Scavenger | From isolation to first connections - 6 years
# Kyr4n is 17
- [2093-07-13] {Kyr4n} Live in Utility Room (15)
- [2095-04-16] {Kyr4n} Find a damaged droid head while scavenging (17)  
- [2095-05-22] {Kyr4n} Meets Isa (17)
  
@ [2099~2100] #yellow {Kyr4n} Infected | Viral transformation and relationship destruction - 2 years

- [2101-11-02] {Kyr4n} TMP-7734 Virus Infection ()
- [2101-12-10] {Kyr4n} Isa Leaves

@ [2115~2125] #red {Kyr4n} Criminal | Embracing power through violence and control

@ [2127~2140] #orange {Kyr4n} Leader | Building empire and losing humanity

- [2140] {Kyr4n} Riley Death

@ [2141~2155] #purple {Kyr4n} Protector | Extreme methods against systems, growing isolation

@ [2156~2165] #green {Kyr4n} Gardener | Redemption and democratic transition
  
@ [2089~2170] {Isa}
- [2089]  #cyan {Isa} Birth
- [2101]  #cyan {Isa} First sale
- [2102]  #cyan {Isa} Live in Stack 4
- [2103]  #cyan {Isa} Meets Kyr4n
- [2115]  #cyan {Isa} Leaves Kyr4n

@ [2089~2170] {Sedh}
- [2103]  #orange {Sedh} Birth
- [2103]  #orange {Sedh} First diagnostic
- [2104]  #orange {Sedh} Sentience
- [2105]  #orange {Sedh} Live in Phoenix Revovery
- [2119]  #orange {Sedh} Leaves Kyr4n
  
@ [2089~2170] {Riley}
- [2089]  #green {Riley} Birth
- [2101]  #green {Riley} First sale
- [2102]  #green {Riley} Live in Stack 4
- [2103]  #green {Riley} Meets Kyr4n
- [2119]  #green {Riley} Leaves Kyr4n


# Events
= [2119-05-12] Fall of The Grip
= [2123-08-28] Operation StoneBone
 
```


```dataviewjs
// Query scenes from the correct folder path
const scenes = dv.pages('"03.Hobbies/Writing/Confluence/Story"')
    .where(p => p.type === "scene" && p.story_date)
    .sort(p => p.story_date, 'asc');

// POV color mapping
const povColors = {
    "Kyr4n": "#red",
    "Arc Protagonist 1": "#blue",
    "Arc Protagonist 2": "#green",
    "Arc Protagonist 3": "#yellow",
    "Zara": "#purple",
    "Marcus": "#orange",
    "Isa": "#pink"
};

// Helper function to format date from datetime object
function formatDate(dateObj) {
    if (!dateObj) return "";
    // Handle string dates
    if (typeof dateObj === 'string') {
        return dateObj.split('T')[0];
    }
    // Handle Luxon DateTime objects (what Dataview uses)
    if (dateObj.toFormat) {
        return dateObj.toFormat('yyyy-MM-dd');
    }
    // Handle JavaScript Date objects
    if (dateObj instanceof Date) {
        return dateObj.toISOString().split('T')[0];
    }
    // Fallback - try to convert to string and extract date
    const str = dateObj.toString();
    if (str.includes('T')) {
        return str.split('T')[0];
    }
    return str;
}

// Build events
let tomeGroups = {};
let periodRanges = {};

for (let scene of scenes) {
    const tome = scene.tome || 1;
    if (!tomeGroups[tome]) {
        tomeGroups[tome] = [];
    }
    
    const startDate = formatDate(scene.story_date);
    const endDate = scene.story_date_end ? formatDate(scene.story_date_end) : null;
    const pov = scene.pov || "Unknown";
    const color = povColors[pov] || "#gray";
    const age = scene.kyr4n_age ? `[Age ${scene.kyr4n_age}]` : "";
    const period = scene.timeline_period || "";
    const title = scene.title || scene.file.name;
    
    // Track period ranges for background shading
    if (period && !periodRanges[period]) {
        periodRanges[period] = { start: startDate, end: startDate };
    } else if (period) {
        if (startDate < periodRanges[period].start) periodRanges[period].start = startDate;
        if (startDate > periodRanges[period].end) periodRanges[period].end = startDate;
    }
    
    // Format event
    let eventLine;
    if (endDate && endDate !== startDate) {
        eventLine = `@ [${startDate}~${endDate}] ${color} ${title} | POV: ${pov} ${age} | [[${scene.file.path}]]`;
    } else {
        eventLine = `- [${startDate}] ${color} ${title} | POV: ${pov} ${age} | [[${scene.file.path}]]`;
    }
    
    tomeGroups[tome].push(eventLine);
}

// Build chronos block using template literal with escaped backticks
let chronosBlock = `\`\`\`chronos
> DEFAULTVIEW 2080|2170\n\n
`;

// Add period backgrounds if any exist
if (Object.keys(periodRanges).length > 0) {
    chronosBlock += "# Story Periods\n";
    const periodColors = ["#lightblue", "#lightgreen", "#lightyellow", "#lightpink", "#lightgray"];
    let colorIndex = 0;
    for (let period of Object.keys(periodRanges)) {
        const range = periodRanges[period];
        chronosBlock += `@ [${range.start}~${range.end}] ${periodColors[colorIndex % periodColors.length]} ${period}\n`;
        colorIndex++;
    }
    chronosBlock += "\n";
}

// Add tome sections with scenes
for (let tome of Object.keys(tomeGroups).sort((a,b) => parseInt(a) - parseInt(b))) {
    chronosBlock += `# Tome ${tome} Scenes\n`;
    chronosBlock += tomeGroups[tome].join("\n") + "\n\n";
}

chronosBlock += `\`\`\``;

dv.paragraph(chronosBlock);
```


