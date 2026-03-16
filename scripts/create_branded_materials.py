#!/usr/bin/env python3
"""
ModelIt! Branded Materials Generator
=====================================
Generates print-ready HTML files using the official ModelIt! Design System.
All printable materials (Student Activity Packs, Teacher's Guides, Coloring Sheets,
Activity Pages, etc.) are generated as HTML with embedded CSS for pixel-perfect
PDF export.

Usage:
    python create_branded_materials.py --grade 05 --lesson 01
    python create_branded_materials.py --grade 05 --all
    python create_branded_materials.py --grade 05 --lesson 01 --type student
    python create_branded_materials.py --grade 05 --lesson 01 --type teacher

Design System: design-prototypes/DESIGN-SYSTEM.md
"""

import argparse
import os
import sys
import importlib.util

# ============================================================
# DESIGN SYSTEM CSS — The complete branded stylesheet
# ============================================================

DESIGN_SYSTEM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Quicksand:wght@400;500;600;700&display=swap');

:root {
  --purple-deep: #4A3A7A;
  --purple-brand: #6B5B95;
  --purple-mid: #8B7BB5;
  --purple-light: #B8A9D4;
  --purple-pale: #E8E0F0;
  --purple-bg: #F5F0FA;
  --teal-brand: #5BBFCF;
  --teal-mid: #7ED4E0;
  --teal-light: #B0E8EF;
  --teal-pale: #E0F5F8;
  --navy: #1E1B4B;
  --dark-text: #2D2A45;
  --body-text: #3E3A55;
  --gray-text: #6B6880;
  --white: #FFFFFF;
  --green-pos: #2ECC71;
  --red-neg: #E74C3C;
  --orange-accent: #F39C12;
  --orange-light: #FEF3E2;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

@page { size: letter; margin: 0.5in; }

@media print {
  body { margin: 0; padding: 0; background: white; }
  .page { page-break-after: always; box-shadow: none !important; margin: 0 !important; border-radius: 0 !important; }
  .page:last-child { page-break-after: avoid; }
}

body {
  font-family: 'Nunito', 'Segoe UI', sans-serif;
  color: var(--body-text);
  background: #E8E0F0;
  line-height: 1.5;
  font-size: 11pt;
}

.page {
  width: 8.5in;
  min-height: 11in;
  margin: 20px auto;
  background: white;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(74,58,122,0.15);
  border-radius: 4px;
}

/* ===== COVER PAGE ===== */
.cover-page { display: flex; flex-direction: column; height: 11in; }

.cover-header {
  background: linear-gradient(135deg, var(--purple-deep) 0%, var(--purple-brand) 50%, var(--teal-brand) 100%);
  padding: 0.6in 0.6in 0.5in;
  position: relative;
  flex: 0 0 auto;
}
.cover-header.teacher-variant {
  background: linear-gradient(135deg, var(--navy) 0%, var(--purple-deep) 40%, var(--purple-brand) 100%);
}
.cover-header::after {
  content: '';
  position: absolute;
  bottom: -30px; left: 0; right: 0;
  height: 60px; background: white;
  border-radius: 50% 50% 0 0 / 100% 100% 0 0;
}

.cover-bubbles { position: absolute; top: 0; left: 0; right: 0; bottom: 0; overflow: hidden; pointer-events: none; }
.cover-bubbles .bubble { position: absolute; border-radius: 50%; background: rgba(255,255,255,0.08); }
.cover-bubbles .b1 { width: 120px; height: 120px; top: -20px; right: 60px; }
.cover-bubbles .b2 { width: 80px; height: 80px; top: 30px; right: 180px; }
.cover-bubbles .b3 { width: 60px; height: 60px; bottom: 40px; left: 40px; }
.cover-bubbles .b4 { width: 40px; height: 40px; top: 15px; left: 120px; }
.cover-bubbles .b5 { width: 90px; height: 90px; bottom: 10px; right: 20px; }

.cover-logo { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; position: relative; z-index: 2; }
.logo-text { font-family: 'Quicksand', sans-serif; font-size: 28pt; font-weight: 700; color: white; letter-spacing: 1px; }

.cover-doc-type {
  background: var(--teal-brand); color: white;
  font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 13pt;
  padding: 6px 24px; border-radius: 20px; display: inline-block;
  position: relative; z-index: 2; letter-spacing: 0.5px;
}
.cover-doc-type.teacher { background: var(--purple-mid); }

.cover-body { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 0.4in 0.7in; text-align: center; }
.cover-title { font-family: 'Quicksand', sans-serif; font-size: 32pt; font-weight: 800; color: var(--navy); line-height: 1.2; margin-bottom: 12px; }
.cover-subtitle { font-size: 14pt; color: var(--gray-text); font-weight: 400; margin-bottom: 30px; line-height: 1.4; }

.cover-meta-row { display: flex; justify-content: center; gap: 16px; margin-bottom: 24px; flex-wrap: wrap; }
.cover-badge { display: inline-flex; align-items: center; gap: 6px; background: var(--purple-pale); color: var(--purple-deep); padding: 6px 16px; border-radius: 20px; font-size: 10pt; font-weight: 700; }
.cover-badge.teal { background: var(--teal-pale); color: #2A8A96; }

.cover-name-block { margin-top: 20px; display: flex; justify-content: center; gap: 30px; }
.cover-field { text-align: left; }
.cover-field label { font-size: 9pt; font-weight: 700; color: var(--purple-brand); text-transform: uppercase; letter-spacing: 1px; }
.cover-field .line { width: 200px; border-bottom: 2px solid var(--purple-light); margin-top: 4px; height: 24px; }

.cover-quick-ref { background: var(--purple-bg); border-radius: 14px; padding: 18px 24px; text-align: left; max-width: 500px; margin: 0 auto; border: 2px solid var(--purple-light); }
.cover-quick-ref h3 { font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 12pt; color: var(--purple-deep); margin-bottom: 10px; text-align: center; }
.qr-row { display: flex; padding: 4px 0; border-bottom: 1px solid var(--purple-pale); font-size: 9.5pt; }
.qr-row:last-child { border-bottom: none; }
.qr-label { font-weight: 700; color: var(--purple-brand); width: 110px; flex-shrink: 0; }
.qr-value { color: var(--dark-text); }

.cover-footer { background: var(--purple-pale); padding: 14px 0.6in; display: flex; justify-content: space-between; align-items: center; font-size: 8pt; color: var(--gray-text); }
.cover-footer.teacher { background: var(--navy); color: rgba(255,255,255,0.5); }
.cover-footer-logo { font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 10pt; color: var(--purple-brand); }
.cover-footer.teacher .cover-footer-logo { color: var(--teal-brand); }

/* ===== INTERIOR PAGES ===== */
.page-header {
  background: linear-gradient(135deg, var(--purple-deep) 0%, var(--purple-brand) 100%);
  padding: 16px 0.5in 14px;
  display: flex; justify-content: space-between; align-items: center;
  position: relative;
}
.page-header.teacher-variant { background: linear-gradient(135deg, var(--navy) 0%, var(--purple-deep) 100%); }
.page-header::after { content: ''; position: absolute; bottom: -12px; left: 0; right: 0; height: 24px; background: white; border-radius: 50% 50% 0 0 / 100% 100% 0 0; }

.page-header-bubbles { position: absolute; top: 0; left: 0; right: 0; bottom: 0; overflow: hidden; pointer-events: none; }
.page-header-bubbles .hb { position: absolute; border-radius: 50%; background: rgba(255,255,255,0.06); }
.page-header-bubbles .hb1 { width: 50px; height: 50px; top: -10px; right: 80px; }
.page-header-bubbles .hb2 { width: 30px; height: 30px; top: 5px; right: 160px; }
.page-header-bubbles .hb3 { width: 40px; height: 40px; bottom: -5px; left: 100px; }

.section-number { background: var(--teal-brand); color: white; font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 16pt; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; position: relative; z-index: 2; flex-shrink: 0; }
.section-title { font-family: 'Quicksand', sans-serif; font-size: 18pt; font-weight: 700; color: white; position: relative; z-index: 2; flex: 1; margin-left: 14px; }
.page-logo-mini { font-family: 'Quicksand', sans-serif; font-size: 10pt; font-weight: 700; color: rgba(255,255,255,0.6); position: relative; z-index: 2; }

.page-content { padding: 0.3in 0.55in 0.4in; }

/* Section intro */
.section-intro { background: var(--purple-bg); border-left: 4px solid var(--purple-brand); border-radius: 0 12px 12px 0; padding: 14px 18px; margin-bottom: 20px; font-size: 11pt; color: var(--dark-text); line-height: 1.6; }

/* Questions */
.question-block { margin-bottom: 18px; }
.question-label { font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 11pt; color: var(--purple-deep); margin-bottom: 6px; display: flex; align-items: flex-start; gap: 8px; }
.q-number { background: var(--purple-brand); color: white; font-size: 9pt; font-weight: 800; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 1px; }

.response-box { border: 2px solid var(--purple-light); border-radius: 10px; min-height: 60px; padding: 8px 12px; background: var(--white); }
.response-box.tall { min-height: 90px; }
.response-box.short { min-height: 45px; }

.response-lines { border: none; background: repeating-linear-gradient(transparent, transparent 23px, var(--purple-pale) 23px, var(--purple-pale) 24px); min-height: 72px; border-radius: 10px; border: 2px solid var(--purple-light); padding: 4px 12px; }
.response-lines.tall { min-height: 108px; }
.response-lines.short { min-height: 50px; }

/* Tables */
.styled-table { width: 100%; border-collapse: separate; border-spacing: 0; border-radius: 10px; overflow: hidden; margin-bottom: 16px; border: 2px solid var(--purple-light); }
.styled-table th { background: var(--purple-brand); color: white; font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 10pt; padding: 10px 14px; text-align: left; }
.styled-table td { padding: 10px 14px; border-bottom: 1px solid var(--purple-pale); font-size: 10pt; vertical-align: top; }
.styled-table tr:nth-child(even) td { background: var(--purple-bg); }
.styled-table tr:last-child td { border-bottom: none; }

/* Rubric */
.rubric-table { width: 100%; border-collapse: separate; border-spacing: 0; border-radius: 10px; overflow: hidden; border: 2px solid var(--purple-light); font-size: 8.5pt; margin-bottom: 16px; }
.rubric-table th { background: var(--purple-brand); color: white; font-family: 'Quicksand', sans-serif; font-weight: 700; padding: 8px 10px; text-align: center; }
.rubric-table th:first-child { text-align: left; }
.rubric-table td { padding: 8px 10px; border-bottom: 1px solid var(--purple-pale); border-right: 1px solid var(--purple-pale); vertical-align: top; line-height: 1.4; }
.rubric-table td:last-child { border-right: none; }
.rubric-table tr:last-child td { border-bottom: none; }
.rubric-table td:first-child { font-family: 'Quicksand', sans-serif; font-weight: 700; color: var(--purple-deep); background: var(--purple-pale); width: 18%; }
.rubric-level { font-size: 7pt; font-weight: 700; color: var(--teal-brand); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 2px; }

/* Scenario cards */
.scenario-card { border: 2px solid var(--teal-brand); border-radius: 14px; margin-bottom: 18px; overflow: hidden; }
.scenario-header { background: linear-gradient(135deg, var(--teal-brand) 0%, #4AA8B8 100%); color: white; padding: 10px 16px; font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 12pt; display: flex; align-items: center; gap: 10px; }
.scenario-icon { width: 30px; height: 30px; background: rgba(255,255,255,0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14pt; }
.scenario-body { padding: 14px 16px; }
.scenario-instruction { background: var(--teal-pale); padding: 8px 14px; border-radius: 8px; margin-bottom: 12px; font-size: 10pt; color: #2A8A96; font-weight: 600; }
.predict-observe { display: flex; gap: 12px; }
.predict-observe > div { flex: 1; }
.po-label { font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 9pt; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; padding-left: 2px; }
.po-label.predict { color: var(--purple-brand); }
.po-label.observe { color: var(--teal-brand); }
.po-box { border-radius: 8px; min-height: 55px; padding: 6px 10px; border: 2px solid; }
.po-box.predict { border-color: var(--purple-light); background: var(--purple-bg); }
.po-box.observe { border-color: var(--teal-light); background: var(--teal-pale); }

/* Callouts */
.callout { border-radius: 12px; padding: 14px 18px; margin-bottom: 16px; }
.callout.purple { background: var(--purple-bg); border: 2px solid var(--purple-light); }
.callout.teal { background: var(--teal-pale); border: 2px solid var(--teal-light); }
.callout.orange { background: var(--orange-light); border: 2px solid #F5D89A; }
.callout-title { font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 11pt; margin-bottom: 6px; }
.callout.purple .callout-title { color: var(--purple-deep); }
.callout.teal .callout-title { color: #2A8A96; }
.callout.orange .callout-title { color: #B8860B; }

/* Sorting */
.sort-columns { display: flex; gap: 14px; margin-bottom: 16px; }
.sort-col { flex: 1; border: 2px solid; border-radius: 12px; overflow: hidden; }
.sort-col.external { border-color: var(--teal-brand); }
.sort-col.internal { border-color: var(--purple-brand); }
.sort-col-header { padding: 8px 14px; font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 11pt; color: white; text-align: center; }
.sort-col.external .sort-col-header { background: var(--teal-brand); }
.sort-col.internal .sort-col-header { background: var(--purple-brand); }
.sort-col-body { padding: 12px; min-height: 100px; }
.sort-item-slot { border: 2px dashed; border-radius: 8px; height: 30px; margin-bottom: 8px; }
.sort-col.external .sort-item-slot { border-color: var(--teal-light); }
.sort-col.internal .sort-item-slot { border-color: var(--purple-light); }

/* Relationship key */
.rel-key { display: flex; gap: 20px; margin-bottom: 14px; }
.rel-key-item { display: flex; align-items: center; gap: 8px; font-size: 10pt; }
.rel-symbol { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 14pt; color: white; }
.rel-symbol.pos { background: var(--green-pos); }
.rel-symbol.neg { background: var(--red-neg); }

/* Sketch area */
.sketch-area { border: 2px solid var(--purple-light); border-radius: 14px; min-height: 220px; background: white; position: relative; margin-bottom: 14px; }
.sketch-area::after { content: 'Draw your model here'; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--purple-light); font-size: 12pt; font-family: 'Quicksand', sans-serif; font-weight: 600; }

/* Component chips */
.component-chips { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 14px; }
.chip { padding: 5px 14px; border-radius: 20px; font-size: 9pt; font-weight: 700; font-family: 'Quicksand', sans-serif; }
.chip.purple { background: var(--purple-pale); color: var(--purple-deep); }
.chip.teal { background: var(--teal-pale); color: #2A8A96; }

/* STEM Mission */
.stem-mission { background: linear-gradient(135deg, var(--navy) 0%, var(--purple-deep) 100%); border-radius: 14px; padding: 18px 22px; color: white; margin-bottom: 16px; position: relative; overflow: hidden; }
.stem-mission::before { content: ''; position: absolute; top: -20px; right: -20px; width: 100px; height: 100px; background: rgba(91,191,207,0.15); border-radius: 50%; }
.stem-mission-title { font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 14pt; color: var(--teal-brand); margin-bottom: 8px; }
.stem-mission p { font-size: 10pt; line-height: 1.6; color: rgba(255,255,255,0.9); }

/* Extension list */
.extension-list { list-style: none; margin-bottom: 14px; }
.extension-list li { padding: 8px 14px; margin-bottom: 6px; background: var(--purple-bg); border-radius: 8px; font-size: 10pt; }
.extension-list li strong { color: var(--purple-deep); font-family: 'Quicksand', sans-serif; }

/* Design grid */
.design-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px; }
.design-box { border: 2px solid var(--teal-light); border-radius: 10px; padding: 10px 14px; min-height: 60px; }
.design-box-label { font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 9pt; color: var(--teal-brand); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }

/* Map area */
.map-area { border: 2px solid var(--teal-brand); border-radius: 14px; height: 200px; background: white; position: relative; margin-bottom: 14px; overflow: hidden; }
.map-area .map-label { position: absolute; top: 8px; left: 12px; font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 9pt; color: var(--teal-brand); text-transform: uppercase; letter-spacing: 1px; }
.map-area .compass { position: absolute; top: 8px; right: 12px; width: 30px; height: 30px; border: 2px solid var(--teal-light); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 9pt; font-weight: 700; color: var(--teal-brand); }

/* Interior headings */
h2.interior-heading { font-family: 'Quicksand', sans-serif; font-size: 14pt; font-weight: 800; color: var(--purple-deep); margin-bottom: 10px; padding-bottom: 4px; border-bottom: 2px solid var(--purple-pale); }
h3.sub-heading { font-family: 'Quicksand', sans-serif; font-size: 11pt; font-weight: 700; color: var(--purple-brand); margin-bottom: 6px; margin-top: 12px; }

/* TOC */
.toc-list { list-style: none; counter-reset: toc-counter; }
.toc-list li { counter-increment: toc-counter; display: flex; align-items: center; padding: 10px 0; border-bottom: 1px dashed var(--purple-pale); font-size: 11pt; }
.toc-list li::before { content: counter(toc-counter); background: var(--purple-brand); color: white; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 10pt; margin-right: 14px; flex-shrink: 0; }
.toc-list li:nth-child(even)::before { background: var(--teal-brand); }
.toc-list li .toc-dots { flex: 1; border-bottom: 1px dotted var(--purple-light); margin: 0 8px; height: 1px; align-self: flex-end; margin-bottom: 4px; }
.toc-list li .toc-page { font-weight: 700; color: var(--purple-brand); font-size: 10pt; }

/* Teacher-specific */
.teacher-tip { background: var(--purple-bg); border-left: 4px solid var(--purple-brand); border-radius: 0 10px 10px 0; padding: 12px 16px; margin-bottom: 14px; font-size: 9.5pt; }
.teacher-tip-title { font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 10pt; color: var(--purple-deep); margin-bottom: 4px; }
.teacher-script { background: var(--teal-pale); border-left: 4px solid var(--teal-brand); border-radius: 0 10px 10px 0; padding: 12px 16px; margin-bottom: 14px; font-size: 9.5pt; font-style: italic; color: #2A6A76; }
.teacher-script strong { color: #1A5A66; font-style: normal; }
.watch-for { background: var(--orange-light); border-left: 4px solid var(--orange-accent); border-radius: 0 10px 10px 0; padding: 12px 16px; margin-bottom: 14px; font-size: 9.5pt; }
.watch-for-title { font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 10pt; color: #B8860B; margin-bottom: 4px; }

/* NGSS table */
.ngss-table { width: 100%; border-collapse: separate; border-spacing: 0; border-radius: 10px; overflow: hidden; border: 2px solid var(--purple-light); margin-bottom: 14px; font-size: 9pt; }
.ngss-table th { background: var(--purple-brand); color: white; font-family: 'Quicksand', sans-serif; font-weight: 700; padding: 8px 12px; text-align: left; }
.ngss-table td { padding: 10px 12px; border-bottom: 1px solid var(--purple-pale); vertical-align: top; line-height: 1.5; }
.ngss-table tr:last-child td { border-bottom: none; }
.ngss-table td:first-child { font-family: 'Quicksand', sans-serif; font-weight: 700; color: var(--purple-deep); background: var(--purple-pale); width: 28%; }

/* Answer key */
.answer-key-box { background: linear-gradient(135deg, var(--navy) 0%, var(--purple-deep) 100%); border-radius: 12px; padding: 14px 18px; margin-bottom: 14px; color: white; }
.answer-key-box h4 { font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 11pt; color: var(--teal-brand); margin-bottom: 6px; }
.answer-key-box p, .answer-key-box li { font-size: 9pt; line-height: 1.6; color: rgba(255,255,255,0.9); }
.answer-key-box ul { margin-left: 16px; }

/* Differentiation */
.diff-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 14px; }
.diff-card { border-radius: 10px; padding: 12px 14px; border: 2px solid; font-size: 9pt; }
.diff-card.below { border-color: var(--teal-light); background: var(--teal-pale); }
.diff-card.advanced { border-color: var(--purple-light); background: var(--purple-bg); }
.diff-card.ell { border-color: #F5D89A; background: var(--orange-light); }
.diff-card.gifted { border-color: var(--teal-brand); background: white; }
.diff-card-title { font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 10pt; margin-bottom: 4px; }
.diff-card.below .diff-card-title { color: #2A8A96; }
.diff-card.advanced .diff-card-title { color: var(--purple-deep); }
.diff-card.ell .diff-card-title { color: #B8860B; }
.diff-card.gifted .diff-card-title { color: var(--teal-brand); }

/* Misconceptions */
.misconception-row { display: flex; gap: 0; margin-bottom: 10px; border-radius: 10px; overflow: hidden; border: 2px solid var(--purple-light); font-size: 9pt; }
.misconception-wrong { background: #FDE8E8; padding: 10px 14px; width: 45%; border-right: 2px solid var(--purple-light); }
.misconception-right { background: #E8F8E8; padding: 10px 14px; width: 55%; }
.misconception-label { font-family: 'Quicksand', sans-serif; font-weight: 800; font-size: 8pt; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px; }
.misconception-wrong .misconception-label { color: var(--red-neg); }
.misconception-right .misconception-label { color: var(--green-pos); }

/* LEVER framework */
.lever-step { display: flex; gap: 10px; margin-bottom: 10px; align-items: flex-start; }
.lever-letter { width: 36px; height: 36px; background: var(--purple-brand); color: white; font-family: 'Quicksand', sans-serif; font-weight: 900; font-size: 16pt; border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.lever-letter.teal { background: var(--teal-brand); }
.lever-desc { font-size: 9.5pt; }
.lever-desc strong { font-family: 'Quicksand', sans-serif; color: var(--purple-deep); display: block; font-size: 10pt; }

/* Slide facilitation */
.slide-card { border: 2px solid var(--purple-light); border-radius: 12px; margin-bottom: 14px; overflow: hidden; }
.slide-card-header { background: var(--purple-brand); color: white; padding: 8px 14px; font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 11pt; display: flex; justify-content: space-between; align-items: center; }
.slide-time { background: rgba(255,255,255,0.2); padding: 2px 10px; border-radius: 12px; font-size: 8pt; }
.slide-card-body { padding: 12px 14px; }

/* CAST questions */
.cast-question { background: var(--purple-bg); border: 2px solid var(--purple-light); border-radius: 10px; padding: 12px 16px; margin-bottom: 10px; font-size: 9pt; }
.cast-question-type { font-family: 'Quicksand', sans-serif; font-weight: 700; font-size: 8pt; color: var(--purple-brand); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }

/* Earth systems table */
.earth-systems-table { width: 100%; border-collapse: separate; border-spacing: 0; border-radius: 10px; overflow: hidden; border: 2px solid var(--teal-light); margin-bottom: 14px; font-size: 9pt; }
.earth-systems-table th { background: var(--teal-brand); color: white; font-family: 'Quicksand', sans-serif; font-weight: 700; padding: 8px 12px; text-align: left; }
.earth-systems-table td { padding: 8px 12px; border-bottom: 1px solid var(--teal-pale); vertical-align: top; }
.earth-systems-table tr:nth-child(even) td { background: var(--teal-pale); }
.earth-systems-table tr:last-child td { border-bottom: none; }

/* Page footer */
.page-footer { position: absolute; bottom: 0; left: 0; right: 0; padding: 8px 0.5in; display: flex; justify-content: space-between; align-items: center; font-size: 7pt; color: var(--gray-text); border-top: 1px solid var(--purple-pale); background: white; }
.page-footer .footer-logo { font-family: 'Quicksand', sans-serif; font-weight: 700; color: var(--purple-brand); font-size: 8pt; }
.page-footer .footer-bar { height: 3px; position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(90deg, var(--purple-brand), var(--teal-brand)); }
"""

# ============================================================
# HELPER: Common HTML fragments
# ============================================================

def bubbles_html():
    return '<div class="cover-bubbles"><div class="bubble b1"></div><div class="bubble b2"></div><div class="bubble b3"></div><div class="bubble b4"></div><div class="bubble b5"></div></div>'

def header_bubbles_html():
    return '<div class="page-header-bubbles"><div class="hb hb1"></div><div class="hb hb2"></div><div class="hb hb3"></div></div>'

def page_footer_html(lesson_id, doc_type, page_num):
    return f'''<div class="page-footer">
    <span class="footer-logo">ModelIt!</span>
    <span>{lesson_id} &bull; {doc_type}</span>
    <span>Page {page_num}</span>
    <div class="footer-bar"></div>
  </div>'''

def section_page_header(num, title, variant=""):
    cls = f' {variant}' if variant else ''
    return f'''<div class="page-header{cls}">
    {header_bubbles_html()}
    <div class="section-number">{num}</div>
    <div class="section-title">{title}</div>
    <div class="page-logo-mini">ModelIt!</div>
  </div>'''

def html_escape(text):
    """Escape HTML special characters."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ============================================================
# STUDENT ACTIVITY PACK GENERATOR
# ============================================================

def generate_student_activity_pack(data):
    """Generate the complete Student Activity Pack HTML from lesson data."""
    lesson_id = data["id"]
    title = html_escape(data["title"])
    subtitle = html_escape(data["subtitle"])
    ngss = data["ngss"]

    # Determine grade display
    grade_num = lesson_id.split("-")[0].replace("G", "").replace("K", "K")
    if grade_num == "K":
        grade_display = "Kindergarten"
    else:
        grade_display = f"Grade {int(grade_num)}" if grade_num.isdigit() else f"Grade {grade_num}"

    # Get crosscutting concept from dimensions if available
    cc = "Systems &amp; Models"
    if "dimensions" in data:
        for dim in data["dimensions"]:
            if "Crosscutting" in dim[0]:
                cc = html_escape(dim[1])
                break

    # Components
    components = data.get("components", [])
    external = [c for c in components if c[2]]  # is_external=True
    internal = [c for c in components if not c[2]]

    # Scenarios
    scenarios = data.get("sim_scenarios", data.get("scenarios", []))

    # Build component chips
    chips_html = ""
    for i, comp in enumerate(components):
        cls = "teal" if comp[2] else "purple"
        chips_html += f'<span class="chip {cls}">{html_escape(comp[0])}</span>'

    # Build sort slots
    ext_slots = ''.join(['<div class="sort-item-slot"></div>' for _ in external])
    int_slots = ''.join(['<div class="sort-item-slot"></div>' for _ in internal])

    # Pre-assessment questions
    pre_qs = data.get("pre_assessment", [
        f"What do you already know about {title.lower()}?",
        "What do you think causes this phenomenon?",
        "What is a model? How do scientists use models?",
        'What does it mean when we say things work as a "system"?'
    ])

    pre_q_html = ""
    for i, q in enumerate(pre_qs, 1):
        pre_q_html += f'''<div class="question-block">
      <div class="question-label"><span class="q-number">{i}</span><span>{html_escape(q)}</span></div>
      <div class="response-lines"></div>
    </div>'''

    # Scenario cards
    scenario_html = ""
    scenario_names = ["1", "2", "3"]
    for i, sc in enumerate(scenarios[:3]):
        sc_title = html_escape(sc[0]) if isinstance(sc, (list, tuple)) else html_escape(str(sc))
        sc_instruction = html_escape(sc[1]) if isinstance(sc, (list, tuple)) and len(sc) > 1 else ""
        sc_predict = html_escape(sc[2]) if isinstance(sc, (list, tuple)) and len(sc) > 2 else "What do you predict will happen?"

        scenario_html += f'''<div class="scenario-card">
      <div class="scenario-header"><div class="scenario-icon">{i+1}</div>Scenario {i+1}: {sc_title}</div>
      <div class="scenario-body">
        <div class="scenario-instruction">{sc_instruction}</div>
        <div class="predict-observe">
          <div><div class="po-label predict">My Prediction</div><div class="po-box predict"></div></div>
          <div><div class="po-label observe">What I Observed</div><div class="po-box observe"></div></div>
        </div>
      </div>
    </div>'''

    # Extension components
    extend_html = ""
    for ec in data.get("extend_components", []):
        name = html_escape(ec[0])
        desc = html_escape(ec[1])
        extend_html += f'<li><strong>{name}</strong> &mdash; {desc}</li>'

    # Reflection questions
    reflection_html = ""
    for i, q in enumerate(data.get("reflections", [])[:5], 1):
        reflection_html += f'''<div class="question-block">
      <div class="question-label"><span class="q-number">{i}</span><span>{html_escape(q)}</span></div>
      <div class="response-lines"></div>
    </div>'''

    # STEM Challenge
    stem_title = html_escape(data.get("stem_title", "STEM Challenge"))
    stem_mission = html_escape(data.get("stem_mission", "Apply what you learned to solve a real-world engineering problem."))
    stem_scenario = html_escape(data.get("stem_scenario", ""))
    stem_design_qs = data.get("stem_design_qs", data.get("stem_questions", []))

    design_boxes = ""
    for i, q in enumerate(stem_design_qs[:4], 1):
        design_boxes += f'<div class="design-box"><div class="design-box-label">{i}. {html_escape(q)}</div></div>'

    # Career connection
    career = html_escape(data.get("career", ""))

    # Assemble full HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ModelIt! Student Activity Pack &mdash; {lesson_id}</title>
<style>{DESIGN_SYSTEM_CSS}</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="page cover-page">
  <div class="cover-header">
    {bubbles_html()}
    <div class="cover-logo"><div class="logo-text">ModelIt!</div></div>
    <div class="cover-doc-type">Student Activity Pack</div>
  </div>
  <div class="cover-body">
    <div class="cover-title">{title}</div>
    <div class="cover-subtitle">{subtitle}</div>
    <div class="cover-meta-row">
      <div class="cover-badge">{grade_display}</div>
      <div class="cover-badge teal">NGSS {ngss}</div>
      <div class="cover-badge">{cc}</div>
    </div>
    <div class="cover-name-block">
      <div class="cover-field"><label>Student Name</label><div class="line"></div></div>
      <div class="cover-field"><label>Date</label><div class="line"></div></div>
    </div>
  </div>
  <div class="cover-footer">
    <div class="cover-footer-logo">ModelIt! &mdash; Discovery Collective</div>
    <div>&copy; 2026 Discovery Collective. All rights reserved.</div>
  </div>
</div>

<!-- TABLE OF CONTENTS -->
<div class="page" style="position:relative;">
  <div class="page-header">
    {header_bubbles_html()}
    <div style="display:flex;align-items:center;position:relative;z-index:2;">
      <div class="section-title" style="margin-left:0;">Table of Contents</div>
    </div>
    <div class="page-logo-mini">ModelIt!</div>
  </div>
  <div class="page-content" style="padding-top: 0.5in;">
    <ul class="toc-list">
      <li><span>Pre-Assessment</span><span class="toc-dots"></span><span class="toc-page">3</span></li>
      <li><span>Scoring Rubric</span><span class="toc-dots"></span><span class="toc-page">4</span></li>
      <li><span>Component Analysis</span><span class="toc-dots"></span><span class="toc-page">5</span></li>
      <li><span>Model Recording Page</span><span class="toc-dots"></span><span class="toc-page">6</span></li>
      <li><span>Simulation Observations</span><span class="toc-dots"></span><span class="toc-page">7</span></li>
      <li><span>Research &amp; Extend</span><span class="toc-dots"></span><span class="toc-page">8</span></li>
      <li><span>Reflection Questions</span><span class="toc-dots"></span><span class="toc-page">9</span></li>
      <li><span>STEM Challenge</span><span class="toc-dots"></span><span class="toc-page">10</span></li>
    </ul>
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 2)}
</div>

<!-- SECTION 1: PRE-ASSESSMENT -->
<div class="page" style="position:relative;">
  {section_page_header("1", "Pre-Assessment")}
  <div class="page-content">
    <div class="section-intro"><strong>What Do You Know?</strong> Answer each question below to the best of your ability. There are no wrong answers &mdash; this helps your teacher understand what you already know!</div>
    {pre_q_html}
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 3)}
</div>

<!-- SECTION 2: SCORING RUBRIC -->
<div class="page" style="position:relative;">
  {section_page_header("2", "Scoring Rubric")}
  <div class="page-content">
    <div class="section-intro">Your teacher will use this rubric to assess your work. Read through each level to understand what is expected!</div>
    <table class="rubric-table">
      <thead><tr><th>Skill</th><th>Expert (4)</th><th>Proficient (3)</th><th>Developing (2)</th><th>Beginning (1)</th></tr></thead>
      <tbody>
        <tr><td>Identifying Components</td><td><span class="rubric-level">Expert</span>Correctly identifies and sorts ALL components as internal or external with detailed reasoning</td><td><span class="rubric-level">Proficient</span>Correctly identifies and sorts MOST components with some reasoning</td><td><span class="rubric-level">Developing</span>Identifies components but has difficulty sorting or explaining</td><td><span class="rubric-level">Beginning</span>Needs significant help identifying components</td></tr>
        <tr><td>Establishing Relationships</td><td><span class="rubric-level">Expert</span>Accurately describes ALL positive and negative relationships with clear evidence</td><td><span class="rubric-level">Proficient</span>Accurately describes MOST relationships with some evidence</td><td><span class="rubric-level">Developing</span>Identifies some relationships but struggles with direction</td><td><span class="rubric-level">Beginning</span>Needs help understanding how components connect</td></tr>
        <tr><td>Running Simulations</td><td><span class="rubric-level">Expert</span>Makes accurate predictions AND explains surprising results using evidence</td><td><span class="rubric-level">Proficient</span>Makes reasonable predictions and records clear observations</td><td><span class="rubric-level">Developing</span>Runs simulations but predictions or observations are incomplete</td><td><span class="rubric-level">Beginning</span>Needs help running simulations or recording data</td></tr>
        <tr><td>Explaining Results</td><td><span class="rubric-level">Expert</span>Uses multiple pieces of evidence to explain HOW and WHY systems interact</td><td><span class="rubric-level">Proficient</span>Uses evidence to explain system interactions</td><td><span class="rubric-level">Developing</span>Gives partial explanations with limited evidence</td><td><span class="rubric-level">Beginning</span>Needs help connecting evidence to explanations</td></tr>
      </tbody>
    </table>
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 4)}
</div>

<!-- SECTION 3: COMPONENT ANALYSIS -->
<div class="page" style="position:relative;">
  {section_page_header("3", "Component Analysis")}
  <div class="page-content">
    <div class="callout teal">
      <div class="callout-title">What is a Component?</div>
      A <strong>component</strong> is a part of a system that plays a specific role. Components can be <strong>EXTERNAL</strong> (come from outside the system) or <strong>INTERNAL</strong> (happen within the system).
    </div>
    <h3 class="sub-heading">Sort These Components</h3>
    <div class="component-chips">{chips_html}</div>
    <div class="sort-columns">
      <div class="sort-col external"><div class="sort-col-header">EXTERNAL</div><div class="sort-col-body">{ext_slots}</div></div>
      <div class="sort-col internal"><div class="sort-col-header">INTERNAL</div><div class="sort-col-body">{int_slots}</div></div>
    </div>
    <div class="question-block">
      <div class="question-label"><span class="q-number">?</span><span>Explain your reasoning: Why did you sort each component the way you did?</span></div>
      <div class="response-lines tall"></div>
    </div>
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 5)}
</div>

<!-- SECTION 4: MODEL RECORDING -->
<div class="page" style="position:relative;">
  {section_page_header("4", "Model Recording Page")}
  <div class="page-content">
    <div class="section-intro">Draw your model showing all components and their relationships. Use the relationship key below to label your arrows!</div>
    <div class="rel-key">
      <div class="rel-key-item"><div class="rel-symbol pos">+</div><span><strong>POSITIVE:</strong> When A increases, B also increases</span></div>
      <div class="rel-key-item"><div class="rel-symbol neg">&minus;</div><span><strong>NEGATIVE:</strong> When A increases, B decreases</span></div>
    </div>
    <div class="sketch-area"></div>
    <div class="question-block">
      <div class="question-label"><span class="q-number">?</span><span>Explain ONE relationship in your model. What happens when one component changes?</span></div>
      <div class="response-lines tall"></div>
    </div>
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 6)}
</div>

<!-- SECTION 5: SIMULATION OBSERVATIONS -->
<div class="page" style="position:relative;">
  {section_page_header("5", "Simulation Observations")}
  <div class="page-content">
    <div class="section-intro">Run each scenario in ModelIt! First, write your <strong>prediction</strong>. Then run the simulation and record what you <strong>observe</strong>.</div>
    {scenario_html}
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 7)}
</div>

<!-- SECTION 6: RESEARCH & EXTEND -->
<div class="page" style="position:relative;">
  {section_page_header("6", "Research &amp; Extend")}
  <div class="page-content">
    <div class="section-intro">Real systems are more complex than our model! Here are additional components scientists study. Choose one and explain how it could connect to our model.</div>
    <h3 class="sub-heading">Possible New Components</h3>
    <ul class="extension-list">{extend_html}</ul>
    <h3 class="sub-heading">My Extension</h3>
    <div class="question-block"><div class="question-label"><span class="q-number">A</span><span>Which new component would you add to the model?</span></div><div class="response-box short"></div></div>
    <div class="question-block"><div class="question-label"><span class="q-number">B</span><span>How would it connect to the existing components? (Draw or describe)</span></div><div class="response-lines tall"></div></div>
    <div class="question-block"><div class="question-label"><span class="q-number">C</span><span>What evidence or reasoning supports your connection?</span></div><div class="response-lines"></div></div>
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 8)}
</div>

<!-- SECTION 7: REFLECTION -->
<div class="page" style="position:relative;">
  {section_page_header("7", "Reflection Questions")}
  <div class="page-content">
    <div class="callout purple">
      <div class="callout-title">The Big Question</div>
      <strong>{html_escape(data.get("big_question", ""))}</strong> Use evidence from your simulation to support your answers.
    </div>
    {reflection_html}
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 9)}
</div>

