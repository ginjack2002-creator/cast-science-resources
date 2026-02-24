using UnityEngine;
using UnityEngine.UI;
using TMPro;

/// <summary>
/// Core simulation manager for the "When Trees Become Matches" wildfire model.
/// Implements the G05-L01 system: Rainfall(-) → Dry Vegetation(+) → Fire Spread ← Wind(+)
/// </summary>
public class SimulationManager : MonoBehaviour
{
    [Header("Grid Settings")]
    public int gridWidth = 30;
    public int gridHeight = 30;
    public float cellSize = 0.3f;

    [Header("Simulation Speed")]
    public float tickInterval = 0.15f;

    [Header("System Components (0-100)")]
    [Range(0, 100)] public float rainfall = 60f;
    [Range(0, 100)] public float wind = 20f;

    [Header("UI References")]
    public Slider rainfallSlider;
    public Slider windSlider;
    public TextMeshProUGUI rainfallLabel;
    public TextMeshProUGUI windLabel;
    public TextMeshProUGUI dryVegLabel;
    public TextMeshProUGUI fireSpreadLabel;
    public TextMeshProUGUI statusLabel;
    public Button startFireButton;
    public Button resetButton;
    public Button droughtButton;
    public Button santaAnaButton;

    // Cell states
    public enum CellState { Wet, Drying, Dry, Burning, Burned }

    // Internal grid
    private CellState[,] grid;
    private float[,] moisture; // 0 = bone dry, 1 = fully wet
    private float[,] burnTimer;
    private GameObject[,] cellObjects;
    private float tickTimer;
    private bool simulationRunning = true;
    private int totalBurning;
    private int totalBurned;
    private float avgDryness;

    // Colors
    private static readonly Color WetColor = new Color(0.18f, 0.65f, 0.25f);       // lush green
    private static readonly Color DryingColor = new Color(0.72f, 0.68f, 0.15f);     // yellow-green
    private static readonly Color DryColor = new Color(0.78f, 0.55f, 0.15f);        // dry brown
    private static readonly Color BurningColor1 = new Color(1f, 0.35f, 0f);         // orange fire
    private static readonly Color BurningColor2 = new Color(1f, 0.1f, 0f);          // red fire
    private static readonly Color BurnedColor = new Color(0.15f, 0.12f, 0.1f);      // charred black
    private static readonly Color EmberColor = new Color(1f, 0.85f, 0f);            // bright ember

    void Start()
    {
        InitializeGrid();
        SetupUI();
    }

    void Update()
    {
        if (!simulationRunning) return;

        tickTimer += Time.deltaTime;
        if (tickTimer >= tickInterval)
        {
            tickTimer = 0f;
            SimulationTick();
            UpdateVisuals();
            UpdateUI();
        }

        // Animate burning cells
        AnimateFire();
    }

