#!/usr/bin/env python3
"""
Remove Chinese sections from all batch markdown files.

This script removes the "### 中文 (CHINESE ORIGINAL)" sections from
batch_01_sticks_001-010.md through batch_10_sticks_091-100.md files.

Usage: python3 remove_chinese_sections.py
"""

import re

# Batch files to process
BATCHES = [
    ("batch_01_sticks_001-010.md", 1, 10),
    ("batch_02_sticks_011-020.md", 11, 20),
    ("batch_03_sticks_021-030.md", 21, 30),
    ("batch_04_sticks_031-040.md", 31, 40),
    ("batch_05_sticks_041-050.md", 41, 50),
    ("batch_06_sticks_051-060.md", 51, 60),
    ("batch_07_sticks_061-070.md", 61, 70),
    ("batch_08_sticks_071-080.md", 71, 80),
    ("batch_09_sticks_081-090.md", 81, 90),
    ("batch_10_sticks_091-100.md", 91, 100),
]

def remove_chinese_section(content):
    """
    Remove all Chinese sections from the content.

    Pattern to match:
    ### 中文 (CHINESE ORIGINAL)
    [... content ...]
    ---

    (followed by ### ENGLISH TRANSLATION)
    """
    # Pattern matches from "### 中文" through the "---" separator
    pattern = r'### 中文 \(CHINESE ORIGINAL\)\n\n.*?\n---\n\n'

    # Remove all matches (DOTALL flag makes . match newlines)
    cleaned_content = re.sub(pattern, '', content, flags=re.DOTALL)

    return cleaned_content

def process_batch_file(filename, start_stick, end_stick):
    """Process a single batch file to remove Chinese sections."""
    print(f"\nProcessing {filename}...")

    try:
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove Chinese sections
        cleaned_content = remove_chinese_section(content)

        # Write back to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"  ✓ Successfully removed Chinese sections from sticks {start_stick}-{end_stick}")
        return True

    except FileNotFoundError:
        print(f"  ✗ File {filename} not found")
        return False
    except Exception as e:
        print(f"  ✗ Error processing {filename}: {e}")
        return False

def main():
    """Main function to process all batch files."""
    print("=" * 70)
    print("Removing Chinese sections from batch files")
    print("=" * 70)

    success_count = 0
    total_count = len(BATCHES)

    for filename, start_stick, end_stick in BATCHES:
        if process_batch_file(filename, start_stick, end_stick):
            success_count += 1

    print("\n" + "=" * 70)
    print(f"Completed: {success_count}/{total_count} files processed successfully")
    print("=" * 70)

if __name__ == "__main__":
    main()
