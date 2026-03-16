# ModelIt! Print Materials Design System

**Version:** 1.0
**Effective Date:** March 14, 2026
**Status:** OFFICIAL — All new and existing materials must follow this system

---

## Overview

All ModelIt! printable classroom materials (Student Activity Packs, Teacher's Guides, Coloring Sheets, Interactive Notebooks, Reading Passages, Parent-Home Connections, Fix Activities, and Differentiated Readers) use this unified design system. Materials are generated as **HTML files** and printed/exported to **PDF** for pixel-perfect consistency across all devices and printers.

**Student Presentations (.pptx) remain as PowerPoint** files for teacher editability, but follow the same color palette and typography principles.

---

## Color Palette

### Primary Colors
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Purple Deep | `#4A3A7A` | 74, 58, 122 | Primary headers, section numbers, dark accents |
| Purple Brand | `#6B5B95` | 107, 91, 149 | Main brand color, table headers, badges |
| Purple Mid | `#8B7BB5` | 139, 123, 181 | Secondary accent, Teacher Guide doc badge |
| Purple Light | `#B8A9D4` | 184, 169, 212 | Borders, lines, response box outlines |
| Purple Pale | `#E8E0F0` | 232, 224, 240 | Subtle backgrounds, table row alternation |
| Purple BG | `#F5F0FA` | 245, 240, 250 | Section intro backgrounds, callout fills |

### Secondary Colors (Teal)
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Teal Brand | `#5BBFCF` | 91, 191, 207 | Section numbers, scenario cards, teal accents |
| Teal Mid | `#7ED4E0` | 126, 212, 224 | Lighter teal elements |
| Teal Light | `#B0E8EF` | 176, 232, 239 | Teal borders, sort column borders |
| Teal Pale | `#E0F5F8` | 224, 245, 248 | Teal background fills, observation boxes |

### Neutral Colors
| Name | Hex | Usage |
|------|-----|-------|
| Navy | `#1E1B4B` | Cover title text, STEM mission backgrounds |
| Dark Text | `#2D2A45` | Primary heading text |
| Body Text | `#3E3A55` | Body copy |
| Gray Text | `#6B6880` | Subtitles, footer text, metadata |
| White | `#FFFFFF` | Page backgrounds, text on dark |

### Semantic Colors
| Name | Hex | Usage |
|------|-----|-------|
| Green Positive | `#2ECC71` | (+) positive relationships, correct answers |
| Red Negative | `#E74C3C` | (-) negative relationships, misconceptions |
| Orange Accent | `#F39C12` | Highlights, career connections, watch-for boxes |
| Orange Light BG | `#FEF3E2` | Orange callout backgrounds |

---

## Typography

### Font Stack
- **Headings:** `'Quicksand', sans-serif` — weight 600-900
- **Body:** `'Nunito', 'Segoe UI', sans-serif` — weight 400-700
- **Google Fonts import:** `https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Quicksand:wght@400;500;600;700&display=swap`

### Type Scale
| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Cover Title | Quicksand | 32pt | 800 | Navy |
| Cover Subtitle | Nunito | 14pt | 400 | Gray Text |
| Page Section Title | Quicksand | 18pt | 700 | White (on header) |
| Interior H2 | Quicksand | 14pt | 800 | Purple Deep |
| Interior H3 | Quicksand | 11pt | 700 | Purple Brand |
| Body Text | Nunito | 11pt | 400 | Body Text |
| Question Text | Quicksand | 11pt | 700 | Purple Deep |
| Table Cell | Nunito | 10pt | 400 | Body Text |
| Table Header | Quicksand | 10pt | 700 | White |
| Footer | Nunito | 7-8pt | 400-700 | Gray Text |
| Callout Title | Quicksand | 11pt | 800 | Varies by type |
| Badge/Chip | Quicksand | 9-10pt | 700 | Varies |

---

## Page Structure

### Page Size
- **US Letter:** 8.5" × 11"
- **Margins:** 0.5" all sides (CSS `@page`)
- **Content padding:** 0.5" horizontal, 0.3" vertical (inside page)

### Cover Page Layout
1. **Header band** — Full-width gradient (purple-deep → purple-brand → teal-brand at 135°)
   - Decorative bubbles (5-6 circles, `rgba(255,255,255,0.08)`)
   - ModelIt! logo (orbital rings icon + "ModelIt!" in Quicksand 28pt white)
   - Document type badge (teal rounded pill for Student, purple-mid for Teacher)
   - Curved bottom edge (CSS pseudo-element with border-radius)
2. **Body** — Centered vertically
   - Lesson title (32pt)
   - Subtitle (14pt)
   - Meta badges row (grade, NGSS standard, crosscutting concept)
   - Name/Date fields (Student packs) or Quick Reference card (Teacher guides)
3. **Footer band** — Purple pale background
   - "ModelIt! — Discovery Collective" left
   - Copyright right

### Interior Page Layout
1. **Page header** — Gradient band (purple-deep → purple-brand)
   - Decorative bubbles (2-3 small circles)
   - Section number (teal circle, 40px)
   - Section title (Quicksand 18pt white)
   - "ModelIt!" mini logo (right side, semi-transparent)
   - Curved bottom edge
2. **Content area** — White background, padded
3. **Page footer** — Fixed bottom
   - "ModelIt!" logo text (left)
   - Lesson ID + document type (center)
   - Page number (right)
   - 3px gradient bar at very bottom (purple → teal)

---

## Component Library

### Section Intro Callout
- Purple BG background
- 4px purple-brand left border
- Border-radius: 0 12px 12px 0
- Used at top of each section

### Question Block
- Numbered circle (purple-brand, 22px, white text)
- Question text in Quicksand 11pt bold
- Response area below (lined or boxed)

### Response Box
- 2px purple-light border
- Border-radius: 10px
- Min-height: 60px (standard), 90px (tall), 45px (short)

### Response Lines
- Repeating gradient for ruled lines (24px spacing)
- 2px purple-light border
- Border-radius: 10px

### Styled Table (Purple variant)
- 2px purple-light border, 10px border-radius
- Header: purple-brand background, white text
- Alternating rows: white / purple-bg

### Styled Table (Teal variant)
- Same structure, teal colors

### Scenario Card
- 2px teal-brand border, 14px border-radius
- Header: teal gradient background
- Scenario icon (numbered circle)
- Instruction box (teal-pale background)
- Predict/Observe two-column layout

### Callout Box (3 variants)
- **Purple:** purple-bg fill, purple-light border
- **Teal:** teal-pale fill, teal-light border
- **Orange:** orange-light fill, gold border

### Sorting Columns
- Two-column layout with dashed drop zones
- External = teal, Internal = purple

### STEM Mission Box
- Navy-to-purple-deep gradient
- White text, teal accent title
- Decorative circle overlay

### Teacher-Specific Components
- **Teacher Tip:** Purple BG, purple left border
- **Teacher Script:** Teal pale, teal left border, italic
- **Watch For:** Orange light, orange left border
- **Answer Key Box:** Navy-to-purple gradient, white text, teal heading
- **Misconception Row:** Red left (wrong) / Green right (correct) split
- **Differentiation Cards:** 2×2 grid, color-coded by level

---

## Document Type Specifications

### Student Activity Pack
- **Cover badge:** Teal
- **Header gradient:** Purple-deep → Purple-brand → Teal-brand
- **Sections:** Pre-Assessment, Rubric, Component Analysis, Model Recording, Simulation Observations, Research & Extend, Reflection, STEM Challenge
- **Footer:** "G05-L01 • Student Activity Pack"

### Teacher's Guide
- **Cover badge:** Purple-mid
- **Header gradient:** Navy → Purple-deep (darker tone)
- **Cover:** Includes Quick Reference card (not name/date)
- **Sections:** NGSS Unpacking, Background Knowledge, LEVER Framework, Slide Facilitation, Answer Key, STEM Guidance, Differentiation, Misconceptions
- **Footer:** "G05-L01 • Teacher's Guide"

### K-3 Coloring Sheet
- **Simpler header** (no section number)
- **Large SVG illustration** (outlined, no fill — for coloring)
- **Instructions box** at bottom
- **Badge:** "Activity Page"

### K-3 Activity Pages (Word Search, Matching, etc.)
- Same header system
- **Badge:** "Puzzle Page" or "Activity Page"
- Adapted typography for younger readers (slightly larger)

### Interactive Notebook
- **Badge:** "Interactive Notebook"
- Draw/write areas with dashed borders
- Vocabulary tables
- "What I Learned" reflection area

### Reading Passage
- **Badge:** "Reading Passage"
- Large illustration area
- Picture-driven narrative
- Comprehension questions

### Parent-Home Connection
- **Badge:** "Family Activity"
- "Dear Family" intro
- Activity grid layout
- Take-home suggestions

### Differentiated Reader
- **Badge shows level:** "Grade Level" / "Advanced" / "Below Level" / "ESL-Assisted"
- Same header system
- Adapted font sizes per reading level

### Student Presentation (.pptx)
- **Stays as PowerPoint** — teachers need to edit
- Apply same color palette (purple-deep, purple-brand, teal-brand)
- Same diagonal corner design elements
- ModelIt! logo in consistent position
- Quicksand font for headers (embedded or substituted)

---

## Print / Export Guidelines

1. **Generate as HTML** with embedded CSS (no external stylesheets)
2. **Export to PDF** via browser Print → Save as PDF (or headless Chrome/Puppeteer)
3. **CSS @page rules** enforce letter size and margins
4. **page-break-after: always** between pages
5. **No background colors lost:** Enable "Background graphics" in print settings
6. All fonts loaded from Google Fonts CDN (works offline once cached)

---

## File Naming Convention

```
{GRADE}-{LESSON}-Student-Activity-Pack.html → .pdf
{GRADE}-{LESSON}-Teachers-Guide.html → .pdf
{GRADE}-{LESSON}-Coloring-Sheet.html → .pdf
{GRADE}-{LESSON}-Word-Search.html → .pdf
{GRADE}-{LESSON}-Vocabulary-Match.html → .pdf
{GRADE}-{LESSON}-Interactive-Notebook.html → .pdf
{GRADE}-{LESSON}-Reading-Passage.html → .pdf
{GRADE}-{LESSON}-Parent-Home-Connection.html → .pdf
{GRADE}-{LESSON}-Fix-Activity.html → .pdf
{GRADE}-{LESSON}-Reader-{Level}.html → .pdf
{GRADE}-{LESSON}-Student-Presentation.pptx (unchanged)
```

---

## Generator Script

The master generator script reads lesson data from Python data files and outputs branded HTML files using this design system. Located at:

```
~/cast-science-resources/scripts/create_branded_materials.py
```

The script uses Jinja2-style string templates with the full CSS design system embedded.