    void InitializeGrid()
    {
        grid = new CellState[gridWidth, gridHeight];
        moisture = new float[gridWidth, gridHeight];
        burnTimer = new float[gridWidth, gridHeight];
        cellObjects = new GameObject[gridWidth, gridHeight];

        // Center the grid
        float offsetX = -(gridWidth * cellSize) / 2f;
        float offsetY = -(gridHeight * cellSize) / 2f;

        for (int x = 0; x < gridWidth; x++)
        {
            for (int y = 0; y < gridHeight; y++)
            {
                // Start fully wet
                moisture[x, y] = 1f;
                grid[x, y] = CellState.Wet;

                // Create cell visual
                GameObject cell = GameObject.CreatePrimitive(PrimitiveType.Quad);
                cell.transform.position = new Vector3(
                    offsetX + x * cellSize + cellSize / 2f,
                    offsetY + y * cellSize + cellSize / 2f,
                    0f
                );
                cell.transform.localScale = new Vector3(cellSize * 0.92f, cellSize * 0.92f, 1f);
                cell.transform.parent = transform;
                cell.name = $"Cell_{x}_{y}";

                // Use unlit material for flat look
                Renderer rend = cell.GetComponent<Renderer>();
                rend.material = new Material(Shader.Find("Unlit/Color"));
                rend.material.color = WetColor;

                // Remove collider for performance
                Destroy(cell.GetComponent<Collider>());

                cellObjects[x, y] = cell;
            }
        }

        // Add some natural variation — patches of slightly different terrain
        for (int i = 0; i < 15; i++)
        {
            int cx = Random.Range(3, gridWidth - 3);
            int cy = Random.Range(3, gridHeight - 3);
            int radius = Random.Range(2, 5);
            float moistureVariation = Random.Range(-0.15f, 0.15f);

            for (int x = cx - radius; x <= cx + radius; x++)
            {
                for (int y = cy - radius; y <= cy + radius; y++)
                {
                    if (x >= 0 && x < gridWidth && y >= 0 && y < gridHeight)
                    {
                        float dist = Vector2.Distance(new Vector2(x, y), new Vector2(cx, cy));
                        if (dist <= radius)
                        {
                            moisture[x, y] = Mathf.Clamp01(moisture[x, y] + moistureVariation);
                        }
                    }
                }
            }
        }
    }

    void SetupUI()
    {
        if (rainfallSlider != null)
        {
            rainfallSlider.minValue = 0;
            rainfallSlider.maxValue = 100;
            rainfallSlider.value = rainfall;
            rainfallSlider.onValueChanged.AddListener(v => rainfall = v);
        }

        if (windSlider != null)
        {
            windSlider.minValue = 0;
            windSlider.maxValue = 100;
            windSlider.value = wind;
            windSlider.onValueChanged.AddListener(v => wind = v);
        }

        if (startFireButton != null)
            startFireButton.onClick.AddListener(StartFire);

        if (resetButton != null)
            resetButton.onClick.AddListener(ResetSimulation);

        if (droughtButton != null)
            droughtButton.onClick.AddListener(SimulateDrought);

        if (santaAnaButton != null)
            santaAnaButton.onClick.AddListener(SimulateSantaAna);
    }

    void SimulationTick()
    {
        float rainfallFactor = rainfall / 100f;
        float windFactor = wind / 100f;
        totalBurning = 0;
        totalBurned = 0;
        float totalDryness = 0f;

        // Create a copy for simultaneous update
        CellState[,] newGrid = (CellState[,])grid.Clone();

        for (int x = 0; x < gridWidth; x++)
        {
            for (int y = 0; y < gridHeight; y++)
            {
                switch (grid[x, y])
                {
                    case CellState.Wet:
                    case CellState.Drying:
                    case CellState.Dry:
                        // RELATIONSHIP: Rainfall(-) → Dry Vegetation
                        // More rain = moisture increases; less rain = moisture decreases
                        float dryingRate = (1f - rainfallFactor) * 0.02f;
                        float wettingRate = rainfallFactor * 0.03f;
                        moisture[x, y] += (wettingRate - dryingRate);
                        moisture[x, y] += Random.Range(-0.005f, 0.005f); // natural variation
                        moisture[x, y] = Mathf.Clamp01(moisture[x, y]);

                        // Update state based on moisture
                        if (moisture[x, y] > 0.6f)
                            newGrid[x, y] = CellState.Wet;
                        else if (moisture[x, y] > 0.3f)
                            newGrid[x, y] = CellState.Drying;
                        else
                            newGrid[x, y] = CellState.Dry;

                        totalDryness += (1f - moisture[x, y]);
                        break;

                    case CellState.Burning:
                        totalBurning++;
                        burnTimer[x, y] += tickInterval;

                        // Fire burns out after a while
                        if (burnTimer[x, y] > 2f)
                        {
                            newGrid[x, y] = CellState.Burned;
                            break;
                        }

                        // RELATIONSHIP: Dry Vegetation(+) → Fire Spread
                        // RELATIONSHIP: Wind(+) → Fire Spread
                        // Try to spread to neighbors
                        TrySpreadFire(x, y, newGrid, windFactor);
                        break;

                    case CellState.Burned:
                        totalBurned++;
                        break;
                }
            }
        }

        grid = newGrid;
        int liveCells = gridWidth * gridHeight - totalBurned - totalBurning;
        avgDryness = liveCells > 0 ? totalDryness / liveCells * 100f : 0f;
    }

