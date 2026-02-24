using UnityEngine;
using UnityEditor;
using UnityEngine.UI;
using TMPro;

/// <summary>
/// Editor tool that automatically builds the entire Wildfire Simulation scene.
/// Usage: In Unity menu bar → CAST Science → Build Wildfire Scene
/// </summary>
public class SceneBuilder : EditorWindow
{
    [MenuItem("CAST Science/Build Wildfire Scene")]
    public static void BuildScene()
    {
        // Clean existing objects
        foreach (var go in FindObjectsByType<SimulationManager>(FindObjectsSortMode.None))
            DestroyImmediate(go.gameObject);

        // ============ CAMERA ============
        Camera cam = Camera.main;
        if (cam == null)
        {
            var camObj = new GameObject("Main Camera");
            cam = camObj.AddComponent<Camera>();
            camObj.AddComponent<AudioListener>();
        }
        cam.transform.position = new Vector3(0, 0, -10);
        cam.orthographic = true;
        cam.orthographicSize = 7f;
        cam.backgroundColor = new Color(0.08f, 0.06f, 0.12f); // dark background
        cam.gameObject.AddComponent<CameraController>();

        // ============ SIMULATION MANAGER ============
        var simObj = new GameObject("SimulationManager");
        var sim = simObj.AddComponent<SimulationManager>();

        // ============ CANVAS (UI) ============
        var canvasObj = new GameObject("UI Canvas");
        var canvas = canvasObj.AddComponent<Canvas>();
        canvas.renderMode = RenderMode.ScreenSpaceOverlay;
        canvasObj.AddComponent<CanvasScaler>().uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
        canvasObj.GetComponent<CanvasScaler>().referenceResolution = new Vector2(1920, 1080);
        canvasObj.AddComponent<GraphicRaycaster>();

        // ---- RIGHT PANEL (Controls) ----
        var rightPanel = CreatePanel(canvasObj.transform, "RightPanel",
            new Vector2(1, 0.5f), new Vector2(1, 0.5f), new Vector2(1, 0.5f),
            new Vector2(-160, 0), new Vector2(300, 600),
            new Color(0.1f, 0.1f, 0.15f, 0.92f));

        // Title
        CreateLabel(rightPanel.transform, "Title",
            "When Trees\nBecome Matches", 22, FontStyles.Bold,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -20), new Vector2(270, 60),
            new Color(1f, 0.65f, 0.15f));

