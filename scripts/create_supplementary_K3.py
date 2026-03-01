#!/usr/bin/env python3
"""ModelIt! K-3 Supplementary Materials Generator

Generates 6 types of supplementary materials for K-3 curriculum:
  K-2: Model Explorer Game (HTML), Coloring Sheet (DOCX)
  G2-3: Fix the System (DOCX), Interactive Notebook (DOCX),
        Reading Passage (DOCX), Parent-Home Connection (DOCX)
  Grade 2 gets ALL 6 types.

Usage:
    python create_supplementary_K3.py K      # Kindergarten: game + coloring
    python create_supplementary_K3.py 1      # Grade 1: game + coloring
    python create_supplementary_K3.py 2      # Grade 2: all 6 types
    python create_supplementary_K3.py 3      # Grade 3: fix + notebook + reading + home
    python create_supplementary_K3.py all    # All grades
"""
import os, sys, time, base64, requests, importlib, json, random
from docx import Document
from docx.shared import Inches as DI, Pt as DP, RGBColor as DR, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import dotenv as _dotenv
_dotenv.load_dotenv(os.path.join(os.path.expanduser('~'), '.env'))
API_KEY = os.environ.get('OPENROUTER_API_KEY', '')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Brand colors (DOCX)
DN  = DR(0x0D, 0x1B, 0x2A)   # Dark Navy
DBB = DR(0x1A, 0x47, 0x80)   # Dark Bold Blue
DMB = DR(0x2E, 0x86, 0xAB)   # Dark Medium Blue
DLB = DR(0x7E, 0xC8, 0xE3)   # Light Blue
DOG = DR(0xE6, 0x7E, 0x22)   # Orange
DWH = DR(0xFF, 0xFF, 0xFF)   # White
DGN = DR(0x27, 0xAE, 0x60)   # Green (positive)
DRD = DR(0xE7, 0x4C, 0x3C)   # Red (negative)

# Brand color hex strings for table shading
HEX_NAVY  = "0D1B2A"
HEX_BB    = "1A4780"
HEX_MB    = "2E86AB"
HEX_LB    = "7EC8E3"
HEX_SB    = "5DB7DE"
HEX_OG    = "E67E22"
HEX_GREEN = "27AE60"
HEX_RED   = "E74C3C"
HEX_LGRAY = "F5F5F5"
HEX_MGRAY = "EEEEEE"

total_cost = 0.0

GRADE_CONFIG = {
    "K":  {"label": "Kindergarten", "age": "5-6 years old", "tier": 1,
           "dir": "grade-K",  "data": "lesson_data_GK",
           "game": True, "coloring": True, "fix": False, "notebook": False,
           "reading": False, "home": False, "num_components": 2},
    "1":  {"label": "1st Grade",    "age": "6-7 years old", "tier": 1,
           "dir": "grade-01", "data": "lesson_data_G01",
           "game": True, "coloring": True, "fix": False, "notebook": False,
           "reading": False, "home": False, "num_components": 2},
    "2":  {"label": "2nd Grade",    "age": "7-8 years old", "tier": 2,
           "dir": "grade-02", "data": "lesson_data_G02",
           "game": True, "coloring": True, "fix": True, "notebook": True,
           "reading": True, "home": True, "num_components": 3},
    "3":  {"label": "3rd Grade",    "age": "8-9 years old", "tier": 2,
           "dir": "grade-03", "data": "lesson_data_G03",
           "game": False, "coloring": False, "fix": True, "notebook": True,
           "reading": True, "home": True, "num_components": 3},
}

# ══════════════════════════════════════════════════════════════
#  SHARED UTILITIES
# ══════════════════════════════════════════════════════════════

def cell_shd(cell, hex_c):
    shd = OxmlElement("w:shd"); shd.set(qn("w:fill"), hex_c)
    cell._tc.get_or_add_tcPr().append(shd)

def hdr(doc, text, lv=1):
    p = doc.add_paragraph(); r = p.add_run(text); r.bold = True
    if lv == 1: r.font.size = DP(24); r.font.color.rgb = DN
    elif lv == 2: r.font.size = DP(18); r.font.color.rgb = DBB
    elif lv == 3: r.font.size = DP(14); r.font.color.rgb = DMB
    return p

def wide_rbox(doc, lines=3, prompt=""):
    if prompt:
        p = doc.add_paragraph(); r = p.add_run(prompt)
        r.font.size = DP(14); r.bold = True
    t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"
    cell = t.rows[0].cells[0]
    for i in range(lines):
        pp = cell.add_paragraph()
        pp.paragraph_format.space_after = DP(6)
        pp.paragraph_format.line_spacing = DP(28)
        r = pp.add_run("_" * 65)
        r.font.size = DP(14); r.font.color.rgb = DR(0xCC, 0xCC, 0xCC)
    doc.add_paragraph(); return t

def drawing_box(doc, lines=8, prompt=""):
    if prompt:
        p = doc.add_paragraph(); r = p.add_run(prompt)
        r.font.size = DP(14); r.bold = True
    t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"
    t.rows[0].cells[0].text = "\n" * lines
    doc.add_paragraph(); return t

def name_date(doc, wide_lines=False):
    t = doc.add_table(rows=1, cols=2); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    sz = DP(16) if wide_lines else DP(11)
    t.rows[0].cells[0].text = "Name: _______________________________"
    t.rows[0].cells[1].text = "Date: _______________"
    for c2 in t.rows[0].cells:
        for r2 in c2.paragraphs[0].runs: r2.font.size = sz
    doc.add_paragraph()

def compose_sentence_frame(c):
    """Build a sentence frame from relationships for G2-3 (which lack sentence_frame key)."""
    if "sentence_frame" in c and c["sentence_frame"]:
        return c["sentence_frame"]
    rels = c.get("relationships", [])
    if rels:
        rel_str, sign, _ = rels[0]
        parts = rel_str.split(" to ")
        if len(parts) == 2:
            fr, to = parts[0].strip(), parts[1].strip()
            direction = "up" if "POSITIVE" in sign or "+" in sign else "down"
            return f"When {fr} goes up, {to} goes _______."
    comps = c.get("components", [])
    ext = [name for name, _, is_ext in comps if is_ext]
    int_ = [name for name, _, is_ext in comps if not is_ext]
    if ext and int_:
        return f"When {ext[0]} changes, {int_[0]} _______."
    return "When _______ changes, _______ _______."

def compose_coloring_desc(c):
    """Build coloring instructions for G2 (which lacks coloring_description key)."""
    if "coloring_description" in c and c["coloring_description"]:
        return c["coloring_description"]
    comps = c.get("components", [])
    names = [name for name, _, _ in comps]
    if len(names) >= 2:
        return (f"Color each part of the system model! Color the {names[0]} box, "
                f"the {names[1]} box, and trace the arrows connecting them. "
                "Use green for arrows that mean 'goes up together' (+) and "
                "red for arrows that mean 'goes opposite' (-).")
    return "Color the parts of the system model and trace the arrows!"

def add_modelit_header(doc, title, lesson_id, grade_label):
    """Add branded header to all supplementary docs."""
    p = doc.add_paragraph()
    r = p.add_run("ModelIt! "); r.bold = True; r.font.size = DP(20)
    r.font.color.rgb = DMB
    r2 = p.add_run(f"  |  {grade_label}"); r2.font.size = DP(12)
    r2.font.color.rgb = DR(0x66, 0x66, 0x66)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p2 = doc.add_paragraph()
    r3 = p2.add_run(f"{lesson_id}: {title}"); r3.bold = True
    r3.font.size = DP(16); r3.font.color.rgb = DBB
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph()

def add_footer_line(doc, lesson_id):
    """Add simple footer with lesson ID."""
    doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run(f"ModelIt! {lesson_id}"); r.font.size = DP(8)
    r.font.color.rgb = DR(0x99, 0x99, 0x99)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER


# ══════════════════════════════════════════════════════════════
#  1. MODEL EXPLORER GAME (K-2) — HTML
# ══════════════════════════════════════════════════════════════