    void TrySpreadFire(int x, int y, CellState[,] newGrid, float windFactor)
    {
        // Check all 8 neighbors
        for (int dx = -1; dx <= 1; dx++)
        {
            for (int dy = -1; dy <= 1; dy++)
            {
                if (dx == 0 && dy == 0) continue;

                int nx = x + dx;
                int ny = y + dy;

                if (nx < 0 || nx >= gridWidth || ny < 0 || ny >= gridHeight) continue;
                if (grid[nx, ny] == CellState.Burning || grid[nx, ny] == CellState.Burned) continue;

                // Fire spread probability depends on:
                // 1. How dry the target cell is (Dry Vegetation → Fire Spread)
                // 2. Wind strength (Wind → Fire Spread)
                float dryness = 1f - moisture[nx, ny];
                float baseChance = dryness * 0.3f;
                float windBoost = windFactor * 0.25f;

                // Wind direction boost (fire spreads faster downwind)
                // Simulate wind blowing from west to east
                if (dx > 0) windBoost *= 1.5f;

                float spreadChance = baseChance + windBoost;

                // Diagonal spread is harder
                if (dx != 0 && dy != 0) spreadChance *= 0.6f;

                if (Random.value < spreadChance)
                {
                    newGrid[nx, ny] = CellState.Burning;
                    burnTimer[nx, ny] = 0f;
                }
            }
        }

        // Wind can cause spot fires (embers flying ahead)
        if (windFactor > 0.5f && Random.value < windFactor * 0.08f)
        {
            int spotX = x + Random.Range(2, 5);
            int spotY = y + Random.Range(-2, 3);
            if (spotX >= 0 && spotX < gridWidth && spotY >= 0 && spotY < gridHeight)
            {
                if (grid[spotX, spotY] != CellState.Burning && grid[spotX, spotY] != CellState.Burned)
                {
                    if (moisture[spotX, spotY] < 0.4f)
                    {
                        newGrid[spotX, spotY] = CellState.Burning;
                        burnTimer[spotX, spotY] = 0f;
                    }
                }
            }
        }
    }

    void UpdateVisuals()
    {
        for (int x = 0; x < gridWidth; x++)
        {
            for (int y = 0; y < gridHeight; y++)
            {
                Renderer rend = cellObjects[x, y].GetComponent<Renderer>();
                switch (grid[x, y])
                {
                    case CellState.Wet:
                        rend.material.color = Color.Lerp(DryingColor, WetColor, moisture[x, y]);
                        break;
                    case CellState.Drying:
                        rend.material.color = Color.Lerp(DryColor, DryingColor,
                            Mathf.InverseLerp(0.3f, 0.6f, moisture[x, y]));
                        break;
                    case CellState.Dry:
                        rend.material.color = Color.Lerp(DryColor, DryingColor, moisture[x, y] / 0.3f);
                        break;
                    case CellState.Burned:
                        rend.material.color = BurnedColor;
                        break;
                    // Burning is handled in AnimateFire()
                }
            }
        }
    }

