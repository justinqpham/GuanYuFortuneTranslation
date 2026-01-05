# Guan Yu Fortune Stick Translation Project

## Project Overview

You are translating 100 Guan Yu (关帝灵签) fortune sticks from Chinese to Vietnamese and English. Each stick contains a fortune rating, sacred meanings, and a poem. You will also generate interpretations based on the content.

**Process:** Translate 10 sticks at a time, present for user confirmation, learn from feedback, then proceed to next batch.

---

## Progress Tracker

**Status:** Phase 1 - Translation in progress

### Completed Batches:
- ✅ Batch 01 (Sticks 1-10) - Verified and Confirmed
  - File: `batch_01_sticks_001-010.md`
  - Major corrections: Stick #1 poem completely wrong (OCR error), Stick #4 litigation meaning
- ✅ Batch 02 (Sticks 11-20) - Verified and Confirmed
  - File: `batch_02_sticks_011-020.md`
  - Major corrections: Stick #20 poem "十八滩头" (Eighteen Rapids) not "十八到頭"
- ✅ Batch 03 (Sticks 21-30) - Verified and Confirmed
  - File: `batch_03_sticks_021-030.md`
  - Major corrections: Sticks #21, #27, #30 (OCR errors corrected via web verification)
- ✅ Batch 04 (Sticks 31-40) - Verified and Confirmed
  - File: `batch_04_sticks_031-040.md`
  - Major corrections: Stick #32 sacred meanings, Stick #38 poem completely wrong (OCR error)

### Pending Batches:
- ⏳ Batch 05 (Sticks 41-50)
- ⏳ Batch 06 (Sticks 51-60)
- ⏳ Batch 07 (Sticks 61-70)
- ⏳ Batch 08 (Sticks 71-80)
- ⏳ Batch 09 (Sticks 81-90)
- ⏳ Batch 10 (Sticks 91-100)

### Translation Notes & Learnings:
- Format updated: Removed "**Fortune Rating:**" label, showing only rating and subtitle directly
- All interpretations tailored to match fortune level tone (positive for good fortunes, cautionary but constructive for poor fortunes)
- Always maintain standard format order: Sacred Meaning before Fortune Poem
- Stick #11 contradiction verified: Poor fortune with optimistic poem is intentional (warns against surface appearances)
- When OCR unclear, cross-reference with web sources for standard sign text
- Stick #25 zodiac timing confirmed: 玉兔金鸡 = Rabbit/Rooster years or months (卯酉)
- **CRITICAL:** After completing each batch translation, IMMEDIATELY web search to verify all call-outs before presenting to user
- Design template verified: Stick #1 demo confirms translations fit perfectly in the final template layout

---

## Source Material

- 100 JPG images of fortune sticks from Thien Hau Temple (Los Angeles)
- Each image contains: stick number, fortune rating, sacred meaning (聖意), and a 4-line poem
- Images are high quality; some may have slight angles but should be readable

---

## Your Task For Each Stick

### 1. OCR & Extract

From each image, extract:
- **Stick number** (e.g., 65)
- **Fortune rating** (e.g., 上上)
- **Sacred meaning section** (聖意) - 8 items
- **Poem** - 4 lines of classical Chinese (read top-to-bottom, right-to-left)

**If OCR is unclear:** Web search for the standard text of that specific sign (e.g., "关帝灵签第65签") to verify. Do not guess.

---

### 2. Map Fortune Rating

Use this fixed mapping table:

| Chinese | Vietnamese | English | Subtitle EN | Subtitle VN |
|---------|------------|---------|-------------|-------------|
| 大吉 | Đại Cát | Great Fortune | (Excellent / Very Auspicious) | (Rất tốt / Đại cát) |
| 上上 | Thượng Thượng | Supreme Fortune | (Excellent / Very Auspicious) | (Rất tốt / Đại cát) |
| 上吉 | Thượng Cát | Upper Fortune | (Good / Auspicious) | (Tốt / Cát) |
| 中吉 | Trung Cát | Middle Fortune | (Moderate / Fairly Auspicious) | (Khá tốt / Trung cát) |
| 中平 | Trung Bình | Average Fortune | (Neutral / Mixed) | (Bình thường / Trung bình) |
| 中下 | Trung Hạ | Below Average | (Caution Advised) | (Cần cẩn thận) |
| 下下 | Hạ Hạ | Poor Fortune | (Unfavorable / Caution) | (Không thuận / Cần đề phòng) |

