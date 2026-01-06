#!/usr/bin/env python3
"""Update all batch scripts with correct batch numbers"""

batch_configs = [
    (3, "03", "021-030"),
    (4, "04", "031-040"),
    (5, "05", "041-050"),
    (6, "06", "051-060"),
    (7, "07", "061-070"),
    (8, "08", "071-080"),
    (9, "09", "081-090"),
    (10, "10", "091-100"),
]

for batch_num, batch_str, stick_range in batch_configs:
    filename = f"generate_batch{batch_str}_html.py"
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update docstring
    content = content.replace(
        'Generate HTML files for Batch 01 (Sticks 1-10)',
        f'Generate HTML files for Batch {batch_str} (Sticks {stick_range.split("-")[0]}-{stick_range.split("-")[1]})'
    )
    
    # Update md_file
    content = content.replace(
        "md_file = 'batch_01_sticks_001-010.md'",
        f"md_file = 'batch_{batch_str}_sticks_{stick_range}.md'"
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")

print("\nAll batch scripts updated!")
