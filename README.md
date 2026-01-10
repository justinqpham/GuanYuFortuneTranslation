# Guan Yu Fortune Translation Project

A complete translation and digitization of 100 traditional Guan Yu (Emperor Guan / 關帝灵签) fortune sticks from the Thien Hau Temple in Los Angeles.

## Overview

This project translates classical Chinese fortune divination texts into English and Vietnamese, with professional HTML and PDF outputs suitable for web viewing and printing.

**Source:** Thien Hau Temple, 756 Yale Street, Los Angeles, CA 90012

## Project Status

✅ **All Phases Complete**

- **Phase 1:** Translation (100 sticks) - COMPLETE
- **Phase 2:** HTML Generation (100 files English/Vietnamese + 100 Chinese) - COMPLETE
- **Phase 3:** PDF Conversion (200 individual + 2 merged) - COMPLETE

## Deliverables

### 1. Translations (Markdown)
- **English/Vietnamese:** `translation_batches/` directory (10 batch files: `batch_01_sticks_001-010.md` through `batch_10_sticks_091-100.md`)
- **Chinese Reference:** `guan_yu_fortune_sticks_chinese.md` (complete 100 sticks with canonical Chinese text)
- **Content:** Bilingual translations with fortune ratings, sacred meanings, poems, and interpretations
- **Format:** Structured markdown with English and Vietnamese columns
- **Chinese Source:** Web-verified from k366.com, 51chouqian.com, nongli.com, zhouyi.cc

### 2. Web Format (HTML)
- **English/Vietnamese:** `output/` directory (100 files: `stick_001.html` - `stick_100.html`)
  - Two-column layout (English/Vietnamese)
  - Letter size (8.5" × 11") optimized for printing
  - EB Garamond typography via Google Fonts
  - Template: `design_template.html`
- **Chinese:** `output/` directory (100 files: `stick_001_chinese.html` - `stick_100_chinese.html`)
  - Single-column centered layout
  - Noto Serif TC typography via Google Fonts (Traditional Chinese)
  - Template: `design_template_chinese.html`

### 3. Print Format (PDF)
- **Individual PDFs:** `output/pdfs/` directory (200 files total)
  - English/Vietnamese: `stick_001.pdf` - `stick_100.pdf` (~82KB each)
  - Chinese: `stick_001_chinese.pdf` - `stick_100_chinese.pdf` (~290KB each)
- **Merged PDFs:**
  - English/Vietnamese: `GuanYu_Fortune_Sticks_Complete.pdf` (8.1MB, 100 pages)
  - Chinese: `GuanYu_Fortune_Sticks_Chinese_Complete.pdf` (25MB, 100 pages)
- **Quality:** High-resolution with embedded fonts, ready for distribution

## Quick Start

### Viewing Individual Fortunes

**HTML (Web):**
```bash
# English/Vietnamese
open output/stick_001.html

# Chinese
open output/stick_001_chinese.html
```

**PDF (Print):**
```bash
# English/Vietnamese
open output/pdfs/stick_001.pdf

# Chinese
open output/pdfs/stick_001_chinese.pdf
```

### Viewing Complete Collection

**PDF (All 100 sticks):**
```bash
# English/Vietnamese
open GuanYu_Fortune_Sticks_Complete.pdf

# Chinese
open GuanYu_Fortune_Sticks_Chinese_Complete.pdf
```

**Markdown Source:**
```bash
# Chinese reference (canonical texts)
open guan_yu_fortune_sticks_chinese.md
```

## File Structure

