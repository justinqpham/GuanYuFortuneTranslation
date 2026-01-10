#!/usr/bin/env python3
"""Generate Chinese HTML for stick #1"""

def generate_chinese_html():
    """Generate HTML for Chinese stick #1"""
    # Read the template
    with open('design_template_chinese.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # Data for stick #1
    stick_data = {
        'stick_num': '第一籤 I',
        'rating': '甲甲 大吉',
        'sacred_meaning': '功名遂、福祿全、訟得理、病即痊<br>桑麻熟、婚姻圓、孕生子、行人還',
        'poem': '巍巍獨步向雲間，\n玉殿千官第一班，\n富貴榮華天付汝，\n福如東海壽如山。',
        'interpretation': '此籤象徵「平步青雲」，一切皆可如願實現，福祿壽喜均圓滿。強調「須要人地相當則應」，需天時、地利、人和三者合一方能無往不利。'
    }

    # Replace placeholders
    html = template.format(**stick_data)

    # Write the output
    output_path = 'output/stick_001_chinese.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Generated: {output_path}")

if __name__ == '__main__':
    generate_chinese_html()