        CreateLabel(rightPanel.transform, "Subtitle",
            "G05-L01 | California Wildfire Model", 11, FontStyles.Italic,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -75), new Vector2(270, 25),
            new Color(0.7f, 0.7f, 0.75f));

        // Divider
        CreateDivider(rightPanel.transform, new Vector2(0, -100));

        // Rainfall slider
        CreateLabel(rightPanel.transform, "RainfallLabel", "Rainfall: 60%", 14, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -120), new Vector2(260, 25),
            new Color(0.4f, 0.75f, 1f));
        sim.rainfallLabel = rightPanel.transform.Find("RainfallLabel").GetComponent<TextMeshProUGUI>();

        var rainfallSlider = CreateSlider(rightPanel.transform, "RainfallSlider",
            new Vector2(0, -148), new Color(0.3f, 0.6f, 1f));
        sim.rainfallSlider = rainfallSlider;

        // Wind slider
        CreateLabel(rightPanel.transform, "WindLabel", "Wind: 20%", 14, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -185), new Vector2(260, 25),
            new Color(0.85f, 0.85f, 0.9f));
        sim.windLabel = rightPanel.transform.Find("WindLabel").GetComponent<TextMeshProUGUI>();

        var windSlider = CreateSlider(rightPanel.transform, "WindSlider",
            new Vector2(0, -213), new Color(0.75f, 0.75f, 0.85f));
        sim.windSlider = windSlider;

        // Divider
        CreateDivider(rightPanel.transform, new Vector2(0, -245));

        // Status labels
        CreateLabel(rightPanel.transform, "DryVegLabel", "Avg Dryness: 0%", 13, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -265), new Vector2(260, 22),
            new Color(0.78f, 0.55f, 0.15f));
        sim.dryVegLabel = rightPanel.transform.Find("DryVegLabel").GetComponent<TextMeshProUGUI>();

        CreateLabel(rightPanel.transform, "FireSpreadLabel", "Fire: 0 burning | 0 burned", 13, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -290), new Vector2(260, 22),
            new Color(1f, 0.4f, 0.15f));
        sim.fireSpreadLabel = rightPanel.transform.Find("FireSpreadLabel").GetComponent<TextMeshProUGUI>();

        CreateLabel(rightPanel.transform, "StatusLabel", "LOW FIRE RISK", 16, FontStyles.Bold,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -320), new Vector2(260, 30),
            new Color(0.3f, 0.85f, 0.4f));
        sim.statusLabel = rightPanel.transform.Find("StatusLabel").GetComponent<TextMeshProUGUI>();

        // Divider
        CreateDivider(rightPanel.transform, new Vector2(0, -350));

        // Buttons
        sim.startFireButton = CreateButton(rightPanel.transform, "StartFireBtn", "START FIRE",
            new Vector2(0, -380), new Vector2(260, 38),
            new Color(0.9f, 0.2f, 0.1f), Color.white);

        sim.droughtButton = CreateButton(rightPanel.transform, "DroughtBtn", "DROUGHT",
            new Vector2(0, -425), new Vector2(125, 35),
            new Color(0.7f, 0.5f, 0.1f), Color.white);
        // Offset drought button left
        var droughtRect = sim.droughtButton.GetComponent<RectTransform>();
        droughtRect.anchoredPosition = new Vector2(-68, -425);

        sim.santaAnaButton = CreateButton(rightPanel.transform, "SantaAnaBtn", "SANTA ANA",
            new Vector2(68, -425), new Vector2(125, 35),
            new Color(0.85f, 0.35f, 0.1f), Color.white);

        sim.resetButton = CreateButton(rightPanel.transform, "ResetBtn", "RESET FOREST",
            new Vector2(0, -470), new Vector2(260, 35),
            new Color(0.25f, 0.55f, 0.3f), Color.white);

        // ---- RELATIONSHIP LEGEND ----
        CreateLabel(rightPanel.transform, "LegendTitle", "MODEL RELATIONSHIPS", 11, FontStyles.Bold,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -510), new Vector2(260, 20),
            new Color(0.6f, 0.6f, 0.65f));

        CreateLabel(rightPanel.transform, "Legend1", "Rainfall −(neg)→ Dry Vegetation", 10, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -530), new Vector2(260, 18),
            new Color(0.4f, 0.75f, 1f));

        CreateLabel(rightPanel.transform, "Legend2", "Dry Vegetation +(pos)→ Fire Spread", 10, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -548), new Vector2(260, 18),
            new Color(0.78f, 0.55f, 0.15f));

        CreateLabel(rightPanel.transform, "Legend3", "Wind +(pos)→ Fire Spread", 10, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -566), new Vector2(260, 18),
            new Color(0.85f, 0.85f, 0.9f));

        // ---- LESSON GUIDE (Left panel) ----
        var guideObj = new GameObject("LessonGuide");
        guideObj.transform.parent = canvasObj.transform;
        var guide = guideObj.AddComponent<LessonGuide>();

        var guidePanel = CreatePanel(canvasObj.transform, "GuidePanel",
            new Vector2(0, 0.5f), new Vector2(0, 0.5f), new Vector2(0, 0.5f),
            new Vector2(180, 0), new Vector2(340, 500),
            new Color(0.08f, 0.08f, 0.14f, 0.95f));
        guide.guidePanel = guidePanel;

        guide.stepTitle = CreateLabel(guidePanel.transform, "StepTitle", "Welcome!", 18, FontStyles.Bold,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -20), new Vector2(310, 40),
            new Color(1f, 0.85f, 0.3f)).GetComponent<TextMeshProUGUI>();

        guide.stepInstructions = CreateLabel(guidePanel.transform, "StepInstructions", "", 13, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -60), new Vector2(310, 350),
            Color.white).GetComponent<TextMeshProUGUI>();
        guide.stepInstructions.alignment = TextAlignmentOptions.TopLeft;
        guide.stepInstructions.overflowMode = TextOverflowModes.Truncate;

        guide.stepCounter = CreateLabel(guidePanel.transform, "StepCounter", "1 / 9", 12, FontStyles.Normal,
            new Vector2(0.5f, 1), new Vector2(0.5f, 1), new Vector2(0.5f, 1),
            new Vector2(0, -420), new Vector2(310, 25),
            new Color(0.5f, 0.5f, 0.55f)).GetComponent<TextMeshProUGUI>();

        guide.prevButton = CreateButton(guidePanel.transform, "PrevBtn", "← BACK",
            new Vector2(-80, -455), new Vector2(140, 32),
            new Color(0.25f, 0.25f, 0.35f), Color.white);

        guide.nextButton = CreateButton(guidePanel.transform, "NextBtn", "NEXT →",
            new Vector2(80, -455), new Vector2(140, 32),
            new Color(0.2f, 0.5f, 0.85f), Color.white);

        // Guide toggle button (top-left corner)
        guide.closeButton = CreateButton(canvasObj.transform, "GuideToggle", "📖 LESSON GUIDE",
            new Vector2(0, 0), new Vector2(160, 35),
            new Color(0.2f, 0.45f, 0.8f, 0.9f), Color.white);
        var toggleRect = guide.closeButton.GetComponent<RectTransform>();
        toggleRect.anchorMin = new Vector2(0, 1);
        toggleRect.anchorMax = new Vector2(0, 1);
        toggleRect.pivot = new Vector2(0, 1);
        toggleRect.anchoredPosition = new Vector2(15, -15);

        // Mark scene dirty
        UnityEditor.SceneManagement.EditorSceneManager.MarkSceneDirty(
            UnityEditor.SceneManagement.EditorSceneManager.GetActiveScene());

        Debug.Log("✅ CAST Science Wildfire Scene built successfully! Press Play to start.");
        EditorUtility.DisplayDialog("Scene Built!",
            "The 'When Trees Become Matches' wildfire simulation is ready.\n\n" +
            "Press PLAY (▶) to start the simulation!\n\n" +
            "The lesson guide on the left will walk students through each step.",
            "Let's Go!");
    }

    // --- Helper Methods ---

    static GameObject CreatePanel(Transform parent, string name,
        Vector2 anchorMin, Vector2 anchorMax, Vector2 pivot,
        Vector2 position, Vector2 size, Color color)
    {
        var panel = new GameObject(name);
        panel.transform.SetParent(parent, false);
        var rect = panel.AddComponent<RectTransform>();
        rect.anchorMin = anchorMin;
        rect.anchorMax = anchorMax;
        rect.pivot = pivot;
        rect.anchoredPosition = position;
        rect.sizeDelta = size;
        var img = panel.AddComponent<Image>();
        img.color = color;

        // Rounded corners via 9-slice would need a sprite; skip for now
        return panel;
    }

    static GameObject CreateLabel(Transform parent, string name, string text,
        float fontSize, FontStyles style,
        Vector2 anchorMin, Vector2 anchorMax, Vector2 pivot,
        Vector2 position, Vector2 size, Color color)
    {
        var label = new GameObject(name);
        label.transform.SetParent(parent, false);
        var rect = label.AddComponent<RectTransform>();
        rect.anchorMin = anchorMin;
        rect.anchorMax = anchorMax;
        rect.pivot = pivot;
        rect.anchoredPosition = position;
        rect.sizeDelta = size;

        var tmp = label.AddComponent<TextMeshProUGUI>();
        tmp.text = text;
        tmp.fontSize = fontSize;
        tmp.fontStyle = style;
        tmp.color = color;
        tmp.alignment = TextAlignmentOptions.Center;
        tmp.enableWordWrapping = true;
        return label;
    }

    static void CreateDivider(Transform parent, Vector2 position)
    {
        var div = new GameObject("Divider");
        div.transform.SetParent(parent, false);
        var rect = div.AddComponent<RectTransform>();
        rect.anchorMin = new Vector2(0.5f, 1);
        rect.anchorMax = new Vector2(0.5f, 1);
        rect.pivot = new Vector2(0.5f, 0.5f);
        rect.anchoredPosition = position;
        rect.sizeDelta = new Vector2(250, 1);
        var img = div.AddComponent<Image>();
        img.color = new Color(1, 1, 1, 0.15f);
    }

    static Slider CreateSlider(Transform parent, string name, Vector2 position, Color fillColor)
    {
        var sliderObj = new GameObject(name);
        sliderObj.transform.SetParent(parent, false);
        var rect = sliderObj.AddComponent<RectTransform>();
        rect.anchorMin = new Vector2(0.5f, 1);
        rect.anchorMax = new Vector2(0.5f, 1);
        rect.pivot = new Vector2(0.5f, 0.5f);
        rect.anchoredPosition = position;
        rect.sizeDelta = new Vector2(250, 20);

        // Background
        var bg = new GameObject("Background");
        bg.transform.SetParent(sliderObj.transform, false);
        var bgRect = bg.AddComponent<RectTransform>();
        bgRect.anchorMin = Vector2.zero;
        bgRect.anchorMax = Vector2.one;
        bgRect.sizeDelta = Vector2.zero;
        var bgImg = bg.AddComponent<Image>();
        bgImg.color = new Color(0.2f, 0.2f, 0.25f);

        // Fill area
        var fillArea = new GameObject("Fill Area");
        fillArea.transform.SetParent(sliderObj.transform, false);
        var fillAreaRect = fillArea.AddComponent<RectTransform>();
        fillAreaRect.anchorMin = Vector2.zero;
        fillAreaRect.anchorMax = Vector2.one;
        fillAreaRect.offsetMin = new Vector2(0, 0);
        fillAreaRect.offsetMax = new Vector2(0, 0);

        var fill = new GameObject("Fill");
        fill.transform.SetParent(fillArea.transform, false);
        var fillRect = fill.AddComponent<RectTransform>();
        fillRect.anchorMin = Vector2.zero;
        fillRect.anchorMax = Vector2.one;
        fillRect.sizeDelta = Vector2.zero;
        var fillImg = fill.AddComponent<Image>();
        fillImg.color = fillColor;

        // Handle area
        var handleArea = new GameObject("Handle Slide Area");
        handleArea.transform.SetParent(sliderObj.transform, false);
        var handleAreaRect = handleArea.AddComponent<RectTransform>();
        handleAreaRect.anchorMin = Vector2.zero;
        handleAreaRect.anchorMax = Vector2.one;
        handleAreaRect.offsetMin = new Vector2(10, 0);
        handleAreaRect.offsetMax = new Vector2(-10, 0);

        var handle = new GameObject("Handle");
        handle.transform.SetParent(handleArea.transform, false);
        var handleRect = handle.AddComponent<RectTransform>();
        handleRect.sizeDelta = new Vector2(16, 24);
        var handleImg = handle.AddComponent<Image>();
        handleImg.color = Color.white;

        var slider = sliderObj.AddComponent<Slider>();
        slider.fillRect = fillRect;
        slider.handleRect = handleRect;
        slider.targetGraphic = handleImg;
        slider.direction = Slider.Direction.LeftToRight;

        return slider;
    }

    static Button CreateButton(Transform parent, string name, string text,
        Vector2 position, Vector2 size, Color bgColor, Color textColor)
    {
        var btnObj = new GameObject(name);
        btnObj.transform.SetParent(parent, false);
        var rect = btnObj.AddComponent<RectTransform>();
        rect.anchorMin = new Vector2(0.5f, 1);
        rect.anchorMax = new Vector2(0.5f, 1);
        rect.pivot = new Vector2(0.5f, 0.5f);
        rect.anchoredPosition = position;
        rect.sizeDelta = size;

        var img = btnObj.AddComponent<Image>();
        img.color = bgColor;

        var btn = btnObj.AddComponent<Button>();
        var colors = btn.colors;
        colors.highlightedColor = bgColor * 1.2f;
        colors.pressedColor = bgColor * 0.8f;
        btn.colors = colors;

        var label = new GameObject("Label");
        label.transform.SetParent(btnObj.transform, false);
        var labelRect = label.AddComponent<RectTransform>();
        labelRect.anchorMin = Vector2.zero;
        labelRect.anchorMax = Vector2.one;
        labelRect.sizeDelta = Vector2.zero;

        var tmp = label.AddComponent<TextMeshProUGUI>();
        tmp.text = text;
        tmp.fontSize = 14;
        tmp.fontStyle = FontStyles.Bold;
        tmp.color = textColor;
        tmp.alignment = TextAlignmentOptions.Center;

        return btn;
    }
}