```
.
├── README.md                                 # This file
├── AGENT_PROMPT.md                           # Complete project documentation
├── HTML_GENERATION_GUIDE.md                  # HTML generation instructions
├── PHASE_2_SUMMARY.md                        # HTML generation completion report
├── PHASE_3_SUMMARY.md                        # PDF conversion completion report
│
├── guan_yu_fortune_sticks_chinese.md         # Chinese reference (all 100 sticks)
├── design_template.html                      # English/Vietnamese template
├── design_template_chinese.html              # Chinese template
├── DivinationReadingTemplate.png             # Original design reference
│
├── translation_batches/                      # English/Vietnamese translations
│   ├── batch_01_sticks_001-010.md
│   ├── batch_02_sticks_011-020.md
│   ├── ...
│   └── batch_10_sticks_091-100.md
│
├── scripts/                                  # Generation and conversion scripts
│   ├── generate_batch01_html.py              # English/Vietnamese batch scripts (10 files)
│   ├── ...
│   ├── generate_batch10_html.py
│   ├── generate_all_chinese_html.py          # Chinese batch generation (all 100)
│   ├── convert_html_to_pdf.sh                # English/Vietnamese PDF conversion
│   ├── convert_chinese_html_to_pdf.sh        # Chinese PDF conversion
│   └── merge_pdfs.sh                         # PDF merging utility
│
├── output/                                   # Generated output files
│   ├── stick_001.html                        # English/Vietnamese HTML (100 files)
│   ├── stick_001_chinese.html                # Chinese HTML (100 files)
│   ├── ...
│   ├── stick_100.html
│   ├── stick_100_chinese.html
│   └── pdfs/                                 # Individual PDF files (200 files)
│       ├── stick_001.pdf                     # English/Vietnamese PDFs (100 files)
│       ├── stick_001_chinese.pdf             # Chinese PDFs (100 files)
│       ├── ...
│       ├── stick_100.pdf
│       └── stick_100_chinese.pdf
│
├── GuanYu_Fortune_Sticks_Complete.pdf        # English/Vietnamese merged (8.1MB)
├── GuanYu_Fortune_Sticks_Chinese_Complete.pdf # Chinese merged (25MB)
│
└── source_images/                            # Source JPG images (100 files)
    ├── 001.jpg
    ├── ...
    └── 100.jpg
```

## Translation Process

### Batch Workflow
1. OCR text extraction from source images
2. Translation to English and Vietnamese
3. Web verification against canonical sources
4. User review and corrections
5. Documentation of changes

### Quality Assurance
- **Web verification:** All call-outs cross-referenced with standard 關帝灵签 sources
- **OCR accuracy:** ~83% match rate; ~17% required corrections
- **Documentation:** Detailed before/after comparisons for all corrections
- **Sacred meanings:** Only canonical categories included (no placeholders)

### Notable Corrections
- **Stick #1:** Complete poem rewrite (OCR misread "登舟坐稳")
- **Stick #20:** "Eighteen Rapids" (十八滩头) restored
- **Stick #27:** "Three winters" (三冬) timing fixed
- **Stick #30:** Family harmony meaning corrected
- **Stick #32:** Complete sacred meanings overhaul
- **Stick #38:** Major poem corrections ("莫非望" restored)
- **Stick #73:** Reversed lines corrected ("兰房分半钗")

See individual batch files for complete correction documentation.

## HTML Generation

### Prerequisites
- Python 3.x
- Web browser for viewing

### Generate HTML Files
```bash
# Generate all batches
python3 scripts/generate_batch01_html.py
python3 scripts/generate_batch02_html.py
# ... continue through batch 10

# Or use a loop
for i in {01..10}; do
    python3 scripts/generate_batch${i}_html.py
done
```

### Key Technical Details
- **Critical regex:** Sacred meanings have colon INSIDE bold markers
  - Format: `- **Label:** value`
  - Pattern: `r'- \*\*([^*]+):\*\*\s*(.+)'`
- See `HTML_GENERATION_GUIDE.md` for complete instructions

## PDF Generation

### Prerequisites
- Google Chrome (for HTML to PDF conversion)
- Ghostscript (for merging PDFs)

### Convert to PDF

**Individual PDFs:**
```bash
./scripts/convert_html_to_pdf.sh
```
Output: 100 PDF files in `output/pdfs/`

**Merge into single PDF:**
```bash
./scripts/merge_pdfs.sh
```
Output: `GuanYu_Fortune_Sticks_Complete.pdf`

### Technical Specifications
- **Format:** PDF 1.7
- **Page size:** Letter (8.5" × 11")
- **Fonts:** EB Garamond (English/Vietnamese), Noto Serif TC (Chinese) - both embedded
- **Color space:** RGB
- **Total size:** 8.1MB (English/Vietnamese), 25MB (Chinese)

## Critical Technical Issues & Solutions

### Issue 1: Blank Pages in PDF Output

**Problem:** Chrome headless PDF generation was creating extra blank pages after each fortune stick page.

