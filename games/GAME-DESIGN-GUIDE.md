# CAST Science Games — Grade 5 Design Guide

## Philosophy

Every game is **fun-first**. No quizzes, no lessons, no "click to learn." Science is embedded invisibly into mechanics — students build intuition through play, not instruction. Think Zelda's cooking system, not Khan Academy.

**The Rule:** If you removed the science label, would a kid still want to play this on their own time? If not, redesign it.

## Technical Standard (Match EMBER Quality)

- Single HTML file, zero dependencies, zero build steps
- HTML5 Canvas 2D rendering with requestAnimationFrame + delta-time
- Procedural audio via Web Audio API (no sound files)
- Typed arrays for performance (particles, grids)
- State machine pattern: TITLE → HOW_TO → SELECT/PLAY → COMPLETE/OVER
- Responsive canvas with DPR scaling
- Multi-input: Keyboard (arrows/WASD) + mouse + touch (virtual joystick where needed)
- localStorage for high scores and progression
- Particle systems with object pooling (600-800 max)
- Screen shake, floating text, visual juice
- Mobile-ready with landscape orientation prompt
- Target: 1500-2500 lines per game
- Deploy: GitHub Pages, instant load (<100KB)

## Color Palettes (Each Game Gets Its Own)

Every game has a unique visual identity. No two games should look alike.

## The 8 Games

### 1. EMBER — Wildfire Growth Arcade (L01: When Trees Become Matches)
- **Genre:** Snake/Katamari growth arcade
- **Style:** Deep indigo/sunset, glowing fire particles, flat terrain
- **You are:** A wildfire. Grow huge by eating dry fuel. Dodge rain.
- **Science:** Drought → dry vegetation → fire spread ← wind
- **Status:** COMPLETE ✅
- **File:** `games/wildfire/ember.html`

### 2. DECOMPOSE — Tower Defense (L02: Nature's Recycling System)
- **Genre:** Tower Defense (Plants vs Zombies meets ecology)
- **Style:** Rich forest floor, earthy greens/browns, cute stylized decomposers
- **You are:** Forest floor manager. Place decomposers to break down falling dead matter.
- **Mechanics:**
  - Waves of dead leaves, branches, dead animals fall from top
  - Place decomposer units on the forest floor: Mushrooms (medium speed, area), Worms (fast, single target), Bacteria (slow, massive area)
  - Each decomposer costs "nutrient points" earned from successful decomposition
  - Dead matter that piles too high blocks sunlight → game over
  - Soil moisture meter: rain events boost all decomposers, drought slows them
  - Nutrients released flow to plants at bottom that visibly grow taller
  - 5 waves per level, 5 levels (spring → summer → fall → winter → mixed)
