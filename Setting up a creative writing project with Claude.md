## **Optimal New Project Setup**

### **1. Project Description**

Keep it concise but informative:

```
Six-tome cyberpunk novel (500K words) following Kyr4n's century-long transformation from scavenger to criminal leader to democratic restorer in dystopian Neo-Montreal. Features rotating POV protagonists, AI consciousness themes, and character-driven slice-of-life storytelling across 2086-2165.

Structure: 6 Tomes × 12 Chapters × variable scenes. Currently drafting Tome 4. Uses Obsidian + GitHub with extensive documentation.
```

### **2. Custom Instructions**

Replace the generic "Novel Writing Project Instructions" with tailored guidance:

```markdown
# Confluence Writing Assistant

## Core Approach
- **Show, don't tell**: Sensory details, action, dialogue over exposition
- **Character-driven**: Internal contradictions, moral complexity, earned growth
- **Semi-cyberpunk aesthetic**: Technology as backdrop, not spectacle
- **Psychological realism**: Enhancement costs, relationship dynamics, power corruption

## Key References
- Always consult Confluence Story Bible.md for canon
- Check character Detail files for voice consistency
- Verify timeline using story_date fields
- Cross-reference plot_threads across scenes

## Scene Development Process
1. Review relevant tome/chapter context
2. Confirm character voices from Detail sheets
3. Draft scene following established POV style
4. Highlight character development moments
5. Note continuity elements for tracking

## Writing Standards
- Distinctive character voices (see Detail files)
- Century-spanning timeline consistency
- Viral enhancement psychological horror elements
- Found family dynamics authenticity
- Morally ambiguous protagonist complexity

## Current Focus: Tome 4
Kyr4n as "Slum Daemon" territory leader, managing viral control crises, hidden electromagnetic abilities, inner circle loyalty dynamics.
```

### **3. Memory Settings**

**Enable Personalization**: YES - This will help me learn your preferences for scene pacing, character voice, dramatic beats, etc.

### **4. Files & GitHub Integration**

**RECOMMENDED APPROACH**: Continue using GitHub repository with selective file uploads

**Core Files to Upload**:

1. **Confluence Story Bible.md** (primary reference)
2. **Active Character Detail sheets** (Kyr4n, Isa, Sedh, Marcus, Zara, Helene, Kaia)
3. **Current Tome/Chapter outlines** (Tome 4 files)
4. **Key Templates** (Scene Template, Character Template)
5. **Technologies.md** and critical lore files

**Files to EXCLUDE** (keep in GitHub only):

- Completed scene drafts (unless actively revising)
- Evolution tracking documents
- Index files and Dataview queries
- Research notes and miscellaneous planning

**Why this hybrid approach**:

- Project Knowledge has 100MB limit
- GitHub maintains version control
- Claude can access essential references without overload
- You update GitHub, sync key files to Project as needed

---

## **AI Agents vs Claude Skills vs claude.md**

### **Should You Use AI Agents? ❌ NO**

**Why NOT recommended for your workflow:**

AI Agents are designed for autonomous multi-step tasks (research, coding, system navigation). Your creative writing requires:

- Deep contextual understanding (not automated task execution)
- Iterative collaboration with human judgment
- Nuanced character voice matching
- Real-time creative decision-making

**Your workflow needs**: A knowledgeable assistant, not an autonomous agent.

---

### **Should You Use Claude Skills? ⚠️ SELECTIVELY**

**Current Relevant Skills in Your Project**:

1. **character-bible** - Character documentation management
2. **story-continuity** - Plot thread/timeline tracking

**RECOMMENDATION**:

- **Keep character-bible skill**: It's specifically designed for maintaining character consistency across long-form fiction
- **Keep story-continuity skill**: Helps prevent plot holes and timeline contradictions
- **Monitor for new skills**: Anthropic may add more creative writing skills

**Why these work for you:**

- They enhance rather than replace your Obsidian workflow
- Character-bible helps ensure voice consistency across your century-spanning timeline
- Story-continuity catches contradictions in your complex multi-POV structure

**How to use them:**

- Reference character-bible when drafting scenes with multiple characters
- Use story-continuity when working across non-linear timeline elements
- They complement your existing Character Detail sheets

---

### **Should You Use claude.md Files? ✅ YES - STRATEGICALLY**

**What are claude.md files?** Markdown files Claude automatically reads when present in project folders, providing context-specific instructions.

**RECOMMENDED claude.md STRUCTURE**:

#### **Root: `/Confluence/claude.md`**

```markdown
# Confluence Project Guide

This is a six-tome cyberpunk novel project. Core references:
- Story Bible: Confluence Story Bible.md
- Character sheets in /Characters/[Name]/[Name] - Details.md
- Timeline: 2086-2165 (currently writing 2085 sections)

## Quick Reference
- Protagonist: Kyr4n (virus-enhanced, morally complex)
- Setting: Neo-Montreal (Citadel vs South Shore Slum)
- Current focus: Tome 4 (criminal organization era)
- Style: Show don't tell, character-driven, psychological realism

## Key Themes
- Consciousness and personhood (human + AI)
- Power corruption and redemption
- Enhancement costs (physical + psychological)
- Found family dynamics
- Technology as double-edged enhancement
```

