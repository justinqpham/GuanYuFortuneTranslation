# Guan Yu Fortune Translation Project

A complete translation and digitization of 100 traditional Guan Yu (Emperor Guan / 關帝灵签) fortune sticks from the Thien Hau Temple in Los Angeles.

## Overview

This project translates classical Chinese fortune divination texts into English and Vietnamese, with professional HTML and PDF outputs suitable for web viewing and printing.

**Source:** Thien Hau Temple, 756 Yale Street, Los Angeles, CA 90012

## Project Status

✅ **All Phases Complete**

- **Phase 1:** Translation (100 sticks) - COMPLETE
- **Phase 2:** HTML Generation (100 files) - COMPLETE
- **Phase 3:** PDF Conversion (100 individual + 1 merged) - COMPLETE

## Deliverables

### 1. Translations (Markdown)
- **Location:** 10 batch files (`batch_01_sticks_001-010.md` through `batch_10_sticks_091-100.md`)
- **Content:** Bilingual translations with fortune ratings, sacred meanings, poems, and interpretations
- **Format:** Structured markdown with English and Vietnamese columns

### 2. Web Format (HTML)
- **Location:** `output/` directory (100 files: `stick_001.html` - `stick_100.html`)
- **Features:**
  - Two-column layout (English/Vietnamese)
  - Letter size (8.5" × 11") optimized for printing
  - EB Garamond typography via Google Fonts
  - Print-ready CSS with proper margins
- **Template:** Based on `design_template.html`

### 3. Print Format (PDF)
- **Individual PDFs:** `output/pdfs/` directory (100 files, ~105KB each)
- **Merged PDF:** `GuanYu_Fortune_Sticks_Complete.pdf` (6.84MB, 100 pages)
- **Quality:** High-resolution with embedded fonts, ready for distribution

## Quick Start

### Viewing Individual Fortunes

**HTML (Web):**
```bash
open output/stick_001.html
```

**PDF (Print):**
```bash
open output/pdfs/stick_001.pdf
```

### Viewing Complete Collection

```bash
open GuanYu_Fortune_Sticks_Complete.pdf
```

## File Structure

```
.
├── README.md                          # This file
├── AGENT_PROMPT.md                    # Complete project documentation
├── HTML_GENERATION_GUIDE.md           # HTML generation instructions
├── PHASE_2_SUMMARY.md                 # HTML generation completion report
├── PHASE_3_SUMMARY.md                 # PDF conversion completion report
│
├── batch_01_sticks_001-010.md         # Translation batches (10 files)
├── batch_02_sticks_011-020.md
├── ...
├── batch_10_sticks_091-100.md
│
├── design_template.html               # HTML template reference
├── generate_batch01_html.py           # HTML generation scripts (10 files)
├── ...
├── generate_batch10_html.py
│
├── convert_html_to_pdf.sh             # PDF conversion script
├── merge_pdfs.sh                      # PDF merging script
│
├── output/                            # Generated HTML files
│   ├── stick_001.html
│   ├── ...
│   ├── stick_100.html
│   └── pdfs/                          # Individual PDF files
│       ├── stick_001.pdf
│       ├── ...
│       └── stick_100.pdf
│
├── GuanYu_Fortune_Sticks_Complete.pdf # Final merged PDF
│
└── images/                            # Source JPG images (100 files)
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
python3 generate_batch01_html.py
python3 generate_batch02_html.py
# ... continue through batch 10

# Or use a loop
for i in {01..10}; do
    python3 generate_batch${i}_html.py
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
./convert_html_to_pdf.sh
```
Output: 100 PDF files in `output/pdfs/`

**Merge into single PDF:**
```bash
./merge_pdfs.sh
```
Output: `GuanYu_Fortune_Sticks_Complete.pdf`

### Technical Specifications
- **Format:** PDF 1.7
- **Page size:** Letter (8.5" × 11")
- **Fonts:** EB Garamond (embedded)
- **Color space:** RGB
- **Total size:** 6.84MB (well under 20MB target)

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
- **Languages:** English, Vietnamese (from Classical Chinese)
- **Markdown files:** 10 (batches of 10 sticks each)
- **HTML files:** 100 (individual sticks)
- **PDF files:** 101 (100 individual + 1 merged)
- **Total HTML size:** ~1.5MB
- **Total PDF size:** 6.84MB (merged)
- **Major corrections:** 17% of sticks required OCR fixes

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
