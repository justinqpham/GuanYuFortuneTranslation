#!/usr/bin/env python3
"""
Generate HTML files for Batch 09 (Sticks 081-090)
"""

import os
import re

def parse_stick_data(md_file_path):
    """Parse markdown file and extract data for each stick"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by stick markers
    sticks = re.split(r'=+\nSTICK #(\d+)\n=+', content)

    parsed_sticks = []
    for i in range(1, len(sticks), 2):
        stick_num = int(sticks[i])
        stick_content = sticks[i + 1]

        # Extract English section
        en_match = re.search(r'### ENGLISH TRANSLATION\n\n(.*?)\n\n---\n\n### VIETNAMESE TRANSLATION', stick_content, re.DOTALL)
        if not en_match:
            continue
        en_section = en_match.group(1)

        # Extract Vietnamese section
        vn_match = re.search(r'### VIETNAMESE TRANSLATION\n\n(.*?)(?:\n\n---|$)', stick_content, re.DOTALL)
        if not vn_match:
            continue
        vn_section = vn_match.group(1)

        # Parse English
        en_rating_match = re.match(r'([^\(]+)\s*\(([^\)]+)\)', en_section)
        en_rating = en_rating_match.group(1).strip() if en_rating_match else ""
        en_subtitle = en_rating_match.group(2).strip() if en_rating_match else ""

        en_sacred = re.search(r'\*\*Sacred Meaning:\*\*\n((- .+\n?)+)', en_section, re.MULTILINE)
        en_sacred_meanings = en_sacred.group(1).strip() if en_sacred else ""

        en_poem_match = re.search(r'\*\*Fortune Poem:\*\*\n((?:(?!\*\*).+\n?)+)', en_section, re.MULTILINE)
        en_poem = en_poem_match.group(1).strip() if en_poem_match else ""

        en_interp_match = re.search(r'\*\*Interpretation:\*\*\n((?:•[^\n]+\n?)+)', en_section, re.MULTILINE)
        en_interpretation = en_interp_match.group(1) if en_interp_match else ""

        # Parse Vietnamese
        vn_rating_match = re.match(r'([^\(]+)\s*\(([^\)]+)\)', vn_section)
        vn_rating = vn_rating_match.group(1).strip() if vn_rating_match else ""
        vn_subtitle = vn_rating_match.group(2).strip() if vn_rating_match else ""

        vn_sacred = re.search(r'\*\*Sacred Meaning:\*\*\n((- .+\n?)+)', vn_section, re.MULTILINE)
        vn_sacred_meanings = vn_sacred.group(1).strip() if vn_sacred else ""

        vn_poem_match = re.search(r'\*\*Bài thơ quẻ:\*\*\n((?:(?!\*\*).+\n?)+)', vn_section, re.MULTILINE)
        vn_poem = vn_poem_match.group(1).strip() if vn_poem_match else ""

        vn_interp_match = re.search(r'\*\*Ý nghĩa:\*\*\n((?:•[^\n]+\n?)+)', vn_section, re.MULTILINE)
        vn_interpretation = vn_interp_match.group(1) if vn_interp_match else ""

        parsed_sticks.append({
            'num': stick_num,
            'en_rating': en_rating,
            'en_subtitle': en_subtitle,
            'en_sacred_meanings': en_sacred_meanings,
            'en_poem': en_poem,
            'en_interpretation': en_interpretation,
            'vn_rating': vn_rating,
            'vn_subtitle': vn_subtitle,
            'vn_sacred_meanings': vn_sacred_meanings,
            'vn_poem': vn_poem,
            'vn_interpretation': vn_interpretation
        })

    return parsed_sticks

def format_sacred_meanings(text):
    """Convert markdown sacred meanings to HTML list items"""
    if not text:
        return ""
    lines = text.strip().split('\n')
    html_lines = []
    for line in lines:
        # Pattern: "- **Label:** value" where colon is inside the bold markers
        match = re.match(r'- \*\*([^*]+):\*\*\s*(.+)', line)
        if match:
            label = match.group(1)
            value = match.group(2)
            html_lines.append(f'          <li><span class="meaning-label">{label}:</span> {value}</li>')
    return '\n'.join(html_lines)

def format_interpretation(text):
    """Convert markdown bullets to HTML list items"""
    lines = text.strip().split('\n')
    html_lines = []
    for line in lines:
        if line.startswith('•'):
            content = line[1:].strip()
            html_lines.append(f'          <li>{content}</li>')
    return '\n'.join(html_lines)

def generate_html(stick_data, template_path='design_template.html'):
    """Generate HTML for a single stick using external template"""
    # Read the template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Replace placeholders
    html = template.format(
        stick_num=stick_data['num'],
        en_rating=stick_data['en_rating'],
        en_subtitle=stick_data['en_subtitle'],
        en_sacred_meanings=format_sacred_meanings(stick_data['en_sacred_meanings']),
        en_poem=stick_data['en_poem'],
        en_interpretation=format_interpretation(stick_data['en_interpretation']),
        vn_rating=stick_data['vn_rating'],
        vn_subtitle=stick_data['vn_subtitle'],
        vn_sacred_meanings=format_sacred_meanings(stick_data['vn_sacred_meanings']),
        vn_poem=stick_data['vn_poem'],
        vn_interpretation=format_interpretation(stick_data['vn_interpretation'])
    )
    return html

def main():
    # Parse batch file
    md_file = 'translation_batches/batch_09_sticks_081-090.md'
    sticks = parse_stick_data(md_file)

    # Create output directory
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    # Generate HTML files
    for stick in sticks:
        html = generate_html(stick)
        filename = f"{output_dir}/stick_{stick['num']:03d}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {filename}")

    print(f"\nSuccessfully generated {len(sticks)} HTML files!")

if __name__ == '__main__':
    main()
