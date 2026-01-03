#!/usr/bin/env python3
"""
Confluence Frontmatter Batch Updater
Processes all Summary.md and Draft.md files in Era 1 folder

Usage:
    python batch_update_frontmatter.py

This script will:
1. Find all Summary.md and Draft.md files in Era 1
2. Standardize their frontmatter
3. Update files in place
4. Generate a detailed report

IMPORTANT: Make sure you have a backup before running!
"""

import os
import re
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Installing PyYAML...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'pyyaml'])
    import yaml

# Configuration
BASE_PATH = os.getcwd()

REQUIRED_FIELDS = [
    'title', 'type', 'status', 'scene_type', 'emotional_tone', 'story_date',
    'pov', 'location', 'characters_present', 'narrative_arc',
    'relationship_developments', 'plot_threads', 'character_arcs',
    'thematic_elements', 'prev_scene', 'next_scene', 'callbacks_to',
    'setups_for', 'content_warnings', 'contains_spoilers_for',
    'requires_knowledge_of', 'words_count', 'estimated_reading_time',
    'version', 'created', 'last_updated', 'revision_notes',
]

PROPERTY_MAPPINGS = {
    'scene_style_tone': 'emotional_tone',
    'scenes_before': 'prev_scene',
    'scenes_after': 'next_scene',
    'primary_themes': 'thematic_elements',
}

COMMENT_OUT = ['story_time', 'description', 'tags', 'era', 'publication_position', 
               'symbolic_elements', 'pass', 'emotional_load_target', 'load_type',
               'system_commands', 'draft_pass', 'source_scene']


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    if not match:
        return None, content
    try:
        fm = yaml.safe_load(match.group(1))
        return fm if fm else {}, match.group(2)
    except Exception as e:
        print(f"  ⚠ YAML parsing error: {e}")
        return None, content


def extract_metadata(filepath):
    """Extract date, time, title from filepath"""
    pattern = r'(\d{4}-\d{2}-\d{2})\s+(\d{4})\s+-\s+(.+?)(?:\s+-\s+Draft\s+\d+)?(?:[/\\]Summary\.md|[/\\]Draft\.md|\.md)?$'
    match = re.search(pattern, filepath)
    metadata = {}
    if match:
        metadata['story_date'] = f"{match.group(1)}T{match.group(2)[:2]}:{match.group(2)[2:]}:00"
        metadata['title'] = match.group(3)
        metadata['created'] = match.group(1)
    return metadata


