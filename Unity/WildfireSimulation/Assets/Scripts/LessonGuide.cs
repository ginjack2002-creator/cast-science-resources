using UnityEngine;
using UnityEngine.UI;
using TMPro;

/// <summary>
/// Step-by-step lesson guide overlay for the G05-L01 wildfire simulation.
/// Walks students through the scientific model building process.
/// </summary>
public class LessonGuide : MonoBehaviour
{
    [Header("UI References")]
    public GameObject guidePanel;
    public TextMeshProUGUI stepTitle;
    public TextMeshProUGUI stepInstructions;
    public TextMeshProUGUI stepCounter;
    public Button nextButton;
    public Button prevButton;
    public Button closeButton;

    private int currentStep = 0;

    private readonly string[] titles = {
        "Welcome, Scientists!",
        "Step 1: Observe the Forest",
        "Step 2: Create a Drought",
        "Step 3: Watch Vegetation Dry Out",
        "Step 4: Start a Fire!",
        "Step 5: Add Santa Ana Winds",
        "Step 6: The Key Discovery",
        "Step 7: Recovery — Bring Back Rain",
        "Challenge: Can You Save the Forest?"
    };

    private readonly string[] instructions = {
        "California burns every single year — not from bad luck, but because of connected Earth systems.\n\n" +
        "In this simulation, you'll discover WHY by building a model of:\n" +
        "• Rainfall (atmosphere)\n• Dry Vegetation (biosphere)\n• Wind (atmosphere)\n• Fire Spread\n\n" +
        "Click NEXT to begin!",

        "Look at the green grid — this is a healthy California forest with good rainfall.\n\n" +
        "Notice the controls on the right:\n" +
        "• Rainfall slider: How much rain falls\n• Wind slider: How strong the wind blows\n\n" +
        "Right now rainfall is at 60% and wind at 20%. The forest is healthy and WET.\n\n" +
        "QUESTION: What do you think will happen if rain stops?",

        "Click the 'DROUGHT' button or drag the Rainfall slider all the way to 0%.\n\n" +
        "This simulates months without rain — a California drought.\n\n" +
        "Watch what happens to the forest colors...\n\n" +
        "RELATIONSHIP: Rainfall ←(negative)→ Dry Vegetation\n" +
        "Less rain = MORE dry vegetation",

        "Watch the 'Avg Dryness' number climb!\n\n" +
        "• Green cells → Yellow cells → Brown cells\n" +
        "• The forest is becoming FUEL for fire\n\n" +
        "Wait until dryness reaches 60% or higher before continuing.\n\n" +
        "QUESTION: Is the forest dangerous yet? What's missing?",

        "Now click 'START FIRE' to simulate an ignition on the left edge.\n\n" +
        "Watch how fire spreads through the dry vegetation!\n\n" +
        "RELATIONSHIP: Dry Vegetation →(positive)→ Fire Spread\n" +
        "More dry fuel = MORE fire spread\n\n" +
        "Notice: fire spreads FASTER through drier areas and SLOWER through wetter patches.",

        "Click 'SANTA ANA WINDS' or crank the Wind slider to 95%.\n\n" +
        "Santa Ana winds are hot, dry winds that blow through California every fall.\n\n" +
        "RELATIONSHIP: Wind →(positive)→ Fire Spread\n" +
        "More wind = MORE fire spread\n\n" +
        "Watch for EMBER SPOTTING — wind carries burning embers ahead of the fire line!\n\n" +
        "This is why California fires can jump highways and rivers.",

        "You just discovered the WILDFIRE CASCADE:\n\n" +
        "1. Rain stops (drought begins)\n" +
        "2. Vegetation dries out (fuel builds up)\n" +
        "3. Any spark starts a fire\n" +
        "4. Wind supercharges the spread\n\n" +
        "This is how Earth's ATMOSPHERE, BIOSPHERE, and HYDROSPHERE interact!\n\n" +
        "Rainfall is the FIRST DOMINO — everything else follows.",

        "Click 'RESET' to restore the forest, then set:\n" +
        "• Rainfall: 80%\n• Wind: 10%\n\n" +
        "Watch how the burned areas (if any remain) get surrounded by recovering green.\n\n" +
        "QUESTION: How long does recovery take compared to destruction?\n" +
        "What does this tell us about protecting forests?",

        "FREE EXPLORATION! Try these scenarios:\n\n" +
        "1. Can you keep wind at 100% but prevent fire with enough rain?\n" +
        "2. What's the MINIMUM rainfall needed to stop fire from spreading?\n" +
        "3. Start a fire, then crank up rainfall — can you put it out?\n" +
        "4. What happens with moderate drought (Rain=30) vs extreme (Rain=0)?\n\n" +
        "Record your observations in your Student Activity Pack!"
    };

    void Start()
    {
        if (nextButton != null) nextButton.onClick.AddListener(NextStep);
        if (prevButton != null) prevButton.onClick.AddListener(PrevStep);
        if (closeButton != null) closeButton.onClick.AddListener(ToggleGuide);
        UpdateDisplay();
    }

    public void NextStep()
    {
        if (currentStep < titles.Length - 1)
        {
            currentStep++;
            UpdateDisplay();
        }
    }

    public void PrevStep()
    {
        if (currentStep > 0)
        {
            currentStep--;
            UpdateDisplay();
        }
    }

    public void ToggleGuide()
    {
        if (guidePanel != null)
            guidePanel.SetActive(!guidePanel.activeSelf);
    }

    void UpdateDisplay()
    {
        if (stepTitle != null) stepTitle.text = titles[currentStep];
        if (stepInstructions != null) stepInstructions.text = instructions[currentStep];
        if (stepCounter != null) stepCounter.text = $"{currentStep + 1} / {titles.Length}";
        if (prevButton != null) prevButton.interactable = currentStep > 0;
        if (nextButton != null) nextButton.interactable = currentStep < titles.Length - 1;
    }
}