---

### 3. Translate Sacred Meaning (聖意)

Use these fixed label mappings:

| Chinese | Vietnamese | English |
|---------|------------|---------|
| 病 | Sức khỏe | Health |
| 財 | Tài lộc | Wealth |
| 名 | Danh tiếng | Reputation |
| 行人 | Người đi xa / Di chuyển | Travel / Movement |
| 婚 | Hôn nhân | Marriage |
| 禍 | Tai họa | Misfortune |
| 福 | Phúc lộc | Blessings |
| 訟 | Kiện tụng | Litigation |

**Translation style:** Interpretive, not literal. Translate the meaning/implication, not word-for-word.

**Format:** Each item has a **bold label** and normal text value.

**Example:**
- Chinese: 病即安
- English: **Health:** safety and recovery
- Vietnamese: **Sức khỏe:** sẽ bình an

---

### 4. Translate Poem

**Structure:** Keep faithful to original 4-line structure. Do not expand to 8 lines.

**Style for Vietnamese:** Balance poetic flow with accurate meaning. Aim for natural Vietnamese that captures the essence. Light rhyme/rhythm is good but don't sacrifice meaning for it.

**Style for English:** Clear, accessible translation that preserves the imagery and meaning of the original.

**Example input (read right-to-left, top-to-bottom):**
```
朔風凜凜正窮冬
漸覺門庭喜氣濃
更入新春人事後
衷言方得信先容
```

**Example output:**

English:
```
Spring winds gradually replace winter's cold,
Joyful energy fills the household gate.
A newcomer arrives bearing good news,
And what follows unfolds in harmony.
```

Vietnamese:
```
Gió xuân dần ấm, xua tan rét đông,
Cảnh cửa nhà rực rỡ, khí vui dồi dào.
Người mới bước vào mang theo tin tốt,
Mọi việc về sau đều thuận hòa.
```

---

### 5. Generate Interpretation

**Process:**
1. First, use your knowledge to interpret the stick based on the poem and sacred meaning
2. Cross-reference with web search (e.g., "关帝灵签第65签解签") for accuracy
3. If discrepancies exist between your interpretation and web sources, flag for user

**Format:** Exactly 3 bullet points, maximum 3 lines each

**Tone:** Match the fortune level:
- Good fortunes (大吉, 上上, 上吉): Positive, encouraging
- Middle fortunes (中吉, 中平): Balanced, practical advice
- Poor fortunes (中下, 下下): Cautionary but constructive, not doom-and-gloom

**Example (for 上上 Supreme Fortune):**

English:
- This is the highest category of fortune in temple divination. It is rare and unambiguous.
- This slip signals a clear transition from hardship to expansion. Not a warning. Not a test.
- The emphasis is on new people, new phase, and compounding good fortune, not sudden luck but sustained momentum.

Vietnamese:
- Vận đã đổi chiều. Giai đoạn khó khăn đã qua. Từ suy sang thịnh, việc cũ khép lại, việc mới mở ra. Không phải may mắn bất ngờ mà là kết quả của thời gian và nhẫn nại.
- Người mới mang cơ hội. Sẽ có người hoặc mối duyên mới xuất hiện, đem theo tin tốt hoặc mở nút thắt cũ. Cơ hội đến thông qua con người, không phải ngẫu nhiên.
- Phúc đến theo chuỗi. Làm đúng một bước sẽ kéo theo nhiều việc thuận lợi sau đó. Giữ hòa khí, chữ tín và tiến chậm mà chắc thì kết quả vượt mong đợi.

---

## Output Format Per Stick

Output each stick with English and Vietnamese translations completely separated. Do NOT include original Chinese text. Do NOT interlace languages.

