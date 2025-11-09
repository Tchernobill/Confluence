## First prompt
I need to migrate an existing scene from my old two-file system into the new 
date-based single-file system.

📁 SOURCE FILES:
1. Summary file: '\Confluence\Story\Tome 1\1.01.001 - Summary.md'
2. Text file: '\Confluence\Story\Tome 1\1.01.001 - Waking-up.md'

📋 TEMPLATE:
'\Confluence\Scenes\2108-00-00_12-00 - scene title.md'

🎯 TASK:
Create a new merged scene file following these steps:

1. EXTRACT INFORMATION FROM BOTH FILES:
   - All YAML frontmatter from both files
   - Scene Information section from summary file
   - The Events section from summary file
   - Details to observe section from summary file
   - The actual prose/draft text from text file
   - Any other relevant sections

2. DETERMINE NEW FILENAME:
   - Format: YYYY-MM-DD_HH-MM_Scene_Title.md
   - Use story_date and time from the YAML
   - Create descriptive title from the scene content
   - Example: 2108-05-01_06-30_Morning_Awakening.md

3. POPULATE THE NEW TEMPLATE:
   - Fill in YAML frontmatter using comprehensive template structure
   - Map old fields to new fields (see mapping below)
   - Add new required fields with placeholder values where information is missing
   - Preserve all existing scene information
   - Include the draft text in the "Draft Text" section

4. HANDLE MISSING INFORMATION:
   - If information doesn't exist in old files, use: [TBD] or leave blank
   - Mark sections that need completion: [TO BE COMPLETED]
   - Preserve any existing notes or comments

📊 FIELD MAPPING (Old → New):
- tome → publication_position (convert: 1.01.001)
- chapter → publication_position
- scene_number → publication_position
- kyr4n_age → Add to scene context notes
- time → story_time (format as HH:MM)
- time_of_day → time_of_day (keep same)
- Add new fields: narrative_arc, scene_type, emotional_tone, etc.

✅ REQUIREMENTS:
- Preserve ALL existing content from both files
- Use proper wiki-link format: [[Link]]
- Maintain chronological accuracy (story_date/time)
- Include both planning content AND draft text
- Keep original prose untouched
- Add contextual notes about what's missing

📝 OUTPUT:
Provide the complete new file content ready to paste into the new location.
Include the recommended filename at the top.

## Follow-up prompt

Using the same process as before, convert these files:
- Summary: '\Confluence\Story\Tome 1\[X.XX.XXX] - Summary.md'
- Text: '\Confluence\Story\Tome 1\[X.XX.XXX] - [Scene Name].md'

Follow the same template structure and field mapping.
New filename should use story_date and time from YAML.