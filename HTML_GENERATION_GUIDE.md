# HTML Generation Guide for Guan Yu Fortune Sticks

## Purpose
This guide explains how to convert markdown translation files (Phase 1) into individual HTML files (Phase 2) that match the design template.

---

## Quick Start

1. **Input:** Markdown batch files (e.g., `batch_01_sticks_001-010.md`)
2. **Output:** Individual HTML files (e.g., `stick_001.html`) in `output/` directory
3. **Template:** Based on `design_template.html`
4. **Process:** Parse markdown → Extract data → Fill HTML template → Write files

---

## Markdown Format Structure

Each stick in the batch files follows this exact structure:

```markdown
===========================================
STICK #5
===========================================

### ENGLISH TRANSLATION

Average Fortune (Neutral / Mixed)

**Sacred Meaning:**
- **Health:** all matters suitable
- **Wealth:** delay and resistance
- **Reputation:** wait for the right time
- **Travel / Movement:** return
- **Marriage:** suitable but proceed with caution
- **Misfortune:** eventually auspicious
- **Blessings:** gradually improving
- **Litigation:** wait for the right time

**Fortune Poem:**
There are three boats that cannot move freely,
The door's court is empty and cold like autumn.
If one meets favorable winds or exchanges with the rat and ox,
All matters will return in spring, no need for worry.

**Interpretation:**
• This fortune describes a period of stagnation that will naturally resolve with time.
• The key is seasonal timing—specifically waiting for spring or the years of Rat and Ox.
• Despite current coldness and emptiness, the fortune is neutral, not negative.

---

### VIETNAMESE TRANSLATION

Trung Bình (Bình thường / Trung bình)

**Sacred Meaning:**
- **Sức khỏe:** mọi việc thích hợp
- **Tài lộc:** trì hoãn và kháng cự
[... more items ...]

**Bài thơ quẻ:**
Có ba chiếc thuyền không thể di chuyển tự do,
Cửa sân trống trải lạnh lẽo như thu.
[... rest of poem ...]

**Ý nghĩa:**
• Quẻ này mô tả giai đoạn trì trệ...
• Chìa khóa là thời điểm theo mùa...
• Mặc dù hiện tại lạnh lẽo...

---
```

---

## Critical Parsing Details

### ⚠️ Sacred Meanings Format - VERY IMPORTANT

**The colon is INSIDE the bold markers!**

❌ **Wrong:** `- **Health**: all matters suitable` (colon outside)
✅ **Correct:** `- **Health:** all matters suitable` (colon inside)

**Correct Regex Pattern:**
```python
# Pattern to match each line
r'- \*\*([^*]+):\*\*\s*(.+)'

# Explanation:
# - \*\*        = literal "- **"
# ([^*]+)       = capture label (any chars except asterisk)
# :             = literal colon (INSIDE the bold)
# \*\*          = closing "**"
# \s*           = optional whitespace
# (.+)          = capture value (rest of line)
```

**Example Match:**
```python
import re
line = "- **Health:** all matters suitable"
match = re.match(r'- \*\*([^*]+):\*\*\s*(.+)', line)
# match.group(1) = "Health"
# match.group(2) = "all matters suitable"
```

### Regex Patterns for All Sections