GAME_HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Model Explorer: {{TITLE}}</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:#f0f7ff;
  min-height:100vh;display:flex;flex-direction:column;align-items:center}
.header{background:linear-gradient(135deg,#1A4780,#2E86AB);color:#fff;
  width:100%;padding:16px 24px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.15)}
.header h1{font-size:clamp(18px,4vw,28px);margin-bottom:4px}
.header .sub{font-size:clamp(12px,2.5vw,16px);opacity:.85}
.nav{display:flex;gap:8px;justify-content:center;padding:12px;flex-wrap:wrap}
.nav button{padding:10px 20px;border:3px solid #1A4780;border-radius:24px;
  background:#fff;color:#1A4780;font-size:clamp(13px,2.5vw,16px);font-weight:700;
  cursor:pointer;transition:all .2s}
.nav button:hover,.nav button.active{background:#1A4780;color:#fff;transform:scale(1.05)}
.nav button.done{border-color:#27AE60;color:#27AE60}
.nav button.done.active{background:#27AE60;color:#fff}
.screen{display:none;width:min(95vw,700px);padding:20px;margin:8px auto}
.screen.active{display:block}
.screen h2{color:#1A4780;font-size:clamp(18px,3.5vw,24px);text-align:center;margin-bottom:16px}
.instruction{background:#fff;border-left:4px solid #E67E22;padding:12px 16px;
  border-radius:0 8px 8px 0;margin-bottom:20px;font-size:clamp(14px,2.5vw,17px);color:#333}

/* Screen 1: Sort */
.sort-area{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-bottom:20px}
.sort-box{background:#fff;border:3px dashed #2E86AB;border-radius:16px;padding:16px;
  min-width:200px;min-height:140px;flex:1;text-align:center;transition:border-color .3s}
.sort-box h3{color:#fff;padding:8px;border-radius:8px;margin-bottom:12px;
  font-size:clamp(13px,2.5vw,16px)}
.sort-box.external h3{background:#E67E22}
.sort-box.internal h3{background:#2E86AB}
.sort-box.highlight{border-color:#E67E22;background:#fff8f0}
.cards{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-bottom:16px}
.card{background:linear-gradient(135deg,#5DB7DE,#2E86AB);color:#fff;
  padding:12px 20px;border-radius:12px;font-size:clamp(14px,2.5vw,18px);
  font-weight:700;cursor:grab;user-select:none;touch-action:none;
  box-shadow:0 3px 8px rgba(0,0,0,.15);transition:transform .2s}
.card:active{transform:scale(1.08);cursor:grabbing}
.card.placed{opacity:.4;pointer-events:none}
.placed-card{background:#E8F5E9;border:2px solid #27AE60;border-radius:10px;
  padding:8px 14px;margin:4px;display:inline-block;font-weight:600;color:#1A4780;
  font-size:clamp(13px,2.5vw,16px)}

/* Screen 2: Fix Arrows */
.model-display{background:#fff;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,.08);
  text-align:center;margin-bottom:16px}
.comp-row{display:flex;align-items:center;justify-content:center;gap:12px;
  flex-wrap:wrap;margin:12px 0}
.comp-box{background:linear-gradient(135deg,#f0f7ff,#e0efff);border:3px solid #1A4780;
  border-radius:12px;padding:14px 20px;font-weight:700;font-size:clamp(14px,2.5vw,18px);
  color:#1A4780;min-width:120px}
.arrow-btn{width:64px;height:64px;border-radius:50%;border:3px solid #ccc;
  font-size:28px;font-weight:900;cursor:pointer;transition:all .3s;
  display:flex;align-items:center;justify-content:center;background:#fff}
.arrow-btn.positive{border-color:#27AE60;color:#27AE60;background:#E8F5E9}
.arrow-btn.negative{border-color:#E74C3C;color:#E74C3C;background:#FDEDEC}
.arrow-btn:hover{transform:scale(1.15)}
.arrow-label{font-size:clamp(11px,2vw,13px);color:#666;margin-top:4px;text-align:center}

/* Screen 3: Explore */
.explore-panel{background:#fff;border-radius:16px;padding:24px;
  box-shadow:0 2px 12px rgba(0,0,0,.08);text-align:center}
.ctrl-row{display:flex;align-items:center;justify-content:center;gap:16px;
  margin:16px 0;flex-wrap:wrap}
.ctrl-label{font-size:clamp(14px,2.5vw,18px);font-weight:700;color:#1A4780;min-width:100px}
.ctrl-btn{width:56px;height:56px;border-radius:50%;border:none;
  font-size:28px;font-weight:900;cursor:pointer;color:#fff;transition:transform .2s}
.ctrl-btn:hover{transform:scale(1.12)}
.ctrl-btn.up{background:#27AE60}
.ctrl-btn.down{background:#E74C3C}
.bar-container{width:min(80%,300px);height:32px;background:#eee;border-radius:16px;
  overflow:hidden;margin:8px auto;position:relative}
.bar-fill{height:100%;border-radius:16px;transition:width .5s ease;
  display:flex;align-items:center;justify-content:flex-end;padding-right:8px;
  font-size:13px;font-weight:700;color:#fff}
.bar-fill.ext{background:linear-gradient(90deg,#E67E22,#F39C12)}
.bar-fill.int{background:linear-gradient(90deg,#2E86AB,#5DB7DE)}
.result-text{font-size:clamp(14px,2.5vw,17px);color:#333;margin:12px 0;
  min-height:48px;line-height:1.5}
.sentence{background:#FFF8E1;border:2px solid #F39C12;border-radius:12px;
  padding:14px 20px;font-size:clamp(14px,2.5vw,17px);font-weight:600;
  color:#1A4780;margin-top:16px}

/* Celebration */
.celebrate{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:999}
.star{position:absolute;font-size:clamp(20px,5vw,36px);animation:fall 1.5s ease-out forwards}
@keyframes fall{0%{opacity:1;transform:translateY(-20px) rotate(0deg) scale(1)}
  100%{opacity:0;transform:translateY(80vh) rotate(720deg) scale(.3)}}
.check-anim{animation:pop .5s ease}
@keyframes pop{0%{transform:scale(0)}50%{transform:scale(1.3)}100%{transform:scale(1)}}

/* Feedback */
.feedback{padding:12px 20px;border-radius:12px;text-align:center;
  font-size:clamp(14px,2.5vw,17px);font-weight:600;margin:12px 0;
  animation:pop .4s ease}
.feedback.correct{background:#E8F5E9;color:#27AE60;border:2px solid #27AE60}
.feedback.wrong{background:#FDEDEC;color:#E74C3C;border:2px solid #E74C3C}
.feedback.info{background:#FFF8E1;color:#E67E22;border:2px solid #E67E22}

.reset-btn{display:block;margin:20px auto 0;padding:10px 24px;border:2px solid #2E86AB;
  border-radius:20px;background:#fff;color:#2E86AB;font-size:15px;font-weight:600;
  cursor:pointer}
.reset-btn:hover{background:#2E86AB;color:#fff}
</style>
</head>
<body>

<div class="header">
  <h1>Model Explorer</h1>
  <div class="sub" id="lessonTitle"></div>
</div>

<div class="nav">
  <button id="nav1" class="active" onclick="showScreen(1)">1. Sort the Parts!</button>
  <button id="nav2" onclick="showScreen(2)">2. Fix the Arrows!</button>
  <button id="nav3" onclick="showScreen(3)">3. What Happens?</button>
</div>

<!-- SCREEN 1: Sort the Parts -->
<div class="screen active" id="screen1">
  <h2>Sort the Parts!</h2>
  <div class="instruction">Drag each part into the correct box. <b>We Control</b> means WE
    decide to change it. <b>Changes by Itself</b> means it changes on its own when something
    else changes.</div>
  <div class="cards" id="cardArea"></div>
  <div class="sort-area">
    <div class="sort-box external" id="extBox" ondragover="allowDrop(event)"
         ondrop="dropCard(event,'external')">
      <h3>We Control (Outside)</h3>
      <div id="extCards"></div>
    </div>
    <div class="sort-box internal" id="intBox" ondragover="allowDrop(event)"
         ondrop="dropCard(event,'internal')">
      <h3>Changes by Itself (Inside)</h3>
      <div id="intCards"></div>
    </div>
  </div>
  <div id="sortFeedback"></div>
</div>

<!-- SCREEN 2: Fix the Arrows -->
<div class="screen" id="screen2">
  <h2>Fix the Arrows!</h2>
  <div class="instruction">The arrows are WRONG! Tap each arrow button to change it between
    <span style="color:#27AE60;font-weight:700">+ (go together)</span> and
    <span style="color:#E74C3C;font-weight:700">- (go opposite)</span> until the model is correct.</div>
  <div class="model-display" id="arrowModel"></div>
  <div id="arrowFeedback"></div>
</div>

<!-- SCREEN 3: Explore -->
<div class="screen" id="screen3">
  <h2>What Happens?</h2>
  <div class="instruction">Press the UP or DOWN buttons to change the outside part.
    Watch what happens to the inside parts!</div>
  <div class="explore-panel" id="explorePanel"></div>
</div>

<script>
// ── Lesson data (injected by Python) ──
const LESSON = {{LESSON_JSON}};

// ── State ──
let screenDone = [false, false, false];
let sortCorrect = {};
let arrowStates = {};
let exploreLevels = {};

// ── Init ──
document.getElementById('lessonTitle').textContent = LESSON.title;
initSort();
initArrows();
initExplore();

// ── Navigation ──
function showScreen(n) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav button').forEach(b => b.classList.remove('active'));
  document.getElementById('screen' + n).classList.add('active');
  document.getElementById('nav' + n).classList.add('active');
}

// ── SCREEN 1: Sort the Parts ──
function initSort() {
  const cardArea = document.getElementById('cardArea');
  // Shuffle components
  let comps = [...LESSON.components];
  for (let i = comps.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [comps[i], comps[j]] = [comps[j], comps[i]];
  }
  comps.forEach((comp, i) => {
    const card = document.createElement('div');
    card.className = 'card';
    card.id = 'card-' + i;
    card.textContent = comp.name;
    card.draggable = true;
    card.dataset.name = comp.name;
    card.dataset.external = comp.external;
    card.ondragstart = e => {
      e.dataTransfer.setData('text/plain', i.toString());
      card.style.opacity = '0.5';
    };
    card.ondragend = () => card.style.opacity = '1';
    // Touch support
    card.ontouchstart = e => {
      e.preventDefault();
      card.dataset.dragging = 'true';
      card.style.transform = 'scale(1.08)';
    };
    card.ontouchend = e => {
      e.preventDefault();
      card.style.transform = '';
      card.dataset.dragging = 'false';
      const touch = e.changedTouches[0];
      const el = document.elementFromPoint(touch.clientX, touch.clientY);
      const box = el ? el.closest('.sort-box') : null;
      if (box) {
        const type = box.classList.contains('external') ? 'external' : 'internal';
        placeCard(i, type);
      }
    };
    cardArea.appendChild(card);
  });
}

function allowDrop(e) { e.preventDefault(); e.currentTarget.classList.add('highlight'); }
document.querySelectorAll('.sort-box').forEach(b => {
  b.ondragleave = () => b.classList.remove('highlight');
});

function dropCard(e, type) {
  e.preventDefault();
  e.currentTarget.classList.remove('highlight');
  const idx = parseInt(e.dataTransfer.getData('text/plain'));
  placeCard(idx, type);
}

function placeCard(idx, type) {
  const comps = LESSON.components;
  const comp = comps[idx];
  if (!comp) return;
  const card = document.getElementById('card-' + idx);
  if (card.classList.contains('placed')) return;

  const isCorrect = (type === 'external') === comp.external;
  const targetId = type === 'external' ? 'extCards' : 'intCards';
  const target = document.getElementById(targetId);

  const placed = document.createElement('div');
  placed.className = 'placed-card';
  placed.textContent = comp.name;
  target.appendChild(placed);
  card.classList.add('placed');
  sortCorrect[idx] = isCorrect;

  if (Object.keys(sortCorrect).length === comps.length) {
    const allRight = Object.values(sortCorrect).every(v => v);
    const fb = document.getElementById('sortFeedback');
    if (allRight) {
      fb.innerHTML = '<div class="feedback correct check-anim">Awesome! You sorted all the parts correctly!</div>';
      screenDone[0] = true;
      document.getElementById('nav1').classList.add('done');
      celebrate();
    } else {
      fb.innerHTML = '<div class="feedback wrong">Not quite! Some parts are in the wrong box. Try again!</div>' +
        '<button class="reset-btn" onclick="resetSort()">Try Again</button>';
    }
  }
}

function resetSort() {
  sortCorrect = {};
  document.getElementById('extCards').innerHTML = '';
  document.getElementById('intCards').innerHTML = '';
  document.getElementById('sortFeedback').innerHTML = '';
  document.querySelectorAll('.card').forEach(c => c.classList.remove('placed'));
}

// ── SCREEN 2: Fix the Arrows ──
function initArrows() {
  const model = document.getElementById('arrowModel');
  let html = '';
  LESSON.relationships.forEach((rel, i) => {
    // Start with WRONG direction
    const correctType = rel.type;
    const wrongType = correctType === '+' ? '-' : '+';
    arrowStates[i] = wrongType;

    html += '<div class="comp-row">';
    html += `<div class="comp-box">${rel.from}</div>`;
    html += '<div style="text-align:center">';
    html += `<button class="arrow-btn ${wrongType === '+' ? 'positive' : 'negative'}"
              id="arrow-${i}" onclick="toggleArrow(${i})"
              title="Tap to change">${wrongType === '+' ? '+ →' : '- →'}</button>`;
    html += `<div class="arrow-label">${wrongType === '+' ? 'Go together' : 'Go opposite'}</div>`;
    html += '</div>';
    html += `<div class="comp-box">${rel.to}</div>`;
    html += '</div>';
  });
  model.innerHTML = html;
}

function toggleArrow(i) {
  const current = arrowStates[i];
  const next = current === '+' ? '-' : '+';
  arrowStates[i] = next;
  const btn = document.getElementById('arrow-' + i);
  btn.textContent = next === '+' ? '+ →' : '- →';
  btn.className = 'arrow-btn ' + (next === '+' ? 'positive' : 'negative');
  btn.nextElementSibling.textContent = next === '+' ? 'Go together' : 'Go opposite';

  // Check if all correct
  const allCorrect = LESSON.relationships.every((rel, j) => arrowStates[j] === rel.type);
  const fb = document.getElementById('arrowFeedback');
  if (allCorrect) {
    fb.innerHTML = '<div class="feedback correct check-anim">You fixed all the arrows! Great job!</div>';
    screenDone[1] = true;
    document.getElementById('nav2').classList.add('done');
    celebrate();
  } else {
    fb.innerHTML = '';
  }
}

// ── SCREEN 3: Explore ──
function initExplore() {
  const panel = document.getElementById('explorePanel');
  let html = '';

  // External components (controls)
  const externals = LESSON.components.filter(c => c.external);
  const internals = LESSON.components.filter(c => !c.external);

  externals.forEach(comp => {
    exploreLevels[comp.name] = 50;
    html += `<div class="ctrl-row">
      <span class="ctrl-label">${comp.name}</span>
      <button class="ctrl-btn down" onclick="adjustLevel('${comp.name}',-25)">▼</button>
      <div class="bar-container">
        <div class="bar-fill ext" id="bar-${css(comp.name)}" style="width:50%">50%</div>
      </div>
      <button class="ctrl-btn up" onclick="adjustLevel('${comp.name}',25)">▲</button>
    </div>`;
  });

  internals.forEach(comp => {
    exploreLevels[comp.name] = 50;
    html += `<div class="ctrl-row">
      <span class="ctrl-label">${comp.name}</span>
      <div class="bar-container">
        <div class="bar-fill int" id="bar-${css(comp.name)}" style="width:50%">50%</div>
      </div>
    </div>`;
  });

  html += '<div class="result-text" id="exploreResult">Press the UP or DOWN buttons to explore!</div>';
  html += `<div class="sentence" id="exploreSentence">${LESSON.sentenceFrame}</div>`;
  panel.innerHTML = html;
}

function css(name) { return name.replace(/[^a-zA-Z0-9]/g, '_'); }

function adjustLevel(name, delta) {
  let val = exploreLevels[name] + delta;
  val = Math.max(0, Math.min(100, val));
  exploreLevels[name] = val;
  updateBar(name, val);

  // Update internal components based on relationships
  LESSON.relationships.forEach(rel => {
    if (rel.from === name) {
      const target = rel.to;
      let targetVal;
      if (rel.type === '+') {
        targetVal = val; // same direction
      } else {
        targetVal = 100 - val; // opposite direction
      }
      exploreLevels[target] = targetVal;
      updateBar(target, targetVal);
    }
  });

  updateExploreText();
  if (!screenDone[2]) {
    screenDone[2] = true;
    document.getElementById('nav3').classList.add('done');
  }
}

function updateBar(name, val) {
  const bar = document.getElementById('bar-' + css(name));
  if (bar) {
    bar.style.width = val + '%';
    bar.textContent = val + '%';
  }
}

function updateExploreText() {
  const el = document.getElementById('exploreResult');
  const ext = LESSON.components.filter(c => c.external);
  const parts = [];
  ext.forEach(comp => {
    const lvl = exploreLevels[comp.name];
    const word = lvl > 60 ? 'HIGH' : lvl < 40 ? 'LOW' : 'MEDIUM';
    LESSON.relationships.forEach(rel => {
      if (rel.from === comp.name) {
        const tLvl = exploreLevels[rel.to];
        const tWord = tLvl > 60 ? 'HIGH' : tLvl < 40 ? 'LOW' : 'MEDIUM';
        parts.push(`When ${comp.name} is ${word}, ${rel.to} is ${tWord}!`);
      }
    });
  });
  el.textContent = parts.join(' ') || 'Press buttons to explore!';
}

// ── Celebration ──
function celebrate() {
  const div = document.createElement('div');
  div.className = 'celebrate';
  const emojis = ['⭐','🌟','✨','🎉','🎊','💫','🏆','👏'];
  for (let i = 0; i < 20; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    star.style.left = Math.random() * 100 + '%';
    star.style.animationDelay = Math.random() * 0.8 + 's';
    div.appendChild(star);
  }
  document.body.appendChild(div);
  setTimeout(() => div.remove(), 2500);
}
</script>
</body>
</html>'''


def make_game(c, grade_config):
    """Build HTML game string for a lesson."""
    comps = c.get("components", [])
    rels = c.get("relationships", [])

    # Build lesson JSON config
    lesson_data = {
        "title": c["title"],
        "components": [],
        "relationships": [],
        "vocabulary": [],
        "sentenceFrame": compose_sentence_frame(c)
    }

    for name, desc, is_ext in comps:
        lesson_data["components"].append({
            "name": name, "desc": desc, "external": is_ext
        })

    for rel_str, sign, explanation in rels:
        parts = rel_str.split(" to ")
        fr = parts[0].strip() if len(parts) >= 2 else ""
        to = parts[1].strip() if len(parts) >= 2 else ""
        rtype = "+" if "POSITIVE" in sign or "+" in sign else "-"
        lesson_data["relationships"].append({
            "from": fr, "to": to, "type": rtype, "explanation": explanation
        })

    for term, defn in c.get("vocabulary", []):
        lesson_data["vocabulary"].append({"term": term, "definition": defn})

    lesson_json = json.dumps(lesson_data, indent=2)
    html = GAME_HTML_TEMPLATE.replace("{{LESSON_JSON}}", lesson_json)
    html = html.replace("{{TITLE}}", c["title"])
    return html


def write_game(c, out_dir, grade_config):
    """Write the game HTML file."""
    lid = c["id"]
    fn = f"{lid}-Model-Explorer.html"
    fp = os.path.join(out_dir, fn)
    html = make_game(c, grade_config)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [OK] Game: {fn}")
    return fp


# ══════════════════════════════════════════════════════════════
#  2. COLORING SHEET (K-2) — DOCX
# ══════════════════════════════════════════════════════════════

def gen_coloring_img(c, img_dir):
    """Generate AI coloring book image for a lesson."""
    global total_cost
    comps = c.get("components", [])
    comp_names = [name for name, _, _ in comps]
    rels = c.get("relationships", [])

    # Build model description
    model_desc = ", ".join(comp_names)
    arrows = []
    for rel_str, sign, _ in rels:
        parts = rel_str.split(" to ")
        if len(parts) == 2:
            direction = "positive (goes up together)" if "+" in sign else "negative (goes opposite)"
            arrows.append(f"an arrow from {parts[0].strip()} to {parts[1].strip()} showing {direction}")
    arrow_desc = " and ".join(arrows) if arrows else "arrows connecting the parts"

    prompt = (
        f"Create a simple coloring book page for young children showing a system model about "
        f"'{c['title']}'. The model has these parts: {model_desc}, connected by {arrow_desc}. "
        "Style: thick black outlines only, no colors, no shading, no gradients, "
        "simple geometric shapes with large clear labels inside them, "
        "big bold arrows connecting the shapes, kid-friendly cartoon style. "
        "White background, clean crisp lines. Each part should be in a rounded rectangle "
        "or circle with its name clearly written inside. "
        "Suitable for ages 5-8 to color in with crayons."
    )

    fn = f"{c['id']}-coloring.png"
    fp = os.path.join(img_dir, fn)
    if os.path.exists(fp):
        print(f"    [SKIP] {fn}")
        return fp

    print(f"  Generating coloring image: {fn}...")
    try:
        r = requests.post("https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
            json={"model": "google/gemini-2.5-flash-image",
                  "messages": [{"role": "user", "content": prompt}],
                  "modalities": ["image", "text"]},
            timeout=180)
        if r.status_code == 200:
            data = r.json()
            imgs = data.get("choices", [{}])[0].get("message", {}).get("images", [])
            if imgs:
                img = imgs[0]
                url = img.get("image_url", {}).get("url", "") if isinstance(img, dict) else ""
                if url.startswith("data:image"):
                    with open(fp, "wb") as f:
                        f.write(base64.b64decode(url.split(",")[1]))
                    total_cost += data.get("usage", {}).get("cost", 0)
                    print(f"    [OK] {fn}")
                    return fp
            print(f"    [!] No image in response")
            return None
        else:
            print(f"    [X] {r.status_code}: {r.text[:100]}")
            return None
    except Exception as e:
        print(f"    [X] {e}")
        return None


def make_coloring(c, out_dir, img_dir, grade_label):
    """Create coloring sheet DOCX."""
    lid = c["id"]
    doc = Document()

    # Set narrow margins
    for section in doc.sections:
        section.top_margin = DI(0.5)
        section.bottom_margin = DI(0.5)
        section.left_margin = DI(0.75)
        section.right_margin = DI(0.75)

    # Header
    p = doc.add_paragraph()
    r = p.add_run("ModelIt! Coloring Sheet"); r.bold = True
    r.font.size = DP(24); r.font.color.rgb = DMB
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p2 = doc.add_paragraph()
    r2 = p2.add_run(f"{c['title']}"); r2.bold = True
    r2.font.size = DP(18); r2.font.color.rgb = DBB
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p3 = doc.add_paragraph()
    r3 = p3.add_run(grade_label); r3.font.size = DP(12)
    r3.font.color.rgb = DR(0x66, 0x66, 0x66)
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Name/Date
    name_date(doc, wide_lines=True)

    # Coloring image
    img_path = os.path.join(img_dir, f"{lid}-coloring.png")
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_img = p_img.add_run()
        r_img.add_picture(img_path, width=DI(5.5))
    else:
        # Placeholder box
        drawing_box(doc, lines=12, prompt="[Coloring image will be placed here]")

    doc.add_paragraph()

    # Instructions
    desc = compose_coloring_desc(c) if "coloring_description" not in c else c["coloring_description"]
    hdr(doc, "Color It!", lv=2)
    p_desc = doc.add_paragraph()
    r_d = p_desc.add_run(desc); r_d.font.size = DP(14)

    doc.add_paragraph()

    # Color key for arrows
    hdr(doc, "Arrow Color Key:", lv=3)
    p_key = doc.add_paragraph()
    r_g = p_key.add_run("Green arrow (+) = Go together (both go up!)  ")
    r_g.font.size = DP(13); r_g.font.color.rgb = DGN; r_g.bold = True
    r_r = p_key.add_run("Red arrow (-) = Go opposite (one up, one down!)")
    r_r.font.size = DP(13); r_r.font.color.rgb = DRD; r_r.bold = True

    # Footer
    add_footer_line(doc, lid)

    fn = f"{lid}-Coloring-Sheet.docx"
    out = os.path.join(out_dir, fn)
    doc.save(out)
    print(f"  [OK] Coloring Sheet: {fn}")
    return out


# ══════════════════════════════════════════════════════════════
#  3. FIX THE SYSTEM ACTIVITY (G2-3) — DOCX
# ══════════════════════════════════════════════════════════════

def make_fix_activity(c, out_dir, grade_label):
    """Create Fix the System activity DOCX with 3 broken diagrams."""
    lid = c["id"]
    doc = Document()

    for section in doc.sections:
        section.top_margin = DI(0.6)
        section.bottom_margin = DI(0.5)
        section.left_margin = DI(0.75)
        section.right_margin = DI(0.75)

    add_modelit_header(doc, c["title"], lid, grade_label)

    hdr(doc, "Can You Fix It?", lv=1)
    p_intro = doc.add_paragraph()
    r_i = p_intro.add_run(
        "Oh no! These system models have mistakes! Look at each model carefully. "
        "Find the error, circle it, and write the correct answer."
    )
    r_i.font.size = DP(13)
    doc.add_paragraph()

    comps = c.get("components", [])
    rels = c.get("relationships", [])
    vocab = c.get("vocabulary", [])

    # ── Error 1: Wrong Direction (flip +/- on first relationship)
    hdr(doc, "Model 1: Wrong Direction!", lv=2)
    p1 = doc.add_paragraph()
    p1.add_run("One arrow has the WRONG sign. Find it and fix it!").font.size = DP(12)

    if rels:
        rel_str, sign, expl = rels[0]
        parts = rel_str.split(" to ")
        fr = parts[0].strip() if len(parts) >= 2 else "Part A"
        to = parts[1].strip() if len(parts) >= 2 else "Part B"
        wrong_sign = "- (opposite)" if "+" in sign else "+ (together)"
        correct_sign = "+ (together)" if "+" in sign else "- (opposite)"

        t = doc.add_table(rows=1, cols=3)
        t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
        cells = t.rows[0].cells
        cells[0].text = fr
        cells[1].text = f"  {wrong_sign} →  "
        cells[2].text = to
        for cell in cells:
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.size = DP(14); r.bold = True
            cell_shd(cell, HEX_LGRAY)

    doc.add_paragraph()
    wide_rbox(doc, lines=2, prompt="Circle the error and write the correct sign:")
    doc.add_paragraph()

    # ── Error 2: Wrong Category (flip external/internal on one component)
    hdr(doc, "Model 2: Wrong Category!", lv=2)
    p2 = doc.add_paragraph()
    p2.add_run("One part is in the WRONG category. Find it and move it!").font.size = DP(12)

    # Pick a component to miscategorize
    if len(comps) >= 2:
        swap_idx = 0  # swap the first component
        swap_name, swap_desc, swap_ext = comps[swap_idx]
        wrong_cat = "Changes by Itself (Inside)" if swap_ext else "We Control (Outside)"
        correct_cat = "We Control (Outside)" if swap_ext else "Changes by Itself (Inside)"

        # Build the model table with wrong categories
        t2 = doc.add_table(rows=len(comps) + 1, cols=2)
        t2.style = "Table Grid"; t2.alignment = WD_TABLE_ALIGNMENT.CENTER
        h_cells = t2.rows[0].cells
        h_cells[0].text = "Part Name"
        h_cells[1].text = "Category"
        cell_shd(h_cells[0], HEX_MB); cell_shd(h_cells[1], HEX_MB)
        for p in h_cells[0].paragraphs:
            for r in p.runs: r.font.color.rgb = DWH; r.bold = True
        for p in h_cells[1].paragraphs:
            for r in p.runs: r.font.color.rgb = DWH; r.bold = True

        for idx, (name, desc, is_ext) in enumerate(comps):
            row = t2.rows[idx + 1].cells
            row[0].text = name
            if idx == swap_idx:
                row[1].text = wrong_cat  # WRONG!
            else:
                row[1].text = "We Control (Outside)" if is_ext else "Changes by Itself (Inside)"
            for p in row[0].paragraphs:
                for r in p.runs: r.font.size = DP(12); r.bold = True
            for p in row[1].paragraphs:
                for r in p.runs: r.font.size = DP(12)

    doc.add_paragraph()
    wide_rbox(doc, lines=2, prompt=f"Which part is in the wrong category? Write where it should go:")
    doc.add_paragraph()

    # ── Error 3: Missing Part (blank out one component)
    hdr(doc, "Model 3: Missing Part!", lv=2)
    p3 = doc.add_paragraph()
    p3.add_run("One part of the model is missing! Use the Word Bank to fill it in.").font.size = DP(12)

    if len(comps) >= 2:
        missing_idx = len(comps) - 1  # hide the last component
        missing_name = comps[missing_idx][0]

        t3 = doc.add_table(rows=1, cols=3 if len(comps) >= 3 else 2)
        t3.style = "Table Grid"; t3.alignment = WD_TABLE_ALIGNMENT.CENTER
        cells3 = t3.rows[0].cells
        col = 0
        for idx, (name, desc, is_ext) in enumerate(comps):
            if col < len(cells3):
                if idx == missing_idx:
                    cells3[col].text = "???"
                    for p in cells3[col].paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        for r in p.runs:
                            r.font.size = DP(18); r.bold = True
                            r.font.color.rgb = DRD
                else:
                    cells3[col].text = name
                    for p in cells3[col].paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        for r in p.runs: r.font.size = DP(14); r.bold = True
                cell_shd(cells3[col], HEX_LGRAY)
                col += 1

    doc.add_paragraph()

    # Word bank with component names + distractors
    hdr(doc, "Word Bank:", lv=3)
    comp_names = [name for name, _, _ in comps]
    # Add distractors from vocabulary
    distractors = []
    for term, defn in vocab:
        if term not in comp_names:
            distractors.append(term)
    word_bank = comp_names + distractors[:2]  # add up to 2 distractors
    random.shuffle(word_bank)

    p_wb = doc.add_paragraph()
    for i, word in enumerate(word_bank):
        r_w = p_wb.add_run(f"  {word}  ")
        r_w.font.size = DP(14); r_w.bold = True
        if i < len(word_bank) - 1:
            r_s = p_wb.add_run("  |  ")
            r_s.font.size = DP(14); r_s.font.color.rgb = DR(0xCC, 0xCC, 0xCC)
    p_wb.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()
    wide_rbox(doc, lines=2, prompt="Write the missing part name and explain what it does:")

    # ── Page 2: Build Your Own ──
    doc.add_page_break()
    add_modelit_header(doc, c["title"], lid, grade_label)

    hdr(doc, "Build Your Own Model!", lv=1)
    p_build = doc.add_paragraph()
    p_build.add_run(
        "Now build the correct model from memory! Draw the parts in the boxes and "
        "draw arrows to show how they connect. Write + or - on each arrow."
    ).font.size = DP(13)

    doc.add_paragraph()

    # Empty model template boxes
    num_boxes = len(comps) if comps else 2
    t_build = doc.add_table(rows=1, cols=num_boxes)
    t_build.style = "Table Grid"; t_build.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i in range(num_boxes):
        cell = t_build.rows[0].cells[i]
        cell.text = "\n\n\n\n"
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cell_shd(cell, HEX_LGRAY)

    doc.add_paragraph()

    # Draw arrows instruction
    p_arrows = doc.add_paragraph()
    p_arrows.add_run("Draw arrows between the boxes above. Write + or - on each arrow.").font.size = DP(12)
    p_arrows.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()

    # Sentence frame
    frame = compose_sentence_frame(c)
    hdr(doc, "Complete the Sentence:", lv=2)
    p_frame = doc.add_paragraph()
    r_f = p_frame.add_run(frame)
    r_f.font.size = DP(16); r_f.bold = True; r_f.font.color.rgb = DBB

    wide_rbox(doc, lines=2)

    add_footer_line(doc, lid)

    fn = f"{lid}-Fix-the-System.docx"
    out = os.path.join(out_dir, fn)
    doc.save(out)
    print(f"  [OK] Fix the System: {fn}")
    return out


# ══════════════════════════════════════════════════════════════
#  4. INTERACTIVE NOTEBOOK INSERT (G2-3) — DOCX
# ══════════════════════════════════════════════════════════════

def make_notebook(c, out_dir, grade_label):
    """Create interactive notebook insert DOCX (landscape, foldable)."""
    lid = c["id"]
    doc = Document()

    # Set to landscape
    section = doc.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = DI(11)
    section.page_height = DI(8.5)
    section.top_margin = DI(0.4)
    section.bottom_margin = DI(0.4)
    section.left_margin = DI(0.5)
    section.right_margin = DI(0.5)

    comps = c.get("components", [])
    rels = c.get("relationships", [])
    vocab = c.get("vocabulary", [])
    frame = compose_sentence_frame(c)

    # ── Cut line indicator at top
    p_cut = doc.add_paragraph()
    r_cut = p_cut.add_run("- - - - - - - - - - - - - - - - - - - - - - - - - - - "
                           "CUT ALONG DASHED LINE - - - - - - - - - - - - - - - - - - - - - - - - - -")
    r_cut.font.size = DP(8); r_cut.font.color.rgb = DR(0x99, 0x99, 0x99)
    p_cut.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ── Main 2-column table (FRONT | INSIDE)
    t = doc.add_table(rows=1, cols=2)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Set column widths
    for cell in t.rows[0].cells:
        cell.width = DI(4.8)

    # ── LEFT SIDE (FRONT - visible when glued in) ──
    front = t.rows[0].cells[0]

    # Title
    p_t = front.add_paragraph()
    r_t = p_t.add_run("ModelIt! Interactive Notebook")
    r_t.bold = True; r_t.font.size = DP(14); r_t.font.color.rgb = DMB
    p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_title = front.add_paragraph()
    r_title = p_title.add_run(c["title"])
    r_title.bold = True; r_title.font.size = DP(16); r_title.font.color.rgb = DBB
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_grade = front.add_paragraph()
    r_grade = p_grade.add_run(f"{grade_label}  |  {c.get('ngss', '')}")
    r_grade.font.size = DP(9); r_grade.font.color.rgb = DR(0x66, 0x66, 0x66)
    p_grade.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Model diagram area
    p_model_h = front.add_paragraph()
    r_mh = p_model_h.add_run("My System Model (color it in!)")
    r_mh.bold = True; r_mh.font.size = DP(11); r_mh.font.color.rgb = DN

    # Component boxes with arrows
    num_comps = len(comps)
    if num_comps > 0:
        inner_t = front.add_table(rows=3, cols=num_comps)
        # Top row: labels (Outside/Inside)
        for idx, (name, desc, is_ext) in enumerate(comps):
            cell = inner_t.rows[0].cells[idx]
            p = cell.add_paragraph()
            label = "OUTSIDE" if is_ext else "INSIDE"
            r = p.add_run(label)
            r.font.size = DP(7); r.bold = True
            r.font.color.rgb = DOG if is_ext else DMB
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Middle row: component names (in boxes to color)
        for idx, (name, desc, is_ext) in enumerate(comps):
            cell = inner_t.rows[1].cells[idx]
            p = cell.add_paragraph()
            r = p.add_run(name)
            r.font.size = DP(11); r.bold = True; r.font.color.rgb = DN
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cell_shd(cell, HEX_LGRAY)

        # Bottom row: arrow indicators
        for idx in range(num_comps):
            cell = inner_t.rows[2].cells[idx]
            # Find relationships from this component
            comp_name = comps[idx][0]
            arrow_text = ""
            for rel_str, sign, _ in rels:
                parts = rel_str.split(" to ")
                if len(parts) == 2 and parts[0].strip() == comp_name:
                    rtype = "+" if "+" in sign else "-"
                    arrow_text += f"→ {rtype} → {parts[1].strip()} "
            if arrow_text:
                p = cell.add_paragraph()
                r = p.add_run(arrow_text.strip())
                r.font.size = DP(8); r.font.color.rgb = DR(0x66, 0x66, 0x66)
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Color key
    p_key = front.add_paragraph()
    r_k1 = p_key.add_run("Color Key: ")
    r_k1.font.size = DP(9); r_k1.bold = True
    r_k2 = p_key.add_run("+ = green arrow  ")
    r_k2.font.size = DP(9); r_k2.font.color.rgb = DGN; r_k2.bold = True
    r_k3 = p_key.add_run("- = red arrow")
    r_k3.font.size = DP(9); r_k3.font.color.rgb = DRD; r_k3.bold = True

    # Fold line indicator
    p_fold = front.add_paragraph()
    r_fold = p_fold.add_run("--- FOLD LINE ---")
    r_fold.font.size = DP(8); r_fold.font.color.rgb = DR(0xAA, 0xAA, 0xAA)
    p_fold.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ── RIGHT SIDE (INSIDE - hidden when folded) ──
    inside = t.rows[0].cells[1]

    p_ih = inside.add_paragraph()
    r_ih = p_ih.add_run("What I Learned")
    r_ih.bold = True; r_ih.font.size = DP(14); r_ih.font.color.rgb = DMB
    p_ih.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Vocabulary
    p_vocab_h = inside.add_paragraph()
    r_vh = p_vocab_h.add_run("Key Words:")
    r_vh.bold = True; r_vh.font.size = DP(11); r_vh.font.color.rgb = DN

    for term, defn in vocab[:4]:  # max 4 terms
        p_v = inside.add_paragraph()
        r_term = p_v.add_run(f"{term}: ")
        r_term.bold = True; r_term.font.size = DP(10); r_term.font.color.rgb = DBB
        r_def = p_v.add_run(defn)
        r_def.font.size = DP(9)

    inside.add_paragraph()

    # Sentence frame
    p_sf_h = inside.add_paragraph()
    r_sfh = p_sf_h.add_run("Complete the Sentence:")
    r_sfh.bold = True; r_sfh.font.size = DP(10); r_sfh.font.color.rgb = DN
    p_sf = inside.add_paragraph()
    r_sf = p_sf.add_run(frame)
    r_sf.font.size = DP(11); r_sf.bold = True; r_sf.font.color.rgb = DBB

    inside.add_paragraph()

    # Writing lines
    p_wh = inside.add_paragraph()
    r_wh = p_wh.add_run("I learned that...")
    r_wh.bold = True; r_wh.font.size = DP(10); r_wh.font.color.rgb = DN
    for _ in range(3):
        p_line = inside.add_paragraph()
        r_line = p_line.add_run("_" * 55)
        r_line.font.size = DP(11); r_line.font.color.rgb = DR(0xCC, 0xCC, 0xCC)
        p_line.paragraph_format.space_after = DP(4)
        p_line.paragraph_format.line_spacing = DP(24)

    # Glue tab
    p_glue = inside.add_paragraph()
    r_glue = p_glue.add_run("-- GLUE TAB (apply glue here to attach to notebook) --")
    r_glue.font.size = DP(7); r_glue.font.color.rgb = DR(0xAA, 0xAA, 0xAA)
    p_glue.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ── Bottom cut line
    p_cut2 = doc.add_paragraph()
    r_cut2 = p_cut2.add_run("- - - - - - - - - - - - - - - - - - - - - - - - - - - "
                             "CUT ALONG DASHED LINE - - - - - - - - - - - - - - - - - - - - - - - - - -")
    r_cut2.font.size = DP(8); r_cut2.font.color.rgb = DR(0x99, 0x99, 0x99)
    p_cut2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    fn = f"{lid}-Interactive-Notebook.docx"
    out = os.path.join(out_dir, fn)
    doc.save(out)
    print(f"  [OK] Interactive Notebook: {fn}")
    return out


# ══════════════════════════════════════════════════════════════
#  5. READING PASSAGE (G2-3) — DOCX
# ══════════════════════════════════════════════════════════════

def compose_passage(c):
    """Build a 150-200 word reading passage from lesson data."""
    title = c.get("title", "")
    big_q = c.get("big_question", title)
    bg_intro = c.get("background_intro", "")
    bg_sections = c.get("background_sections", [])
    answer = c.get("answer", "")

    # Hook
    hook = f"Have you ever wondered: {big_q} Let's find out!"

    # Body paragraph 1 - from background intro or first section
    body1 = ""
    if bg_sections and len(bg_sections) >= 1:
        section_title, section_text = bg_sections[0]
        # Take first ~2 sentences (simplify for kids)
        sentences = section_text.split(".")
        body1 = ". ".join(s.strip() for s in sentences[:2] if s.strip()) + "."
    elif bg_intro:
        sentences = bg_intro.split(".")
        body1 = ". ".join(s.strip() for s in sentences[:2] if s.strip()) + "."

    # Body paragraph 2 - from second section if available
    body2 = ""
    if len(bg_sections) >= 2:
        section_title, section_text = bg_sections[1]
        sentences = section_text.split(".")
        body2 = ". ".join(s.strip() for s in sentences[:2] if s.strip()) + "."

    # Closing - simplified answer
    closing = ""
    if answer:
        sentences = answer.split(".")
        closing = "Now you know! " + ". ".join(s.strip() for s in sentences[:2] if s.strip()) + "."

    # Combine and truncate to ~200 words
    passage = f"{hook}\n\n{body1}"
    if body2:
        passage += f"\n\n{body2}"
    passage += f"\n\n{closing}"

    # Trim if too long
    words = passage.split()
    if len(words) > 220:
        passage = " ".join(words[:200]) + "..."

    return passage


def make_reading(c, out_dir, grade_label):
    """Create reading passage DOCX."""
    lid = c["id"]
    doc = Document()

    for section in doc.sections:
        section.top_margin = DI(0.6)
        section.bottom_margin = DI(0.5)
        section.left_margin = DI(0.75)
        section.right_margin = DI(0.75)

    add_modelit_header(doc, c["title"], lid, grade_label)

    # Title tied to big question
    big_q = c.get("big_question", c["title"])
    hdr(doc, big_q, lv=1)
    doc.add_paragraph()

    # Name/Date
    name_date(doc)

    # Reading passage
    passage = compose_passage(c)
    paragraphs = passage.split("\n\n")
    for para_text in paragraphs:
        if para_text.strip():
            p = doc.add_paragraph()
            r = p.add_run(para_text.strip())
            r.font.size = DP(13)
            p.paragraph_format.space_after = DP(8)
            p.paragraph_format.line_spacing = DP(22)

    doc.add_paragraph()

    # Fun Fact sidebar
    misconceptions = c.get("misconceptions", [])
    if misconceptions:
        misc_text, reality, _ = misconceptions[0]

        t_fun = doc.add_table(rows=1, cols=1)
        t_fun.style = "Table Grid"; t_fun.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = t_fun.rows[0].cells[0]
        cell_shd(cell, "FFF8E1")

        p_fun_h = cell.add_paragraph()
        r_fh = p_fun_h.add_run("Fun Fact!")
        r_fh.bold = True; r_fh.font.size = DP(14); r_fh.font.color.rgb = DOG
        p_fun_h.alignment = WD_ALIGN_PARAGRAPH.CENTER

        p_fun = cell.add_paragraph()
        r_fb = p_fun.add_run(f"Some people think: \"{misc_text}\" — but that's not true! {reality}")
        r_fb.font.size = DP(11)

    doc.add_paragraph()

    # Think About It (NOT quiz-style — open-ended)
    hdr(doc, "Think About It", lv=2)

    # Build 2 open-ended questions from lesson data
    questions = []
    if c.get("big_question"):
        questions.append(f"What surprised you most about learning {c['big_question'].lower().rstrip('?')}?")
    if c.get("discoveries") and len(c["discoveries"]) >= 1:
        questions.append(f"How could you explain what you learned to a friend or family member?")

    # Fallback questions
    if len(questions) < 2:
        questions.append("What do you think would happen if you tried this at home?")

    for i, q in enumerate(questions[:2], 1):
        p_q = doc.add_paragraph()
        r_q = p_q.add_run(f"{i}. {q}")
        r_q.font.size = DP(13); r_q.bold = True
        # Writing lines
        for _ in range(3):
            p_line = doc.add_paragraph()
            r_line = p_line.add_run("_" * 75)
            r_line.font.size = DP(12); r_line.font.color.rgb = DR(0xCC, 0xCC, 0xCC)
            p_line.paragraph_format.space_after = DP(4)
            p_line.paragraph_format.line_spacing = DP(24)
        doc.add_paragraph()

    add_footer_line(doc, lid)

    fn = f"{lid}-Reading-Passage.docx"
    out = os.path.join(out_dir, fn)
    doc.save(out)
    print(f"  [OK] Reading Passage: {fn}")
    return out


# ══════════════════════════════════════════════════════════════
#  6. PARENT-HOME CONNECTION (G2-3) — DOCX
# ══════════════════════════════════════════════════════════════

def make_home_connection(c, out_dir, grade_label):
    """Create parent-home connection single-page take-home sheet."""
    lid = c["id"]
    doc = Document()

    for section in doc.sections:
        section.top_margin = DI(0.5)
        section.bottom_margin = DI(0.4)
        section.left_margin = DI(0.75)
        section.right_margin = DI(0.75)

    # ── Header ──
    p_brand = doc.add_paragraph()
    r_brand = p_brand.add_run("ModelIt! Family Science Connection")
    r_brand.bold = True; r_brand.font.size = DP(20); r_brand.font.color.rgb = DMB
    p_brand.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run(f"{grade_label}  |  {lid}")
    r_sub.font.size = DP(10); r_sub.font.color.rgb = DR(0x66, 0x66, 0x66)
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()

    # ── Dear Family intro ──
    p_dear = doc.add_paragraph()
    r_d = p_dear.add_run(f"Dear Family, today your child learned about: {c['title']}!")
    r_d.font.size = DP(13); r_d.italic = True

    doc.add_paragraph()

    # ── Section 1: Talk About It ──
    t1 = doc.add_table(rows=1, cols=1)
    t1.style = "Table Grid"
    cell1 = t1.rows[0].cells[0]
    cell_shd(cell1, HEX_LGRAY)

    p1h = cell1.add_paragraph()
    r1h = p1h.add_run("Talk About It")
    r1h.bold = True; r1h.font.size = DP(14); r1h.font.color.rgb = DOG

    big_q = c.get("big_question", c["title"])
    p1b = cell1.add_paragraph()
    r1b = p1b.add_run(f"Ask your child: \"{big_q}\" — and listen to what they say! "
                       "They have been exploring this question in class using a system model.")
    r1b.font.size = DP(11)

    doc.add_paragraph()

    # ── Section 2: Try It at Home ──
    t2 = doc.add_table(rows=1, cols=1)
    t2.style = "Table Grid"
    cell2 = t2.rows[0].cells[0]
    cell_shd(cell2, "E8F5E9")

    p2h = cell2.add_paragraph()
    r2h = p2h.add_run("Try It at Home")
    r2h.bold = True; r2h.font.size = DP(14); r2h.font.color.rgb = DGN

    scenarios = c.get("scenarios", [])
    if scenarios:
        scen_name, scen_desc = scenarios[0][:2]
        p2b = cell2.add_paragraph()
        r2b = p2b.add_run(f"Here's a simple activity you can do together (no special materials needed!):\n\n"
                           f"{scen_desc}")
        r2b.font.size = DP(11)
    else:
        p2b = cell2.add_paragraph()
        r2b = p2b.add_run("Try observing this topic together at home or on a walk. "
                           "Talk about what you notice and why it might happen.")
        r2b.font.size = DP(11)

    doc.add_paragraph()

    # ── Section 3: Words to Know ──
    t3 = doc.add_table(rows=1, cols=1)
    t3.style = "Table Grid"
    cell3 = t3.rows[0].cells[0]
    cell_shd(cell3, "FFF8E1")

    p3h = cell3.add_paragraph()
    r3h = p3h.add_run("Words to Know")
    r3h.bold = True; r3h.font.size = DP(14); r3h.font.color.rgb = DBB

    vocab = c.get("vocabulary", [])
    for term, defn in vocab[:4]:  # max 4 terms
        p_v = cell3.add_paragraph()
        r_term = p_v.add_run(f"{term}: ")
        r_term.bold = True; r_term.font.size = DP(11); r_term.font.color.rgb = DBB
        r_def = p_v.add_run(defn)
        r_def.font.size = DP(11)

    doc.add_paragraph()

    # ── Section 4: Keep Exploring ──
    t4 = doc.add_table(rows=1, cols=1)
    t4.style = "Table Grid"
    cell4 = t4.rows[0].cells[0]
    cell_shd(cell4, "EDE7F6")

    p4h = cell4.add_paragraph()
    r4h = p4h.add_run("Keep Exploring")
    r4h.bold = True; r4h.font.size = DP(14); r4h.font.color.rgb = DR(0x67, 0x3D, 0xE6)

    cross_curr = c.get("cross_curr", [])
    if cross_curr:
        for subject, connection in cross_curr[:2]:  # max 2
            p_cc = cell4.add_paragraph()
            r_subj = p_cc.add_run(f"{subject}: ")
            r_subj.bold = True; r_subj.font.size = DP(11)
            r_conn = p_cc.add_run(connection)
            r_conn.font.size = DP(11)
    else:
        p_cc = cell4.add_paragraph()
        r_cc = p_cc.add_run("Go on a nature walk and look for examples of what we learned about. "
                             "Talk about what you see!")
        r_cc.font.size = DP(11)

    doc.add_paragraph()

    # ── Footer ──
    frame = compose_sentence_frame(c)
    p_footer = doc.add_paragraph()
    r_ask = p_footer.add_run(f"Ask your child to complete: \"{frame}\"")
    r_ask.font.size = DP(12); r_ask.bold = True; r_ask.font.color.rgb = DBB
    p_footer.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_brand2 = doc.add_paragraph()
    r_b2 = p_brand2.add_run(f"ModelIt! {lid}")
    r_b2.font.size = DP(8); r_b2.font.color.rgb = DR(0x99, 0x99, 0x99)
    p_brand2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    fn = f"{lid}-Parent-Home-Connection.docx"
    out = os.path.join(out_dir, fn)
    doc.save(out)
    print(f"  [OK] Parent-Home Connection: {fn}")
    return out


# ══════════════════════════════════════════════════════════════
#  MAIN ORCHESTRATOR
# ══════════════════════════════════════════════════════════════

def load_lessons(grade_key):
    """Dynamically import lesson data for a grade."""
    cfg = GRADE_CONFIG[grade_key]
    mod_name = cfg["data"]
    mod = importlib.import_module(mod_name)
    return mod.ALL_LESSONS


def generate_supplementary(c, grade_key):
    """Generate all supplementary materials for one lesson."""
    cfg = GRADE_CONFIG[grade_key]
    lid = c["id"]
    base_dir = os.path.join(SCRIPT_DIR, '..', 'materials', cfg["dir"])
    out_dir = os.path.join(base_dir, lid)
    img_dir = os.path.join(out_dir, "images")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)

    grade_label = cfg["label"]
    count = 0

    print(f"\n{'-'*50}")
    print(f"  {lid}: {c['title']} ({grade_label})")
    print(f"{'-'*50}")

    # K-2: Model Explorer Game
    if cfg["game"]:
        write_game(c, out_dir, cfg)
        count += 1

    # K-2: Coloring Sheet (with AI image generation)
    if cfg["coloring"]:
        gen_coloring_img(c, img_dir)
        make_coloring(c, out_dir, img_dir, grade_label)
        count += 1
        time.sleep(3)  # rate limit for API

    # G2-3: Fix the System
    if cfg["fix"]:
        make_fix_activity(c, out_dir, grade_label)
        count += 1

    # G2-3: Interactive Notebook
    if cfg["notebook"]:
        make_notebook(c, out_dir, grade_label)
        count += 1

    # G2-3: Reading Passage
    if cfg["reading"]:
        make_reading(c, out_dir, grade_label)
        count += 1

    # G2-3: Parent-Home Connection
    if cfg["home"]:
        make_home_connection(c, out_dir, grade_label)
        count += 1

    print(f"  [{count} files created for {lid}]")
    return count


def run_grade(grade_key):
    """Generate supplementary materials for all lessons in a grade."""
    cfg = GRADE_CONFIG[grade_key]
    lessons = load_lessons(grade_key)

    # Calculate expected output
    types = []
    if cfg["game"]: types.append("Game")
    if cfg["coloring"]: types.append("Coloring")
    if cfg["fix"]: types.append("Fix Activity")
    if cfg["notebook"]: types.append("Notebook")
    if cfg["reading"]: types.append("Reading")
    if cfg["home"]: types.append("Home Connection")

    print("\n" + "=" * 60)
    print(f"  ModelIt! Supplementary Materials - {cfg['label']}")
    print(f"  {len(lessons)} lessons × {len(types)} types = {len(lessons) * len(types)} files")
    print(f"  Types: {', '.join(types)}")
    print("=" * 60)

    for lesson in lessons:
        print(f"  - {lesson['id']}: {lesson['title']}")
    print()

    start_time = time.time()
    total_files = 0

    for i, lesson in enumerate(lessons, 1):
        print(f"\n[{i}/{len(lessons)}] Processing {lesson['id']}...")
        total_files += generate_supplementary(lesson, grade_key)

    elapsed = time.time() - start_time
    print("\n" + "=" * 60)
    print(f"  BATCH COMPLETE: {cfg['label']}")
    print("=" * 60)
    print(f"  Lessons processed: {len(lessons)}")
    print(f"  Files created: {total_files}")
    print(f"  Total time: {elapsed / 60:.1f} minutes")
    if cfg["coloring"]:
        print(f"  Estimated image cost: ${total_cost:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_supplementary_K3.py [K|1|2|3|all]")
        print()
        print("  K    Kindergarten: game + coloring")
        print("  1    Grade 1: game + coloring")
        print("  2    Grade 2: game + coloring + fix + notebook + reading + home")
        print("  3    Grade 3: fix + notebook + reading + home")
        print("  all  All grades")
        sys.exit(1)

    grade = sys.argv[1].upper()
    if grade == "ALL":
        for g in ["K", "1", "2", "3"]:
            run_grade(g)
    elif grade in GRADE_CONFIG:
        run_grade(grade)
    else:
        print(f"Unknown grade: {grade}. Use K, 1, 2, 3, or all.")
        sys.exit(1)