**Root Cause:** CSS properties causing page breaks during print rendering:
- Missing `page-break-after: avoid` on `.page` element
- Missing `overflow: hidden` on `.page` element

**Solution:** Add the following CSS in `@media print` section:

```css
@media print {
  body {
    background: white;
  }
  .page {
    margin: 0;
    padding: 32px 80px;
    page-break-after: avoid;  /* CRITICAL: Prevents blank pages */
    overflow: hidden;          /* CRITICAL: Prevents overflow page breaks */
  }
}
```

**Files affected:**
- `design_template.html`
- `design_template_chinese.html`

**Impact:** Without these fixes, PDF generation creates 200 pages (100 content + 100 blank) instead of 100 pages.

### Issue 2: Chinese PDF Rendering Empty Content

**Problem:** Chinese PDFs showed only the decorative frame border, no text content. HTML files displayed correctly in browser.

**Root Cause:** Google Fonts (Noto Serif TC) not loading before PDF generation in headless Chrome. The font download takes time, but headless mode generates PDF immediately without waiting.

**Solution:** Add `--virtual-time-budget=10000` flag to Chrome command:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="output.pdf" \
  --print-to-pdf-no-header \
  --no-margins \
  --virtual-time-budget=10000 \  # CRITICAL: Gives 10 seconds for font loading
  "file://input.html"
```

**Evidence:**
- Without flag: PDF file size ~17KB (frame only)
- With flag: PDF file size ~290-364KB (full content with fonts)

**Files affected:**
- `scripts/convert_chinese_html_to_pdf.sh`

**Why this happens:** External fonts from Google Fonts CDN require network requests and time to download. Headless Chrome doesn't wait for these resources by default. The virtual-time-budget flag gives the browser virtual time to complete resource loading.

**Important:** This issue affects ANY PDF generation using external fonts (Google Fonts, Adobe Fonts, etc.). Always use `--virtual-time-budget` when generating PDFs with web fonts.

### Issue 3: Markdown Parsing Incomplete (39 of 100 sticks)

**Problem:** `generate_all_chinese_html.py` initially extracted only 39 out of 100 sticks from markdown.

**Root Cause:** Roman numeral regex pattern `[IVX]+` only matched I, V, X but not L (50) or C (100).

**Failing examples:**
- Stick 40: "XL" (contains L)
- Stick 50: "L"
- Stick 90: "XC" (contains C)
- Stick 100: "C"

**Solution:** Update regex pattern to include all Roman numeral characters:

```python
# OLD - Only matches up to 39
match = re.match(r'第(.+?)籤\s+([IVX]+)\s+(.+)', header)

# NEW - Matches all 100 sticks
match = re.match(r'第(.+?)籤\s+([IVXLC]+)\s+(.+)', header)
```

**Files affected:**
- `scripts/generate_all_chinese_html.py`

### Issue 4: Multi-line Content Not Captured

**Problem:** Interpretation sections (解籤) were truncated to first line only.

**Root Cause:** Regex pattern `([^\n]+)` stops at first newline, but many interpretations span multiple lines.

**Solution:** Use negative lookahead to capture until next section marker:

```python
# OLD - Only captures single line
interpretation_match = re.search(r'\*\*解籤:\*\*\s*\n([^\n]+)', body)

# NEW - Captures all lines until next section
interpretation_match = re.search(r'\*\*解籤:\*\*\s*\n((?:(?!\*\*).+\n?)+)', body)
```

**Pattern explanation:**
- `(?:(?!\*\*).)` - Match any character that's NOT the start of `**`
- `+` - One or more such characters
- `\n?` - Optional newline
- `()+` - Capture one or more lines

**Files affected:**
- `scripts/generate_all_chinese_html.py` (applied to sacred_meaning, poem, and interpretation sections)

### Issue 5: Python Template String Conflicts

**Problem:** CSS curly braces `{}` conflict with Python's `.format()` template strings, causing `KeyError` exceptions.

**Root Cause:** CSS uses `{` and `}` extensively for style rules. Python's `.format()` interprets these as placeholder markers.

**Solution:** Escape all CSS curly braces by doubling them:

```python
# In CSS sections of HTML template
style {{  # Double braces for literal {
  margin: 0;
}}        # Double braces for literal }