<!-- SECTION 8: STEM CHALLENGE -->
<div class="page" style="position:relative;">
  {section_page_header("8", f"STEM Challenge: {stem_title}")}
  <div class="page-content">
    <div class="stem-mission">
      <div class="stem-mission-title">YOUR ENGINEERING MISSION</div>
      <p>{stem_mission}</p>
    </div>
    {"<div class='callout orange'><div class='callout-title'>THE SCENARIO</div>" + stem_scenario + "</div>" if stem_scenario else ""}
    <h3 class="sub-heading">Engineering Design Thinking</h3>
    <div class="design-grid">{design_boxes}</div>
    <h3 class="sub-heading">My Design</h3>
    <div class="map-area"><div class="map-label">Design Area &mdash; Draw Your Solution</div><div class="compass">N</div></div>
    <div class="question-block">
      <div class="question-label"><span class="q-number">!</span><span>Explain your design using scientific evidence from the simulation:</span></div>
      <div class="response-lines tall"></div>
    </div>
    {"<div class='callout teal'><div class='callout-title'>Real Career Connection</div>" + career + "</div>" if career else ""}
  </div>
  {page_footer_html(lesson_id, "Student Activity Pack", 10)}
</div>

</body>
</html>'''

    return html


# ============================================================
# TEACHER'S GUIDE GENERATOR
# ============================================================

def generate_teachers_guide(data):
    """Generate the complete Teacher's Guide HTML from lesson data."""
    lesson_id = data["id"]
    title = html_escape(data["title"])
    subtitle = html_escape(data["subtitle"])
    ngss = data["ngss"]
    ngss_desc = html_escape(data.get("ngss_desc", ""))

    grade_num = lesson_id.split("-")[0].replace("G", "").replace("K", "K")
    if grade_num == "K":
        grade_display = "Kindergarten"
    else:
        grade_display = f"Grade {int(grade_num)}" if grade_num.isdigit() else f"Grade {grade_num}"

    # NGSS dimensions
    dimensions = data.get("dimensions", [])
    ngss_rows = ""
    for dim in dimensions:
        ngss_rows += f'<tr><td>{html_escape(dim[0])}</td><td><strong>{html_escape(dim[1])}</strong> &mdash; {html_escape(dim[2])}</td></tr>'

    # CAST questions
    cast_html = ""
    for cq in data.get("cast_questions", []):
        cast_html += f'<div class="cast-question"><div class="cast-question-type">{html_escape(cq[0])}</div>{html_escape(cq[1])}</div>'

    # Background sections
    bg_intro = html_escape(data.get("background_intro", ""))
    bg_sections = ""
    for section in data.get("background_sections", []):
        bg_sections += f'<h3 class="sub-heading">{html_escape(section[0])}</h3><p style="font-size:9.5pt; margin-bottom: 10px;">{html_escape(section[1])}</p>'

    # LEVER framework
    lever_html = ""
    lever_data = [
        ("L", data.get("lever_L", "Students identify the system components."), "Locate the System", ""),
        ("E", data.get("lever_E", "Students determine relationships between components."), "Establish Relationships", "teal"),
        ("V", data.get("lever_V", "Students build their model in ModelIt!"), "Visualize & Model", ""),
        ("E", data.get("lever_Ev", "Students run simulations and evaluate outcomes."), "Evaluate Outcomes", "teal"),
        ("R", data.get("lever_R", "Students revise and extend their models."), "Revise & Extend", ""),
    ]
    for letter, desc, label, cls in lever_data:
        teal_cls = f' {cls}' if cls else ''
        lever_html += f'''<div class="lever-step">
      <div class="lever-letter{teal_cls}">{letter}</div>
      <div class="lever-desc"><strong>{html_escape(label)}</strong>{html_escape(desc)}</div>
    </div>'''

    # Slide-by-slide facilitation
    slides_html = ""
    for slide in data.get("slides_guide", []):
        slides_html += f'''<div class="slide-card">
      <div class="slide-card-header"><span>{html_escape(slide.get("num", ""))}: {html_escape(slide.get("title", ""))}</span><span class="slide-time">{html_escape(slide.get("time", ""))}</span></div>
      <div class="slide-card-body">
        <div class="teacher-script"><strong>Say:</strong> &ldquo;{html_escape(slide.get("say", ""))}&rdquo;</div>
        <div class="watch-for"><div class="watch-for-title">Watch For</div>{html_escape(slide.get("do", ""))}</div>
      </div>
    </div>'''

    # Answer key - relationships
    answer_rels = ""
    for rel in data.get("relationships", []):
        answer_rels += f'<li><strong>{html_escape(rel[0])}:</strong> {html_escape(rel[1])} &mdash; {html_escape(rel[2])}</li>'

    # Answer key - discoveries
    answer_disc = ""
    for disc in data.get("discoveries", []):
        answer_disc += f'<li>{html_escape(disc)}</li>'

    # Misconceptions
    misconceptions_html = ""
    for mc in data.get("misconceptions", []):
        mc_wrong = html_escape(mc[0])
        mc_right = html_escape(mc[1])
        misconceptions_html += f'''<div class="misconception-row">
      <div class="misconception-wrong"><div class="misconception-label">Students May Think</div>&ldquo;{mc_wrong}&rdquo;</div>
      <div class="misconception-right"><div class="misconception-label">Scientific Understanding</div>{mc_right}</div>
    </div>'''

    # Components for answer key
    components = data.get("components", [])
    ext_names = ", ".join([c[0] for c in components if c[2]])
    int_names = ", ".join([c[0] for c in components if not c[2]])

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ModelIt! Teacher&#39;s Guide &mdash; {lesson_id}</title>
<style>{DESIGN_SYSTEM_CSS}</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="page cover-page">
  <div class="cover-header teacher-variant">
    {bubbles_html()}
    <div class="cover-logo"><div class="logo-text">ModelIt!</div></div>
    <div class="cover-doc-type teacher">Teacher&#39;s Guide</div>
  </div>
  <div class="cover-body">
    <div class="cover-title">{title}</div>
    <div class="cover-subtitle">{subtitle}</div>
    <div class="cover-quick-ref">
      <h3>Quick Reference</h3>
      <div class="qr-row"><span class="qr-label">Grade Level</span><span class="qr-value">{grade_display}</span></div>
      <div class="qr-row"><span class="qr-label">NGSS Standard</span><span class="qr-value">{ngss}</span></div>
      <div class="qr-row"><span class="qr-label">Time</span><span class="qr-value">45&ndash;60 minutes (core lesson)</span></div>
      <div class="qr-row"><span class="qr-label">Materials</span><span class="qr-value">Student Activity Pack, devices with ModelIt! access</span></div>
      <div class="qr-row"><span class="qr-label">Prep</span><span class="qr-value">Print activity packs, test ModelIt! on student devices</span></div>
      <div class="qr-row"><span class="qr-label">Grouping</span><span class="qr-value">Partners or small groups (2&ndash;4)</span></div>
    </div>
  </div>
  <div class="cover-footer teacher">
    <div class="cover-footer-logo">ModelIt! &mdash; Discovery Collective</div>
    <div>&copy; 2026 Discovery Collective. All rights reserved. For teacher use only.</div>
  </div>
</div>

<!-- TABLE OF CONTENTS -->
<div class="page" style="position:relative;">
  <div class="page-header teacher-variant">
    {header_bubbles_html()}
    <div style="display:flex;align-items:center;position:relative;z-index:2;">
      <div class="section-title" style="margin-left:0;">Table of Contents</div>
    </div>
    <div class="page-logo-mini">ModelIt!</div>
  </div>
  <div class="page-content" style="padding-top: 0.45in;">
    <ul class="toc-list">
      <li><span>NGSS Standards Unpacking &amp; CAST Alignment</span><span class="toc-dots"></span><span class="toc-page">3</span></li>
      <li><span>Scoring Rubric</span><span class="toc-dots"></span><span class="toc-page">4</span></li>
      <li><span>Background Content Knowledge</span><span class="toc-dots"></span><span class="toc-page">5</span></li>
      <li><span>The LEVER Framework</span><span class="toc-dots"></span><span class="toc-page">6</span></li>
      <li><span>Slide-by-Slide Facilitation Guide</span><span class="toc-dots"></span><span class="toc-page">7</span></li>
      <li><span>Answer Key &amp; Expected Responses</span><span class="toc-dots"></span><span class="toc-page">9</span></li>
      <li><span>Collaborative Learning Protocols</span><span class="toc-dots"></span><span class="toc-page">10</span></li>
      <li><span>Differentiation &amp; Extensions</span><span class="toc-dots"></span><span class="toc-page">11</span></li>
      <li><span>Common Misconceptions</span><span class="toc-dots"></span><span class="toc-page">12</span></li>
    </ul>
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 2)}
</div>

<!-- SECTION 1: NGSS UNPACKING -->
<div class="page" style="position:relative;">
  {section_page_header("1", "NGSS Standards &amp; CAST Alignment", "teacher-variant")}
  <div class="page-content">
    <div class="teacher-tip"><div class="teacher-tip-title">Performance Expectation: {ngss}</div>{ngss_desc}</div>
    <h2 class="interior-heading">Three-Dimensional Learning</h2>
    <table class="ngss-table">{ngss_rows}</table>
    <h2 class="interior-heading">CAST Testing Alignment</h2>
    {cast_html}
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 3)}
</div>

<!-- SECTION 2: SCORING RUBRIC (Teacher Reference) -->
<div class="page" style="position:relative;">
  {section_page_header("2", "Scoring Rubric", "teacher-variant")}
  <div class="page-content">
    <div class="teacher-tip"><div class="teacher-tip-title">Assessment Reference</div>This is the same rubric students see in their Activity Pack. Use it during and after the lesson for formative and summative assessment. Circle or highlight the proficiency level for each skill.</div>
    <table class="rubric-table">
      <thead><tr><th>Skill</th><th>Expert (4)</th><th>Proficient (3)</th><th>Developing (2)</th><th>Beginning (1)</th></tr></thead>
      <tbody>
        <tr><td>Identifying Components</td><td><span class="rubric-level">Expert</span>Correctly identifies and sorts ALL components as internal or external with detailed reasoning</td><td><span class="rubric-level">Proficient</span>Correctly identifies and sorts MOST components with some reasoning</td><td><span class="rubric-level">Developing</span>Identifies components but has difficulty sorting or explaining</td><td><span class="rubric-level">Beginning</span>Needs significant help identifying components</td></tr>
        <tr><td>Establishing Relationships</td><td><span class="rubric-level">Expert</span>Accurately describes ALL positive and negative relationships with clear evidence</td><td><span class="rubric-level">Proficient</span>Accurately describes MOST relationships with some evidence</td><td><span class="rubric-level">Developing</span>Identifies some relationships but struggles with direction</td><td><span class="rubric-level">Beginning</span>Needs help understanding how components connect</td></tr>
        <tr><td>Running Simulations</td><td><span class="rubric-level">Expert</span>Makes accurate predictions AND explains surprising results using evidence</td><td><span class="rubric-level">Proficient</span>Makes reasonable predictions and records clear observations</td><td><span class="rubric-level">Developing</span>Runs simulations but predictions or observations are incomplete</td><td><span class="rubric-level">Beginning</span>Needs help running simulations or recording data</td></tr>
        <tr><td>Explaining Results</td><td><span class="rubric-level">Expert</span>Uses multiple pieces of evidence to explain HOW and WHY systems interact</td><td><span class="rubric-level">Proficient</span>Uses evidence to explain system interactions</td><td><span class="rubric-level">Developing</span>Gives partial explanations with limited evidence</td><td><span class="rubric-level">Beginning</span>Needs help connecting evidence to explanations</td></tr>
      </tbody>
    </table>
    <div class="callout teal">
      <div class="callout-title">Scoring Guidance</div>
      <strong>Expert (4):</strong> Student demonstrates deep understanding and can transfer knowledge to new contexts.<br>
      <strong>Proficient (3):</strong> Student meets grade-level expectations and shows solid understanding.<br>
      <strong>Developing (2):</strong> Student is making progress but needs additional scaffolding or practice.<br>
      <strong>Beginning (1):</strong> Student needs significant support; consider using Differentiation strategies (Section 7).
    </div>
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 4)}
</div>

<!-- SECTION 3: BACKGROUND KNOWLEDGE -->
<div class="page" style="position:relative;">
  {section_page_header("3", "Background Content Knowledge", "teacher-variant")}
  <div class="page-content">
    <div class="teacher-tip"><div class="teacher-tip-title">For Your Confidence</div>This section provides the science background you need to facilitate this lesson with authority. You don&rsquo;t need to teach all of this &mdash; it&rsquo;s here so you can answer student questions accurately.</div>
    <p style="font-size:9.5pt; margin-bottom: 10px;">{bg_intro}</p>
    {bg_sections}
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 4)}
</div>

<!-- SECTION 4: LEVER FRAMEWORK -->
<div class="page" style="position:relative;">
  {section_page_header("4", "The LEVER Framework", "teacher-variant")}
  <div class="page-content">
    <div class="teacher-tip"><div class="teacher-tip-title">About LEVER</div>LEVER is how every ModelIt! lesson works. Students move through five phases to build, test, and refine a computational model. Each lesson is self-contained &mdash; students complete all five phases in one session.</div>
    {lever_html}

    <div style="background: linear-gradient(135deg, var(--navy), var(--purple-deep)); border-radius: 12px; padding: 16px 20px; margin-top: 14px; color: white;">
      <h3 style="font-family: Quicksand, sans-serif; font-weight: 800; font-size: 11pt; color: var(--teal-brand); margin-bottom: 8px;">Dropping ModelIt! Into Your Existing Unit</h3>
      <p style="font-size: 9pt; line-height: 1.6; color: rgba(255,255,255,0.9); margin-bottom: 8px;">ModelIt! is a <strong>supplement</strong>, not a replacement for your science curriculum. Each lesson stands alone, but it becomes even more powerful when students revisit their model throughout a unit. Here are easy ways to weave it in:</p>
      <table style="width: 100%; font-size: 8.5pt; border-collapse: collapse; color: rgba(255,255,255,0.9);">
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
          <td style="padding: 5px 8px; font-weight: 700; color: var(--teal-brand); width: 30%; vertical-align: top;">At the start of a unit</td>
          <td style="padding: 5px 8px;">Use this lesson to introduce the phenomenon. Students build a &ldquo;first draft&rdquo; model based on what they already know. Save it.</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
          <td style="padding: 5px 8px; font-weight: 700; color: var(--teal-brand); vertical-align: top;">After a reading or lab</td>
          <td style="padding: 5px 8px;">Have students reopen their model and update it: &ldquo;Based on what you just learned, would you add a component? Change a relationship?&rdquo; Takes 10&ndash;15 minutes.</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
          <td style="padding: 5px 8px; font-weight: 700; color: var(--teal-brand); vertical-align: top;">As a &ldquo;what-if&rdquo; tool</td>
          <td style="padding: 5px 8px;">When students ask questions during class, say: &ldquo;Great question &mdash; go test that in your model!&rdquo; Students run new scenarios and report back.</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
          <td style="padding: 5px 8px; font-weight: 700; color: var(--teal-brand); vertical-align: top;">For peer discussion</td>
          <td style="padding: 5px 8px;">Partners compare models: &ldquo;Why does your model have this arrow and mine doesn&rsquo;t?&rdquo; Differences spark scientific debate using evidence.</td>
        </tr>
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
          <td style="padding: 5px 8px; font-weight: 700; color: var(--teal-brand); vertical-align: top;">As a presentation tool</td>
          <td style="padding: 5px 8px;">Students project their model and walk the class through it live &mdash; showing components, running scenarios, answering audience &ldquo;what-if&rdquo; challenges in real time.</td>
        </tr>
        <tr>
          <td style="padding: 5px 8px; font-weight: 700; color: var(--teal-brand); vertical-align: top;">At the end of a unit</td>
          <td style="padding: 5px 8px;">Compare Day 1 model to final model. The growth IS the assessment &mdash; students see how their thinking evolved.</td>
        </tr>
      </table>
    </div>
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 6)}
</div>

<!-- SECTION 4: SLIDE FACILITATION -->
<div class="page" style="position:relative;">
  {section_page_header("5", "Slide-by-Slide Facilitation", "teacher-variant")}
  <div class="page-content">
    {slides_html}
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 6)}
</div>

<!-- SECTION 5: ANSWER KEY -->
<div class="page" style="position:relative;">
  {section_page_header("6", "Answer Key &amp; Expected Responses", "teacher-variant")}
  <div class="page-content">
    <div class="answer-key-box">
      <h4>Component Sorting</h4>
      <ul><li><strong>EXTERNAL:</strong> {html_escape(ext_names)}</li><li><strong>INTERNAL:</strong> {html_escape(int_names)}</li></ul>
    </div>
    <div class="answer-key-box">
      <h4>Relationships</h4>
      <ul>{answer_rels}</ul>
    </div>
    <div class="answer-key-box">
      <h4>Key Discoveries</h4>
      <ul>{answer_disc}</ul>
    </div>
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 8)}
</div>

<!-- SECTION 7: COLLABORATIVE LEARNING PROTOCOLS -->
<div class="page" style="position:relative;">
  {section_page_header("7", "Collaborative Learning Protocols", "teacher-variant")}
  <div class="page-content">
    <div class="teacher-tip">
      <div class="teacher-tip-title">Why This Matters</div>
      ModelIt! is a digital tool, but the deepest learning happens between humans. Computational modeling is most powerful when students build understanding <em>together</em> &mdash; debating relationships, challenging predictions, and constructing explanations as a community. These protocols ensure every student&rsquo;s voice is part of the model. Use at least ONE per lesson.
    </div>

    <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 12px;">
      <div style="border: 2px solid var(--teal-brand); border-radius: 12px; overflow: hidden;">
        <div style="background: var(--teal-brand); color: white; padding: 8px 14px; font-family: Quicksand, sans-serif; font-weight: 700; font-size: 10pt;">Model Gallery Walk</div>
        <div style="padding: 10px 14px; font-size: 9pt;">
          <strong>When:</strong> After students build models (LEVER Phase V)<br>
          <strong>Setup:</strong> Groups post their models on screens/desks. Half the class stays to &ldquo;defend,&rdquo; half rotates with sticky notes.<br>
          <strong>Protocol:</strong> Visitors leave 2 sticky notes: one &ldquo;I notice...&rdquo; and one &ldquo;I wonder...&rdquo; After rotation, defenders read feedback aloud. Class discusses patterns.<br>
          <strong>Why it works:</strong> Students see that the SAME phenomenon can be modeled differently &mdash; and that&rsquo;s how real science works. (Bandura: learning through observation of peers)
        </div>
      </div>
      <div style="border: 2px solid var(--purple-brand); border-radius: 12px; overflow: hidden;">
        <div style="background: var(--purple-brand); color: white; padding: 8px 14px; font-family: Quicksand, sans-serif; font-weight: 700; font-size: 10pt;">Scientist Fishbowl</div>
        <div style="padding: 10px 14px; font-size: 9pt;">
          <strong>When:</strong> During simulation discussion (LEVER Phase E)<br>
          <strong>Setup:</strong> 4-5 students sit in center circle. Rest of class observes with clipboards.<br>
          <strong>Protocol:</strong> Inner circle discusses: &ldquo;What happened in Scenario 3 and WHY?&rdquo; using only evidence from their models. Outer circle records strongest arguments. Swap groups.<br>
          <strong>Why it works:</strong> Students practice scientific discourse without teacher directing. Observers learn to evaluate arguments. (Freire: dialogue as the foundation of critical consciousness)
        </div>
      </div>
    </div>

    <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 12px;">
      <div style="border: 2px solid var(--orange-accent); border-radius: 12px; overflow: hidden;">
        <div style="background: var(--orange-accent); color: white; padding: 8px 14px; font-family: Quicksand, sans-serif; font-weight: 700; font-size: 10pt;">Component Jigsaw</div>
        <div style="padding: 10px 14px; font-size: 9pt;">
          <strong>When:</strong> During component analysis (LEVER Phase L)<br>
          <strong>Setup:</strong> Assign each group ONE component to become &ldquo;experts&rdquo; on. They research it, discuss it, draw it.<br>
          <strong>Protocol:</strong> Regroup so each new team has one expert per component. Experts teach their component to the team. Team builds the model together using everyone&rsquo;s expertise.<br>
          <strong>Why it works:</strong> Every student is essential &mdash; the model literally cannot be built without each person&rsquo;s knowledge. Interdependence drives engagement. (Lave &amp; Wenger: learning through legitimate peripheral participation)
        </div>
      </div>
      <div style="border: 2px solid var(--green-pos); border-radius: 12px; overflow: hidden;">
        <div style="background: var(--green-pos); color: white; padding: 8px 14px; font-family: Quicksand, sans-serif; font-weight: 700; font-size: 10pt;">Prediction Debate</div>
        <div style="padding: 10px 14px; font-size: 9pt;">
          <strong>When:</strong> Before running simulations (LEVER Phase E)<br>
          <strong>Setup:</strong> Post a scenario. Students physically move to corners: &ldquo;Fire Spread will INCREASE a lot&rdquo; / &ldquo;INCREASE a little&rdquo; / &ldquo;STAY the same&rdquo; / &ldquo;DECREASE.&rdquo;<br>
          <strong>Protocol:</strong> Each corner group has 2 minutes to build their argument using model logic. One spokesperson presents. Then RUN the simulation. Losing corners explain what they missed.<br>
          <strong>Why it works:</strong> Movement + social risk + immediate feedback. Students CARE about the outcome because they committed publicly. Wrong predictions become the best learning moments.
        </div>
      </div>
    </div>

    <div style="border: 2px solid var(--purple-light); border-radius: 12px; overflow: hidden; margin-bottom: 12px;">
      <div style="background: linear-gradient(135deg, var(--navy), var(--purple-deep)); color: white; padding: 8px 14px; font-family: Quicksand, sans-serif; font-weight: 700; font-size: 10pt;">Pair Programming for Models (Digital Collaboration)</div>
      <div style="padding: 10px 14px; font-size: 9pt;">
        <strong>When:</strong> Throughout model building<br>
        <strong>Setup:</strong> Two students, one device. <strong>Driver</strong> controls the mouse/keyboard. <strong>Navigator</strong> directs strategy and catches errors. Switch every 5 minutes.<br>
        <strong>Protocol:</strong> Navigator must verbalize every decision: &ldquo;I think we should add a negative arrow from Rainfall to Dry Vegetation because...&rdquo; Driver cannot act without Navigator&rsquo;s reasoning.<br>
        <strong>Why it works:</strong> Forces articulation of scientific thinking. The model becomes a shared artifact, not an individual assignment. Students who struggle with writing can demonstrate understanding verbally. Borrowed from computer science &mdash; where the best code is written in pairs.
      </div>
    </div>

    <div class="callout teal">
      <div class="callout-title">Quick Protocol Selection Guide</div>
      <table style="width:100%; font-size: 8.5pt; border-collapse: collapse;">
        <tr style="border-bottom: 1px solid var(--teal-light);"><td style="padding: 4px 8px; font-weight: 700; width: 35%;">Short on time (5 min)</td><td style="padding: 4px 8px;">Prediction Debate &mdash; gets bodies moving, generates energy fast</td></tr>
        <tr style="border-bottom: 1px solid var(--teal-light);"><td style="padding: 4px 8px; font-weight: 700;">Full period available</td><td style="padding: 4px 8px;">Component Jigsaw &mdash; deep collaboration, every student contributes</td></tr>
        <tr style="border-bottom: 1px solid var(--teal-light);"><td style="padding: 4px 8px; font-weight: 700;">After simulation day</td><td style="padding: 4px 8px;">Model Gallery Walk &mdash; peer feedback, multiple perspectives</td></tr>
        <tr style="border-bottom: 1px solid var(--teal-light);"><td style="padding: 4px 8px; font-weight: 700;">Advanced discussion</td><td style="padding: 4px 8px;">Scientist Fishbowl &mdash; builds academic discourse skills</td></tr>
        <tr><td style="padding: 4px 8px; font-weight: 700;">Every day default</td><td style="padding: 4px 8px;">Pair Programming &mdash; transforms individual work into dialogue</td></tr>
      </table>
    </div>
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 10)}
</div>

<!-- SECTION 8: DIFFERENTIATION -->
<div class="page" style="position:relative;">
  {section_page_header("8", "Differentiation &amp; Extensions", "teacher-variant")}
    <!-- NOTE: These suggestions become the basis for the Differentiation & Scaffolding Pack add-on -->
  <div class="page-content">
    <div class="diff-grid">
      <div class="diff-card below"><div class="diff-card-title">Below Grade Level</div><ul style="margin-left:14px;font-size:9pt;line-height:1.6;"><li>Pre-sort components as a whole class</li><li>Provide sentence frames for relationships</li><li>Use visual vocabulary cards</li><li>Pair with a strong reader</li></ul></div>
      <div class="diff-card advanced"><div class="diff-card-title">Advanced Learners</div><ul style="margin-left:14px;font-size:9pt;line-height:1.6;"><li>Add 2-3 additional components</li><li>Research real-world data</li><li>Create multi-step causal chains</li><li>Compare to similar systems globally</li></ul></div>
      <div class="diff-card ell"><div class="diff-card-title">English Language Learners</div><ul style="margin-left:14px;font-size:9pt;line-height:1.6;"><li>Pre-teach key vocabulary</li><li>Provide bilingual glossary</li><li>Use visual supports with text</li><li>Allow verbal responses</li></ul></div>
      <div class="diff-card gifted"><div class="diff-card-title">Gifted &amp; Talented</div><ul style="margin-left:14px;font-size:9pt;line-height:1.6;"><li>Create feedback loop diagrams</li><li>Research prevention strategies</li><li>Write a policy brief</li><li>Connect to climate change</li></ul></div>
    </div>
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 10)}
</div>

<!-- SECTION 8: MISCONCEPTIONS -->
<div class="page" style="position:relative;">
  {section_page_header("9", "Common Misconceptions", "teacher-variant")}
  <div class="page-content">
    <div class="teacher-tip"><div class="teacher-tip-title">Why This Matters</div>Addressing misconceptions proactively helps students build accurate scientific understanding. Use these as formative assessment checkpoints during the lesson.</div>
    {misconceptions_html}
  </div>
  {page_footer_html(lesson_id, "Teacher's Guide", 11)}
</div>

</body>
</html>'''

    return html


