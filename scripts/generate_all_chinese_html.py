#!/usr/bin/env python3
"""Generate all Chinese HTML files from markdown"""

import re

def parse_chinese_markdown(filepath):
    """Parse the Chinese markdown file and extract all stick data"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by stick sections (## 第...籤)
    sections = re.split(r'\n## (第.+籤.*?)\n', content)[1:]  # Skip intro

    sticks = []
    for i in range(0, len(sections), 2):
        if i + 1 >= len(sections):
            break

        header = sections[i]
        body = sections[i + 1]

        # Extract stick number and rating from header
        # e.g., "第一籤 I 甲甲 大吉" or "第四十籤 XL 上吉" or "第九十三籤 XCIII 癸丙 中吉"
        match = re.match(r'第(.+?)籤\s+([IVXLC]+)\s+(.+)', header)
        if not match:
            continue

        stick_chinese_num = match.group(1)
        stick_roman = match.group(2)
        rating = match.group(3).strip()

        # Format stick number for display - use the index (i//2 + 1) for regular number
        regular_num = i // 2 + 1
        stick_num = f'第{stick_chinese_num}籤 {regular_num}'

        # Extract sections from body
        sacred_meaning_match = re.search(r'\*\*聖意:\*\*\s*\n((?:(?!\*\*).+\n?)+)', body)
        poem_match = re.search(r'\*\*籤詩:\*\*\s*\n((?:(?!\*\*).+\n?)+)', body)
        interpretation_match = re.search(r'\*\*解籤:\*\*\s*\n((?:(?!\*\*).+\n?)+)', body)

        sacred_meaning = sacred_meaning_match.group(1).strip() if sacred_meaning_match else ''
        poem = poem_match.group(1).strip() if poem_match else ''
        interpretation = interpretation_match.group(1).strip() if interpretation_match else ''

        # Clean up sacred meaning - replace special chars with <br>
        sacred_meaning = sacred_meaning.replace('、', '、').replace('\n', '<br>')
        if '、' in sacred_meaning:
            # Split on 、 and rejoin with <br>
            parts = [p.strip() for p in sacred_meaning.split('、') if p.strip()]
            # Group into two lines
            if len(parts) >= 4:
                line1 = '、'.join(parts[:4])
                line2 = '、'.join(parts[4:])
                sacred_meaning = f'{line1}<br>{line2}'

        sticks.append({
            'stick_num': stick_num,
            'rating': rating,
            'sacred_meaning': sacred_meaning,
            'poem': poem,
            'interpretation': interpretation
        })

    return sticks

def generate_html(stick_data, template_path='design_template_chinese.html'):
    """Generate HTML for a single stick using external template"""
    # Read the template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Replace placeholders
    html = template.format(
        stick_num=stick_data['stick_num'],
        rating=stick_data['rating'],
        sacred_meaning=stick_data['sacred_meaning'],
        poem=stick_data['poem'],
        interpretation=stick_data['interpretation']
    )
    return html

def main():
    """Generate all Chinese HTML files"""
    # Parse markdown
    sticks = parse_chinese_markdown('guan_yu_fortune_sticks_chinese.md')

    print(f"Found {len(sticks)} sticks in markdown")

    # Generate HTML for each stick
    for i, stick_data in enumerate(sticks, 1):
        html = generate_html(stick_data)

        # Write output
        output_path = f'output/stick_{i:03d}_chinese.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"Generated: {output_path}")

    print(f"\nSuccessfully generated {len(sticks)} Chinese HTML files!")

if __name__ == '__main__':
    main()