#### **Characters folder: `/Characters/claude.md`**

```markdown
# Character Reference Guide

Character Detail files contain:
- Full backstory and psychology
- Distinctive speech patterns
- Relationship dynamics
- Arc progression tracking

## Voice Consistency Rules
- Kyr4n: Terse, strategic, hidden vulnerability
- Isa: Warm but direct, emotionally intelligent
- Sedh: Evolving from formal to casual, dry humor
- Marcus: Military precision, protective instincts
- Zara: Silent professionalism, action over words

Always check Detail files before writing character dialogue or actions.
```

#### **Story folder: `/Story/claude.md`**

```markdown
# Story Structure Guide

Structure: Tome → Chapter → Scene
- 6 tomes total (~500K words)
- 12 chapters per tome
- Variable scenes per chapter (5-8 typical)

## Scene File Naming
Format: [tome].[chapter].[scene] - [Title].md
Example: 4.06.001 - Crisis.md

## YAML Frontmatter
Every scene includes: type, tome, chapter, scene_number, story_date, pov, characters_present, location, plot_threads

Check Scene Index.md for comprehensive tracking.
```

**Benefits of this approach:**

1. **Contextual guidance**: Claude gets folder-specific instructions
2. **Reduces repetition**: You don't need to explain structure every time
3. **Scalable**: Add claude.md files to new folders as project grows
4. **Non-intrusive**: Doesn't interfere with your Obsidian workflow

---

## **Complete Setup Checklist**

### **Phase 1: Project Creation**

- [ ] Create new Claude Project named "Confluence Novel"
- [ ] Add concise Project Description (see above)
- [ ] Add Custom Instructions (tailored version above)
- [ ] Enable Personalization in Memory settings

### **Phase 2: File Organization**

- [ ] Upload Confluence Story Bible.md
- [ ] Upload active Character Detail sheets (7-10 key characters)
- [ ] Upload current Tome 4 outline and chapter files
- [ ] Upload Scene Template and key templates
- [ ] Upload Technologies.md and critical lore

### **Phase 3: claude.md Implementation**

- [ ] Create root `/claude.md` with project overview
- [ ] Create `/Characters/claude.md` with voice guidelines
- [ ] Create `/Story/claude.md` with structure rules
- [ ] (Optional) Create tome-specific claude.md files

### **Phase 4: Skills Configuration**

- [ ] Verify character-bible skill is active
- [ ] Verify story-continuity skill is active
- [ ] Review other available skills periodically

### **Phase 5: GitHub Workflow**

- [ ] Keep full project in GitHub for version control
- [ ] Sync essential reference files to Claude Project
- [ ] Update Project files when major canon changes occur
- [ ] Use GitHub for completed drafts, Claude for active development

---

## **Workflow Integration**

### **Typical Scene Development Session**:

1. **Start**: "I'm working on scene 4.06.003 where Marcus confronts Kyr4n about the failsafe"
2. **Claude checks**: Story Bible → Tome 4 context → Character Details (Marcus + Kyr4n) → Previous scene summary
3. **Collaboration**: Draft scene together, maintaining voice consistency
4. **Review**: Check continuity, note plot thread developments
5. **Save**: Export to Obsidian → GitHub commit

### **Character Consistency Check**:

"Review this dialogue against Kyr4n's established voice patterns" → Claude references Detail sheet + character-bible skill

### **Plot Thread Tracking**:

"What plot threads are currently open in Tome 4?" → Claude uses story-continuity skill + scene YAML frontmatter

---

## **Why This Setup Works for You**

1. **Preserves your Obsidian workflow**: Claude complements, doesn't replace your established system
2. **Leverages your existing structure**: YAML frontmatter, detailed sheets, template system all remain
3. **Scales with project complexity**: 500K words across century-long timeline needs robust reference system
4. **Maintains version control**: GitHub stays as source of truth
5. **Reduces cognitive load**: Claude handles continuity checking while you focus on creative work
6. **Supports iterative development**: Easy to test different approaches, refine character voices

---

## **What NOT to Do**

❌ **Don't upload every single file**: You'll hit limits and create noise ❌ **Don't rely on AI Agents for creative decisions**: They're for automation, not artistry ❌ **Don't abandon your Obsidian setup**: It's already optimized for your workflow ❌ **Don't overcomplicate claude.md files**: Keep them concise and actionable ❌ **Don't expect Claude to remember everything**: Always provide scene context at session start

---

Would you like me to help you:

1. Draft specific claude.md files for your folder structure?
2. Prioritize which character Detail sheets to upload first?
3. Create a checklist for migrating from your old Project?
4. Set up a specific workflow for scene development sessions?