# In Python placeholders
<div>{stick_num}</div>  # Single braces for actual placeholders
```

**Automation:** Use regex replacement:

```python
import re
style_content = re.sub(r'(?<!\{)\{(?!\{)', '{{', style_content)  # { -> {{
style_content = re.sub(r'(?<!\})\}(?!\})', '}}', style_content)  # } -> }}
```

**Files affected:**
- `design_template.html`
- `design_template_chinese.html`

### Best Practices for Future Agents

1. **PDF Generation with External Fonts:**
   - Always use `--virtual-time-budget=10000` (minimum) for Google Fonts
   - Increase to 15000-20000 for slower networks or multiple fonts
   - Test generated PDF file size - too small indicates missing content

2. **CSS for Print Media:**
   - Always include `page-break-after: avoid` on main content containers
   - Add `overflow: hidden` to prevent content overflow creating extra pages
   - Test PDF output, not just HTML preview

3. **Markdown Parsing:**
   - Test regex patterns with edge cases (numbers 40, 50, 90, 100)
   - Use negative lookahead for multi-line content sections
   - Verify extraction count matches expected total

4. **Python Template Strings:**
   - Escape ALL CSS/JavaScript curly braces when using `.format()`
   - Use automated regex replacement to avoid manual errors
   - Test with simple data first before processing all files

5. **Roman Numerals:**
   - Full character set needed: `[IVXLC]` (covers 1-100)
   - Extended set for larger numbers: `[IVXLCDM]` (covers 1-3999)

## Fortune Stick Structure

Each fortune stick contains:

1. **Fortune Rating** - Overall assessment (e.g., "Excellent Fortune")
2. **Sacred Meaning** (聖意) - Guidance across life domains:
   - Home/Family (家宅)
   - Self/Body (自身)
   - Wealth (求財)
   - Transactions (交易)
   - Marriage (婚姻)
   - Six Relations (六甲)
   - Travelers (行人)
   - Field/Harvest (田蠶)
   - Livestock (六畜)
   - Seeking Person (尋人)
   - Public Affairs (公訟)
   - Migration (移徙)
   - Lost Property (失物)
   - Illness (疾病)
   - Mountain Grave (山墳)
3. **Fortune Poem** - Classical 4-line poem with metaphorical guidance
4. **Interpretation** - Modern explanation and practical application

## Documentation

- **`AGENT_PROMPT.md`** - Complete project documentation with progress tracker
- **`HTML_GENERATION_GUIDE.md`** - Detailed HTML generation instructions (600+ lines)
- **`PHASE_2_SUMMARY.md`** - HTML generation completion report
- **`PHASE_3_SUMMARY.md`** - PDF conversion completion report

## Technical Stack

- **Translation:** Manual translation with OCR assistance
- **Web verification:** Cross-referenced with canonical 關帝灵签 sources
- **HTML generation:** Python 3 with regex parsing
- **PDF conversion:** Chrome headless mode
- **PDF merging:** Ghostscript 10.06.0
- **Typography:** EB Garamond (Google Fonts)
- **Version control:** Git

## Statistics

- **Total sticks:** 100
- **Languages:** English, Vietnamese, Traditional Chinese
- **Markdown files:** 11 total (10 translation batches + 1 Chinese reference)
- **HTML files:** 200 (100 English/Vietnamese + 100 Chinese)
- **PDF files:** 202 (200 individual + 2 merged)
- **Total HTML size:** ~7.8MB (200 files)
- **Total PDF size:** 33.1MB (8.1MB English/Vietnamese + 25MB Chinese merged)
- **Major corrections:** 17% of sticks required OCR fixes
- **Chinese sources:** k366.com, 51chouqian.com, nongli.com, zhouyi.cc
- **Generation scripts:** 14 total (10 English/Vietnamese batch scripts + 1 Chinese batch script + 3 conversion/merge scripts)

## License

This is a cultural preservation and translation project. The original fortune texts are traditional Chinese cultural heritage. The translations and interpretations are original work.

## Contact

**Thien Hau Temple**
756 Yale Street
Los Angeles, CA 90012
(213) 680-1860

---

**Project completed:** January 2026
**Translation accuracy:** Web-verified against canonical sources
**Format compatibility:** Web (HTML) and Print (PDF)