# ============================================================
# MAIN: Load data and generate
# ============================================================

def load_lesson_data(grade, lesson_num):
    """Load lesson data from the appropriate data file."""
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    grade_lower = grade.lower()

    # Determine data file path
    data_file = None

    # Nature's Engineers
    if grade_lower in ["ne", "natures-engineers"]:
        data_file = os.path.join(scripts_dir, "lesson_data_natures_engineers.py")
    # K-8 standard grades
    elif grade_lower in ["k", "0k", "00"]:
        data_file = os.path.join(scripts_dir, "lesson_data_GK.py")
    elif grade_lower in ["01", "1"]:
        data_file = os.path.join(scripts_dir, "lesson_data_G01.py")
    elif grade_lower in ["02", "2"]:
        data_file = os.path.join(scripts_dir, "lesson_data_G02.py")
    elif grade_lower in ["03", "3"]:
        data_file = os.path.join(scripts_dir, "lesson_data_G03.py")
    elif grade_lower in ["04", "4"]:
        data_file = os.path.join(scripts_dir, "lesson_data_G04.py")
    elif grade_lower in ["05", "5"]:
        if lesson_num == 1:
            data_file = os.path.join(scripts_dir, "create_reader.py")
        else:
            data_file = os.path.join(scripts_dir, "lesson_data_L02_L10.py")
    elif grade_lower in ["06", "6"]:
        data_file = os.path.join(scripts_dir, "lesson_data_G06.py")
    elif grade_lower in ["07", "7"]:
        data_file = os.path.join(scripts_dir, "lesson_data_G07.py")
    elif grade_lower in ["08", "8"]:
        data_file = os.path.join(scripts_dir, "lesson_data_G08.py")
    else:
        # High school levels: 09_L1, 09_L2, 09_L3, 10_L1, etc.
        data_file = os.path.join(scripts_dir, f"lesson_data_G{grade_lower}.py")

    if not data_file or not os.path.exists(data_file):
        print(f"ERROR: Data file not found for grade '{grade}': {data_file}")
        return None

    # Load the module
    spec = importlib.util.spec_from_file_location(f"lesson_data_{grade}", data_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Find the lesson data - try multiple key patterns
    lesson_key = f"L{lesson_num:02d}"

    # Pattern 1: Direct attribute L01, L02, etc.
    if hasattr(mod, lesson_key):
        return getattr(mod, lesson_key)

    # Pattern 2: Nature's Engineers uses L1_01-L1_06, L2_01-L2_06
    if grade_lower in ["ne", "natures-engineers"]:
        if lesson_num <= 6:
            ne_key = f"L1_{lesson_num:02d}"
        else:
            ne_key = f"L2_{lesson_num - 6:02d}"
        if hasattr(mod, ne_key):
            return getattr(mod, ne_key)

    # Pattern 3: Function get_L01_data()
    func_name = f"get_{lesson_key}_data"
    if hasattr(mod, func_name):
        return getattr(mod, func_name)()

    # Pattern 4: lessons dict
    if hasattr(mod, "lessons"):
        lessons = mod.lessons
        if lesson_key in lessons:
            return lessons[lesson_key]

    print(f"WARNING: Could not find lesson {lesson_key} in {data_file}")
    attrs = [a for a in dir(mod) if not a.startswith('_') and not a.startswith('__')]
    print(f"  Available: {attrs[:20]}")
    return None


def get_output_dir(grade, lesson_num):
    """Get the materials output directory."""
    base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "materials")

    grade_lower = grade.lower()

    # Nature's Engineers: L1 = lessons 1-6, L2 = lessons 7-12
    if grade_lower in ["ne", "natures-engineers"]:
        grade_folder = "natures-engineers"
        if lesson_num <= 6:
            lesson_prefix = "NE-L1"
            ne_num = lesson_num
        else:
            lesson_prefix = "NE-L2"
            ne_num = lesson_num - 6
        lesson_folder = f"{lesson_prefix}-{ne_num:02d}"
        output_dir = os.path.join(base, grade_folder, lesson_folder)
        os.makedirs(output_dir, exist_ok=True)
        return output_dir, lesson_folder

    if grade_lower in ["k", "0k", "00"]:
        grade_folder = "grade-K"
        lesson_prefix = "GK"
    elif len(grade_lower) == 1:
        grade_folder = f"grade-0{grade_lower}"
        lesson_prefix = f"G0{grade_lower}"
    elif "_" in grade_lower:
        # High school levels: "09_L1", "10_L2", etc.
        grade_num, level = grade_lower.split("_")
        grade_folder = f"grade-{grade_num}"
        level_num = level.replace("l", "").replace("L", "")
        level_folder = f"level-{level_num}"
        lesson_prefix = f"G{grade_num}L{level_num}"
        lesson_folder = f"{lesson_prefix}-L{lesson_num:02d}"
        output_dir = os.path.join(base, grade_folder, level_folder, lesson_folder)
        os.makedirs(output_dir, exist_ok=True)
        return output_dir, lesson_folder
    else:
        grade_folder = f"grade-{grade_lower}"
        lesson_prefix = f"G{grade_lower}"

    lesson_folder = f"{lesson_prefix}-L{lesson_num:02d}"
    output_dir = os.path.join(base, grade_folder, lesson_folder)

    os.makedirs(output_dir, exist_ok=True)
    return output_dir, lesson_folder