```python
import re

# 1. Split sticks in batch file
stick_pattern = r'=+\nSTICK #(\d+)\n=+'
sticks = re.split(stick_pattern, content)
# Result: ['', '1', '<stick 1 content>', '2', '<stick 2 content>', ...]

# 2. Extract English section
en_pattern = r'### ENGLISH TRANSLATION\n\n(.*?)\n\n---\n\n### VIETNAMESE TRANSLATION'
en_match = re.search(en_pattern, stick_content, re.DOTALL)
en_section = en_match.group(1)

# 3. Extract Vietnamese section
vn_pattern = r'### VIETNAMESE TRANSLATION\n\n(.*?)(?:\n\n---|$)'
vn_match = re.search(vn_pattern, stick_content, re.DOTALL)
vn_section = vn_match.group(1)

# 4. Extract rating and subtitle (both languages)
rating_pattern = r'([^\(]+)\s*\(([^\)]+)\)'
match = re.match(rating_pattern, section)
rating = match.group(1).strip()      # e.g., "Average Fortune"
subtitle = match.group(2).strip()    # e.g., "Neutral / Mixed"

# 5. Extract sacred meanings block
sacred_pattern = r'\*\*Sacred Meaning:\*\*\n((- .+\n?)+)'
sacred_match = re.search(sacred_pattern, en_section, re.MULTILINE)
sacred_text = sacred_match.group(1).strip()

# 6. Extract poem (English)
poem_pattern = r'\*\*Fortune Poem:\*\*\n((?:(?!\*\*).+\n?)+)'
poem_match = re.search(poem_pattern, en_section, re.MULTILINE)
poem = poem_match.group(1).strip()

# 7. Extract poem (Vietnamese)
vn_poem_pattern = r'\*\*Bài thơ quẻ:\*\*\n((?:(?!\*\*).+\n?)+)'
vn_poem_match = re.search(vn_poem_pattern, vn_section, re.MULTILINE)
vn_poem = vn_poem_match.group(1).strip()

# 8. Extract interpretation (English)
interp_pattern = r'\*\*Interpretation:\*\*\n((?:•[^\n]+\n?)+)'
interp_match = re.search(interp_pattern, en_section, re.MULTILINE)
interpretation = interp_match.group(1)

# 9. Extract interpretation (Vietnamese)
vn_interp_pattern = r'\*\*Ý nghĩa:\*\*\n((?:•[^\n]+\n?)+)'
vn_interp_match = re.search(vn_interp_pattern, vn_section, re.MULTILINE)
vn_interpretation = vn_interp_match.group(1)
```

---

## HTML Template Structure

### Complete HTML Template

The HTML template is based on `design_template.html` with these specifications:

- **Page size:** Letter (8.5" × 11")
- **Font:** EB Garamond (loaded from Google Fonts)
- **Layout:** Flexbox two-column (English left, Vietnamese right)
- **Sections per column:**
  1. Fortune rating + subtitle
  2. Sacred meanings (bulleted list)
  3. Fortune poem (right-aligned for English, justified for Vietnamese)
  4. Interpretation (bulleted list, left-aligned)

### Key CSS Classes

```css
.page                      /* Letter size page container */
.header                    /* Centered header with titles and stick number */
.stick-number              /* Large 48px stick number */
.content                   /* Flex container for two columns */
.column-english            /* Left column, bottom-aligned */
.column-vietnamese         /* Right column, top-aligned */
.fortune-rating            /* Rating and subtitle container */
.section                   /* Each content section */
.meaning-list              /* Sacred meanings <ul> */
.meaning-label             /* Bold labels in sacred meanings */
.poem-title                /* "Fortune Poem" / "Bài thơ quẻ" */
.poem-stanza               /* Poem text with right-alignment */
.interpretation-list       /* Interpretation <ul> */
.footer                    /* Temple name and address */
```

### Template Placeholders

```python
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Emperor Guan Divination Reading - Stick {stick_num}</title>
  <!-- Google Fonts and CSS here -->
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
      <!-- Same structure for Vietnamese -->
      {vn_rating}
      {vn_subtitle}
      {vn_sacred_meanings}
      {vn_poem}
      {vn_interpretation}
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
```

---

## Formatting Functions

### Format Sacred Meanings

Convert markdown sacred meanings to HTML list items:

```python
def format_sacred_meanings(text):
    """
    Input: "- **Health:** immediate recovery\n- **Wealth:** success..."
    Output: HTML <li> tags with styled labels
    """
    if not text:
        return ""

    lines = text.strip().split('\n')
    html_lines = []

    for line in lines:
        # CRITICAL: Colon is INSIDE the bold markers
        match = re.match(r'- \*\*([^*]+):\*\*\s*(.+)', line)
        if match:
            label = match.group(1)
            value = match.group(2)
            html_lines.append(
                f'          <li><span class="meaning-label">{label}:</span> {value}</li>'
            )

    return '\n'.join(html_lines)
```

**Example:**
```python
text = "- **Health:** immediate recovery\n- **Wealth:** success"
result = format_sacred_meanings(text)
# Result:
#           <li><span class="meaning-label">Health:</span> immediate recovery</li>
#           <li><span class="meaning-label">Wealth:</span> success</li>
```

### Format Interpretation

Convert bullet points to HTML list items:

```python
def format_interpretation(text):
    """
    Input: "• Point 1\n• Point 2\n• Point 3"
    Output: HTML <li> tags
    """
    lines = text.strip().split('\n')
    html_lines = []

    for line in lines:
        if line.startswith('•'):
            content = line[1:].strip()  # Remove bullet character
            html_lines.append(f'          <li>{content}</li>')

    return '\n'.join(html_lines)
```

---

## Complete Python Script Structure

```python
#!/usr/bin/env python3
"""
Generate HTML files for a batch of Guan Yu fortune sticks
"""

import os
import re

# HTML_TEMPLATE constant here (see design_template.html)
HTML_TEMPLATE = '''...'''

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

        # Extract English and Vietnamese sections
        en_match = re.search(
            r'### ENGLISH TRANSLATION\n\n(.*?)\n\n---\n\n### VIETNAMESE TRANSLATION',
            stick_content,
            re.DOTALL
        )
        vn_match = re.search(
            r'### VIETNAMESE TRANSLATION\n\n(.*?)(?:\n\n---|$)',
            stick_content,
            re.DOTALL
        )

        if not en_match or not vn_match:
            continue

        en_section = en_match.group(1)
        vn_section = vn_match.group(1)

        # Parse English components
        en_rating_match = re.match(r'([^\(]+)\s*\(([^\)]+)\)', en_section)
        en_rating = en_rating_match.group(1).strip() if en_rating_match else ""
        en_subtitle = en_rating_match.group(2).strip() if en_rating_match else ""

        en_sacred = re.search(
            r'\*\*Sacred Meaning:\*\*\n((- .+\n?)+)',
            en_section,
            re.MULTILINE
        )
        en_sacred_meanings = en_sacred.group(1).strip() if en_sacred else ""

        en_poem_match = re.search(
            r'\*\*Fortune Poem:\*\*\n((?:(?!\*\*).+\n?)+)',
            en_section,
            re.MULTILINE
        )
        en_poem = en_poem_match.group(1).strip() if en_poem_match else ""

        en_interp_match = re.search(
            r'\*\*Interpretation:\*\*\n((?:•[^\n]+\n?)+)',
            en_section,
            re.MULTILINE
        )
        en_interpretation = en_interp_match.group(1) if en_interp_match else ""

        # Parse Vietnamese components (same pattern)
        vn_rating_match = re.match(r'([^\(]+)\s*\(([^\)]+)\)', vn_section)
        vn_rating = vn_rating_match.group(1).strip() if vn_rating_match else ""
        vn_subtitle = vn_rating_match.group(2).strip() if vn_rating_match else ""

        vn_sacred = re.search(
            r'\*\*Sacred Meaning:\*\*\n((- .+\n?)+)',
            vn_section,
            re.MULTILINE
        )
        vn_sacred_meanings = vn_sacred.group(1).strip() if vn_sacred else ""

        vn_poem_match = re.search(
            r'\*\*Bài thơ quẻ:\*\*\n((?:(?!\*\*).+\n?)+)',
            vn_section,
            re.MULTILINE
        )
        vn_poem = vn_poem_match.group(1).strip() if vn_poem_match else ""

        vn_interp_match = re.search(
            r'\*\*Ý nghĩa:\*\*\n((?:•[^\n]+\n?)+)',
            vn_section,
            re.MULTILINE
        )
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
            html_lines.append(
                f'          <li><span class="meaning-label">{label}:</span> {value}</li>'
            )
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
    md_file = 'batch_01_sticks_001-010.md'  # Change for each batch
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
```

---

## File Naming Convention

**Pattern:** `stick_[3-digit-number].html`

**Examples:**
- Stick #1 → `stick_001.html`
- Stick #5 → `stick_005.html`
- Stick #65 → `stick_065.html`
- Stick #100 → `stick_100.html`

**Python formatting:**
```python
filename = f"output/stick_{stick_num:03d}.html"
```

---

## Batch Processing Workflow

### For Each Batch:

1. **Update script input file:**
   ```python
   md_file = 'batch_01_sticks_001-010.md'  # Batch 01
   md_file = 'batch_02_sticks_011-020.md'  # Batch 02
   # ... etc
   ```

2. **Run script:**
   ```bash
   python3 generate_batch[XX]_html.py
   ```