```
===========================================
STICK #[NUMBER]
===========================================

### ENGLISH TRANSLATION

[Rating] ([Subtitle])

**Sacred Meaning:**
- **Health:** [translation]
- **Wealth:** [translation]
- **Reputation:** [translation]
- **Travel / Movement:** [translation]
- **Marriage:** [translation]
- **Misfortune:** [translation]
- **Blessings:** [translation]
- **Litigation:** [translation]

**Fortune Poem:**
[Line 1]
[Line 2]
[Line 3]
[Line 4]

**Interpretation:**
• [Point 1 - max 3 lines]
• [Point 2 - max 3 lines]
• [Point 3 - max 3 lines]

---

### VIETNAMESE TRANSLATION

[Rating] ([Subtitle])

**Sacred Meaning:**
- **Sức khỏe:** [translation]
- **Tài lộc:** [translation]
- **Danh tiếng:** [translation]
- **Người đi xa / Di chuyển:** [translation]
- **Hôn nhân:** [translation]
- **Tai họa:** [translation]
- **Phúc lộc:** [translation]
- **Kiện tụng:** [translation]

**Bài thơ quẻ:**
[Line 1]
[Line 2]
[Line 3]
[Line 4]

**Ý nghĩa:**
• [Point 1 - max 3 lines]
• [Point 2 - max 3 lines]
• [Point 3 - max 3 lines]

---

### CALL-OUTS

**After completing the batch:**
1. Review all your call-outs and uncertainties
2. Web search each one to verify against standard texts (use queries like "关帝灵签第[NUMBER]签")
3. Apply corrections based on verification
4. Update this section to state "All call-outs verified and corrected:" with a summary of what was verified/corrected

[List any initial uncertainties, then update with verification results]
```

---

## Output Files

**IMPORTANT:** Save each batch to a markdown file to avoid session limits.

### Batch Files (Human Review)

After translating each batch of 10, save to:
- `batch_01_sticks_001-010.md`
- `batch_02_sticks_011-020.md`
- `batch_03_sticks_021-030.md`
- ... and so on

### JSON Data Files (For Template)

After user confirms each batch, save structured data to:
- `data_batch_01.json`
- `data_batch_02.json`
- ... and so on

After all batches confirmed, combine into:
- `translations_all.json`

---

## JSON Data Structure

The JSON structure separates English and Vietnamese completely:

```json
{
  "stick_number": 65,
  
  "english": {
    "fortune_rating_title": "Supreme Fortune",
    "fortune_rating_subtitle": "(Excellent / Very Auspicious)",
    "sacred_meaning": [
      {"label": "Health", "value": "safety and recovery"},
      {"label": "Wealth", "value": "abundant gains"},
      {"label": "Reputation", "value": "rising"},
      {"label": "Travel / Movement", "value": "favorable"},
      {"label": "Marriage", "value": "suitable to pursue"},
      {"label": "Misfortune", "value": "dissolves"},
      {"label": "Blessings", "value": "increase"},
      {"label": "Litigation", "value": "highly favorable"}
    ],
    "poem_title": "Fortune Poem",
    "poem_lines": [
      "Spring winds gradually replace winter's cold,",
      "Joyful energy fills the household gate.",
      "A newcomer arrives bearing good news,",
      "And what follows unfolds in harmony."
    ],
    "interpretation_title": "Interpretation",
    "interpretation_points": [
      "This is the highest category of fortune in temple divination. It is rare and unambiguous.",
      "This slip signals a clear transition from hardship to expansion. Not a warning. Not a test.",
      "The emphasis is on new people, new phase, and compounding good fortune, not sudden luck but sustained momentum."
    ]
  },
  
  "vietnamese": {
    "fortune_rating_title": "Thượng Thượng",
    "fortune_rating_subtitle": "(Rất tốt / Đại cát)",
    "sacred_meaning": [
      {"label": "Sức khỏe", "value": "sẽ bình an"},
      {"label": "Tài lộc", "value": "thu được nhiều"},
      {"label": "Danh tiếng", "value": "đang lên cao"},
      {"label": "Người đi xa / Di chuyển", "value": "thuận lợi"},
      {"label": "Hôn nhân", "value": "có thể hỏi (điềm tốt)"},
      {"label": "Tai họa", "value": "tiêu tan"},
      {"label": "Phúc lộc", "value": "tăng thêm"},
      {"label": "Kiện tụng", "value": "rất thích hợp"}
    ],
    "poem_title": "Bài thơ quẻ",
    "poem_lines": [
      "Gió xuân dần ấm, xua tan rét đông,",
      "Cảnh cửa nhà rực rỡ, khí vui dồi dào.",
      "Người mới bước vào mang theo tin tốt,",
      "Mọi việc về sau đều thuận hòa."
    ],
    "interpretation_title": "Ý nghĩa",
    "interpretation_points": [
      "Vận đã đổi chiều. Giai đoạn khó khăn đã qua. Từ suy sang thịnh, việc cũ khép lại, việc mới mở ra.",
      "Người mới mang cơ hội. Sẽ có người hoặc mối duyên mới xuất hiện, đem theo tin tốt hoặc mở nút thắt cũ.",
      "Phúc đến theo chuỗi. Làm đúng một bước sẽ kéo theo nhiều việc thuận lợi sau đó."
    ]
  }
}
```