def main():
    parser = argparse.ArgumentParser(description="ModelIt! Branded Materials Generator")
    parser.add_argument("--grade", required=True, help="Grade level (K, 01-12)")
    parser.add_argument("--lesson", type=int, help="Lesson number (1-10)")
    parser.add_argument("--all", action="store_true", help="Generate all lessons for the grade")
    parser.add_argument("--type", choices=["student", "teacher", "both"], default="both",
                       help="Which document to generate")

    args = parser.parse_args()

    if args.all:
        if args.grade.lower() in ["ne", "natures-engineers"]:
            lessons = range(1, 13)  # 12 NE lessons: L1(1-6) + L2(7-12)
        else:
            lessons = range(1, 11)
    elif args.lesson:
        lessons = [args.lesson]
    else:
        print("ERROR: Specify --lesson N or --all")
        sys.exit(1)

    for lesson_num in lessons:
        print(f"\n{'='*60}")
        print(f"Generating materials for Grade {args.grade}, Lesson {lesson_num}")
        print(f"{'='*60}")

        try:
            data = load_lesson_data(args.grade, lesson_num)
        except Exception as e:
            print(f"WARNING: Could not load lesson {lesson_num}: {e}")
            continue

        output_dir, lesson_folder = get_output_dir(args.grade, lesson_num)

        if args.type in ("student", "both"):
            html = generate_student_activity_pack(data)
            filepath = os.path.join(output_dir, f"{lesson_folder}-Student-Activity-Pack.html")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  [OK] Student Activity Pack: {filepath}")

        if args.type in ("teacher", "both"):
            html = generate_teachers_guide(data)
            filepath = os.path.join(output_dir, f"{lesson_folder}-Teachers-Guide.html")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  [OK] Teacher's Guide: {filepath}")

    print(f"\nDone! Generated materials in {os.path.dirname(output_dir)}/")


if __name__ == "__main__":
    main()