3. **Verify output:**
   - Check `output/` directory for new files
   - Open 1-2 HTML files in browser
   - Verify all sections populated
   - Check for empty lists or missing content

4. **User verification:**
   - Present batch to user for review
   - Wait for approval before proceeding to next batch

---

## Common Issues & Solutions

### Issue: Empty Sacred Meanings

**Symptom:** Sacred meanings `<ul>` is empty

**Causes:**
1. Wrong regex pattern (colon outside bold)
2. Not using `re.MULTILINE` flag
3. Pattern requires trailing newline

**Solution:**
```python
# Correct pattern
sacred_pattern = r'\*\*Sacred Meaning:\*\*\n((- .+\n?)+)'
match = re.search(sacred_pattern, text, re.MULTILINE)

# Correct formatting function
def format_sacred_meanings(text):
    match = re.match(r'- \*\*([^*]+):\*\*\s*(.+)', line)
    #                      ^^^^^^^ colon HERE inside bold
```

### Issue: Empty Poem Section

**Symptom:** Poem `<div>` is empty

**Cause:** Pattern too restrictive, not matching actual format

**Solution:**
```python
# Use negative lookahead to capture until next **
poem_pattern = r'\*\*Fortune Poem:\*\*\n((?:(?!\*\*).+\n?)+)'
```

### Issue: Interpretation Not Parsing

**Symptom:** Interpretation list empty

**Cause:** Bullet character `•` not matching or encoding issue

**Solution:**
```python
# Match both • and fallback patterns
if line.startswith('•') or line.startswith('- '):
    content = line[1:].strip()
```

### Issue: Wrong Stick Numbers

**Symptom:** File `stick_005.html` contains data from Stick #6

**Cause:** Off-by-one error in split parsing

**Solution:**
```python
# When using re.split, groups alternate between separators and content
sticks = re.split(r'=+\nSTICK #(\d+)\n=+', content)
# Result: ['', '1', '<content 1>', '2', '<content 2>', ...]
# Index: [0]  [1]  [2]            [3]  [4]

for i in range(1, len(sticks), 2):  # Step by 2, start at 1
    stick_num = int(sticks[i])       # Odd indices = numbers
    stick_content = sticks[i + 1]    # Even indices = content
```

---

## Testing Checklist

For each generated HTML file:

- [ ] File exists with correct naming (`stick_###.html`)
- [ ] Opens in browser without errors
- [ ] Stick number displays correctly in header
- [ ] Fortune rating and subtitle present (both languages)
- [ ] Sacred meanings populated (not empty list)
- [ ] Sacred meaning labels are bold
- [ ] Poem displays with proper line breaks
- [ ] Poem right-aligned (English) / justified (Vietnamese)
- [ ] Interpretation has 3 bullet points
- [ ] Footer shows temple info
- [ ] Page fits on Letter size (8.5" × 11")
- [ ] Print preview looks correct
- [ ] No HTML escaping issues (quotes, apostrophes display correctly)

---

## Reference Files

- **Working Script:** `generate_batch01_html.py`
- **Design Template:** `design_template.html`
- **Example Output:** `output/stick_001.html`, `output/stick_005.html`
- **Batch Files:** `batch_01_sticks_001-010.md` through `batch_10_sticks_091-100.md`

---

## Next Steps After HTML Generation

Once all 100 HTML files are generated and verified:

1. **Phase 3:** Convert HTML to PDF using Puppeteer or similar
2. **Phase 4:** Merge 100 individual PDFs into single final PDF
3. **Verify:** Final PDF size under 20MB target

---

## Quick Reference: Key Patterns

```python
# Stick split
r'=+\nSTICK #(\d+)\n=+'

# Section extraction
r'### ENGLISH TRANSLATION\n\n(.*?)\n\n---'

# Rating + subtitle
r'([^\(]+)\s*\(([^\)]+)\)'

# Sacred meanings block
r'\*\*Sacred Meaning:\*\*\n((- .+\n?)+)'

# Sacred meaning line (CRITICAL)
r'- \*\*([^*]+):\*\*\s*(.+)'

# Poem
r'\*\*Fortune Poem:\*\*\n((?:(?!\*\*).+\n?)+)'

# Interpretation
r'\*\*Interpretation:\*\*\n((?:•[^\n]+\n?)+)'
```
