# Wildfire Simulation — "When Trees Become Matches"

Interactive Unity simulation for CAST Science lesson G05-L01.

Students model why California experiences devastating wildfires by manipulating Rainfall and Wind to observe how Earth systems interact to create fire conditions.

## The Scientific Model

```
Rainfall ─(negative)─→ Dry Vegetation ─(positive)─→ Fire Spread ←─(positive)─ Wind
```

- **Less rain** → more dry vegetation (plants become fuel)
- **More dry fuel** → fire spreads faster
- **More wind** → fire spreads further (embers fly ahead)

## How to Open

1. Open **Unity Hub**
2. Click **Open** → navigate to this `WildfireSimulation` folder
3. Select your Unity editor (2022.3+ or Unity 6)
4. Once the project opens, go to menu: **CAST Science → Build Wildfire Scene**
5. Press **Play (▶)** to start

## Controls

| Control | What It Does |
|---------|-------------|
| **Rainfall slider** | Controls precipitation (0-100%) |
| **Wind slider** | Controls wind strength (0-100%) |
| **START FIRE** | Ignites vegetation on the left edge |
| **DROUGHT** | Sets rainfall to 0% (simulates months without rain) |
| **SANTA ANA** | Drought + 95% wind (extreme California fire weather) |
| **RESET FOREST** | Restores healthy green forest |
| **Scroll wheel** | Zoom in/out |
| **Right-click drag** | Pan camera |

## Lesson Guide

The built-in lesson guide (left panel) walks students through 9 steps:
1. Observe healthy forest
2. Create a drought
3. Watch vegetation dry out
4. Start a fire
5. Add Santa Ana winds
6. Discover the cascade
7. Recovery with rain
8. Free exploration challenges

## NGSS Alignment

**5-ESS2-1**: Develop a model using an example to describe ways the geosphere, biosphere, hydrosphere, and/or atmosphere interact.

## Files

```
Assets/
├── Scripts/
│   ├── SimulationManager.cs    # Core simulation engine
│   ├── CameraController.cs     # Zoom and pan
│   └── LessonGuide.cs          # Step-by-step student guide
└── Editor/
    └── SceneBuilder.cs         # Auto-builds the scene (menu tool)
```