---

## HTML Template Element Mapping Reference

| JSON Path | HTML Element/Class |
|-----------|-------------------|
| `stick_number` | `.stick-number` |
| `english.fortune_rating_title` | `.column-english .fortune-rating-title` |
| `english.fortune_rating_subtitle` | `.column-english .fortune-rating-subtitle` |
| `english.sacred_meaning[].label` | `.column-english .meaning-label` |
| `english.sacred_meaning[].value` | Text after `.meaning-label` |
| `english.poem_title` | `.column-english .poem-title` |
| `english.poem_lines[]` | `.column-english .poem-stanza` (join with newlines) |
| `english.interpretation_title` | `.column-english .section-title` (Interpretation section) |
| `english.interpretation_points[]` | `.column-english .interpretation-list li` |
| `vietnamese.fortune_rating_title` | `.column-vietnamese .fortune-rating-title` |
| `vietnamese.fortune_rating_subtitle` | `.column-vietnamese .fortune-rating-subtitle` |
| `vietnamese.sacred_meaning[].label` | `.column-vietnamese .meaning-label` |
| `vietnamese.sacred_meaning[].value` | Text after `.meaning-label` |
| `vietnamese.poem_title` | `.column-vietnamese .poem-title` |
| `vietnamese.poem_lines[]` | `.column-vietnamese .poem-stanza` (join with newlines) |
| `vietnamese.interpretation_title` | `.column-vietnamese .section-title` (Ý nghĩa section) |
| `vietnamese.interpretation_points[]` | `.column-vietnamese .interpretation-list li` |

---

## Batch Process

1. **Batch size:** 10 sticks per batch
2. **After each batch:** Present translations and wait for user confirmation
3. **Learn from feedback:** If user corrects something, apply that learning to future batches
4. **Track confirmations:** Note which translation choices have been confirmed so you don't re-ask

---

## When to Ask User

- OCR is unclear or ambiguous
- Discrepancy between your interpretation and web sources
- Translation choice that could go multiple ways
- Anything you're less than 90% confident about

**Do NOT guess.** Flag it and ask.

---

## Files Provided

1. **100 JPG images** - Named by stick number (e.g., 001.jpg, 065.jpg)
2. **divination-template.html** - Reference for final layout (Phase 2)

---

## Phase Summary

**Current Phase: Phase 1 - Translation**
- Translate all 100 sticks in batches of 10
- Get user confirmation after each batch
- Output: Structured translation data for all 100 sticks

**Future Phases (not yet):**
- Phase 2: Finalize template design
- Phase 3: Fit translations to final template
- Phase 4: Compile into single PDF

---

## Begin

Start with sticks #1-10. Present the translations in the format above, including any call-outs. Wait for user confirmation before proceeding to the next batch.
