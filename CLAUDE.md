# ModelIt! CAST Science Resources — Claude Code Instructions

## Repository Overview
This repository contains all ModelIt! K-12 lesson materials, generation scripts, and supporting assets for Discovery Collective's computational modeling curriculum.

## CRITICAL: Material Branding Protocol (Effective March 14, 2026)

**ALL printable classroom materials MUST use the official ModelIt! Design System.** This is non-negotiable for any new or updated materials.

### Design System Location
- **Full specification:** `design-prototypes/DESIGN-SYSTEM.md`
- **Prototype examples:** `design-prototypes/` folder (student-activity-pack.html, teachers-guide.html, coloring-activity-page.html)

### Format Rules
| Material Type | Format | Editable? |
|---|---|---|
| Student Activity Packs | HTML → PDF | No (print-ready) |
| Teacher's Guides | HTML → PDF | No (print-ready) |
| Coloring Sheets | HTML → PDF | No (print-ready) |
| Activity Pages (word search, matching, etc.) | HTML → PDF | No (print-ready) |
| Interactive Notebooks | HTML → PDF | No (print-ready) |
| Reading Passages | HTML → PDF | No (print-ready) |
| Parent-Home Connections | HTML → PDF | No (print-ready) |
| Fix the System Activities | HTML → PDF | No (print-ready) |
| Differentiated Readers | HTML → PDF | No (print-ready) |
| **Student Presentations** | **.pptx** | **Yes — teachers must be able to edit** |

### Why HTML → PDF (Not Word .docx)
Word documents have inconsistent rendering across machines — spacing shifts, fonts substitute, pagination breaks differently. HTML/CSS gives pixel-perfect control that prints identically everywhere. All printable materials are generated as HTML with embedded CSS and exported to PDF.

### Color Palette (Quick Reference)
```
Purple Deep:    #4A3A7A  (headers, dark accents)
Purple Brand:   #6B5B95  (main brand, table headers)
Purple Light:   #B8A9D4  (borders, response boxes)
Purple Pale:    #E8E0F0  (backgrounds, alternating rows)
Purple BG:      #F5F0FA  (section intros, callouts)
Teal Brand:     #5BBFCF  (section numbers, scenario cards)
Teal Pale:      #E0F5F8  (teal backgrounds)
Navy:           #1E1B4B  (cover titles, STEM missions)
Green (+):      #2ECC71  (positive relationships)
Red (-):        #E74C3C  (negative relationships)
Orange:         #F39C12  (career connections, watch-for)
```

### Typography
- **Headings:** Quicksand (Google Fonts) — weight 600-900
- **Body:** Nunito (Google Fonts) — weight 400-700
- Import: `https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Quicksand:wght@400;500;600;700&display=swap`

### Page Structure Requirements
Every printable page MUST have:
1. **Header band** — Purple gradient with decorative bubbles, section number (teal circle), section title, "ModelIt!" mini logo
2. **Content area** — White background, consistent padding
3. **Footer** — "ModelIt!" logo, lesson ID, page number, gradient bottom bar (purple → teal)
4. **Cover page** — Full gradient header, lesson title, meta badges, name/date (student) or quick ref (teacher)

### When Creating ANY New Materials
1. Reference the prototype HTML files in `design-prototypes/` for the exact CSS
2. Use the design system colors, fonts, and component patterns
3. Generate as HTML with embedded styles (no external CSS files)
4. Ensure print-ready with `@page` rules and `page-break-after`
5. Test by opening in browser and using Print → Save as PDF
6. PowerPoints use the same color palette but stay as .pptx

## Lesson Data Structure
- Lesson data files: `scripts/lesson_data_*.py`
- Each contains dictionaries with lesson content (titles, components, relationships, scenarios, questions, etc.)
- The generator scripts read this data and produce formatted materials

## Key Scripts
| Script | Purpose |
|--------|---------|
| `scripts/create_lesson_materials.py` | Original DOCX/PPTX generator (legacy) |
| `scripts/create_branded_materials.py` | **NEW** HTML/PDF branded generator |
| `scripts/create_supplementary_K3.py` | K-3 supplementary materials |
| `scripts/create_all_lessons_*.py` | Batch generators per grade |
| `scripts/create_reader.py` | Differentiated readers |

## Three Required Documents Per Lesson (All Grades)
1. **Student Presentation** (.pptx — 9 slides, branded with ModelIt! palette)
2. **Student Activity Pack** (HTML → PDF — Pre-Assessment, Rubric, Component Analysis, Model Sketch, Simulation Observations, Research & Extend, Reflection, STEM Challenge)
3. **Teacher's Guide** (HTML → PDF — NGSS Unpacking, CAST Alignment, Background Content, LEVER Framework, Slide-by-Slide Facilitation, Answer Key, STEM Guidance, Differentiation, Misconceptions)

## K-3 Additional Materials
- **K-2:** Coloring Sheets + Model Explorer Games (HTML interactive)
- **G2-3:** Fix Activities + Interactive Notebooks + Reading Passages + Parent-Home Connections

## Directory Structure
```
materials/
├── grade-K/          (10 lessons)
├── grade-01/         (10 lessons)
├── grade-02/         (10 lessons)
├── grade-03/         (10 lessons)
├── grade-04/         (10 lessons)
├── grade-05/         (10 lessons, G05-L01 = exemplar)
├── grade-06/         (10 lessons)
├── grade-07/         (10 lessons)
├── grade-08/         (10 lessons)
├── grade-09/         (10 lessons × 3 levels)
├── grade-10/         (10 lessons × 3 levels)
├── grade-11/         (10 lessons × 3 levels)
├── grade-12/         (10 lessons × 3 levels)
└── natures-engineers/ (10 lessons)

design-prototypes/    (brand reference — DO NOT DELETE)
├── DESIGN-SYSTEM.md
├── student-activity-pack.html
├── teachers-guide.html
└── coloring-activity-page.html
```

## Branding Rules (from main CLAUDE.md)
- ModelIt! parent company = **Discovery Collective**
- NEVER place TRPEC branding in ModelIt! materials
- Cell Collective powers ModelIt — NOT a competitor
- CAST = California Assessment of Student Performance and Progress (test name only)