- **Science:** Decomposer types, moisture dependency, nutrient cycling, matter doesn't disappear
- **Palette:** Forest greens (#3B5B3A), rich soil browns (#5C3D2E), mushroom cream (#E8D5B7), worm pink (#D4848C), bacteria teal (#5BA89F)
- **File:** `games/decompose/index.html`

### 3. PHOTON — Endless Runner (L03: Powered by the Sun)
- **Genre:** Geometry Dash / Temple Run style rhythm runner
- **Style:** Bright synthwave neon, energy trails, pulsing colors
- **You are:** A photon of light racing from the sun through a food chain.
- **Mechanics:**
  - Side-scrolling auto-runner, tap/click to jump, hold to glide
  - Phase 1: Race through space as sunlight, dodge asteroids/clouds
  - Phase 2: Hit a leaf → become plant energy (green), collect nutrients
  - Phase 3: Caterpillar eats plant → become animal energy (yellow), faster
  - Phase 4: Bird eats caterpillar → become predator energy (red), fastest
  - Each transfer: energy bar drops to 10% (the 10% rule!) — you must collect more
  - Miss collections → energy runs out → game over
  - Obstacles change per phase: clouds → thorns → predators → humans
  - Combo: collect without missing = score multiplier
  - 5 levels with different biomes (grassland, ocean, desert, rainforest, arctic)
- **Science:** Sun → photosynthesis → food chain, 10% energy transfer rule, why animals need so much food
- **Palette:** Solar gold (#FFD700), leaf green (#00E676), caterpillar yellow (#FFEB3B), bird crimson (#FF1744), space indigo (#1A0A3E)
- **File:** `games/photon/index.html`

### 4. AQUIFER — Puzzle Strategy (L04: Earth's Hidden Water)
- **Genre:** Pipe puzzle / resource management (Mini Motorways meets water cycle)
- **Style:** Clean isometric, watercolor blues, infographic-inspired
- **You are:** Water cycle controller. Keep cities alive with freshwater.
- **Mechanics:**
  - Top-down map with cities, oceans, glaciers, rivers, aquifers
  - Drag cloud paths to create rain over land (not ocean — wasted!)
  - Build channels to route water from rain → reservoir → city
  - Temperature gauge: higher = more evaporation = less water reaches cities
  - 97% of water is ocean (visible but unusable), 2% is ice (locked), only 1% accessible
  - Cities grow and demand more water over time
  - Drought events: temperature spikes, evaporation surges
  - Ice caps: can "unlock" glacial melt but it's temporary and causes flooding
  - 5 scenarios: coastal, inland, arctic, desert, mega-city
  - Star rating based on efficiency (water wasted vs delivered)
- **Science:** Water distribution (97/2/1 split), evaporation, precipitation, freshwater scarcity
- **Palette:** Ocean deep (#1B3A5C), fresh water (#4FC3F7), ice white (#E3F2FD), desert amber (#FFB74D), city gray (#546E7A)
- **File:** `games/aquifer/index.html`

### 5. PHASE SHIFT — Physics Platformer (L05: The Disappearing Act)
- **Genre:** Puzzle platformer (like Celeste meets state-of-matter switching)
- **Style:** Clean vector art, smooth transitions, satisfying physics
- **You are:** A cluster of H₂O molecules. Shift between ice, water, and steam to navigate.
- **Mechanics:**
  - Press 1/2/3 (or swipe gestures) to switch states:
    - ICE: Heavy, slides on slopes, can stack/bridge gaps, breaks fragile floors
    - WATER: Flows through narrow gaps, fills containers, moves at medium speed
    - STEAM: Floats upward, passes through grates, blown by fans, lightest
  - Mass counter ALWAYS visible — never changes regardless of state (the core lesson)
  - Temperature zones on map: hot zones force steam, cold zones force ice
  - Puzzle elements: pressure plates (need ice weight), pipes (need water flow), vents (need steam rise)
  - Collect all molecule pickups in each level to complete it
  - 25 short levels across 5 worlds (5 levels each)
  - World themes: Kitchen, Arctic, Volcano, Laboratory, Cloud City
- **Science:** Conservation of mass, states of matter, phase transitions don't change mass
- **Palette:** Ice crystal (#B3E5FC), water blue (#2196F3), steam white (#F5F5F5), hot zone red (#FF5722), cold zone cyan (#00BCD4)
- **File:** `games/phase-shift/index.html`

### 6. CARBON — Idle Growth Sim (L06: Where Does a Tree's Mass Come From?)
- **Genre:** Idle/clicker growth simulation (Cookie Clicker meets botany)
- **Style:** Side-view growing tree, beautiful gradient skies, seasons changing
- **You are:** A redwood seedling. Absorb CO₂ from the air to grow into a giant.
- **Mechanics:**
  - CO₂ molecules float across the screen — tap/click leaves to catch them
  - Each CO₂ absorbed adds to tree mass (visible counter: "Mass from AIR: 95%")
  - Tree visibly grows: seedling → sapling → young tree → mature → ancient giant
  - Upgrade system (spend accumulated carbon):
    - More leaves (bigger catch area)
    - Deeper roots (stability in storms, tiny soil nutrients = "Mass from SOIL: 5%")
    - Thicker trunk (survives storms)
    - Wider canopy (shade out competitors)
  - Day/night cycle: photosynthesis only during day (respiration at night costs carbon!)
  - Seasonal events: spring growth boost, summer drought, fall leaf drop, winter dormancy
  - Storm events: high wind can break branches (lose mass) if trunk too thin
  - Goal: grow from 1g seedling to 1,000,000g (1 metric ton) giant
  - Prestige system: "plant a new seed" with bonuses
- **Science:** 95% of tree mass comes from CO₂ in air (not soil!), photosynthesis, carbon storage
- **Palette:** Bark brown (#5D4037), leaf green (#4CAF50), CO₂ gray (#90A4AE), sky blue (#87CEEB), soil dark (#3E2723), sunset (#FF7043)
- **File:** `games/carbon/index.html`

### 7. MYCELIUM — Network Strategy (L07: The Mushroom Network Under Your Feet)
- **Genre:** Network builder / logistics (Mini Metro meets underground ecology)
- **Style:** Split-view forest/underground, ethereal mycelium glow, organic shapes
- **You are:** The Wood Wide Web. Connect trees with fungal threads to keep the forest alive.
- **Mechanics:**
  - Top half: forest canopy view with trees of varying health (green → yellow → red)
  - Bottom half: underground view with root systems and your mycelium threads
  - Click-drag to grow mycelium connections between tree roots
  - Healthy trees produce nutrient packets (green dots)
  - Sick/shaded trees need nutrients (pulse red)
  - Route nutrients through your network from healthy → needy trees
  - Network costs energy to maintain (fungal metabolism) — you take a small cut (mutualism!)
  - Events: drought (connections thin, transfer slower), logging (tree removed, network broken), seasons
  - If 3+ trees die, forest collapses → game over
  - Mother trees: ancient large trees that produce extra nutrients for the network
  - 5 forest scenarios: young plantation, old growth, mixed forest, drought-stressed, logged
- **Science:** Mycorrhizal networks, mutualism, nutrient sharing, ecosystem resilience
- **Palette:** Underground purple (#2C1654), mycelium glow (#E1BEE7), nutrient green (#69F0AE), root brown (#795548), canopy emerald (#2E7D32)
- **File:** `games/mycelium/index.html`

### 8. SOAP STRIKE — Arena Action (L08: How Soap Destroys Viruses)
- **Genre:** Arena action / twin-stick shooter (Vampire Survivors meets microbiology)
- **Style:** Microscopic neon world, cell-shaded, vibrant pops and bursts
- **You are:** A soap molecule. Ram into viruses to tear their membranes apart.
- **Mechanics:**
  - Top-down arena (water droplet)
  - Move with WASD/arrows, auto-attack nearby viruses
  - Your molecule has two ends: hydrophilic head (blue, anchors in water) and hydrophobic tail (yellow, grabs fat)
  - Approach viruses tail-first to grab their lipid membrane
  - Pull away to rip the membrane open — virus pops in satisfying burst
  - Wrong angle (head-first) = bounce off, take damage
  - More soap molecules join your squad over time (they orbit you)
  - Bigger squad = more simultaneous attacks
  - Virus types: small (1 hit), medium (3 hits, shoots proteins), large (5 hits, spawns small on damage)
  - Water level: if arena "dries," you slow down (soap needs water!)
  - Wash timer: survive waves of increasing virus count
  - 5 levels: hand washing (20 seconds!), kitchen counter, hospital, school desk, phone screen
- **Science:** Soap amphiphilic structure, lipid membrane destruction, water as medium, 20-second wash rule
- **Palette:** Water droplet (#E3F2FD), soap yellow (#FFD54F), virus red (#EF5350), membrane green (#66BB6A), protein purple (#AB47BC)
- **File:** `games/soap-strike/index.html`

---

## Design Variety Matrix

| Game | Genre | Camera | Speed | Complexity | Visual Style |
|------|-------|--------|-------|------------|-------------|
| EMBER | Growth arcade | Top-down grid | Fast | Medium | Dark sunset, fire glow |
| DECOMPOSE | Tower defense | Side-view lanes | Medium | Medium-High | Forest floor, earthy |
| PHOTON | Endless runner | Side-scroll | Fast | Low-Medium | Neon synthwave |
| AQUIFER | Puzzle strategy | Top-down map | Slow-Medium | High | Isometric watercolor |
| PHASE SHIFT | Puzzle platformer | Side-view | Medium | Medium | Clean vector, physics |
| CARBON | Idle growth sim | Side-view tree | Slow | Low-Medium | Gradient sky, botanical |
| MYCELIUM | Network strategy | Split view | Medium | Medium-High | Ethereal underground glow |
| SOAP STRIKE | Arena action | Top-down arena | Fast | Medium | Microscopic neon |

**No two games share the same genre, camera angle, speed feel, or visual style.**

---

## Deployment

All games deploy to GitHub Pages at:
```
https://alexandriasworld1234-source.github.io/cast-science-resources/games/{folder}/index.html
```

Exception: EMBER lives at `games/wildfire/ember.html` (legacy path).

## Game Index

A master game index page should be created at `games/index.html` linking to all 8 games with thumbnails and descriptions.
