#!/usr/bin/env python3
"""
Generate HTML files for Batch 06 (Sticks 051-060)
"""

import os
import re

# Template HTML structure
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Emperor Guan Divination Reading - Stick {stick_num}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    @page {{
      size: letter;
      margin: 0;
    }}

    body {{
      font-family: 'EB Garamond', Georgia, serif;
      font-size: 10px;
      line-height: 1.4;
      color: #000;
      background: #f5f5f5;
    }}

    .page {{
      width: 8.5in;
      height: 11in;
      background: white;
      padding: 24px 60px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      position: relative;
    }}

    @media print {{
      body {{
        background: white;
      }}
      .page {{
        margin: 0;
        padding: 24px 60px;
      }}
    }}

    .header {{
      text-align: center;
      margin-bottom: 24px;
      padding-top: 20px;
    }}

    .header-title {{
      font-size: 20px;
      font-weight: 700;
      font-style: italic;
      margin-bottom: 4px;
    }}

    .header-title-vn {{
      font-size: 20px;
      font-weight: 700;
      font-style: italic;
      margin-bottom: 16px;
    }}

    .stick-number {{
      font-size: 48px;
      font-weight: 700;
      line-height: 1;
    }}

    .content {{
      display: flex;
      gap: 42px;
      flex: 1;
    }}

    .column {{
      flex: 1;
      display: flex;
      flex-direction: column;
    }}

    .column-english {{
      justify-content: flex-end;
      padding-bottom: 52px;
    }}

    .column-vietnamese {{
      justify-content: flex-start;
      padding-top: 20px;
    }}

    .fortune-rating {{
      margin-bottom: 16px;
    }}

    .fortune-rating-title {{
      font-size: 16px;
      font-weight: 700;
    }}

    .fortune-rating-subtitle {{
      font-size: 12px;
      font-weight: 700;
    }}

    .section {{
      margin-bottom: 4px;
    }}

    .section-title {{
      font-size: 14px;
      font-weight: 700;
    }}

    .section-content {{
      font-size: 12px;
      font-weight: 400;
    }}

    .meaning-list {{
      list-style: disc;
      padding-left: 16px;
    }}

    .meaning-list li {{
      margin-bottom: 1px;
    }}

    .meaning-label {{
      font-weight: 700;
    }}

    .poem {{
      font-style: normal;
    }}

    .poem-title {{
      font-size: 14px;
      font-weight: 700;
      text-align: right;
    }}

    .poem-stanza {{
      margin-bottom: 8px;
      white-space: pre-line;
      text-align: justify;
      text-align-last: right;
    }}

    .interpretation-list {{
      list-style: disc;
      padding-left: 16px;
    }}

    .interpretation-list li {{
      margin-bottom: 4px;
      text-align: justify;
      text-align-last: left;
    }}

    .footer {{
      text-align: center;
      padding-top: 16px;
      margin-top: auto;
      border-top: none;
      padding-bottom: 20px;
    }}

    .footer-temple {{
      font-size: 12px;
      font-weight: 700;
    }}

    .footer-address {{
      font-size: 12px;
      font-weight: 400;
    }}
  </style>
</head>
<body>

<div class="page">
  <header class="header">
    <div class="header-title">Emperor Guan Divination Reading</div>
    <div class="header-title-vn">Linh Quẻ Quan Thánh Đế Quân</div>
    <div class="stick-number">{stick_num}</div>
  </header>

  <main class="content">
    <div class="column column-english">
      <div class="fortune-rating">
        <div class="fortune-rating-title">{en_rating}</div>
        <div class="fortune-rating-subtitle">({en_subtitle})</div>
      </div>

      <div class="section">
        <div class="section-title">Sacred meaning</div>
        <ul class="meaning-list section-content">
{en_sacred_meanings}
        </ul>
      </div>

      <div class="section">
        <div class="poem-title">Fortune Poem</div>
        <div class="poem section-content">
          <div class="poem-stanza">{en_poem}</div>
        </div>
      </div>

      <div class="section">
        <div class="section-title">Interpretation</div>
        <ul class="interpretation-list section-content">
{en_interpretation}
        </ul>
      </div>
    </div>

    <div class="column column-vietnamese">
      <div class="fortune-rating">
        <div class="fortune-rating-title">{vn_rating}</div>
        <div class="fortune-rating-subtitle">({vn_subtitle})</div>
      </div>

      <div class="section">
        <div class="section-title">Thánh ý</div>
        <ul class="meaning-list section-content">
{vn_sacred_meanings}
        </ul>
      </div>

      <div class="section">
        <div class="poem-title">Bài thơ quẻ</div>
        <div class="poem section-content">
          <div class="poem-stanza">{vn_poem}</div>
        </div>
      </div>

      <div class="section">
        <div class="section-title">Ý nghĩa</div>
        <ul class="interpretation-list section-content">
{vn_interpretation}
        </ul>
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="footer-temple">Thien Hau Temple</div>
    <div class="footer-address">756 Yale Street Los Angeles, CA 90012 · (213) 680-1860</div>
  </footer>
</div>

</body>
</html>
'''

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

def generate_html(stick_data):
    """Generate HTML for a single stick"""
    html = HTML_TEMPLATE.format(
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
    md_file = 'batch_06_sticks_051-060.md'
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