    void AnimateFire()
    {
        for (int x = 0; x < gridWidth; x++)
        {
            for (int y = 0; y < gridHeight; y++)
            {
                if (grid[x, y] == CellState.Burning)
                {
                    // Flicker effect
                    float flicker = Mathf.PerlinNoise(x * 0.5f + Time.time * 8f, y * 0.5f + Time.time * 6f);
                    Color fireColor = Color.Lerp(BurningColor1, BurningColor2, flicker);

                    // Occasional bright ember flash
                    if (flicker > 0.85f)
                        fireColor = Color.Lerp(fireColor, EmberColor, (flicker - 0.85f) * 6f);

                    cellObjects[x, y].GetComponent<Renderer>().material.color = fireColor;

                    // Slight scale pulse
                    float pulse = 1f + Mathf.Sin(Time.time * 12f + x + y) * 0.05f;
                    cellObjects[x, y].transform.localScale = new Vector3(
                        cellSize * 0.92f * pulse, cellSize * 0.92f * pulse, 1f);
                }
            }
        }
    }

    void UpdateUI()
    {
        if (rainfallLabel != null)
            rainfallLabel.text = $"Rainfall: {rainfall:F0}%";
        if (windLabel != null)
            windLabel.text = $"Wind: {wind:F0}%";
        if (dryVegLabel != null)
            dryVegLabel.text = $"Avg Dryness: {avgDryness:F0}%";
        if (fireSpreadLabel != null)
        {
            float firePercent = (float)(totalBurning + totalBurned) / (gridWidth * gridHeight) * 100f;
            fireSpreadLabel.text = $"Fire: {totalBurning} burning | {totalBurned} burned ({firePercent:F1}%)";
        }
        if (statusLabel != null)
        {
            if (totalBurning > 0)
                statusLabel.text = "ACTIVE WILDFIRE";
            else if (avgDryness > 70)
                statusLabel.text = "EXTREME FIRE DANGER";
            else if (avgDryness > 40)
                statusLabel.text = "HIGH FIRE RISK";
            else
                statusLabel.text = "LOW FIRE RISK";
        }
    }

    // --- Button Actions ---

    public void StartFire()
    {
        // Start fire at a random dry spot on the left edge (simulating ignition)
        for (int attempt = 0; attempt < 50; attempt++)
        {
            int x = Random.Range(0, 3);
            int y = Random.Range(5, gridHeight - 5);
            if (grid[x, y] != CellState.Burned && grid[x, y] != CellState.Burning)
            {
                grid[x, y] = CellState.Burning;
                burnTimer[x, y] = 0f;
                // Start a small cluster
                for (int dx = 0; dx <= 1; dx++)
                {
                    for (int dy = -1; dy <= 1; dy++)
                    {
                        int nx = x + dx, ny = y + dy;
                        if (nx >= 0 && nx < gridWidth && ny >= 0 && ny < gridHeight)
                        {
                            grid[nx, ny] = CellState.Burning;
                            burnTimer[nx, ny] = 0f;
                        }
                    }
                }
                break;
            }
        }
    }

    public void ResetSimulation()
    {
        rainfall = 60f;
        wind = 20f;
        if (rainfallSlider != null) rainfallSlider.value = rainfall;
        if (windSlider != null) windSlider.value = wind;

        for (int x = 0; x < gridWidth; x++)
        {
            for (int y = 0; y < gridHeight; y++)
            {
                moisture[x, y] = 0.8f + Random.Range(-0.1f, 0.1f);
                grid[x, y] = CellState.Wet;
                burnTimer[x, y] = 0f;
                cellObjects[x, y].transform.localScale = new Vector3(
                    cellSize * 0.92f, cellSize * 0.92f, 1f);
            }
        }
    }

    public void SimulateDrought()
    {
        // Scenario: Lock rainfall to 0 — watch vegetation dry out
        rainfall = 0f;
        wind = 20f;
        if (rainfallSlider != null) rainfallSlider.value = 0f;
        if (windSlider != null) windSlider.value = 20f;
    }

    public void SimulateSantaAna()
    {
        // Scenario: Drought + Santa Ana winds — extreme fire conditions
        rainfall = 0f;
        wind = 95f;
        if (rainfallSlider != null) rainfallSlider.value = 0f;
        if (windSlider != null) windSlider.value = 95f;
    }
}