def standardize(existing, filepath):
    """Standardize frontmatter"""
    std, extra = {}, {}
    file_meta = extract_metadata(filepath)
    
    if not existing:
        existing = {}
    
    # Apply mappings
    mapped = {}
    for old, val in existing.items():
        if old in PROPERTY_MAPPINGS:
            mapped[PROPERTY_MAPPINGS[old]] = val
        elif old in COMMENT_OUT:
            extra[old] = val
        else:
            mapped[old] = val
    
    # Build standardized
    for field in REQUIRED_FIELDS:
        if field in mapped and mapped[field] not in [None, '']:
            std[field] = mapped[field]
        elif field in file_meta:
            std[field] = file_meta[field]
        else:
            if field in ['scene_type', 'emotional_tone', 'characters_present', 
                        'relationship_developments', 'plot_threads', 'character_arcs',
                        'thematic_elements', 'callbacks_to', 'setups_for',
                        'content_warnings', 'contains_spoilers_for', 'requires_knowledge_of']:
                std[field] = []
            elif field == 'words_count':
                std[field] = 0
            elif field == 'estimated_reading_time':
                std[field] = '0 minutes'
            elif field == 'version':
                std[field] = '0.1'
            elif field == 'narrative_arc':
                std[field] = 'arc_identifier'
            else:
                std[field] = ''
    
    # Preserve important values
    for key in ['type', 'status', 'version', 'narrative_arc', 'words_count']:
        if key in existing and existing[key] not in [None, '']:
            std[key] = existing[key]
    
    if not std.get('created'):
        std['created'] = datetime.now().strftime('%Y-%m-%d')
    std['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    if not std.get('revision_notes'):
        std['revision_notes'] = 'Frontmatter standardized'
    
    for field, val in mapped.items():
        if field not in REQUIRED_FIELDS and field not in extra:
            extra[field] = val
    
    return std, extra


def format_yaml(std, extra):
    """Format YAML with commented extra fields"""
    lines = []
    yaml_str = yaml.dump(std, default_flow_style=False, sort_keys=False, allow_unicode=True)
    lines.append(yaml_str.rstrip())
    
    if extra:
        lines.append('\n# Additional properties (commented out):')
        for key, val in extra.items():
            val_str = yaml.dump({key: val}, default_flow_style=False, allow_unicode=True).rstrip()
            commented = '\n'.join(f'# {line}' for line in val_str.split('\n'))
            lines.append(commented)
    
    return '\n'.join(lines)


def process_file(filepath):
    """Process a single file"""
    result = {
        'filepath': filepath,
        'filename': os.path.basename(filepath),
        'success': False,
        'action': 'none',
        'changes': [],
        'error': None
    }
    
    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract existing frontmatter
        existing_fm, body = extract_frontmatter(content)
        
        if existing_fm is None:
            result['error'] = 'No frontmatter found'
            return result
        
        # Standardize
        std_fm, extra_fm = standardize(existing_fm, filepath)
        
        # Track changes
        if not existing_fm:
            result['action'] = 'created'
            result['changes'].append('Frontmatter created from scratch')
        else:
            result['action'] = 'updated'
            added = [f for f in REQUIRED_FIELDS if f not in existing_fm]
            if added:
                result['changes'].append(f'Added {len(added)} missing fields')
            if extra_fm:
                result['changes'].append(f'Moved {len(extra_fm)} extra fields to comments')
        
        # Format YAML
        yaml_content = format_yaml(std_fm, extra_fm)
        
        # Write back
        new_content = f"---\n{yaml_content}\n---\n{body}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        result['success'] = True
        
    except Exception as e:
        result['error'] = str(e)
    
    return result


def find_all_files():
    """Find all Summary.md and Draft.md files"""
    files = []
    
    # Walk through all directories
    for root, dirs, filenames in os.walk(BASE_PATH):
        for filename in filenames:
            if filename in ['Summary.md', 'Draft.md'] or filename.endswith(' - Draft 1.md'):
                files.append(os.path.join(root, filename))
    
    return sorted(files)


def main():
    """Main processing function"""
    print("=" * 80)
    print("CONFLUENCE FRONTMATTER BATCH UPDATE")
    print("=" * 80)
    print(f"Base path: {BASE_PATH}")
    print()
    
    # Find all files
    print("Finding files...")
    files = find_all_files()
    print(f"Found {len(files)} files to process")
    print()
    
    # Confirm
    response = input("Process all files? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Cancelled.")
        return
    
    print()
    print("Processing files...")
    print()
    
    # Process all files
    results = []
    for i, filepath in enumerate(files, 1):
        filename = os.path.basename(filepath)
        parent = os.path.basename(os.path.dirname(filepath))
        display_name = f"{parent}/{filename}" if filename in ['Summary.md', 'Draft.md'] else filename
        
        print(f"[{i}/{len(files)}] {display_name}...", end=' ')
        
        result = process_file(filepath)
        results.append(result)
        
        if result['success']:
            print(f"✓ {result['action']}")
            if result['changes']:
                for change in result['changes']:
                    print(f"    • {change}")
        else:
            print(f"✗ FAILED")
            if result['error']:
                print(f"    ⚠ {result['error']}")
    
    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    created = [r for r in results if r['action'] == 'created']
    updated = [r for r in results if r['action'] == 'updated']
    
    print(f"Successful: {len(successful)}/{len(results)}")
    print(f"  - Created: {len(created)}")
    print(f"  - Updated: {len(updated)}")
    print(f"Failed: {len(failed)}")
    
    if failed:
        print()
        print("FAILED FILES:")
        for r in failed:
            print(f"  • {r['filename']}: {r['error']}")
    
    print()
    print("✓ Batch update complete!")
    print()
    
    # Write report
    report_path = os.path.join(BASE_PATH, '_FRONTMATTER_UPDATE_REPORT.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("CONFLUENCE FRONTMATTER BATCH UPDATE REPORT\n")
        f.write("=" * 80 + "\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total files: {len(results)}\n")
        f.write(f"Successful: {len(successful)}\n")
        f.write(f"Failed: {len(failed)}\n")
        f.write("\n")
        f.write("TRANSFORMATIONS APPLIED:\n")
        f.write("  • scene_style_tone → emotional_tone\n")
        f.write("  • scenes_before → prev_scene\n")
        f.write("  • scenes_after → next_scene\n")
        f.write("  • primary_themes → thematic_elements\n")
        f.write("  • Moved extra properties to comments\n")
        f.write("  • Added all 27 required fields\n")
        f.write("\n")
        
        if failed:
            f.write("FAILED FILES:\n")
            for r in failed:
                f.write(f"  • {r['filepath']}: {r['error']}\n")
    
    print(f"Report saved to: {report_path}")


if __name__ == '__main__':
    main()
