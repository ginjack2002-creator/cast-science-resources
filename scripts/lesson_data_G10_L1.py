#!/usr/bin/env python3
"""Complete lesson data for G10L1-L01 through G10L1-L10 (Grade 10 Level 1: How the World Works)"""

L01 = {
    "id": "G10L1-L01",
    "title": "Why Do Fireworks Explode in Different Colors?",
    "subtitle": "Modeling Electron Energy Transitions and Emission Spectra",
    "ngss": "HS-PS1-1, HS-PS1-2",
    "ngss_desc": "Use the periodic table as a model to predict the relative properties of elements based on the patterns of electrons in the outermost energy level of atoms. Construct and revise an explanation for the outcome of a simple chemical reaction based on the outermost electron states of atoms, trends in the periodic table, and knowledge of the patterns of chemical properties.",
    "big_question": "How can burning the same gunpowder produce red, blue, green, and gold — and what does that tell us about the hidden structure of atoms?",
    "objectives": [
        "Model how different metal elements produce distinct colors when their electrons transition between energy levels",
        "Explain the relationship between electron energy transitions, photon emission, and visible light wavelength",
        "Predict the color a firework will produce based on the metal salts used and their atomic structure",
        "Analyze how oxidizer strength and combustion temperature affect the intensity and purity of firework colors"
    ],
    "vocabulary": [
        ("Electron Energy Level", "Discrete orbits around an atom's nucleus where electrons reside — electrons can jump between levels by absorbing or releasing specific amounts of energy as photons"),
        ("Emission Spectrum", "The unique pattern of light wavelengths emitted by an element when its excited electrons fall back to lower energy levels — like a chemical fingerprint"),
        ("Photon", "A packet of electromagnetic energy released when an excited electron drops to a lower energy level — its wavelength determines the color of light we see"),
        ("Metal Salt", "An ionic compound containing a metal ion that produces a characteristic color when heated — strontium for red, barium for green, copper for blue")
    ],
    "components": [
        ("Element Type", "The specific metal salt loaded into the firework shell, which determines the electron energy gap and therefore the color of light emitted", True),
        ("Electron Energy Level", "The quantized orbit an electron occupies — when electrons absorb thermal energy they jump to higher levels, then release photons as they fall back down", False),
        ("Oxidizer Strength", "The power of the chemical oxidizer (like potassium perchlorate) that drives the combustion reaction, controlling how much energy is available to excite electrons", True),
        ("Combustion Temperature", "The temperature reached during the firework explosion, which must be high enough to excite electrons but not so high that it produces white-hot blackbody radiation", False),
        ("Color Wavelength", "The specific wavelength of visible light emitted, determined by the energy gap between electron levels — ranging from ~400nm (violet) to ~700nm (red)", False)
    ],
    "think_about_it": "If you change the Element Type from strontium to copper, the color changes from red to blue. But the gunpowder is the same. What does this tell you about the internal structure of different atoms?",
    "scenarios": [
        ("Strontium Red Firework", "Set Element Type to strontium chloride with moderate Oxidizer Strength — observe how Electron Energy Level transitions produce red light at ~650nm"),
        ("Copper Blue Firework", "Set Element Type to copper chloride with high Oxidizer Strength — observe the different energy gap producing blue light at ~450nm"),
        ("Temperature Override", "Increase Oxidizer Strength to maximum — observe how excessive Combustion Temperature washes out the color toward white")
    ],
    "sim_scenarios": [
        ("Strontium Red", "Element: Strontium chloride | Oxidizer: Moderate", "What color do you predict strontium will produce, and why might the energy gap in strontium atoms determine this?"),
        ("Copper Blue", "Element: Copper chloride | Oxidizer: High", "Why do you predict copper produces a different color than strontium even though the explosion chemistry is similar?"),
        ("Temperature Override", "Element: Strontium | Oxidizer: Maximum", "What do you predict happens to color purity when the combustion temperature becomes extremely high?")
    ],
    "discoveries": [
        "Each element produces a unique color because its electrons have specific, quantized energy gaps — the color is determined by atomic structure, not the explosion itself",
        "The color of light corresponds directly to the energy released when an excited electron falls back to a lower level — red light carries less energy per photon than blue light",
        "Oxidizer strength must be carefully balanced — too little and electrons aren't excited enough, too much and the extreme temperature produces white blackbody radiation that drowns out the element's color",
        "Firework chemistry is applied quantum mechanics — the same electron transitions that produce firework colors are used by astronomers to identify elements in distant stars"
    ],
    "answer": "Fireworks produce different colors because different metal elements have unique electron energy level spacing. When the explosion's heat excites electrons to higher energy levels, they immediately fall back down and release photons with specific wavelengths. Strontium's electron gaps produce red photons (~650nm), copper produces blue (~450nm), and barium produces green (~525nm). The color isn't in the fire — it's in the atoms. This is quantum mechanics you can see with your naked eye.",
    "stem_title": "Design a Custom Fireworks Color Sequence",
    "stem_mission": "Design a firework shell that produces a specific three-color sequence by selecting the right metal salts and optimizing oxidizer ratios for maximum color purity.",
    "stem_scenario": "A fireworks company has been hired to create a custom show for a city's 250th anniversary. The city's colors are deep red, emerald green, and royal blue. Your team must design shells that produce these exact colors in sequence, with maximum brightness and color purity. The company needs your spectral analysis and chemical formulations.",
    "stem_questions": [
        "Which metal salts will produce each of the three required colors?",
        "How does the oxidizer ratio affect color purity versus brightness?",
        "What combustion temperature range gives the best balance of intensity and color accuracy?"
    ],
    "stem_design_qs": [
        "What specific metal compounds will you use for each color and what is the scientific basis for your choice?",
        "How will you prevent colors from blending when multiple shells burst in sequence?",
        "What oxidizer concentrations will you use and how did your model data inform this decision?",
        "How would you test your formulations before a live show?"
    ],
    "career": "Pyrotechnic Chemists design firework formulations by applying quantum mechanics and combustion chemistry. They work for fireworks manufacturers, special effects companies, and military ordnance programs, earning $50,000–$95,000/year. Spectroscopists who analyze light from atoms earn $65,000–$120,000/year in research and industry.",
    "images": {
        "cover": ("G10L1-L01-cover.png", "A photorealistic, cinematic image of a spectacular fireworks display over a city skyline showing vivid red, blue, green, and gold bursts against a dark night sky, sparks trailing downward, dramatic wide-angle composition"),
        "landscape": ("G10L1-L01-landscape.png", "A diverse group of 15-16 year old students in a modern chemistry lab performing flame tests with metal salts, bunsen burners producing colored flames — green, red, violet — students wearing safety goggles with excited expressions, natural lab lighting"),
        "modeling": ("G10L1-L01-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of electron energy transitions, modern classroom with periodic table and emission spectra posters on the walls, collaborative atmosphere"),
        "discussion": ("G10L1-L01-discussion.png", "A teacher leading an animated discussion with diverse 15-16 year old students about atomic emission spectra, a Bohr model diagram and emission spectrum displayed on a smartboard, students gesturing toward the display"),
        "stem": ("G10L1-L01-stem.png", "Diverse 15-16 year old students designing firework color sequences on large whiteboards with spectral charts and chemical formulas, periodic table references visible, engineering design atmosphere")
    },
    "pre_assessment": [
        "Why do you think fireworks come in so many different colors — where does the color come from?",
        "What do you think happens to electrons inside an atom when it is heated to extreme temperatures?",
        "Draw a diagram of what you think is happening inside an atom when it gives off colored light.",
        "If two different metals are burned and produce different colors, what does that tell you about their atoms?"
    ],
    "extend_components": [
        ("Atmospheric Oxygen", "The concentration of oxygen available for combustion, which affects the completeness of the reaction and whether metal atoms fully oxidize or remain in colored ionic states"),
        ("Shell Burst Pattern", "The physical design of the firework shell that determines how metal salts are distributed during detonation, affecting the spatial distribution and mixing of colors"),
        ("Spectral Purity", "A measure of how clean and saturated the emitted color is, affected by contamination from other elements, blackbody radiation, and incomplete combustion")
    ],
    "reflections": [
        "How does your model demonstrate that color is a property of atomic structure rather than the chemical reaction itself?",
        "Why does increasing combustion temperature beyond a certain point actually reduce color quality?",
        "How could astronomers use the same principles as fireworks to identify elements in stars billions of miles away?",
        "What would happen to the firework's color if you mixed two different metal salts in the same shell?",
        "What are the limitations of modeling quantum electron transitions with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop computational models to predict how different metal elements produce specific colors through electron energy transitions during combustion."),
        ("Disciplinary Core Idea", "PS1.A Structure and Properties of Matter", "Each atom has a characteristic electron configuration. When electrons transition between energy levels, they emit or absorb photons of specific wavelengths, producing the element's unique emission spectrum."),
        ("Crosscutting Concept", "Patterns", "Students identify the pattern that each element's unique electron energy gaps produce a characteristic emission spectrum, enabling identification and prediction of atomic behavior.")
    ],
    "cast_items": [
        "Model how electron energy level transitions produce element-specific colors during combustion",
        "Predict firework color output based on metal salt selection and combustion conditions",
        "Explain the quantum mechanical basis of emission spectra using computational evidence"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A pyrotechnician adds strontium chloride to a firework shell and observes bright red light at 650nm. If they replace the strontium with copper chloride, what change would the model predict and why?"),
        ("Constructed Response:", "Using your model, explain why every element produces a unique color when heated. Connect your explanation to electron energy levels, photon emission, and the electromagnetic spectrum.")
    ],
    "background_intro": "Every Fourth of July, millions of people watch quantum mechanics in action without realizing it. The dazzling colors of fireworks are not produced by dyes or pigments — they are the direct result of electrons inside metal atoms jumping between quantized energy levels and releasing photons of specific wavelengths. Understanding firework colors means understanding the fundamental structure of atoms.",
    "background_sections": [
        ("Quantized Electron Energy Levels", "In 1913, Niels Bohr proposed that electrons orbit the nucleus only at specific, allowed energy levels — not at arbitrary distances. When an electron absorbs energy, it jumps to a higher level (excitation). When it falls back down, it releases that exact energy difference as a photon of light. The energy gap between levels is unique to each element, which is why each element has a unique emission spectrum."),
        ("How Fireworks Produce Color", "A firework shell contains fuel (charcoal, sulfur), an oxidizer (potassium perchlorate), and a color-producing metal salt. When the shell detonates, the combustion reaction reaches 1000-2500°C, providing enough thermal energy to excite the metal's electrons. As billions of electrons simultaneously fall back to lower energy levels, they emit photons at the element's characteristic wavelength — strontium emits at ~650nm (red), barium at ~525nm (green), copper at ~450nm (blue)."),
        ("The Electromagnetic Spectrum and Color", "Visible light is a narrow band of the electromagnetic spectrum, from about 380nm (violet) to 700nm (red). The energy of a photon is inversely proportional to its wavelength: E = hc/λ. This means blue photons carry more energy than red photons. When we see a red firework, we're seeing lower-energy photons from smaller electron energy gaps; blue fireworks release higher-energy photons from larger gaps."),
        ("Temperature and Color Purity", "Combustion temperature is a critical variable. Too low, and insufficient electrons are excited, producing a dim display. Too high, and the intense heat generates blackbody radiation — a continuous spectrum of white light that washes out the element's characteristic color. Master pyrotechnicians carefully balance oxidizer strength to reach the 'sweet spot' where electron excitation is maximized without excessive blackbody contamination.")
    ],
    "lever_L": "Students identify element type, electron energy level, oxidizer strength, combustion temperature, and color wavelength as the key components of the firework color system.",
    "lever_E": "Students determine that element type sets the electron energy gap, oxidizer strength drives combustion temperature, and the energy gap determines the photon wavelength (color) emitted when excited electrons fall back down.",
    "lever_V": "Students build a computational model showing how metal salt selection and combustion conditions interact to produce specific colors through electron energy transitions.",
    "lever_Ev": "Students run strontium red, copper blue, and temperature override scenarios to test predictions about color output and discover the relationship between energy gaps and photon wavelength.",
    "lever_R": "Students add atmospheric oxygen, shell burst pattern, or spectral purity to explore how real-world factors affect color quality and display design.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with spectacular fireworks image", "say": "Every color in that fireworks show is quantum mechanics you can see with your naked eye. Red, blue, green — each one is atoms telling you their secrets.", "do": "Show a 15-second fireworks video clip. Ask: Where do you think the colors come from? Is it a dye?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary terms", "say": "Today we're going to decode the atomic science behind every firework you've ever seen.", "do": "Have students read objectives. Pre-teach 'emission spectrum' and 'photon' with quick visual aids.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Same explosion, different colors — why?", "say": "The gunpowder is the same. The fuse is the same. The shell is the same. So WHY are the colors different?", "do": "Quick-write: Students hypothesize what makes red different from blue in a firework. Share out.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to build a model that predicts what color a firework produces based on what's inside it.", "do": "Preview each LEVER step. Emphasize that this is about atomic structure, not just chemistry.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for firework color model", "say": "What factors determine the color of a firework? Which ones can a pyrotechnician control?", "do": "Guide sorting of external vs. internal components. Discuss why element type and oxidizer are choices (external).", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When strontium is heated, what happens inside each atom? Follow the energy from explosion to your eye.", "do": "Trace the pathway: heat → electron excitation → photon emission → color. Use Bohr model diagrams.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results for different metals", "say": "Let's test three metals and see if the model can predict the color before we see it.", "do": "Students predict colors for strontium, copper, and barium. Run simulations. Then test the temperature override.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings — emission spectra comparison chart", "say": "So the color isn't in the fire — it's in the atoms. And astronomers use this exact same science to identify what stars are made of.", "do": "Show real emission spectra for hydrogen, sodium, and neon. Connect fireworks to stellar spectroscopy.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Custom fireworks design challenge", "say": "A city just hired your team to design a three-color fireworks show. Pick your metals, set your oxidizers, and prove your colors will work.", "do": "Groups select metal salts, determine oxidizer ratios from model data, and present spectral predictions.", "time": "12 min"}
    ],
    "sort_reasoning": "Element Type and Oxidizer Strength are external components because they represent choices made by the pyrotechnician — which metal salt to use and how much oxidizer to add. Electron Energy Level, Combustion Temperature, and Color Wavelength are internal because they are physical outcomes determined by atomic structure and reaction conditions that cannot be directly set by the designer.",
    "relationships": [
        ("Element Type to Electron Energy Level", "DETERMINES", "Each element has a unique set of quantized electron energy levels. The specific metal salt selected defines the energy gaps available for electron transitions, which ultimately determines the color of light emitted."),
        ("Oxidizer Strength to Combustion Temperature", "POSITIVE (+)", "Stronger oxidizers drive more vigorous combustion reactions, producing higher temperatures. Higher temperatures provide more thermal energy to excite electrons to upper energy levels."),
        ("Electron Energy Level to Color Wavelength", "DETERMINES", "The energy gap between the excited level and the ground state determines the exact wavelength of the emitted photon. Larger gaps produce shorter wavelengths (blue), smaller gaps produce longer wavelengths (red).")
    ],
    "sim_answers": [
        ("Strontium Red Scenario", "When Element Type is set to strontium chloride with moderate Oxidizer Strength, the model shows electrons being excited to specific energy levels and then falling back, emitting photons at approximately 650nm — deep red. Combustion Temperature stays in the optimal range, so blackbody radiation is minimal and the red color is vivid and pure."),
        ("Temperature Override Scenario", "When Oxidizer Strength is pushed to maximum, Combustion Temperature spikes well above optimal. While more electrons are excited, the extreme heat also produces intense blackbody radiation — a continuous white glow. This white light overwhelms the element's characteristic red emission, washing the color toward white-orange. This explains why the hottest fireworks often appear white or golden rather than a pure color.")
    ],
    "reflection_exemplars": [
        ("Why is color a property of the atom, not the fire?", "Fire itself is a chemical reaction that releases energy. The color we see depends on WHICH atoms are being excited by that energy. The same fire can produce red (strontium), green (barium), or blue (copper) because each element's electrons have different energy gaps. Change the metal, change the color — because you're changing the quantum energy levels, not the combustion reaction. This is why emission spectra are called 'atomic fingerprints.'"),
        ("How can astronomers use this to study stars?", "Stars are essentially giant fireworks — they contain hot, excited atoms emitting photons at characteristic wavelengths. By analyzing the light from a star through a spectrometer, astronomers can identify which elements are present based on the emission (or absorption) lines. The same quantum mechanics that makes a strontium firework red tells us what a star 100 light-years away is made of. Our model demonstrates this principle at a scale we can see and test.")
    ],
    "stem_intro": "Present the challenge: A fireworks company needs your team to design shells that produce three specific colors — deep red, emerald green, and royal blue — for a city anniversary celebration. Use your model data to select metal salts, optimize oxidizer ratios, and predict spectral output for each shell.",
    "stem_concepts": [
        ("Spectral Analysis", "Scientists use spectrometers to separate light into its component wavelengths. By analyzing the emission lines of heated elements, they can identify the element and measure the energy of electron transitions with extreme precision."),
        ("Color Mixing in Pyrotechnics", "Unlike paint mixing (subtractive), firework color mixing is additive — combining red and green emitters produces yellow. Pyrotechnicians must carefully isolate metal salts or use timed delays to prevent unwanted color blending."),
        ("Combustion Engineering", "The oxidizer-to-fuel ratio determines combustion temperature and duration. Pyrotechnicians balance these ratios to achieve optimal electron excitation while minimizing blackbody contamination and ensuring safe burn rates.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design specifies correct metal salts for each color with scientific justification, optimizes oxidizer ratios using model data, addresses color purity and blackbody contamination, and includes spectral predictions"),
        ("Proficient (3)", "Design selects appropriate metal salts and provides reasonable oxidizer settings with some reference to model evidence"),
        ("Developing (2)", "Design identifies some metal salts but lacks optimization detail or spectral analysis"),
        ("Beginning (1)", "Design is incomplete or does not connect metal selection to electron energy transitions")
    ],
    "support": [
        "Provide a reference chart matching common metal salts to their emission wavelengths and visible colors",
        "Use a simplified Bohr model diagram with labeled energy levels and transition arrows for each metal",
        "Sentence frames: 'When __ is heated, its electrons jump to the __ energy level and release __ nm photons, which appear __ in color'"
    ],
    "extensions": [
        "Research how neon signs work using the same electron excitation principles and compare their emission spectra to firework metals",
        "Investigate why blue fireworks are the hardest to produce — what makes copper's emission so challenging for pyrotechnicians?",
        "Explore how spectroscopy is used in forensic science to identify unknown substances at crime scenes"
    ],
    "cross_curr": [
        ("Math", "Calculate the energy of photons emitted by strontium (650nm), barium (525nm), and copper (450nm) using E = hc/λ. Which color carries the most energy per photon and what does that mean about the electron energy gap?"),
        ("ELA", "Write a science explainer article for a teen magazine that explains why fireworks have different colors using accurate atomic science but accessible language"),
        ("History", "Research the history of fireworks from ancient China to modern pyrotechnics — how did understanding of chemistry and atomic structure transform the art over 1000 years?")
    ],
    "misconceptions": [
        ("Firework colors come from dyes or pigments", "There are no dyes in fireworks. The colors are produced by electron transitions within metal atoms. When heated, electrons jump to higher energy levels and then release photons of specific wavelengths as they fall back down. Each element has unique energy gaps, producing unique colors. This is fundamentally different from pigments, which absorb certain wavelengths and reflect others.", "Demonstration: Perform a flame test with sodium chloride (yellow) and copper sulfate (green). Ask: Where's the dye? There is none — the color comes from the atoms themselves."),
        ("Hotter fire always means brighter colors", "Increasing temperature does excite more electrons, but beyond an optimal point, the extreme heat produces blackbody radiation — a continuous white glow that drowns out the element's characteristic color. This is why the hottest stars appear white, not colored. Master pyrotechnicians carefully control temperature to maximize color purity.", "Show two flame tests: one at optimal temperature (vivid color) and one overheated (washed-out white). Ask: Which is hotter? Which has better color?"),
        ("All light is the same — just different shades", "Light is electromagnetic radiation, and different colors correspond to different wavelengths and energies. Red light (~650nm) has longer wavelength and less energy per photon than blue light (~450nm). These are fundamentally different photons carrying different amounts of energy, produced by different-sized electron energy gaps. Color isn't just appearance — it's physics.", "Calculate: Using E = hc/λ, show that a blue photon carries about 1.4x more energy than a red photon. Color is literally a measure of energy.")
    ]
}

L02 = {
    "id": "G10L1-L02",
    "title": "Can Nuclear Power Actually Save the Planet?",
    "subtitle": "Modeling Nuclear Fission, Energy Output, and Environmental Trade-offs",
    "ngss": "HS-PS1-8, HS-ESS3-2",
    "ngss_desc": "Develop models to illustrate the changes in the composition of the nucleus of the atom and the energy released during the processes of fission, fusion, and radioactive decay. Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios.",
    "big_question": "If nuclear power produces almost zero carbon emissions, why is the world still arguing about whether to use it?",
    "objectives": [
        "Model how nuclear fission of uranium produces enormous energy from tiny amounts of fuel",
        "Analyze the relationship between fission rate, energy output, radioactive waste, and carbon emissions avoided",
        "Evaluate the trade-offs between nuclear power's clean energy benefits and its waste disposal challenges",
        "Predict the environmental impact of different energy mix scenarios including nuclear power"
    ],
    "vocabulary": [
        ("Nuclear Fission", "The splitting of a heavy atomic nucleus (like uranium-235) into two lighter nuclei, releasing enormous energy — a single fission event releases about 200 million electron volts, roughly 50 million times more than a chemical reaction"),
        ("Radioactive Decay", "The spontaneous emission of radiation from unstable atomic nuclei as they transform into more stable configurations — the source of both nuclear energy and radioactive waste hazards"),
        ("Half-Life", "The time it takes for half of a radioactive isotope to decay — ranging from fractions of a second to billions of years, determining how long nuclear waste remains dangerous"),
        ("Carbon-Free Energy", "Energy production that releases no carbon dioxide during operation — nuclear power produces 12 grams of CO2 per kilowatt-hour over its lifecycle, compared to 820 for coal and 490 for natural gas")
    ],
    "components": [
        ("Uranium Fuel Supply", "The amount of enriched uranium-235 fuel available for the reactor, measured in metric tons — a single fuel pellet the size of a pencil eraser produces as much energy as one ton of coal", True),
        ("Fission Rate", "The number of uranium-235 atoms splitting per second in the reactor core, controlled by neutron-absorbing control rods — determines the power output", False),
        ("Energy Output", "The total electrical energy produced by the nuclear plant, measured in gigawatt-hours — a typical reactor produces enough electricity for 700,000 homes", False),
        ("Radioactive Waste", "The spent nuclear fuel and byproducts that remain dangerously radioactive for thousands to hundreds of thousands of years, requiring secure long-term storage", False),
        ("Carbon Emissions Avoided", "The amount of CO2 that would have been released if the same energy had been produced by fossil fuel plants — nuclear power prevents about 2 billion tons of CO2 emissions annually worldwide", False)
    ],
    "think_about_it": "Nuclear power produces massive Energy Output with almost zero Carbon Emissions — but it also produces Radioactive Waste that remains dangerous for 10,000+ years. How do you weigh a benefit measured in decades against a cost measured in millennia?",
    "scenarios": [
        ("Full Power Operation", "Set Uranium Fuel Supply to standard load and allow Fission Rate to reach full capacity — observe Energy Output and Carbon Emissions Avoided versus Radioactive Waste generated"),
        ("Reduced Power Mode", "Reduce Fission Rate to 50% by inserting control rods — observe how Energy Output, waste, and carbon avoidance all decrease proportionally"),
        ("Fuel Depletion", "Run the reactor until Uranium Fuel Supply is exhausted — observe the total energy produced, total waste generated, and lifetime carbon impact")
    ],
    "sim_scenarios": [
        ("Full Power", "Uranium fuel: Standard load | Fission rate: 100%", "What do you predict the ratio of energy produced to waste generated will be at full power operation?"),
        ("Reduced Power", "Uranium fuel: Standard | Fission rate: 50%", "If we cut the fission rate in half, do you predict waste will also be cut exactly in half? Why or why not?"),
        ("Fuel Depletion", "Full operation until fuel exhaustion", "Over the reactor's entire fuel cycle, how much carbon emission does your model predict is avoided compared to a coal plant producing the same energy?")
    ],
    "discoveries": [
        "Nuclear fission releases roughly 2 million times more energy per kilogram of fuel than burning coal — making it extraordinarily energy-dense and low-carbon",
        "Radioactive waste is produced in relatively small volumes (about 2,000 metric tons per year for the entire US fleet) but remains hazardous for extremely long periods",
        "The carbon emissions avoided by nuclear power are enormous — replacing a single nuclear plant with natural gas would add millions of tons of CO2 per year",
        "The nuclear debate is fundamentally a trade-off between a certain, manageable risk (waste storage) and a catastrophic, diffuse risk (climate change from fossil fuels)"
    ],
    "answer": "Nuclear power is one of the most powerful tools we have against climate change — it produces enormous amounts of electricity with virtually no carbon emissions during operation. A single uranium fuel pellet the size of a pencil eraser produces as much energy as a ton of coal. But it comes with a genuine trade-off: spent fuel remains radioactively dangerous for tens of thousands of years and requires engineered storage that must outlast entire civilizations. The real question isn't whether nuclear is perfect — it's whether the alternative (more fossil fuels and more climate change) is worse.",
    "stem_title": "Design a National Energy Portfolio",
    "stem_mission": "Design a national energy mix for 2050 that meets electricity demand while minimizing both carbon emissions and nuclear waste, balancing cost, reliability, and environmental impact.",
    "stem_scenario": "The Department of Energy has tasked your team with proposing a 2050 energy portfolio for a nation of 350 million people. You must meet a demand of 4,000 terawatt-hours per year while reducing carbon emissions by 80% from current levels. Nuclear, solar, wind, hydro, and natural gas are all available — but each has trade-offs your model has revealed.",
    "stem_questions": [
        "What percentage of the energy mix should come from nuclear power, and what evidence supports your decision?",
        "How will you address the waste storage challenge for the nuclear component?",
        "What happens to your carbon reduction targets if you reduce or eliminate nuclear from the portfolio?"
    ],
    "stem_design_qs": [
        "What is the optimal balance between nuclear baseload power and renewable intermittent sources?",
        "How will you handle the waste generated over the 30-year operating life of each nuclear plant?",
        "What backup generation will you include for when wind and solar output drops?",
        "How does your portfolio compare to current energy mixes in terms of cost, reliability, and emissions?"
    ],
    "career": "Nuclear Engineers design, operate, and maintain nuclear reactors and manage radioactive materials. They work at power plants, national laboratories, the Navy's nuclear fleet, and regulatory agencies, earning $80,000–$150,000/year. Energy Policy Analysts who evaluate energy portfolios for governments earn $65,000–$130,000/year.",
    "images": {
        "cover": ("G10L1-L02-cover.png", "A photorealistic, cinematic image of a modern nuclear power plant with cooling towers releasing clean white steam against a clear blue sky, wind turbines visible in the background, green landscape surrounding the facility, dramatic golden hour lighting"),
        "landscape": ("G10L1-L02-landscape.png", "A diverse group of 15-16 year old students in a modern physics lab examining models of uranium atoms and nuclear reactor components, engaged expressions, periodic table and nuclear energy posters on walls"),
        "modeling": ("G10L1-L02-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of nuclear energy systems, modern classroom with energy comparison charts and reactor diagrams visible"),
        "discussion": ("G10L1-L02-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about nuclear energy trade-offs, a fission chain reaction diagram displayed on a smartboard, students engaged in debate"),
        "stem": ("G10L1-L02-stem.png", "Diverse 15-16 year old students designing energy portfolio proposals on large whiteboards with pie charts and energy data, calculator and reference materials on desks, collaborative engineering atmosphere")
    },
    "pre_assessment": [
        "What do you already know about how nuclear power plants produce electricity?",
        "Why do you think some people support nuclear power while others oppose it?",
        "Draw a diagram showing what you think happens inside a nuclear reactor to produce energy.",
        "How does the amount of waste from a nuclear plant compare to the waste from a coal plant producing the same energy?"
    ],
    "extend_components": [
        ("Cooling Water Demand", "The enormous volume of water needed to cool the reactor and condense steam — a typical plant uses 1-2 billion gallons per day, raising concerns about thermal pollution and water scarcity"),
        ("Fuel Enrichment Level", "The percentage of uranium-235 in the fuel — natural uranium is 0.7% U-235, reactor fuel is enriched to 3-5%, and weapons-grade is 90%+, raising proliferation concerns"),
        ("Public Risk Perception", "The level of public fear about nuclear accidents, which is often disproportionate to actual statistical risk but profoundly influences energy policy decisions")
    ],
    "reflections": [
        "How does your model demonstrate the extraordinary energy density of nuclear fuel compared to fossil fuels?",
        "What does the model reveal about the trade-off between carbon avoidance and waste generation?",
        "If nuclear power is the lowest-carbon reliable energy source, why do many countries still rely heavily on fossil fuels?",
        "How should society weigh risks that last decades (climate change) against risks that last millennia (nuclear waste)?",
        "What assumptions does your model make about waste storage technology and safety?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop computational models to illustrate the energy released during fission and evaluate the environmental trade-offs of nuclear power generation."),
        ("Disciplinary Core Idea", "PS1.C Nuclear Processes / ESS3.A Natural Resources", "Nuclear fission releases energy when heavy nuclei split, and evaluating nuclear power requires analyzing costs and benefits of energy resource management."),
        ("Crosscutting Concept", "Energy and Matter", "Students track energy transformations from nuclear binding energy to thermal energy to electrical energy, and trace matter flows from uranium fuel to fission products and waste.")
    ],
    "cast_items": [
        "Model the energy transformation from nuclear fission to electrical output",
        "Evaluate the environmental trade-offs between nuclear energy and fossil fuel alternatives",
        "Predict the long-term waste management requirements for different nuclear energy scenarios"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A nuclear power plant produces 8 billion kWh of electricity per year with near-zero CO2 emissions. If this plant were replaced by a natural gas plant, approximately how much additional CO2 would be released annually?"),
        ("Constructed Response:", "Using your model, evaluate whether nuclear power should be expanded as a strategy to combat climate change. Discuss both the carbon emission benefits and the radioactive waste challenges, using model evidence to support your argument.")
    ],
    "background_intro": "Nuclear energy occupies a unique position in the climate debate: it is the most energy-dense, lowest-carbon reliable power source available, yet it produces waste that remains dangerous for longer than human civilization has existed. Understanding the science of fission — and the genuine trade-offs it presents — is essential for making informed decisions about our energy future.",
    "background_sections": [
        ("The Physics of Fission", "When a neutron strikes a uranium-235 nucleus, the atom splits into two lighter elements (fission products), releases 2-3 additional neutrons, and converts a tiny amount of mass into enormous energy via Einstein's E=mc². A single fission event releases about 200 MeV — roughly 50 million times more energy than burning one molecule of methane. This is why nuclear fuel is so extraordinarily energy-dense."),
        ("Chain Reactions and Control", "The neutrons released by one fission event can trigger additional fissions, creating a chain reaction. In a reactor, this chain reaction is carefully controlled using neutron-absorbing control rods — pushed in to slow the reaction, pulled out to speed it up. In a bomb, the chain reaction is uncontrolled. The key engineering challenge is maintaining criticality — exactly one neutron from each fission causing exactly one more fission."),
        ("The Waste Problem", "Spent nuclear fuel contains fission products and transuranic elements that emit dangerous radiation. Some isotopes (like cesium-137) have half-lives of 30 years; others (like plutonium-239) have half-lives of 24,000 years. The US has accumulated about 83,000 metric tons of spent fuel with no permanent repository. Finland's Onkalo facility, designed to store waste for 100,000 years, is the world's first deep geological repository."),
        ("Nuclear vs. Fossil Fuels: The Numbers", "Over its lifecycle, nuclear power emits about 12 grams of CO2 per kWh — comparable to wind (11g) and far below solar (44g), natural gas (490g), and coal (820g). The world's 440 nuclear reactors prevent about 2 billion tons of CO2 emissions annually. However, nuclear plants are expensive to build ($10-20 billion each), take 10-15 years to construct, and face significant public opposition due to accidents at Chernobyl (1986) and Fukushima (2011).")
    ],
    "lever_L": "Students identify uranium fuel supply, fission rate, energy output, radioactive waste, and carbon emissions avoided as the key components of the nuclear energy system.",
    "lever_E": "Students determine that uranium fuel supply enables fission, fission rate drives both energy output and waste production, and energy output directly determines how much carbon emission is avoided compared to fossil fuels.",
    "lever_V": "Students build a computational model showing the relationships between fuel input, fission rate, useful energy output, waste generation, and climate impact.",
    "lever_Ev": "Students run full power, reduced power, and fuel depletion scenarios to quantify the trade-offs between energy production, waste generation, and carbon avoidance.",
    "lever_R": "Students add cooling water demand, fuel enrichment level, or public risk perception to model more complex real-world nuclear energy dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with nuclear plant and climate imagery", "say": "What if I told you there's an energy source that produces almost zero carbon, fits a year's fuel in a pickup truck, but creates waste that's dangerous for 100,000 years? Would you use it?", "do": "Show the scale comparison: a uranium pellet vs. a ton of coal producing the same energy. Let students react.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're modeling the most controversial clean energy source on Earth — and you'll decide if it should be expanded.", "do": "Have students read objectives. Pre-teach 'fission' and 'half-life' with animations.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Nuclear: climate savior or ticking time bomb?", "say": "Nuclear produces almost zero carbon. So why isn't every country building reactors as fast as possible?", "do": "Quick poll: Who thinks nuclear should be expanded? Who thinks it should be phased out? Record the split for later.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're going to model the complete nuclear system — energy in, energy out, waste produced, carbon avoided.", "do": "Preview LEVER steps. Emphasize that this is about TRADE-OFFS, not right/wrong answers.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for nuclear energy model", "say": "What goes INTO a nuclear plant and what comes OUT? Sort the inputs from the outputs.", "do": "Guide sorting. Uranium supply is the only true external input; fission rate is controlled but internal.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "More fission means more energy — but it also means more waste. Can you have one without the other?", "do": "Help students map the dual outputs. Use green arrows for benefits, red for costs.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Graph predictions and simulation results", "say": "Let's run a nuclear plant for a year and see exactly what we get — energy AND waste.", "do": "Students predict output ratios. Run full power, reduced, and depletion scenarios. Compare trade-offs.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings and comparison data", "say": "One uranium pellet equals one ton of coal. But that pellet also creates waste that outlasts the pyramids. How do we weigh that?", "do": "Revisit the opening poll. Has anyone changed their mind? Discuss what evidence shifted perspectives.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "National energy portfolio design", "say": "You're advising the President on the 2050 energy mix. 350 million people need power. Climate targets must be met. What's your plan?", "do": "Groups design energy portfolios balancing nuclear, renewables, and fossil fuels. Present and defend choices.", "time": "12 min"}
    ],
    "sort_reasoning": "Uranium Fuel Supply is the external component because it is the resource input that must be mined, enriched, and loaded — a deliberate human choice. Fission Rate, Energy Output, Radioactive Waste, and Carbon Emissions Avoided are all internal because they are physical consequences of the nuclear reaction and cannot be independently set — they are determined by the physics of fission and the amount of fuel consumed.",
    "relationships": [
        ("Uranium Fuel Supply to Fission Rate", "POSITIVE (+)", "More available uranium fuel allows for sustained or increased fission rates. As fuel is consumed, fewer fissile atoms remain, eventually requiring fuel replacement to maintain output."),
        ("Fission Rate to Energy Output", "POSITIVE (+)", "Higher fission rates mean more atoms splitting per second, releasing more thermal energy to generate steam and drive turbines. Doubling the fission rate approximately doubles the electrical output."),
        ("Fission Rate to Radioactive Waste", "POSITIVE (+)", "Higher fission rates produce more fission products and transuranic elements per unit time. Energy and waste are inseparable outputs of the fission process — you cannot have one without the other.")
    ],
    "sim_answers": [
        ("Full Power Scenario", "At full power operation, the model shows enormous Energy Output — a single reactor producing enough electricity for 700,000 homes while avoiding millions of tons of CO2 emissions annually. Simultaneously, Radioactive Waste accumulates at about 20 metric tons of spent fuel per reactor per year. The ratio is striking: massive clean energy from tiny fuel amounts, but waste that will remain hazardous for millennia."),
        ("Fuel Depletion Scenario", "Over a full fuel cycle (approximately 18-24 months), the model shows that a single fuel load produces tens of billions of kilowatt-hours of electricity, avoids millions of tons of CO2 compared to coal, and generates approximately 20 tons of spent fuel. The lifetime totals make the trade-off stark: extraordinary energy density and climate benefit versus a permanent waste legacy.")
    ],
    "reflection_exemplars": [
        ("How do you weigh benefits in decades versus costs in millennia?", "This is the central dilemma of nuclear power. Climate change is an urgent crisis measured in decades — we need to reduce emissions NOW to avoid catastrophic warming. Nuclear waste is a slow-motion challenge measured in millennia — spent fuel remains dangerous for 10,000-100,000 years. My model shows that the carbon avoidance benefit is immediate and enormous, while the waste volume is relatively small but the time horizon is almost incomprehensible. There's no purely scientific answer — it requires weighing present certainty against future uncertainty."),
        ("Why do countries disagree about nuclear power?", "Different countries weight the trade-offs differently based on their unique circumstances. France generates 70% of its electricity from nuclear because it has no domestic fossil fuels and prioritized energy independence. Germany is phasing out nuclear due to public fear after Fukushima, but its carbon emissions INCREASED as it burned more coal to compensate. The model shows the same physics everywhere — the disagreement is about VALUES, not science: how much risk is acceptable, and who bears the cost.")
    ],
    "stem_intro": "Present the challenge: The Department of Energy needs a 2050 energy portfolio proposal that meets national electricity demand while cutting carbon emissions by 80%. Your team must balance nuclear baseload, renewable intermittency, and fossil fuel flexibility using evidence from your model to justify every decision.",
    "stem_concepts": [
        ("Baseload vs. Intermittent Power", "Baseload power runs 24/7 regardless of weather — nuclear and fossil fuels provide this. Intermittent sources like wind and solar produce power only when conditions are right. A reliable grid needs a mix of both, plus storage for when intermittent sources aren't producing."),
        ("Deep Geological Storage", "The leading solution for nuclear waste is burial in stable geological formations hundreds of meters underground. Finland's Onkalo repository is designed to isolate waste for 100,000 years in ancient bedrock. The engineering is proven — the challenge is political and social acceptance."),
        ("Levelized Cost of Energy", "LCOE measures the total cost of building, fueling, and operating a power plant divided by total energy produced over its lifetime. Nuclear LCOE is higher than wind and solar but lower than coal with carbon capture. However, nuclear provides firm, 24/7 power that renewables alone cannot.")
    ],
    "stem_eval": [
        ("Expert (4)", "Portfolio meets carbon targets with detailed justification, includes nuclear waste management plan, addresses intermittency and baseload needs, and uses model data to defend all design choices"),
        ("Proficient (3)", "Portfolio meets carbon targets with reasonable energy mix and some use of model evidence to justify decisions"),
        ("Developing (2)", "Portfolio addresses carbon reduction but lacks detail on waste management, intermittency, or model-based justification"),
        ("Beginning (1)", "Portfolio is incomplete or doesn't realistically address the carbon-waste trade-off")
    ],
    "support": [
        "Provide an energy source comparison card showing carbon emissions, cost, reliability, and waste for each option",
        "Use a visual pie chart template to help students build and adjust their energy portfolios",
        "Sentence frames: 'Our portfolio includes __% nuclear because our model shows that __, which helps us meet our carbon target by __'"
    ],
    "extensions": [
        "Research nuclear fusion as a potential future energy source — how does fusion differ from fission, and would it solve the waste problem?",
        "Investigate the Chernobyl and Fukushima disasters — what went wrong, what safety improvements resulted, and how do modern reactor designs prevent these failures?",
        "Compare the lifecycle environmental impact of nuclear power to solar panels, including mining, manufacturing, land use, and end-of-life disposal"
    ],
    "cross_curr": [
        ("Math", "Calculate: If a nuclear plant produces 8 billion kWh/year and avoids 4 million tons of CO2 compared to natural gas, how much CO2 is avoided per kWh? Compare this to the lifecycle emissions of other energy sources."),
        ("ELA", "Write a persuasive policy brief either supporting or opposing nuclear expansion, using model evidence for your central claims and addressing the strongest counterarguments"),
        ("Social Studies", "Research the history of nuclear energy policy in three countries (France, Germany, Japan) and analyze how culture, politics, and historical events shaped different approaches to the same technology")
    ],
    "misconceptions": [
        ("Nuclear power plants can explode like atomic bombs", "A nuclear reactor cannot produce a nuclear explosion. Reactor fuel is enriched to 3-5% uranium-235; a nuclear weapon requires 90%+ enrichment. The worst-case reactor accident is a meltdown — where fuel overheats and damages the containment — not a nuclear detonation. Chernobyl's explosion was a steam explosion from overheated water, not a nuclear blast.", "Analogy: You can't make a stick of dynamite from a campfire just by adding more wood. The physics are fundamentally different — low enrichment cannot sustain the supercritical chain reaction needed for a weapon."),
        ("Nuclear waste glows green and will poison the Earth forever", "Spent nuclear fuel doesn't glow green — that's a Hollywood invention. It's a solid ceramic material stored in steel and concrete casks. While it is genuinely dangerous due to radiation, the total volume is small (all US nuclear waste from 60 years fits on one football field, 10 yards deep). The longest-lived isotopes are actually the LEAST radioactive — the most dangerous waste decays within a few hundred years.", "Show actual photos of dry cask storage vs. movie depictions. Calculate: 83,000 metric tons of waste from 60 years of powering 20% of America — is that a lot or a little compared to coal waste?"),
        ("Renewable energy can completely replace nuclear without trade-offs", "Wind and solar are excellent but intermittent — the sun doesn't always shine and the wind doesn't always blow. Without massive battery storage (which doesn't yet exist at grid scale), removing nuclear baseload power means burning fossil fuels during renewable gaps. Germany's nuclear phase-out led to increased coal burning and higher emissions. The model shows that nuclear provides the firm, 24/7 clean power that renewables alone cannot yet deliver.", "Show Germany's emissions data before and after nuclear phase-out. Ask: If the goal is reducing carbon, did removing nuclear help or hurt?")
    ]
}

L03 = {
    "id": "G10L1-L03",
    "title": "Why Do Roller Coasters Make You Scream?",
    "subtitle": "Modeling Forces, Energy Conversion, and the Physics of Thrills",
    "ngss": "HS-PS2-1, HS-PS3-2",
    "ngss_desc": "Analyze data to support the claim that Newton's second law of motion describes the mathematical relationship among the net force on a macroscopic object, its mass, and its acceleration. Develop and use models to illustrate that energy at the macroscopic scale can be accounted for as a combination of energy associated with the motion of particles and energy associated with the relative positions of particles.",
    "big_question": "How do roller coaster designers use physics to create the most thrilling — but still safe — ride possible?",
    "objectives": [
        "Model how gravitational potential energy converts to kinetic energy as a coaster descends from its highest point",
        "Explain how coaster mass, track height, and velocity interact to determine the G-force experienced by riders",
        "Predict the velocity at any point on the track using energy conservation principles",
        "Analyze how engineers balance maximum thrills (high G-forces) with rider safety limits"
    ],
    "vocabulary": [
        ("Gravitational Potential Energy", "Energy stored due to an object's height above the ground — calculated as PE = mgh, where m is mass, g is gravitational acceleration, and h is height. The first hill of a roller coaster is its energy bank."),
        ("Kinetic Energy", "Energy of motion — calculated as KE = ½mv², meaning energy increases with the SQUARE of velocity. Doubling speed quadruples kinetic energy."),
        ("G-Force", "The force of acceleration experienced relative to gravity — 1G is normal gravity, 2G means you feel twice your weight, and 0G is weightlessness. Roller coasters typically reach 3-5G."),
        ("Energy Conservation", "The principle that energy cannot be created or destroyed, only converted between forms — on a roller coaster, potential energy converts to kinetic energy and vice versa, minus friction losses")
    ],
    "components": [
        ("Coaster Mass", "The total mass of the coaster train plus riders, measured in kilograms — heavier coasters have more potential energy at the top but the same velocity at the bottom (in ideal conditions)", True),
        ("Track Height", "The height of hills, drops, and loops on the track — the first hill determines maximum potential energy and therefore the maximum possible speed", True),
        ("Velocity", "The speed of the coaster at any point on the track, determined by how much potential energy has been converted to kinetic energy minus friction losses", False),
        ("G-Force on Rider", "The acceleration force experienced by riders, determined by velocity and the curvature of the track — centripetal acceleration in loops and valleys creates the thrilling sensations", False),
        ("Energy Conversion", "The continuous exchange between gravitational potential energy (height) and kinetic energy (speed) as the coaster moves along the track, with some energy lost to friction and air resistance", False)
    ],
    "think_about_it": "At the very top of the first hill, the coaster is barely moving — all its energy is potential. At the very bottom, it's going fastest — all potential has become kinetic. But where did the energy come from in the first place, and where does it go?",
    "scenarios": [
        ("Maximum Drop", "Set Track Height to maximum for the first hill and observe how Velocity, G-Force, and Energy Conversion change as the coaster plummets to the lowest point"),
        ("Mass Comparison", "Run the same track with different Coaster Mass values — does a heavier coaster go faster at the bottom?"),
        ("Loop-the-Loop", "Add a vertical loop to the track — what minimum Velocity is needed at the top of the loop to prevent the coaster from falling, and what G-Force do riders experience at the bottom?")
    ],
    "sim_scenarios": [
        ("Maximum Drop", "Track Height: Maximum first hill | Full drop", "What do you predict the coaster's velocity will be at the bottom of the tallest drop? How does height relate to speed?"),
        ("Mass Comparison", "Same track | Different coaster masses", "Do you predict a heavier coaster will go faster, slower, or the same speed at the bottom? Why?"),
        ("Loop-the-Loop", "Track includes a vertical loop", "What minimum speed do you predict the coaster needs at the top of the loop to avoid falling? What happens to G-Force at the loop's bottom?")
    ],
    "discoveries": [
        "The first hill of a roller coaster is its entire energy budget — every subsequent hill must be shorter because friction continuously removes energy from the system",
        "Coaster mass does NOT affect the speed at the bottom in ideal conditions (just like Galileo's famous experiment) — the velocity depends only on the height dropped",
        "G-force is created by centripetal acceleration in curves and loops — riders feel heaviest at the bottom of drops and lightest (or weightless) at the top of hills",
        "Energy conservation means the coaster can never go higher than its first hill without additional energy input — the chain lift at the start is the only motor"
    ],
    "answer": "Roller coasters exploit the physics of energy conservation and Newton's laws to create extreme sensations safely. The chain lift hauls the coaster to the top of the first hill, loading it with gravitational potential energy. As it drops, that potential energy converts to kinetic energy — speed. At the bottom, the coaster is going fastest; in loops and valleys, the rapid change in direction creates G-forces that push riders into their seats at 3-5 times their body weight, or make them weightless at crests. Engineers design every curve using F=ma and energy conservation to maximize thrills while keeping forces within safe human limits.",
    "stem_title": "Design the Ultimate Roller Coaster",
    "stem_mission": "Design a roller coaster track that maximizes rider excitement (measured by G-force variations and speed) while keeping all forces within safe human limits (under 5G sustained, under 6G instantaneous).",
    "stem_scenario": "A theme park has hired your engineering team to design their new signature coaster. The park has a 60-meter height limit and requires the ride to last at least 90 seconds. The coaster must include at least one vertical loop, one high-speed turn, and one airtime hill. Your design must prove — using physics calculations — that no point on the track exceeds safe G-force limits.",
    "stem_questions": [
        "What is the maximum speed your coaster can achieve given the 60-meter height limit?",
        "How will you design the loop diameter to ensure riders feel intense but safe G-forces?",
        "Where on your track will riders experience weightlessness, and how did you engineer that sensation?"
    ],
    "stem_design_qs": [
        "What height will your first hill be and how much potential energy does that give the coaster?",
        "How will you calculate the minimum speed needed at the top of each loop?",
        "Where will you place banked turns to manage lateral G-forces?",
        "How does friction affect your design — will the coaster have enough energy to complete the full track?"
    ],
    "career": "Roller Coaster Engineers (a specialty within Mechanical Engineering) design rides using fluid dynamics, structural analysis, and biomechanical G-force modeling. They work for companies like Bolliger & Mabillard, Intamin, and Disney Imagineering, earning $75,000–$140,000/year. Biomechanical engineers who study human G-force tolerance earn $70,000–$130,000/year.",
    "images": {
        "cover": ("G10L1-L03-cover.png", "A photorealistic, cinematic image of a roller coaster at the peak of a massive drop with riders' hands raised, dramatic angle from below showing the steep descent, blue sky background, motion blur on the track"),
        "landscape": ("G10L1-L03-landscape.png", "A diverse group of 15-16 year old students in a modern physics lab conducting experiments with ramp-and-marble setups to measure velocity and energy conversion, engaged expressions, lab equipment visible"),
        "modeling": ("G10L1-L03-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of roller coaster physics, screens showing energy diagrams and velocity curves, modern classroom"),
        "discussion": ("G10L1-L03-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about forces and energy, a free-body diagram and energy bar chart displayed on a smartboard, students gesturing and asking questions"),
        "stem": ("G10L1-L03-stem.png", "Diverse 15-16 year old students designing roller coaster tracks on large poster paper with rulers and protractors, some building small-scale models with foam tubing and marbles, collaborative engineering atmosphere")
    },
    "pre_assessment": [
        "What is it about a roller coaster that makes your stomach drop or pushes you into your seat?",
        "Where on a roller coaster are you going fastest? Where are you going slowest? Why?",
        "Draw an energy diagram showing what happens to energy as a roller coaster goes from the top of the first hill to the bottom.",
        "Why can't the second hill on a roller coaster ever be taller than the first?"
    ],
    "extend_components": [
        ("Friction and Air Resistance", "Energy losses due to wheel friction on the track and aerodynamic drag, which continuously reduce the coaster's total mechanical energy and limit how far the ride can travel"),
        ("Track Curvature Radius", "The radius of curves, loops, and transitions, which determines centripetal acceleration — tighter curves at high speed produce higher G-forces"),
        ("Rider Body Position", "How the rider's body orientation relative to the direction of force affects the G-force experience — positive Gs push blood down, negative Gs push blood to the head")
    ],
    "reflections": [
        "How does your model demonstrate the law of conservation of energy on a roller coaster?",
        "Why does mass cancel out of the velocity equation for an ideal coaster — and what does this tell us about gravity?",
        "Where on your coaster do riders experience maximum positive G-force? Maximum negative G-force? Weightlessness?",
        "How does friction change the energy conservation equation, and what does this mean for coaster design?",
        "What are the limitations of modeling a roller coaster with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students use mathematical models (PE=mgh, KE=½mv², F=ma, ac=v²/r) to predict coaster velocity, G-forces, and energy distribution at every point on the track."),
        ("Disciplinary Core Idea", "PS2.A Forces and Motion / PS3.A Definitions of Energy", "Newton's second law describes the relationship between net force, mass, and acceleration. Energy at the macroscopic scale can be accounted for as combinations of kinetic and potential energy."),
        ("Crosscutting Concept", "Energy and Matter", "Students track the conservation and conversion of energy throughout the coaster system, accounting for potential, kinetic, and thermal (friction) energy at every point.")
    ],
    "cast_items": [
        "Model energy conversion between gravitational potential and kinetic energy on a roller coaster track",
        "Calculate G-forces at specific track points using velocity and curvature data",
        "Design track geometry that maximizes rider experience while maintaining safe force limits"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A roller coaster with a first hill height of 50 meters reaches the bottom of the drop. Ignoring friction, which expression best predicts the coaster's velocity at the bottom?"),
        ("Constructed Response:", "Using your model and energy conservation principles, explain why the second hill on a roller coaster must always be shorter than the first. Include the role of friction in your explanation and calculate the maximum height of the second hill if the first hill is 60 meters and 10% of energy is lost to friction.")
    ],
    "background_intro": "Roller coasters are physics textbooks made of steel. Every drop, loop, and corkscrew is an exercise in energy conservation, Newton's laws, and human biomechanics. Engineers don't just build exciting rides — they calculate exactly how much force the human body can handle and design tracks that push right up to that limit without crossing it.",
    "background_sections": [
        ("Energy Conservation on a Coaster", "The chain lift at the start is the coaster's only energy input. It converts electrical energy into gravitational potential energy (PE = mgh). From the top of the first hill, all motion comes from converting this stored potential energy into kinetic energy (KE = ½mv²). At any point, PE + KE + Energy lost to friction = Initial PE. This is why every subsequent hill must be shorter — friction continuously removes energy from the system."),
        ("Why Mass Doesn't Matter", "Setting PE = KE: mgh = ½mv². The mass cancels: v = √(2gh). This means a 1,000 kg coaster and a 10,000 kg coaster reach the SAME speed at the bottom of the same drop. This is Galileo's insight — all objects fall at the same rate regardless of mass. In practice, heavier coasters lose slightly less speed to air resistance (proportionally) but more to friction."),
        ("G-Forces and Human Limits", "G-force is the acceleration experienced relative to gravity. At the bottom of a drop, centripetal acceleration adds to gravity: riders feel 1G (gravity) + v²/rg additional Gs. In a 3G turn, a 70 kg person feels 210 kg of force. Fighter pilots black out above 9G; most people become uncomfortable above 4G sustained. Coaster designers keep instantaneous peaks below 6G and sustained forces below 4G."),
        ("The Art of Airtime", "Airtime — the feeling of weightlessness — occurs when the coaster crests a hill and the track curves away faster than gravity pulls riders down. At the top of a parabolic hill, riders experience less than 1G — even 0G or negative G (floating off the seat). Engineers calculate the exact hill shape needed for each airtime moment using v²/r = g for 0G. This is what makes riders scream with delight.")
    ],
    "lever_L": "Students identify coaster mass, track height, velocity, G-force on rider, and energy conversion as the key components of the roller coaster physics system.",
    "lever_E": "Students determine that track height sets the potential energy budget, velocity depends on how much potential energy has converted to kinetic, and G-force depends on velocity and track curvature.",
    "lever_V": "Students build a computational model showing energy conversion along the track and G-force at key points including drops, loops, and hills.",
    "lever_Ev": "Students run maximum drop, mass comparison, and loop-the-loop scenarios to verify energy conservation and discover the relationship between track geometry and rider experience.",
    "lever_R": "Students add friction/air resistance, track curvature radius, or rider body position to model more realistic coaster dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic roller coaster image", "say": "The fastest coasters hit 150 mph. The most extreme pull 6 Gs — close to what fighter pilots experience. How do engineers build a ride that terrifies you but never hurts you?", "do": "Show a POV roller coaster video for 15 seconds. Ask: What's happening to your ENERGY and your BODY?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're using physics to design the most thrilling ride possible — and proving it's safe with math.", "do": "Have students read objectives. Pre-teach 'gravitational potential energy' and 'G-force.'", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do engineers build maximum thrills within safety limits?", "say": "At the top of the first hill, you're barely moving. At the bottom, you're going 100 mph. Where did that energy come from?", "do": "Students draw energy bar charts for top-of-hill vs. bottom-of-hill. Compare predictions.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building a physics model that can calculate the speed and G-force at every point on a roller coaster.", "do": "Preview LEVER steps. Emphasize this is engineering design backed by physics calculations.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for coaster physics model", "say": "What can coaster designers CHOOSE? What do the laws of physics DETERMINE for them?", "do": "Guide sorting. Mass and height are designer choices; velocity, G-force, and energy conversion are physics outcomes.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows and equations", "say": "The first hill is your energy bank. Every meter of height is money in the account. Every meter of friction is money spent.", "do": "Introduce PE=mgh, KE=½mv², and show how conservation connects height to speed.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Energy and velocity graphs along the track", "say": "Let's race — heavy coaster vs. light coaster. Same track. Who gets to the bottom first?", "do": "Students predict mass effects. Run simulation. Discover mass cancels. Then test the loop.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings and energy diagrams", "say": "Mass doesn't matter. Galileo was right 400 years ago. And now you know why the second hill is always shorter.", "do": "Connect discoveries to energy conservation. Discuss where friction fits in the real world.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Roller coaster design challenge", "say": "The theme park wants your design. 60 meters max height. At least one loop. Prove with math that nobody gets hurt.", "do": "Groups design tracks, calculate velocities and G-forces at key points. Present and defend designs.", "time": "12 min"}
    ],
    "sort_reasoning": "Coaster Mass and Track Height are external components because they are design choices made by engineers before the ride is built — they can be set to any value within constraints. Velocity, G-Force on Rider, and Energy Conversion are internal because they are physical outcomes determined by the laws of physics (conservation of energy, Newton's second law) once mass and track geometry are set.",
    "relationships": [
        ("Track Height to Velocity", "POSITIVE (+)", "Greater track height means more gravitational potential energy at the top. As the coaster drops, this converts to kinetic energy: v = √(2gh). A 60m drop produces about 34 m/s (76 mph) at the bottom, ignoring friction."),
        ("Velocity to G-Force on Rider", "POSITIVE (+)", "Higher velocity through curves and loops produces greater centripetal acceleration (a = v²/r), which translates to higher G-forces felt by riders. Doubling velocity quadruples the centripetal force."),
        ("Track Height to Energy Conversion", "DETERMINES", "The first hill height sets the total energy budget for the entire ride. Energy Conversion at any point follows conservation: KE + PE + friction losses = initial PE. No subsequent hill can exceed the first without additional energy input.")
    ],
    "sim_answers": [
        ("Maximum Drop Scenario", "As the coaster descends from maximum Track Height, the model shows potential energy converting smoothly to kinetic energy. At the lowest point, nearly all PE has become KE, and Velocity peaks. G-Force spikes in the transition curve at the bottom as centripetal acceleration adds to gravity. For a 60m drop, the coaster reaches approximately 34 m/s (76 mph), and a tight radius transition could produce 4-5G."),
        ("Mass Comparison Scenario", "The model reveals a surprising result: changing Coaster Mass does not change the velocity at the bottom. From v = √(2gh), mass cancels out entirely. A 5,000 kg coaster reaches exactly the same speed as a 10,000 kg coaster on the same drop. However, the heavier coaster has MORE kinetic energy (KE = ½mv²) and therefore more momentum, which affects braking distance and structural loads.")
    ],
    "reflection_exemplars": [
        ("Why does mass cancel out?", "When we set gravitational PE equal to kinetic energy at the bottom: mgh = ½mv². Dividing both sides by m gives gh = ½v², so v = √(2gh). Mass appears on BOTH sides and cancels. This is the same physics Galileo demonstrated — all objects fall at the same rate in a vacuum. The coaster is essentially 'falling' along a curved track, and like all falling objects, its speed depends only on how far it falls, not how heavy it is."),
        ("Where do riders feel weightless?", "Weightlessness occurs at the top of parabolic hills where the track curves away faster than gravity pulls the rider down. When the centripetal acceleration needed to follow the track equals g (9.8 m/s²), the rider experiences 0G — they feel no force from their seat. The model shows this happens when v²/r = g, or when the hill's radius of curvature r = v²/g. Engineers design these 'airtime' hills precisely to create floating sensations.")
    ],
    "stem_intro": "Present the challenge: A theme park is building a new signature coaster with a 60-meter height limit. Your engineering team must design a track that includes at least one loop, one banked turn, and one airtime hill, all while keeping G-forces within safe human limits. Use physics calculations to prove your design works.",
    "stem_concepts": [
        ("Centripetal Acceleration", "Any object moving in a curved path experiences centripetal acceleration toward the center of the curve: a = v²/r. On a roller coaster, this creates the forces that push riders into seats (bottom of loops) or lift them off (top of hills). Tighter radius + higher speed = more Gs."),
        ("Clothoid Loops", "Modern coasters don't use circular loops — they use clothoid (teardrop) shapes. The radius is larger at the bottom (reducing G-forces where speed is highest) and smaller at the top (maintaining enough centripetal force to keep riders pressed in). This design keeps G-forces between 3-5G throughout the loop."),
        ("Safety Margins", "Engineers design coasters with significant safety margins. If a track section produces 4G in calculations, the structure is built to withstand 8-10G. Human comfort limits (sustained 4G, instantaneous 6G) determine the design envelope, with additional factors for rider size and health variation.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design includes all required elements with correct physics calculations for velocity and G-force at every key point, demonstrates safe force limits, and optimizes for rider experience"),
        ("Proficient (3)", "Design includes required elements with reasonable velocity and G-force calculations at most key points"),
        ("Developing (2)", "Design includes some elements but calculations are incomplete or G-force safety isn't verified"),
        ("Beginning (1)", "Design lacks physics calculations or doesn't realistically address energy conservation and force limits")
    ],
    "support": [
        "Provide a formula reference card with PE=mgh, KE=½mv², v=√(2gh), a=v²/r, and G=a/g+1",
        "Use energy bar chart templates where students can shade PE and KE at each point along the track",
        "Sentence frames: 'At the bottom of the __ meter drop, the velocity is __ m/s because __, which produces __ G of force'"
    ],
    "extensions": [
        "Research the physics of the world's fastest coaster (Formula Rossa, 240 km/h) — how does it exceed the speed possible from its first hill?",
        "Investigate how roller coaster designers use computer simulations to test thousands of track designs before building prototypes",
        "Calculate the energy lost to friction on a real coaster by comparing actual speeds at the bottom of drops to ideal frictionless predictions"
    ],
    "cross_curr": [
        ("Math", "Calculate the velocity at the bottom of a 50m drop using v=√(2gh), then determine the G-force in a loop with a 15m radius at that speed. Graph energy conversion (PE and KE) versus position along the entire track."),
        ("ELA", "Write a physics-based review of a roller coaster you've ridden (or researched), explaining the science behind every sensation you felt — drops, loops, turns, and airtime moments"),
        ("Art/Engineering", "Create a detailed scale drawing of your coaster design with accurate dimensions, labeled physics quantities, and aesthetic theming that would attract riders")
    ],
    "misconceptions": [
        ("Heavier coasters go faster", "Mass cancels from the energy conservation equation: v = √(2gh). A heavier coaster has MORE energy but also requires MORE energy to accelerate — the effects cancel perfectly. This is Galileo's insight: all objects fall at the same rate regardless of mass (in a vacuum). In practice, heavier coasters lose slightly less speed to air resistance per unit mass, but this is a small effect.", "Drop two different-mass marbles down the same ramp. Measure their speeds at the bottom with a photogate timer. They're essentially identical — just like the equation predicts."),
        ("The motor drives the coaster through the whole ride", "The chain lift or launch at the start is the coaster's ONLY energy input. After that, the ride runs entirely on gravity and energy conservation. Every drop, loop, and turn uses energy from the first hill. The brakes at the end REMOVE energy — they don't add it. This is why the ride always comes back to a lower point than where it started.", "Watch a coaster video and identify: When is energy being ADDED? (Only the lift hill.) When is energy being REMOVED? (Friction throughout, brakes at the end.) Everything else is conversion."),
        ("G-forces are dangerous — the more the better for thrills", "G-forces are only thrilling within a narrow range. Below 0.5G, riders feel pleasantly floaty. At 3-5G, the sensation is intense and exciting. Above 6G sustained, blood pools in the legs and riders can lose vision (greyout) or consciousness (blackout). Above 9G, even fighter pilots in pressure suits can lose consciousness. Engineers design for the 'sweet spot' — intense enough to thrill, safe enough to ride 100 times.", "Research: What G-forces do astronauts experience during launch? (About 3G.) What about fighter pilots in tight turns? (6-9G.) Why do they need special suits?")
    ]
}

L04 = {
    "id": "G10L1-L04",
    "title": "How Does Your Phone Fit 10,000 Songs?",
    "subtitle": "Modeling Digital Signal Processing, Data Compression, and Recommendation Algorithms",
    "ngss": "HS-PS4-5, HS-ETS1-1",
    "ngss_desc": "Communicate technical information about how some technological devices use the principles of wave behavior and wave interactions with matter to transmit and capture information and energy. Analyze a major global challenge to specify qualitative and quantitative criteria and constraints for solutions that account for societal needs and wants.",
    "big_question": "How does a device the size of your palm store an entire music library and somehow know what song you want to hear next?",
    "objectives": [
        "Model how analog audio signals are digitized, compressed, and stored on electronic devices",
        "Explain the trade-off between audio quality and file size in data compression algorithms",
        "Analyze how recommendation algorithms use listening data to predict user preferences",
        "Evaluate the engineering trade-offs between signal quality, storage efficiency, and user experience"
    ],
    "vocabulary": [
        ("Digital Signal Processing", "The mathematical manipulation of analog signals (like sound waves) after they've been converted to digital data — enabling compression, filtering, and enhancement of audio information"),
        ("Data Compression", "Algorithms that reduce file size by removing redundant or imperceptible information — lossy compression (like MP3) permanently removes data, while lossless (like FLAC) preserves all original information"),
        ("Sampling Rate", "The number of times per second an analog sound wave is measured and converted to a digital value — CD quality uses 44,100 samples per second, capturing frequencies up to 22,050 Hz"),
        ("Recommendation Algorithm", "A computational system that analyzes patterns in user behavior data to predict preferences — Spotify's algorithm processes 100+ data points per listening session to suggest songs")
    ],
    "components": [
        ("Audio Signal Quality", "The fidelity of the original sound wave capture, determined by sampling rate and bit depth — higher quality means larger raw files but more accurate sound reproduction", True),
        ("Data Compression Rate", "The ratio of original file size to compressed file size, controlled by the compression algorithm settings — higher compression means smaller files but more information lost", True),
        ("Algorithm Accuracy", "How effectively the recommendation system predicts songs the user will enjoy, based on the quantity and quality of listening data processed", False),
        ("User Engagement", "The amount of time users spend listening and interacting with the platform, which generates more data and improves algorithm accuracy in a feedback loop", False),
        ("Recommendation Match", "The percentage of algorithmically suggested songs that the user actually listens to and enjoys, representing the system's real-world performance", False)
    ],
    "think_about_it": "When you compress a song from 50MB to 5MB, something must be removed. How does the algorithm decide what you won't miss — and what happens to the music experience when it removes too much?",
    "scenarios": [
        ("High Quality, Low Compression", "Set Audio Signal Quality to maximum and Data Compression Rate to minimal — observe file size, storage capacity, and audio fidelity"),
        ("Maximum Compression", "Push Data Compression Rate to extreme levels — observe how audio quality degrades and at what point the listener notices"),
        ("New User vs. Veteran", "Compare Algorithm Accuracy for a brand-new user (no data) versus a user with 10,000 listening hours — observe how data quantity drives recommendation quality")
    ],
    "sim_scenarios": [
        ("High Quality", "Audio Quality: Maximum | Compression: Minimal", "How many songs do you predict can fit on a 64GB device at maximum quality versus maximum compression?"),
        ("Maximum Compression", "Audio Quality: Standard | Compression: Maximum", "At what compression ratio do you predict the average listener will start noticing audio quality loss?"),
        ("New vs. Veteran User", "Comparing algorithm with 0 vs. 10,000 hours of data", "How many data points do you predict the algorithm needs before its recommendations match what you'd choose yourself?")
    ],
    "discoveries": [
        "Data compression exploits human perception limits — MP3 removes frequencies most people can't hear and sounds masked by louder sounds, reducing file size by 90% with minimal perceived quality loss",
        "There's a critical compression threshold beyond which quality drops noticeably — the algorithm must balance file size against the limits of human hearing perception",
        "Recommendation algorithms improve through a feedback loop: more listening generates more data, which improves predictions, which increases engagement, which generates more data",
        "The entire modern music industry depends on the same wave physics principles that govern how sound travels through air — digitization is simply converting those waves to numbers"
    ],
    "answer": "Your phone fits 10,000 songs through a brilliant exploitation of psychoacoustics — the science of human hearing perception. Compression algorithms like AAC and MP3 analyze each song's sound waves and remove frequencies your ear can't hear (above ~20kHz), sounds masked by louder sounds, and redundant data patterns. A 50MB raw audio file becomes 5MB with virtually no perceptible quality loss. Recommendation algorithms then use your listening patterns — skip rates, repeat plays, time of day, genre sequences — to predict what you want to hear next. Both technologies are applied wave physics and computational mathematics working together.",
    "stem_title": "Design a Music Discovery Platform",
    "stem_mission": "Design a music streaming system that optimizes the balance between audio quality, storage efficiency, and recommendation accuracy for a target user group.",
    "stem_scenario": "A startup is building a music app for students that must work on devices with limited storage (16GB) and unreliable cellular data. The app needs to store enough songs for offline listening while still delivering good sound quality and accurate recommendations. Your team must specify the compression settings, storage allocation, and recommendation algorithm approach.",
    "stem_questions": [
        "What compression format and settings will you use to balance quality and storage on limited devices?",
        "How will your recommendation algorithm handle new users with no listening history?",
        "What data will you collect from users, and how does privacy factor into your design?"
    ],
    "stem_design_qs": [
        "How much storage will you allocate for music versus app functionality and cached data?",
        "What audio quality settings will you offer and what are the trade-offs of each?",
        "How will you handle the cold-start problem when a new user has no listening data?",
        "What metrics will you use to measure whether your recommendations are actually good?"
    ],
    "career": "Audio Engineers design sound recording, processing, and playback systems using wave physics and digital signal processing. They work in music studios, tech companies (Spotify, Apple, Sony), and live sound, earning $50,000–$120,000/year. Data Scientists who build recommendation algorithms earn $90,000–$180,000/year at tech companies.",
    "images": {
        "cover": ("G10L1-L04-cover.png", "A photorealistic, cinematic image of a smartphone displaying a music app with colorful waveform visualizations, high-quality earbuds connected, sound wave patterns emanating from the phone in a creative artistic style, modern dark background"),
        "landscape": ("G10L1-L04-landscape.png", "A diverse group of 15-16 year old students in a modern technology lab comparing audio files at different compression levels using headphones and waveform displays on computer screens, engaged expressions"),
        "modeling": ("G10L1-L04-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of data compression and signal processing, modern classroom with audio equipment and wave diagrams visible"),
        "discussion": ("G10L1-L04-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about how digital audio works, waveform comparisons displayed on a smartboard showing original versus compressed audio signals"),
        "stem": ("G10L1-L04-stem.png", "Diverse 15-16 year old students designing a music app prototype on whiteboards with wireframes, data flow diagrams, and compression charts, collaborative design thinking atmosphere")
    },
    "pre_assessment": [
        "How do you think a song gets from a recording studio onto your phone?",
        "What do you think happens to the sound quality when a music file is compressed to save space?",
        "Draw a diagram showing how you think sound waves are converted into digital data.",
        "How do you think Spotify or Apple Music knows what songs to recommend to you?"
    ],
    "extend_components": [
        ("Bit Depth", "The number of bits used to represent each audio sample — 16-bit provides 65,536 possible values per sample while 24-bit provides over 16 million, capturing quieter details and greater dynamic range"),
        ("Network Bandwidth", "The speed of the data connection available for streaming, which limits the quality of audio that can be delivered in real time and determines whether compression must be increased"),
        ("Listening Context", "Environmental factors like background noise, earphone quality, and listener attention that affect whether compression artifacts are perceptible")
    ],
    "reflections": [
        "How does your model demonstrate the trade-off between file size and audio quality?",
        "Why is it important that compression algorithms are based on human perception rather than pure mathematics?",
        "What feedback loop drives recommendation algorithm improvement, and what are its limitations?",
        "How would your model change if the target user was an audiophile versus a casual listener?",
        "What ethical questions arise from algorithms that learn your preferences and influence your listening behavior?"
    ],
    "dimensions": [
        ("Science Practice", "Constructing Explanations and Designing Solutions", "Students construct explanations of how wave behavior enables digital audio capture and design solutions that balance quality, storage, and user experience."),
        ("Disciplinary Core Idea", "PS4.C Information Technologies and Instrumentation / ETS1.A Defining and Delimiting Engineering Problems", "Technological devices use wave principles to capture, process, and transmit audio information. Engineering problems require specifying criteria and constraints."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the music streaming system as interconnected subsystems — signal capture, compression, storage, and recommendation — that must be optimized together.")
    ],
    "cast_items": [
        "Model how analog audio signals are digitized and compressed using wave behavior principles",
        "Evaluate the trade-off between audio fidelity and storage efficiency at different compression levels",
        "Analyze how recommendation algorithms use data patterns to predict user preferences"
    ],
    "cast_questions": [
        ("Multiple Choice:", "An uncompressed WAV file of a 3-minute song is 30MB. After MP3 compression at 128kbps, the file is 2.8MB. What percentage of the original data was removed, and why don't most listeners notice?"),
        ("Constructed Response:", "Using your model, explain how a music streaming service can deliver audio that sounds nearly identical to the original recording while using only 10% of the data. Connect your explanation to wave behavior, human hearing perception, and compression algorithm design.")
    ],
    "background_intro": "The ability to carry thousands of songs in your pocket represents one of the most remarkable applications of wave physics and computational mathematics in history. Every song on your phone began as vibrations in air, was converted to electrical signals, digitized into numbers, compressed by algorithms that exploit human hearing limits, and stored as magnetic patterns on a tiny chip. Understanding this chain means understanding both the physics of waves and the engineering of information.",
    "background_sections": [
        ("Sound as Waves", "Sound is a longitudinal pressure wave traveling through air at about 343 m/s. The wave's frequency (20 Hz to 20,000 Hz for human hearing) determines pitch, and its amplitude determines loudness. When a microphone captures sound, it converts these pressure variations into an analog electrical signal that mirrors the original wave pattern."),
        ("Analog-to-Digital Conversion", "To store sound digitally, the analog signal must be sampled — measured at regular intervals — and quantized — rounded to the nearest digital value. CD quality uses 44,100 samples per second (Nyquist theorem requires 2x the highest frequency) at 16-bit depth (65,536 possible values per sample). This produces about 10MB of raw data per minute of stereo music."),
        ("Psychoacoustic Compression", "MP3, AAC, and Ogg Vorbis compression algorithms exploit the limits of human hearing through a technique called perceptual coding. Sounds below the hearing threshold are removed. When a loud sound masks a quiet sound (simultaneous masking), the quiet sound is removed. Sounds that occur just before or after a loud sound are also removed (temporal masking). The result: 90% data reduction with minimal perceived quality loss."),
        ("Machine Learning Recommendations", "Modern recommendation systems use collaborative filtering (users who liked X also liked Y), content analysis (analyzing the audio features of songs — tempo, key, energy, danceability), and deep learning (neural networks that find complex patterns in billions of listening sessions). Spotify's 'Discover Weekly' playlist analyzes over 100 data points per song per listener to generate 30 personalized recommendations each Monday.")
    ],
    "lever_L": "Students identify audio signal quality, data compression rate, algorithm accuracy, user engagement, and recommendation match as the key components of the digital music system.",
    "lever_E": "Students determine that audio quality and compression rate have an inverse relationship, and that algorithm accuracy improves through a feedback loop with user engagement — more data means better predictions.",
    "lever_V": "Students build a computational model showing how compression settings affect storage capacity and audio fidelity, and how user data volume drives recommendation performance.",
    "lever_Ev": "Students run high quality, maximum compression, and new-vs-veteran user scenarios to discover the perception threshold for compression and the data requirement for accurate recommendations.",
    "lever_R": "Students add bit depth, network bandwidth, or listening context to model more realistic streaming system dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with phone displaying music library", "say": "Your phone has 10,000 songs on it. Each song started as vibrations in a recording studio. How did AIR VIBRATIONS become DATA in your pocket?", "do": "Show file size comparison: one uncompressed WAV song (50MB) vs. 10,000 compressed songs on a 64GB phone. How is that possible?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're tracing the journey of a sound wave from a singer's mouth to your earbuds — and every transformation along the way.", "do": "Have students read objectives. Pre-teach 'data compression' and 'sampling rate' with audio examples.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does 10,000 songs fit in your palm?", "say": "If one song takes 50MB uncompressed, 10,000 songs would need 500GB. Your phone has 64GB. Something is being removed. What?", "do": "Students calculate: How much data must be removed? What could possibly be expendable in a song?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're modeling the entire chain — from sound wave to compressed file to recommended playlist.", "do": "Preview LEVER steps. Emphasize this connects wave physics to information technology.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for digital music model", "say": "What can a streaming service CONTROL? What outcomes emerge from those choices?", "do": "Guide sorting. Audio quality and compression rate are design choices; engagement and match are outcomes.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "More compression means smaller files but worse sound. Where's the sweet spot where your ears can't tell the difference?", "do": "Play audio samples at different compression levels. Can students identify which is compressed?", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Compression quality curves and recommendation accuracy graphs", "say": "Let's find the threshold — the exact compression level where your ears stop noticing the difference.", "do": "Students predict the perception threshold. Run simulations. Then test new-user vs. veteran recommendation accuracy.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings about compression and algorithms", "say": "The algorithm removes sounds you literally CANNOT hear. And the recommendation engine gets better every time you press play or skip.", "do": "Connect psychoacoustic masking to wave physics. Discuss the feedback loop driving algorithm improvement.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Music platform design challenge", "say": "Build a music app for students with cheap phones and bad wifi. Make it sound good, fit a lot of songs, and recommend what they'll love.", "do": "Groups design streaming systems balancing quality, storage, and recommendation. Present solutions.", "time": "12 min"}
    ],
    "sort_reasoning": "Audio Signal Quality and Data Compression Rate are external components because they are engineering design choices — a streaming service decides what recording quality to use and how aggressively to compress files. Algorithm Accuracy, User Engagement, and Recommendation Match are internal because they emerge from the interaction between the system and user behavior — they cannot be directly set but result from how well the system works.",
    "relationships": [
        ("Audio Signal Quality to Data Compression Rate", "INVERSE", "Higher audio quality means larger raw files that require more aggressive compression to fit in limited storage. Engineers must balance capturing high-fidelity sound against the need to reduce file size for practical storage and streaming."),
        ("Data Compression Rate to User Engagement", "COMPLEX (+/-)", "Moderate compression maintains audio quality that keeps users engaged. But excessive compression degrades quality enough that users disengage — there is an optimal zone where files are small enough to store efficiently but good enough to enjoy."),
        ("User Engagement to Algorithm Accuracy", "POSITIVE (+)", "More user engagement generates more listening data — play counts, skip rates, completion rates, time-of-day patterns. This data trains the recommendation algorithm, improving its accuracy. The more you listen, the better it knows you.")
    ],
    "sim_answers": [
        ("High Quality Scenario", "At maximum Audio Signal Quality with minimal Data Compression Rate, each song takes approximately 50MB (uncompressed WAV) or 15MB (lossless FLAC). A 64GB device holds only about 1,200-4,200 songs at these settings. The audio fidelity is perfect, but storage is severely limited. Most listeners cannot distinguish this quality from well-compressed audio in typical listening environments."),
        ("New vs. Veteran User Scenario", "A brand-new user with zero listening history receives generic, popularity-based recommendations with about 20-30% match rate. After 100 hours of listening, the algorithm has enough behavioral data to identify genre preferences, increasing match to ~50%. After 1,000+ hours, the system understands nuanced taste patterns — tempo preferences, lyrical themes, seasonal patterns — reaching 70-80% match rate. This demonstrates the feedback loop: engagement drives data, data drives accuracy.")
    ],
    "reflection_exemplars": [
        ("Why is human perception the key to compression?", "Compression algorithms don't just remove random data — they remove data that human ears cannot perceive. The MP3 algorithm uses a psychoacoustic model that predicts which frequencies are masked by louder sounds, which sounds fall below the hearing threshold, and which temporal details the brain fills in automatically. This means compression is fundamentally about BIOLOGY as much as mathematics — the algorithm succeeds because it exploits the limitations of the human auditory system."),
        ("What ethical concerns arise from recommendation algorithms?", "Recommendation algorithms create filter bubbles — by always suggesting similar music, they can narrow a listener's exposure and reinforce existing preferences rather than introducing diversity. The engagement feedback loop optimizes for TIME SPENT, not necessarily for genuine satisfaction or musical growth. Additionally, these systems collect enormous amounts of behavioral data — what you listen to, when, where, and how you react — raising significant privacy concerns. The model reveals that optimizing for engagement can conflict with optimizing for user well-being.")
    ],
    "stem_intro": "Present the challenge: A startup needs a music app that works on budget devices with 16GB storage and unreliable connectivity. Your team must specify compression formats, quality settings, storage allocation, and a recommendation approach that provides an excellent experience within severe technical constraints.",
    "stem_concepts": [
        ("Perceptual Coding", "The mathematical technique that analyzes audio signals to identify and remove sounds that fall below human perception thresholds. It relies on psychoacoustic models derived from decades of hearing research and is the foundation of all modern lossy audio compression."),
        ("Cold-Start Problem", "The challenge of making recommendations for new users who have no listening history. Solutions include asking for initial preferences, using demographic data, or starting with popular content and rapidly adapting as the user provides implicit feedback through plays and skips."),
        ("Adaptive Bitrate Streaming", "Technology that automatically adjusts audio quality based on available network bandwidth. When connection is strong, full-quality audio streams; when connection weakens, the system seamlessly drops to lower quality to prevent buffering. This requires encoding each song at multiple quality levels.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design specifies compression format with justified quality settings, addresses storage allocation with calculations, solves the cold-start problem for recommendations, and accounts for variable network conditions"),
        ("Proficient (3)", "Design addresses compression quality and storage with reasonable specifications and mentions recommendation approach"),
        ("Developing (2)", "Design identifies some technical considerations but lacks specific settings, calculations, or justified trade-offs"),
        ("Beginning (1)", "Design is incomplete or doesn't connect wave physics principles to digital audio technology")
    ],
    "support": [
        "Provide a visual diagram showing the analog-to-digital conversion pipeline from microphone to compressed file",
        "Use a listening comparison activity where students rate audio quality at 64kbps, 128kbps, 256kbps, and lossless",
        "Sentence frames: 'Compressing at __ kbps reduces file size by __% because the algorithm removes __, which listeners __'"
    ],
    "extensions": [
        "Research how Dolby Atmos and spatial audio encode 3D sound positioning information — what additional data is needed and how is it compressed?",
        "Investigate the audiophile debate: Can trained listeners really distinguish between 320kbps MP3 and lossless FLAC? Design a double-blind test to find out.",
        "Explore how deepfake audio technology uses AI to synthesize realistic speech and music — what are the ethical implications?"
    ],
    "cross_curr": [
        ("Math", "Calculate storage requirements: A 44,100 Hz sampling rate at 16-bit stereo produces how many bytes per second? Per minute? How does 10:1 compression change these numbers? How many songs fit on 64GB?"),
        ("ELA", "Write a persuasive essay arguing whether music streaming algorithms are beneficial (helping discover new music) or harmful (creating filter bubbles and reducing musical diversity)"),
        ("Social Studies", "Research how music streaming has transformed the music industry economically — who benefits and who loses when physical albums are replaced by algorithmic playlists?")
    ],
    "misconceptions": [
        ("Compressed music sounds terrible compared to the original", "Modern lossy compression at 256kbps or higher is virtually indistinguishable from the original in controlled listening tests. The compression algorithm specifically removes sounds that fall below human perception thresholds — frequencies you can't hear and sounds masked by louder sounds. Most people cannot identify the compressed version in a blind A/B test at standard quality settings.", "Run a blind listening test in class: play a WAV and a 256kbps AAC version of the same song. Can anyone consistently identify which is compressed? Most cannot."),
        ("More data always means better recommendations", "While more data generally improves recommendations, there are diminishing returns and quality matters more than quantity. An algorithm with 100 hours of diverse listening data often outperforms one with 1,000 hours of repetitive data. Additionally, more data collection raises privacy concerns — the question isn't just CAN we collect more data, but SHOULD we.", "Thought experiment: If the algorithm tracked your location, heart rate, and mood while listening, it would make better recommendations. Would you accept that trade-off?"),
        ("Digital music perfectly captures the original sound", "Digitization is a sampling process that captures snapshots of the sound wave at regular intervals. Between samples, the original analog information is lost and must be interpolated. At CD quality (44.1kHz), the Nyquist theorem guarantees frequencies up to 22.05kHz are captured accurately — sufficient for human hearing (20Hz-20kHz). But no digital format captures every infinitesimal detail of the original analog wave.", "Show a zoomed-in view of a smooth sine wave versus its sampled staircase approximation. At normal zoom, they look identical. The difference is real but below human perception — which is the entire point.")
    ]
}

L05 = {
    "id": "G10L1-L05",
    "title": "Why Are You Taller Than Your Grandparents?",
    "subtitle": "Modeling Gene Expression, Nutrition, and the Secular Trend in Human Height",
    "ngss": "HS-LS3-2, HS-LS3-3",
    "ngss_desc": "Make and defend a claim based on evidence that inheritable genetic variations may result from new genetic combinations through meiosis, viable errors occurring during replication, and/or mutations caused by environmental factors. Apply concepts of statistics and probability to explain the variation and distribution of expressed traits in a population.",
    "big_question": "If your DNA is inherited from your grandparents, how can you be significantly taller than they were at your age?",
    "objectives": [
        "Model how gene expression and environmental factors interact to determine final adult height",
        "Explain the role of nutrition, growth hormones, and bone growth in the secular trend toward increased height",
        "Predict how changes in nutrition quality and gene expression affect growth trajectories",
        "Analyze the statistical distribution of height in populations and the relative contributions of genetics versus environment"
    ],
    "vocabulary": [
        ("Gene Expression", "The process by which information from a gene is used to create a functional product like a protein — not all genes are active at all times, and environmental factors can turn genes on or off"),
        ("Secular Trend", "A change in a population's physical characteristics over generations due to environmental improvements — average human height has increased about 10cm in developed countries over the past 150 years"),
        ("Epigenetics", "Changes in gene activity that do not alter the DNA sequence itself — environmental factors like nutrition can activate or silence growth-related genes through chemical modifications to DNA"),
        ("Growth Plate", "Areas of developing cartilage near the ends of long bones where new bone tissue is produced — when growth plates close (fuse) in late adolescence, height increase stops permanently")
    ],
    "components": [
        ("Gene Expression Level", "The degree to which height-related genes are activated and producing growth proteins — determined by both inherited DNA and epigenetic modifications from environmental signals", False),
        ("Growth Hormone Release", "The amount of human growth hormone (HGH) secreted by the pituitary gland, which stimulates cell reproduction and bone growth — influenced by sleep, exercise, and nutrition", False),
        ("Nutrition Quality", "The availability of essential proteins, minerals (calcium, zinc), and vitamins (D, A) required for bone growth and overall development — the primary environmental driver of the secular height trend", True),
        ("Bone Growth Rate", "The speed at which growth plates produce new cartilage that ossifies into bone, extending the length of long bones — active until plates fuse in late teens", False),
        ("Final Height", "The adult height reached when growth plates close, representing the cumulative result of genetic potential interacting with environmental conditions throughout childhood and adolescence", False)
    ],
    "think_about_it": "Your grandparents had similar genes to yours, but many grew up during times of food scarcity or lower-quality nutrition. If the DNA blueprint is the same, how can the outcome — your height — be so different?",
    "scenarios": [
        ("Optimal Nutrition", "Set Nutrition Quality to maximum — observe how Gene Expression Level, Growth Hormone Release, and Bone Growth Rate respond to abundant nutrients, maximizing genetic height potential"),
        ("Nutritional Deprivation", "Set Nutrition Quality to low — observe how growth-related gene expression is suppressed and Bone Growth Rate decreases even with the same genetic potential"),
        ("Generational Comparison", "Compare two scenarios with identical genetic components but 1940s nutrition versus 2020s nutrition — observe the height difference that results purely from environmental change")
    ],
    "sim_scenarios": [
        ("Optimal Nutrition", "Nutrition Quality: Maximum | All other factors responding", "What do you predict happens to Final Height when nutrition is excellent throughout childhood?"),
        ("Nutritional Deprivation", "Nutrition Quality: Low | Simulating historical conditions", "How much shorter do you predict a person will be if nutrition is poor, even with the same genes?"),
        ("Generational Comparison", "Same genes | 1940s vs. 2020s nutrition", "What height difference do you predict between genetically similar people raised in different nutritional environments?")
    ],
    "discoveries": [
        "Genetics sets a RANGE of possible heights (about 80% of variation), but environmental factors — especially nutrition — determine where within that range an individual falls",
        "The secular trend in height is almost entirely explained by improvements in childhood nutrition, not by genetic changes (evolution works too slowly for this)",
        "Nutrition quality affects gene expression epigenetically — better nutrition activates more growth-related genes and increases growth hormone release",
        "Growth plates have a limited window of activity — once they fuse in late adolescence, no amount of nutrition or hormones can increase height, making childhood nutrition critically important"
    ],
    "answer": "You're taller than your grandparents not because your DNA changed — it's essentially the same — but because your environment is radically different. Better nutrition during your childhood provided the raw materials (proteins, calcium, zinc, vitamin D) for maximum bone growth, triggered higher growth hormone release, and activated gene expression that might have remained dormant under poorer conditions. Your genes set a height RANGE; nutrition determines where in that range you land. Your grandparents had the same genetic potential but didn't have the environmental conditions to reach it.",
    "stem_title": "Design a Childhood Nutrition Optimization Program",
    "stem_mission": "Design an evidence-based nutrition program for a school district that maximizes growth potential and health outcomes for students, particularly those from food-insecure backgrounds.",
    "stem_scenario": "A school district serving 15,000 students has identified that 40% of its students are food insecure and many are below expected height-for-age percentiles. The superintendent has hired your team to design a comprehensive school nutrition program that uses the science of gene expression and growth to optimize student health outcomes within a realistic budget.",
    "stem_questions": [
        "Which specific nutrients are most critical for bone growth and at what ages do they matter most?",
        "How will you address food insecurity during weekends, holidays, and summer when school meals aren't available?",
        "What measurable outcomes will you track to evaluate whether your program is working?"
    ],
    "stem_design_qs": [
        "What will a growth-optimized school breakfast and lunch look like based on the science of bone growth?",
        "How will you ensure students from food-insecure homes receive adequate nutrition outside school hours?",
        "What role should nutrition education play alongside direct food provision?",
        "How would you measure the program's impact on student growth trajectories over 3-5 years?"
    ],
    "career": "Nutritional Scientists study how food components affect gene expression, growth, and health. They work in research institutions, public health agencies, and food companies, earning $55,000–$110,000/year. Endocrinologists who specialize in growth hormones and developmental biology earn $200,000–$350,000/year as medical specialists.",
    "images": {
        "cover": ("G10L1-L05-cover.png", "A photorealistic, cinematic image showing a height comparison between generations — a tall diverse 15-16 year old student standing back-to-back with a shorter grandparent figure, both smiling warmly, a growth chart visible in the background, warm natural lighting"),
        "landscape": ("G10L1-L05-landscape.png", "A diverse group of 15-16 year old students in a modern biology lab examining bone growth plate models and DNA diagrams, measuring tools and growth charts visible, engaged expressions"),
        "modeling": ("G10L1-L05-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of gene expression and growth, classroom with genetics posters and height distribution charts on walls"),
        "discussion": ("G10L1-L05-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about genetics and environment, a gene expression diagram and height data graphs displayed on a smartboard, students taking notes"),
        "stem": ("G10L1-L05-stem.png", "Diverse 15-16 year old students designing nutrition program proposals on large poster boards with food pyramids, growth data charts, and budget calculations, collaborative health science atmosphere")
    },
    "pre_assessment": [
        "Are you taller or shorter than your parents were at your age? What about your grandparents?",
        "How much of your height do you think is determined by your genes versus your environment?",
        "Draw a diagram showing what factors you think contribute to how tall you grow.",
        "Why do you think the average height of people in many countries has increased over the past century?"
    ],
    "extend_components": [
        ("Sleep Quality", "The duration and depth of sleep, particularly deep sleep stages when growth hormone is released in its largest pulses — chronic sleep deprivation during childhood can significantly reduce growth"),
        ("Physical Activity Level", "Exercise stimulates growth hormone release and bone remodeling — weight-bearing exercise increases bone density, and moderate exercise promotes growth plate activity"),
        ("Stress Hormone Levels", "Chronic stress increases cortisol, which inhibits growth hormone release and can suppress growth plate activity — childhood adversity has measurable effects on growth trajectories")
    ],
    "reflections": [
        "How does your model demonstrate that identical genes can produce different heights depending on environment?",
        "What does the 80/20 genetics-environment split mean for predicting height — can we predict adult height from DNA alone?",
        "Why is the secular trend in height evidence for environmental influence rather than genetic evolution?",
        "How does the concept of epigenetics challenge the traditional nature-versus-nurture debate?",
        "What are the limitations of modeling a complex biological process like growth with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Engaging in Argument from Evidence", "Students make and defend claims about the relative contributions of genetic variation and environmental factors to expressed traits in populations."),
        ("Disciplinary Core Idea", "LS3.B Variation of Traits", "Environmental factors also affect expression of traits. Genes may be turned on or off by environmental conditions, and the expression of genes influences an organism's traits."),
        ("Crosscutting Concept", "Cause and Effect", "Students analyze the causal relationships between nutrition, gene expression, growth hormone release, and final height, distinguishing genetic causes from environmental ones.")
    ],
    "cast_items": [
        "Model the interaction between genetic potential and environmental factors in determining expressed height",
        "Analyze population height data to distinguish genetic variation from environmental effects",
        "Predict how changes in nutrition quality affect growth trajectories and final adult height"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A study finds that identical twins raised in different countries with different nutrition levels differ in adult height by 8 cm. What does this most strongly support about the determinants of height?"),
        ("Constructed Response:", "Using your model, explain why average human height in developed nations increased by approximately 10 cm over the past 150 years despite no significant genetic changes in the population. Include the roles of gene expression, nutrition, and growth hormones in your explanation.")
    ],
    "background_intro": "Over the past 150 years, the average height of people in developed countries has increased by about 10 centimeters — roughly 4 inches. This 'secular trend' happened far too quickly to be genetic evolution (which takes thousands of years). The explanation lies in the remarkable interaction between genes and environment: your DNA sets the blueprint, but the materials and conditions during construction determine the final product.",
    "background_sections": [
        ("The Genetics of Height", "Height is a polygenic trait — controlled by over 700 identified genetic variants, each contributing a small amount. Together, genetics accounts for about 80% of height variation within a population. However, this 80% is the variation between individuals in the SAME environment. When environments differ dramatically (as between your generation and your grandparents'), environmental factors can shift the entire distribution by centimeters."),
        ("The Secular Trend in Height", "In the Netherlands, average male height increased from 165 cm in 1860 to 183 cm in 2020 — an increase of 18 cm in just 160 years (about 6 generations). Japan saw a 15 cm increase in the 50 years after World War II when nutrition rapidly improved. In contrast, North Koreans are now about 8 cm shorter than South Koreans on average — same genetic background, dramatically different nutrition."),
        ("Nutrition and Gene Expression", "Nutrition affects height through multiple pathways. Protein provides amino acids for growth hormone and bone matrix. Calcium and phosphorus form hydroxyapatite crystals in bone. Vitamin D enables calcium absorption. Zinc is essential for growth plate function. When these nutrients are abundant, growth-related genes are fully expressed. When they're scarce, epigenetic mechanisms dial down gene expression — the genetic potential exists but isn't realized."),
        ("Growth Plates and the Window of Opportunity", "Growth plates (epiphyseal plates) are zones of cartilage near the ends of long bones. Chondrocytes in these plates divide, producing new cartilage that gradually calcifies into bone, lengthening the bone. Growth hormone and sex hormones (estrogen, testosterone) regulate this process. In late adolescence, rising sex hormone levels trigger growth plate closure (fusion). Once closed, no further height increase is possible — making childhood and adolescent nutrition critically important.")
    ],
    "lever_L": "Students identify gene expression level, growth hormone release, nutrition quality, bone growth rate, and final height as the key components of the human growth system.",
    "lever_E": "Students determine that nutrition quality drives gene expression and growth hormone release, which together control bone growth rate, and that the cumulative effect of bone growth determines final height.",
    "lever_V": "Students build a computational model showing how environmental nutrition interacts with genetic potential through gene expression to determine growth trajectory and final height.",
    "lever_Ev": "Students run optimal nutrition, deprivation, and generational comparison scenarios to quantify the environmental contribution to height and model the secular trend.",
    "lever_R": "Students add sleep quality, physical activity level, or stress hormone levels to model more realistic growth dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with generational height comparison image", "say": "Look at photos of your grandparents as teenagers. Many of you are 3-5 inches taller than they were. Same family. Same genes. So what changed?", "do": "Show historical photos of teenagers from the 1940s vs. today. Ask students to observe the visible height difference.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're solving a genetic mystery — how can your DNA be basically the same as your grandparents' but you're significantly taller?", "do": "Have students read objectives. Pre-teach 'gene expression' and 'epigenetics' — genes are like a library, but environment decides which books get read.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Same genes, different heights — how?", "say": "If height is 80% genetic and your DNA came from your grandparents, why aren't you the same height?", "do": "Quick survey: Are you taller than your grandparents were at your age? Taller than your parents? Discuss patterns.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're modeling the interaction between your genes and your environment to solve this height mystery.", "do": "Preview LEVER steps. Emphasize this is about gene-ENVIRONMENT interaction, not just genetics.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for growth model", "say": "What factors determine how tall you grow? Which ones come from outside your body?", "do": "Guide sorting. Nutrition is the key external input. Discuss why gene expression responds to environment.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between components", "say": "When nutrition improves, what chain reaction happens inside your body? Follow the pathway from food to bone growth.", "do": "Map the cascade: nutrition → gene expression → growth hormone → bone growth → height. Discuss where the pathway can be limited.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Growth curves and height distribution graphs", "say": "Let's model the height difference between your grandparents' nutrition and yours. How many centimeters does nutrition add?", "do": "Students predict the nutrition effect. Run generational comparison. Compare to real secular trend data.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings — genetics vs. environment data", "say": "Your genes set the ceiling. Your nutrition determines how close you get to it. Your grandparents had the same ceiling — they just couldn't reach it.", "do": "Show North Korea vs. South Korea height comparison. Same genes, 8 cm difference. Discuss implications.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Nutrition program design challenge", "say": "40% of students in this school district are food insecure. If nutrition determines how close kids get to their genetic potential, what should we do about it?", "do": "Groups design school nutrition programs that optimize growth. Must include specific nutrients, delivery systems, and evaluation metrics.", "time": "12 min"}
    ],
    "sort_reasoning": "Nutrition Quality is the external component because it represents the environmental input that can be changed through food access, diet quality, and supplementation — it comes from outside the body. Gene Expression Level, Growth Hormone Release, Bone Growth Rate, and Final Height are all internal because they are biological processes and outcomes that occur within the body in response to both genetic programming and environmental inputs.",
    "relationships": [
        ("Nutrition Quality to Gene Expression Level", "POSITIVE (+)", "Better nutrition — especially protein, calcium, zinc, and vitamin D — provides the molecular signals that activate height-related genes through epigenetic mechanisms. Nutrient abundance turns on growth genes that remain dormant under scarcity."),
        ("Gene Expression Level to Growth Hormone Release", "POSITIVE (+)", "When growth-related genes are actively expressed, they produce proteins that stimulate the pituitary gland to release more growth hormone. Gene expression sets the biological stage for the hormonal cascade that drives growth."),
        ("Growth Hormone Release to Bone Growth Rate", "POSITIVE (+)", "Growth hormone directly stimulates chondrocyte proliferation in growth plates and promotes IGF-1 production, which drives bone lengthening. More growth hormone during the active growth period means faster bone elongation and ultimately greater height.")
    ],
    "sim_answers": [
        ("Optimal Nutrition Scenario", "When Nutrition Quality is at maximum, the model shows height-related Gene Expression Level increasing significantly as growth genes are fully activated. Growth Hormone Release rises correspondingly, driving high Bone Growth Rate throughout childhood and adolescence. Final Height approaches the maximum of the individual's genetic potential — the full 'ceiling' set by their DNA."),
        ("Generational Comparison Scenario", "With identical genetic components but 1940s-level nutrition versus 2020s-level nutrition, the model shows a striking difference. The 1940s scenario has lower gene expression, reduced growth hormone, and slower bone growth — resulting in a Final Height approximately 8-12 cm shorter. This matches real-world secular trend data and demonstrates that the height increase across generations is environmental, not genetic.")
    ],
    "reflection_exemplars": [
        ("How can identical genes produce different heights?", "Genes don't directly produce traits — they produce PROTEINS, and the rate at which they do so (gene expression) is regulated by environmental signals. When nutrition is abundant, epigenetic markers activate growth genes at full capacity. When nutrition is scarce, those same genes are partially silenced. The DNA sequence is identical, but the epigenetic settings are different. It's like having the same recipe but different amounts of ingredients — the instructions haven't changed, but the result depends on what's available."),
        ("Why is the secular trend evidence against genetic change?", "The secular trend happened over 150 years — about 6 human generations. Genetic evolution through natural selection requires hundreds of generations for significant trait changes. The speed of the height increase rules out genetic change and points to environmental factors. Additional evidence: populations that experienced rapid nutritional improvement (Japan after WWII, South Korea) showed immediate height increases within a single generation. The model confirms that changing only the nutrition input while keeping genes constant reproduces the observed trend.")
    ],
    "stem_intro": "Present the challenge: A school district with 40% food-insecure students needs an evidence-based nutrition program. Your team will design a comprehensive program that addresses the specific nutrients critical for bone growth, provides coverage beyond school hours, and includes measurable outcome tracking. Use your model data to justify every design decision.",
    "stem_concepts": [
        ("Critical Nutrient Windows", "Certain nutrients are most important during specific growth phases. Protein is critical throughout childhood; calcium and vitamin D peak in importance during the adolescent growth spurt; zinc is essential for growth plate function. Deficiency during these windows has disproportionate effects on final height."),
        ("Food Security Interventions", "School meal programs, weekend food backpacks, summer feeding programs, and community food banks address different aspects of food insecurity. The most effective interventions combine direct nutrition with education and address the specific nutrients most likely to be deficient in the target population."),
        ("Growth Monitoring", "Height-for-age percentile tracking is a sensitive indicator of nutritional status. A child who drops from the 50th to the 25th percentile over a year is showing signs of nutritional deficiency even if they appear healthy. Population-level growth curves can evaluate program effectiveness within 2-3 years.")
    ],
    "stem_eval": [
        ("Expert (4)", "Program addresses specific critical nutrients with scientific justification, covers school and non-school hours, includes growth monitoring metrics, and uses model evidence to defend design decisions"),
        ("Proficient (3)", "Program identifies key nutrients and provides reasonable delivery mechanisms with some connection to model evidence"),
        ("Developing (2)", "Program addresses nutrition generally but lacks specific nutrient targeting or evaluation metrics"),
        ("Beginning (1)", "Program is incomplete or doesn't connect nutrition science to growth outcomes")
    ],
    "support": [
        "Provide a table of critical growth nutrients with recommended daily amounts and common food sources",
        "Use a growth chart template showing percentile curves to help students visualize growth trajectories",
        "Sentence frames: 'Our program provides __ mg of __ daily because our model shows that this nutrient affects __ by __'"
    ],
    "extensions": [
        "Research the Dutch famine of 1944-45 and its effects on the height and health of children conceived or born during the famine — how does this support the epigenetic model?",
        "Investigate how growth hormone therapy works and the ethical debates surrounding its use for children who are short but not growth-hormone deficient",
        "Compare height trends in different countries and correlate them with GDP, nutrition data, and healthcare access — what does the global pattern reveal?"
    ],
    "cross_curr": [
        ("Math", "Analyze height distribution data: Calculate mean, standard deviation, and z-scores for height-for-age in two populations with different nutrition levels. How does the entire distribution shift with improved nutrition?"),
        ("ELA", "Write a research-based argument addressing: 'Should school meal programs be funded as a public health investment?' Use evidence from your model about the relationship between nutrition and growth."),
        ("Social Studies", "Research the history of school lunch programs in the US, from their origins in the National School Lunch Act of 1946 to current debates. How has understanding of nutrition science changed policy?")
    ],
    "misconceptions": [
        ("Height is entirely determined by genetics", "While genetics accounts for about 80% of height variation WITHIN a population sharing the same environment, environmental factors — especially childhood nutrition — can shift entire populations by 10+ centimeters. The 80% figure describes variation between individuals in similar conditions, not the total potential range. North and South Koreans share nearly identical genetics but differ by about 8 cm in average height due to nutrition differences.", "Thought experiment: If height were 100% genetic, identical twins raised on different diets would be the same height. They're not — studies show 2-5 cm differences in twins raised in different nutritional environments."),
        ("You can increase your height by eating well as an adult", "Once growth plates close (typically ages 16-18 for girls and 18-21 for boys), no amount of nutrition, exercise, or supplements can increase height. Growth plates fuse permanently, and the window for height increase is gone. This is why childhood and adolescent nutrition is so critically important — the window is limited and cannot be reopened.", "Show X-rays of open vs. fused growth plates. Ask: If the construction zone is permanently closed, can you add more floors to the building? The blueprint (genes) still exists, but the building period is over."),
        ("Modern humans are evolving to be taller", "The height increase over the past 150 years is too fast for genetic evolution, which requires hundreds to thousands of generations. The secular trend is almost entirely environmental — better nutrition, reduced childhood disease, and improved healthcare allow people to reach more of their genetic potential. In fact, there's no evidence that the genetic potential for height has changed at all.", "Evidence: Populations that experienced sudden nutritional improvements (post-war Japan, South Korea) showed immediate height increases in a single generation. Evolution takes hundreds of generations. The speed of change proves the cause is environmental, not genetic.")
    ]
}

L06 = {
    "id": "G10L1-L06",
    "title": "What Happens When Wolves Disappear?",
    "subtitle": "Modeling Trophic Cascades, Population Dynamics, and Ecosystem Stability",
    "ngss": "HS-LS2-1, HS-LS2-2",
    "ngss_desc": "Use mathematical and/or computational representations to support explanations of factors that affect carrying capacity of ecosystems at different scales. Use mathematical representations to support and revise explanations based on evidence about factors affecting biodiversity and populations in ecosystems.",
    "big_question": "When Yellowstone removed wolves, the rivers moved. When wolves returned, the rivers came back. How can one species reshape an entire landscape?",
    "objectives": [
        "Model how the removal or addition of a top predator cascades through multiple trophic levels to affect the entire ecosystem",
        "Explain the relationship between population size, food availability, predator pressure, and habitat area in maintaining ecosystem balance",
        "Predict the consequences of removing a keystone species on biodiversity and ecosystem stability",
        "Analyze how trophic cascades can produce unexpected effects far beyond the food web"
    ],
    "vocabulary": [
        ("Trophic Cascade", "An ecological phenomenon where changes at the top of the food web ripple down through every level — removing a top predator causes prey populations to explode, which overgrazes vegetation, which erodes soil, which changes water flow"),
        ("Keystone Species", "A species whose impact on the ecosystem is disproportionately large compared to its population size — removing a keystone species causes the ecosystem to fundamentally change or collapse"),
        ("Carrying Capacity", "The maximum population size that an environment can sustain indefinitely given available food, water, shelter, and space — exceeding carrying capacity leads to resource depletion and population crash"),
        ("Biodiversity Index", "A measure of the variety of species in an ecosystem — higher biodiversity generally indicates a healthier, more resilient ecosystem with more complex food webs and interactions")
    ],
    "components": [
        ("Population Size", "The number of individuals in the prey species population (elk in the Yellowstone model) — determined by birth rate, death rate, food availability, and predation pressure", False),
        ("Food Availability", "The amount and quality of vegetation available for herbivore consumption — decreases as population size increases and recovers when grazing pressure is reduced", False),
        ("Predator Pressure", "The intensity of hunting by top predators (wolves), which controls prey population through both direct killing and the 'ecology of fear' that changes prey behavior", True),
        ("Habitat Area", "The total area of viable ecosystem supporting the food web — can expand as vegetation recovers or shrink as overgrazing degrades the landscape", False),
        ("Extinction Risk", "The probability that a species in the ecosystem will be locally eliminated, increasing with reduced food, habitat loss, and population fragmentation", False)
    ],
    "think_about_it": "When wolves were removed from Yellowstone, elk populations exploded. But then something unexpected happened — the rivers literally changed course. How can removing a predator change the physical geography of a landscape?",
    "scenarios": [
        ("Wolves Present", "Set Predator Pressure to natural wolf levels — observe how Population Size is controlled, Food Availability remains stable, and Habitat Area is maintained"),
        ("Wolves Removed", "Set Predator Pressure to zero — observe the cascade: elk population explosion → overgrazing → habitat degradation → extinction risk for other species"),
        ("Wolf Reintroduction", "Start from the degraded state and restore Predator Pressure — observe whether and how quickly the ecosystem recovers")
    ],
    "sim_scenarios": [
        ("Wolves Present", "Predator Pressure: Natural wolf population", "What do you predict elk Population Size will be with wolves present, and how does this affect vegetation?"),
        ("Wolves Removed", "Predator Pressure: Zero (wolves eliminated)", "What chain of events do you predict will follow when the top predator is completely removed?"),
        ("Wolf Reintroduction", "Predator Pressure restored after degradation", "How quickly do you predict the ecosystem will recover after wolves are returned? Will it fully recover?")
    ],
    "discoveries": [
        "Removing a top predator doesn't just increase prey numbers — it triggers a cascade that transforms the entire ecosystem, including vegetation, other species, and even physical geography",
        "The 'ecology of fear' may be as important as direct predation — wolves change WHERE elk graze, not just HOW MANY elk there are, allowing vegetation recovery in areas elk now avoid",
        "Ecosystem recovery after predator reintroduction is possible but slow — some changes (soil erosion, species loss) may take decades to reverse and some are irreversible",
        "Trophic cascades demonstrate that ecosystems are not simple food chains but complex interconnected webs where changes at any level produce unpredictable effects throughout"
    ],
    "answer": "When Yellowstone removed wolves in 1926, elk populations soared unchecked. Elk overgrazed willows and aspens along riverbanks, destroying the root systems that held soil in place. Without roots, riverbanks eroded and rivers widened and shifted course. Songbirds lost nesting habitat. Beavers lost their food source and disappeared, eliminating the dams that created ponds for fish, amphibians, and other species. One predator's absence unraveled the entire web. When wolves were reintroduced in 1995, elk moved away from riverbanks (ecology of fear), vegetation recovered, riverbanks stabilized, beavers returned, and biodiversity surged. One species reshaped an entire landscape — twice.",
    "stem_title": "Design a Wildlife Corridor and Reintroduction Plan",
    "stem_mission": "Design a wildlife management plan for reintroducing a keystone predator to a degraded ecosystem, including corridor connections, population targets, and monitoring protocols.",
    "stem_scenario": "A state wildlife agency is considering reintroducing wolves to a region where they were eliminated 80 years ago. The ecosystem has degraded significantly — elk overgraze, riparian habitats are damaged, and biodiversity has declined. However, local ranchers and communities oppose reintroduction. Your team must design a science-based plan that maximizes ecological benefit while addressing human concerns.",
    "stem_questions": [
        "What is the minimum wolf population needed to create a meaningful trophic cascade based on your model?",
        "How will you design wildlife corridors to connect isolated habitat patches?",
        "What monitoring data will you collect to measure whether the reintroduction is working?"
    ],
    "stem_design_qs": [
        "What is the target wolf population and how did your model inform this number?",
        "How will you address conflicts between wolves and livestock operations?",
        "What corridor connections are needed and what minimum width ensures viable wolf movement?",
        "What ecological indicators will you monitor and at what intervals to assess cascade effects?"
    ],
    "career": "Wildlife Ecologists study the interactions between species and their environments, managing ecosystems and designing conservation strategies. They work for federal and state wildlife agencies, conservation organizations, and research institutions, earning $50,000–$95,000/year. Conservation Biologists who specialize in endangered species earn $55,000–$100,000/year.",
    "images": {
        "cover": ("G10L1-L06-cover.png", "A photorealistic, cinematic image of a wolf pack in Yellowstone National Park with mountains in the background, dramatic golden hour lighting, elk visible in the distance, lush green valley with a winding river"),
        "landscape": ("G10L1-L06-landscape.png", "A diverse group of 15-16 year old students in a modern biology lab examining ecosystem models and food web diagrams, animal population data charts on screens, engaged expressions"),
        "modeling": ("G10L1-L06-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of predator-prey population dynamics, classroom with wildlife posters and ecosystem diagrams"),
        "discussion": ("G10L1-L06-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about trophic cascades, before-and-after Yellowstone photos displayed on a smartboard, students actively debating"),
        "stem": ("G10L1-L06-stem.png", "Diverse 15-16 year old students designing wildlife management plans on large maps with colored zones, population graphs, and corridor designs, collaborative conservation planning atmosphere")
    },
    "pre_assessment": [
        "What do you think would happen to an ecosystem if its top predator was completely removed?",
        "How can one species affect an entire landscape — including rivers and soil?",
        "Draw a food web showing at least four trophic levels and predict what happens if you remove the top level.",
        "What does 'balance of nature' mean, and do ecosystems naturally maintain balance without human interference?"
    ],
    "extend_components": [
        ("Behavioral Response", "Changes in prey behavior (where they graze, how long they stay in one area) caused by the presence or fear of predators — the 'ecology of fear' that may be more important than direct killing"),
        ("Riparian Vegetation", "Trees, shrubs, and grasses growing along riverbanks that depend on grazing pressure remaining below critical levels — willows and aspens are keystone species in Yellowstone's riparian zones"),
        ("Species Diversity Count", "The total number of species present in the ecosystem, which typically increases when trophic cascades maintain habitat diversity and decreases when overgrazing homogenizes the landscape")
    ],
    "reflections": [
        "How does your model demonstrate that ecosystems are complex interconnected systems rather than simple food chains?",
        "Why might the 'ecology of fear' be as important as direct predation in maintaining ecosystem balance?",
        "What does the Yellowstone case reveal about the unintended consequences of wildlife management decisions?",
        "How does your model help explain why removing one species can cause rivers to change course?",
        "What are the limitations of modeling a complex ecosystem with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Using Mathematics and Computational Thinking", "Students use computational models to represent factors affecting carrying capacity and predict population dynamics across multiple trophic levels."),
        ("Disciplinary Core Idea", "LS2.A Interdependent Relationships in Ecosystems / LS2.C Ecosystem Dynamics, Functioning, and Resilience", "Ecosystems have carrying capacities that depend on biotic and abiotic factors. Trophic cascades demonstrate how interdependent relationships maintain or disrupt ecosystem functioning."),
        ("Crosscutting Concept", "Stability and Change", "Students analyze how the removal or addition of a keystone species pushes ecosystems between stable states and investigate the conditions required for ecosystem recovery.")
    ],
    "cast_items": [
        "Model how removal of a keystone predator cascades through multiple trophic levels to transform an ecosystem",
        "Use computational representations to predict population dynamics under different predator pressure scenarios",
        "Analyze the conditions required for ecosystem recovery after trophic cascade degradation"
    ],
    "cast_questions": [
        ("Multiple Choice:", "After wolves were removed from Yellowstone, elk populations increased by 300%. According to the trophic cascade model, which of the following would be the most likely SECOND-ORDER effect?"),
        ("Constructed Response:", "Using your model, explain the complete trophic cascade that occurred when wolves were removed from Yellowstone. Trace the effects from predator removal through prey population increase, vegetation change, erosion, and river course alteration. Include at least three trophic levels in your explanation.")
    ],
    "background_intro": "In 1995, one of the most famous experiments in ecological history began: wolves were reintroduced to Yellowstone National Park after a 70-year absence. What happened next stunned scientists — the wolves didn't just control elk populations, they transformed the entire landscape. Rivers moved. Forests regrew. Species that had vanished returned. This is the power of a trophic cascade: a change at the top of the food web that ripples through every level, reshaping the physical geography of the land itself.",
    "background_sections": [
        ("The Yellowstone Experiment", "Wolves were eliminated from Yellowstone by 1926 as part of federal predator control programs. Without wolves, elk populations grew unchecked from about 5,000 to over 20,000. The elk overgrazed willows, aspens, and cottonwoods — especially along rivers where they felt safe without predators. By the 1990s, riparian vegetation was devastated, riverbanks were eroding, and biodiversity had plummeted. In 1995, 31 wolves were reintroduced from Canada."),
        ("The Trophic Cascade", "Within years of wolf reintroduction, elk began avoiding areas where they were vulnerable to wolf predation — especially river valleys and narrow gorges. This 'ecology of fear' allowed willows and aspens to regrow in these areas for the first time in decades. Vegetation recovery stabilized riverbanks, reducing erosion. Beavers returned (willows are their primary food), building dams that created ponds for fish, amphibians, and waterfowl. Songbird populations increased with the return of nesting habitat."),
        ("Carrying Capacity and Population Dynamics", "Carrying capacity (K) is not fixed — it changes as the ecosystem changes. When wolves were absent, elk exceeded the vegetation carrying capacity, degraded the habitat, and lowered the carrying capacity further — a destructive feedback loop. Wolf reintroduction broke this loop by reducing elk numbers below the vegetation recovery threshold, which restored habitat, which increased carrying capacity for dozens of other species."),
        ("Keystone Species and Biodiversity", "A keystone species has an effect on its ecosystem disproportionate to its population size. Wolves comprise a tiny fraction of Yellowstone's biomass but their presence or absence determines the structure of the entire ecosystem. Similarly, sea otters control sea urchin populations that would otherwise destroy kelp forests; starfish control mussel populations on rocky shores. Removing a keystone species doesn't just reduce biodiversity — it fundamentally reorganizes the ecosystem into a different, often degraded state.")
    ],
    "lever_L": "Students identify population size, food availability, predator pressure, habitat area, and extinction risk as the key components of the ecosystem dynamics model.",
    "lever_E": "Students determine that predator pressure controls population size, which determines food availability, which affects habitat area, and that the cascade from top predator to physical landscape demonstrates interconnected trophic levels.",
    "lever_V": "Students build a computational model showing how changes in predator pressure cascade through prey populations, vegetation, habitat quality, and biodiversity.",
    "lever_Ev": "Students run wolves-present, wolves-removed, and wolf-reintroduction scenarios to observe trophic cascades and test whether degraded ecosystems can recover.",
    "lever_R": "Students add behavioral response, riparian vegetation, or species diversity count to model more complete ecosystem dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with Yellowstone wolves image", "say": "When wolves disappeared from Yellowstone, the rivers literally moved. When wolves came back, the rivers returned. How is that possible?", "do": "Show the famous 'How Wolves Changed Rivers' comparison photos. Let students try to explain the connection.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're modeling something that might be the most surprising discovery in ecology — how one species can reshape an entire landscape.", "do": "Have students read objectives. Pre-teach 'trophic cascade' and 'keystone species' with visual food web.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How can removing one species change rivers?", "say": "Wolves eat elk. But somehow, removing wolves changed rivers, forests, songbirds, fish, and even soil erosion. What's the connection?", "do": "Students attempt to draw the connection from wolves to rivers. Most will struggle — that's the point.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building a model of an entire ecosystem to see how changes at the top cascade all the way to the bottom.", "do": "Preview LEVER steps. Emphasize this is about SYSTEMS thinking — everything is connected.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for ecosystem model", "say": "What are the key players in this ecosystem? Which ones can wildlife managers actually control?", "do": "Guide sorting. Predator pressure is the primary external lever. Discuss how everything else responds to it.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows through trophic levels", "say": "Follow the cascade: No wolves means more elk. More elk means less vegetation. Less vegetation means... what?", "do": "Build the full cascade chain step by step. Students add each link and predict the next.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Population and habitat graphs over time", "say": "Let's remove the wolves and watch what happens over 70 years. Then bring them back and see if we can undo the damage.", "do": "Run wolves-removed scenario first. Then run reintroduction. Compare timescales of degradation vs. recovery.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings — before and after comparison", "say": "It took 70 years without wolves to degrade Yellowstone. It took only 20 years with wolves to start recovery. What does that tell us?", "do": "Discuss asymmetry: degradation is faster than recovery. Some damage may be irreversible. Connect to conservation urgency.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Wildlife reintroduction planning challenge", "say": "A state agency wants to bring wolves back to a region where they've been gone for 80 years. Ranchers are furious. Ecologists say it's essential. Design the plan.", "do": "Groups create reintroduction plans balancing ecology, human concerns, corridors, and monitoring. Present and debate.", "time": "12 min"}
    ],
    "sort_reasoning": "Predator Pressure is the external component because it can be directly managed through wildlife management decisions — adding or removing wolves, setting hunting quotas, or establishing protected areas. Population Size, Food Availability, Habitat Area, and Extinction Risk are internal because they are ecosystem outcomes that emerge from the complex interactions between species and their environment — they cannot be directly set by managers but respond to predator pressure and each other.",
    "relationships": [
        ("Predator Pressure to Population Size", "NEGATIVE (-)", "Higher predator pressure reduces prey population through direct predation and the ecology of fear (behavioral changes that reduce reproduction and survival). Wolf presence keeps elk numbers well below the vegetation carrying capacity."),
        ("Population Size to Food Availability", "NEGATIVE (-)", "Larger prey populations consume more vegetation, reducing food availability for all herbivores. When elk populations exceed carrying capacity, they overgraze to the point where vegetation cannot recover."),
        ("Food Availability to Habitat Area", "POSITIVE (+)", "Greater food availability means healthier, more abundant vegetation, which provides habitat for many species. Riparian vegetation stabilizes riverbanks, creates nesting sites, and supports the entire food web. When vegetation is destroyed by overgrazing, habitat area shrinks for all dependent species.")
    ],
    "sim_answers": [
        ("Wolves Removed Scenario", "When Predator Pressure drops to zero, the model shows elk Population Size rapidly increasing toward and beyond vegetation carrying capacity. Food Availability plummets as elk overgraze willows, aspens, and grasses. Habitat Area shrinks as vegetation loss leads to soil erosion and riverbank collapse. Extinction Risk rises sharply for riparian species (beavers, songbirds, amphibians) that depend on the vegetation wolves indirectly protected. The cascade transforms a diverse ecosystem into a degraded one."),
        ("Wolf Reintroduction Scenario", "When Predator Pressure is restored, Population Size decreases through predation and behavioral changes. Elk begin avoiding river valleys (ecology of fear), allowing Food Availability to recover in these zones. As vegetation returns, Habitat Area gradually expands and Extinction Risk decreases. However, the recovery is slower than the degradation — some soil erosion is irreversible, and species that were lost may take decades to return. The model shows that prevention is far easier than restoration.")
    ],
    "reflection_exemplars": [
        ("How can wolves change rivers?", "The cascade is: Wolves eat elk and scare them away from river valleys → Elk stop overgrazing willows and aspens along rivers → Vegetation regrows, and root systems stabilize riverbanks → Banks stop eroding and rivers narrow back to natural channels → Beavers return (willows = food) and build dams → Dams create pools that slow water flow further. Every link in the chain is necessary. Remove any one, and the cascade breaks. This demonstrates that ecosystems are interconnected systems, not isolated components."),
        ("Why is degradation faster than recovery?", "Degradation is fast because it involves destruction — overgrazing kills plants quickly, erosion removes soil rapidly, and species can be locally eliminated in years. Recovery is slow because it requires rebuilding — vegetation must regrow from seeds or roots, soil must accumulate, and species must recolonize from distant populations. Some changes are effectively irreversible on human timescales: eroded soil may take centuries to rebuild, and locally extinct species may never return if source populations are too distant. The model shows a fundamental asymmetry in ecosystem dynamics.")
    ],
    "stem_intro": "Present the challenge: A state wildlife agency is debating wolf reintroduction in a region where wolves have been absent for 80 years. Your team must design a plan that uses model evidence to justify ecological goals, addresses rancher and community concerns, includes wildlife corridor design, and specifies monitoring protocols for measuring cascade effects.",
    "stem_concepts": [
        ("Wildlife Corridors", "Connected strips of habitat that allow animals to move between isolated habitat patches. Effective corridors must be wide enough for the target species (wolves need corridors at least 1 km wide), contain suitable habitat, and minimize road crossings and human contact zones."),
        ("Coexistence Strategies", "Methods for reducing conflict between predators and human communities: livestock guardian animals, range riders, fladry (flag barriers), compensation programs for livestock losses, and non-lethal deterrents. Successful reintroduction programs address human concerns proactively."),
        ("Indicator Species Monitoring", "Tracking specific species that serve as indicators of ecosystem health. In a wolf reintroduction, monitoring riparian vegetation cover, beaver dam counts, songbird species diversity, and elk browsing patterns can reveal whether the trophic cascade is functioning.")
    ],
    "stem_eval": [
        ("Expert (4)", "Plan specifies science-based population targets, includes corridor design with dimensions, addresses human-wildlife conflict with specific strategies, and uses model evidence to justify monitoring protocols"),
        ("Proficient (3)", "Plan addresses wolf reintroduction with reasonable population targets and corridor concepts, with some reference to model evidence"),
        ("Developing (2)", "Plan identifies reintroduction need but lacks specific targets, corridor design, or conflict management strategies"),
        ("Beginning (1)", "Plan is incomplete or doesn't connect predator reintroduction to ecosystem cascade effects")
    ],
    "support": [
        "Provide a trophic cascade diagram showing the chain from wolves through elk through vegetation to rivers",
        "Use a before/after photo comparison of Yellowstone riparian zones pre- and post-wolf reintroduction",
        "Sentence frames: 'Our model shows that __ wolves will reduce elk population to __, which will allow vegetation to recover because __'"
    ],
    "extensions": [
        "Research the trophic cascade caused by sea otter decline in Pacific kelp forests — how does it mirror the Yellowstone wolf story?",
        "Investigate the rewilding movement in Europe — what keystone species are being reintroduced and what cascade effects are expected?",
        "Calculate the economic value of the Yellowstone trophic cascade — wolves generate over $35 million in annual tourism. Compare this to livestock losses."
    ],
    "cross_curr": [
        ("Math", "Model elk population growth using the logistic growth equation: dN/dt = rN(1-N/K). Calculate the population trajectory with and without wolf predation pressure. Graph the difference."),
        ("ELA", "Write a multi-perspective essay about wolf reintroduction: present the ecologist's argument (ecosystem health), the rancher's concern (livestock losses), and the tourist economy argument. Synthesize a position using evidence."),
        ("Social Studies", "Research how Indigenous peoples in North America understood and managed predator-prey relationships for thousands of years. Compare traditional ecological knowledge with modern conservation biology.")
    ],
    "misconceptions": [
        ("Removing one species can't affect the whole ecosystem", "Trophic cascades demonstrate that a single keystone species can determine the structure of an entire ecosystem. Removing wolves from Yellowstone changed elk populations, vegetation, river courses, beaver populations, songbird habitat, and soil stability. The cascade model shows that ecosystems are tightly interconnected — a change at any level propagates throughout the system.", "Show the Yellowstone cascade chain: wolves → elk → willows → riverbanks → rivers → beavers → ponds → fish → songbirds. Removing one link changes everything downstream."),
        ("Nature will balance itself without predators", "Without top predators, herbivore populations do NOT self-regulate at a sustainable level. Instead, they boom until they exceed carrying capacity, overgraze their food supply, crash, then repeat in destructive boom-bust cycles. This oscillation prevents vegetation recovery and can permanently degrade the ecosystem. Predators provide a continuous, stabilizing control that prey species cannot provide for themselves.", "Graph the boom-bust cycle: Population overshoots carrying capacity → overgrazing → food collapse → population crash → partial recovery → overshoot again. Compare to the stable population with predator regulation."),
        ("Predators are bad for ecosystems because they kill animals", "Predators are essential for ecosystem health precisely BECAUSE they kill animals. By keeping herbivore populations below carrying capacity, predators prevent overgrazing, maintain vegetation diversity, and support dozens of other species that depend on healthy habitats. The 'ecology of fear' also distributes grazing pressure more evenly across the landscape. Ecosystems without predators consistently show lower biodiversity and more degraded habitats.", "Compare two real ecosystems: Yellowstone WITH wolves (high biodiversity, healthy vegetation, stable rivers) vs. Yellowstone WITHOUT wolves (overgrazing, erosion, species decline). Which is healthier? The one with active predation.")
    ]
}

L07 = {
    "id": "G10L1-L07",
    "title": "Why Can't Weather Apps Get It Right?",
    "subtitle": "Modeling Atmospheric Systems, Chaos Theory, and the Limits of Prediction",
    "ngss": "HS-ESS2-5, HS-ESS2-3",
    "ngss_desc": "Plan and conduct an investigation of the properties of water and its effects on Earth materials and surface processes. Develop a model based on evidence of Earth's interior to describe the cycling of matter by thermal convection.",
    "big_question": "If we have supercomputers, satellites, and thousands of weather stations, why is a 10-day forecast still barely better than a coin flip?",
    "objectives": [
        "Model how solar radiation, temperature, moisture, and wind interact to produce weather patterns",
        "Explain why small differences in initial conditions can produce dramatically different weather outcomes (chaos theory)",
        "Predict storm probability based on the interaction of atmospheric variables",
        "Analyze the fundamental limits of weather prediction and why forecast accuracy decreases with time"
    ],
    "vocabulary": [
        ("Atmospheric Convection", "The vertical movement of air caused by differential heating — warm air rises, expands, and cools; cool air sinks, compresses, and warms. This cycling drives weather patterns from local thunderstorms to global circulation cells"),
        ("Sensitive Dependence", "The mathematical property of chaotic systems where tiny differences in starting conditions lead to vastly different outcomes over time — popularly called the 'butterfly effect' in weather forecasting"),
        ("Relative Humidity", "The amount of water vapor in the air expressed as a percentage of the maximum the air could hold at that temperature — warm air can hold more moisture, so cooling air causes humidity to rise toward saturation and precipitation"),
        ("Atmospheric Instability", "A condition where warm, moist air near the surface is overlain by cooler, drier air above — this temperature structure promotes rapid vertical convection and can trigger thunderstorms")
    ],
    "components": [
        ("Solar Radiation Input", "The amount of solar energy reaching the surface, which varies by latitude, season, time of day, and cloud cover — the primary energy source driving all atmospheric motion", True),
        ("Air Temperature", "The temperature of the air mass, determined by solar heating, latitude, elevation, and nearby land/ocean surfaces — temperature differences between air masses are the engine of weather", False),
        ("Moisture Content", "The amount of water vapor in the air, supplied by evaporation from oceans, lakes, and vegetation — determines precipitation potential and releases latent heat when it condenses", False),
        ("Wind Speed", "The velocity of air movement, driven by pressure differences created by differential heating — carries heat and moisture horizontally and determines storm movement and intensity", False),
        ("Storm Probability", "The likelihood of significant weather events (thunderstorms, rain, severe weather) based on the interaction of temperature, moisture, instability, and forcing mechanisms", False)
    ],
    "think_about_it": "If you change the Solar Radiation Input by just 1% in one location, the resulting temperature change alters wind patterns, which shifts moisture, which changes where storms form. How does this tiny initial difference grow into a completely different forecast?",
    "scenarios": [
        ("Sunny and Stable", "Set Solar Radiation Input to moderate with dry air — observe how stable, fair-weather conditions develop with low Storm Probability"),
        ("Approaching Front", "Increase Moisture Content significantly while maintaining strong Solar Radiation — observe how the combination drives instability and Storm Probability spikes"),
        ("Butterfly Effect Test", "Run the same scenario twice with Solar Radiation differing by just 0.1% — observe how the forecasts diverge dramatically after several simulated days")
    ],
    "sim_scenarios": [
        ("Sunny and Stable", "Solar Radiation: Moderate | Air: Dry and stable", "What do you predict Storm Probability will be under clear, stable conditions?"),
        ("Approaching Front", "Solar Radiation: Strong | Moisture: High and rising", "When warm, moist air meets strong solar heating, what do you predict happens to Storm Probability?"),
        ("Butterfly Effect", "Two runs with 0.1% difference in Solar Radiation", "How different do you predict the weather forecasts will be after 3, 7, and 14 simulated days?")
    ],
    "discoveries": [
        "Weather is driven by energy transfers — solar radiation heats the surface unevenly, creating temperature differences that drive wind, which carries moisture, which produces precipitation",
        "The atmosphere is a chaotic system — tiny measurement errors in initial conditions amplify over time, making long-range forecasts fundamentally unreliable beyond about 10-14 days",
        "Storm formation requires the simultaneous interaction of multiple factors: instability, moisture, lifting mechanism, and wind shear — missing any one ingredient dramatically reduces storm probability",
        "Weather prediction accuracy decreases predictably: 1-day forecasts are about 95% accurate, 5-day about 80%, 10-day about 50%, and beyond 14 days, forecasts provide little useful information"
    ],
    "answer": "Weather apps struggle with accuracy because the atmosphere is a chaotic system — mathematically, this means tiny measurement errors in today's conditions grow exponentially over time until the forecast becomes meaningless. Even with millions of data points from satellites, weather balloons, and ground stations, we can't measure EVERYTHING with perfect precision. A temperature measurement off by 0.01°C in one location can cascade through the atmospheric equations and produce a completely different forecast a week later. This isn't a technology problem — it's a fundamental mathematical limit discovered by Edward Lorenz in 1961. We'll never have a perfectly accurate 14-day forecast, no matter how powerful our computers become.",
    "stem_title": "Design a Severe Weather Alert System",
    "stem_mission": "Design a localized severe weather monitoring and alert system that maximizes warning time for thunderstorms and tornadoes while minimizing false alarms.",
    "stem_scenario": "A school district in an area prone to severe thunderstorms and occasional tornadoes needs a better warning system than just watching the news. The current system provides only 13 minutes of average tornado warning time, and false alarms have trained people to ignore alerts. Your team must design a monitoring system that provides earlier, more accurate warnings for the school and surrounding community.",
    "stem_questions": [
        "What atmospheric variables does your system monitor and what thresholds trigger alerts?",
        "How will you balance early warnings (more lead time) against false alarm rates (crying wolf)?",
        "What data sources will you combine for the most accurate short-term predictions?"
    ],
    "stem_design_qs": [
        "What sensors and data sources will your system use and where will they be placed?",
        "How will you define alert thresholds that maximize warning time without triggering too many false alarms?",
        "What communication channels will you use to reach students, staff, and the community quickly?",
        "How will you test and validate your system before relying on it for safety?"
    ],
    "career": "Meteorologists study atmospheric science and forecast weather using computational models, satellite data, and field observations. They work for the National Weather Service, media organizations, private weather companies, and aviation, earning $55,000–$120,000/year. Atmospheric Scientists who research climate modeling and chaos theory earn $70,000–$140,000/year.",
    "images": {
        "cover": ("G10L1-L07-cover.png", "A photorealistic, cinematic image of a dramatic thunderstorm forming over a landscape, dark cumulonimbus clouds with visible lightning, rain curtain in the distance, dramatic lighting with sun still visible on the horizon"),
        "landscape": ("G10L1-L07-landscape.png", "A diverse group of 15-16 year old students in a modern earth science lab examining weather station instruments — barometer, anemometer, hygrometer — with weather maps on screens, engaged expressions"),
        "modeling": ("G10L1-L07-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational weather models, screens showing atmospheric data, radar imagery, and forecast maps, modern classroom"),
        "discussion": ("G10L1-L07-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about weather prediction challenges, a butterfly effect diagram and weather model comparison displayed on a smartboard"),
        "stem": ("G10L1-L07-stem.png", "Diverse 15-16 year old students designing severe weather alert systems with sensor diagrams, communication flow charts, and alert threshold tables on whiteboards, collaborative engineering atmosphere")
    },
    "pre_assessment": [
        "Why do you think weather forecasts become less accurate for days further in the future?",
        "What information do you think meteorologists use to predict tomorrow's weather?",
        "Draw a diagram showing how you think a thunderstorm forms — what ingredients are needed?",
        "Have you ever heard of the 'butterfly effect'? What do you think it means for weather prediction?"
    ],
    "extend_components": [
        ("Pressure Gradient", "The difference in atmospheric pressure between two locations, which directly drives wind speed and direction — steeper gradients produce stronger winds and more dynamic weather"),
        ("Wind Shear", "The change in wind speed or direction with altitude, which is critical for severe weather development — strong wind shear helps organize thunderstorms into supercells capable of producing tornadoes"),
        ("Land-Ocean Contrast", "The difference in heating rate between land and water surfaces, which creates sea breezes, monsoons, and coastal weather patterns that complicate forecasting")
    ],
    "reflections": [
        "How does your model demonstrate that weather is a chaotic system where small changes produce large effects?",
        "Why does the butterfly effect set a fundamental limit on forecast accuracy that better technology cannot overcome?",
        "What does the model reveal about why severe weather forecasting is harder than fair-weather forecasting?",
        "How could understanding chaos theory help people make better decisions about weather-dependent activities?",
        "What are the limitations of modeling the atmosphere with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Planning and Carrying Out Investigations", "Students plan investigations to test how varying initial conditions in their atmospheric model affect forecast outcomes, demonstrating sensitive dependence."),
        ("Disciplinary Core Idea", "ESS2.D Weather and Climate", "The foundation for Earth's global climate system is the electromagnetic radiation from the sun and its interaction with Earth's surface and atmosphere. Weather results from complex interactions among atmospheric variables driven by solar energy."),
        ("Crosscutting Concept", "Cause and Effect", "Students investigate how small causes (tiny measurement errors) can produce large, unpredictable effects in complex systems, distinguishing deterministic chaos from randomness.")
    ],
    "cast_items": [
        "Model how atmospheric variables interact to produce weather patterns and storm formation",
        "Demonstrate the butterfly effect by comparing forecasts from slightly different initial conditions",
        "Analyze why weather forecast accuracy decreases predictably with forecast lead time"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A meteorologist runs two computer forecasts with initial temperatures differing by only 0.01°C. The 3-day forecasts are nearly identical, but the 10-day forecasts predict completely different weather. This is best explained by:"),
        ("Constructed Response:", "Using your model, explain why it is mathematically impossible to produce an accurate 30-day weather forecast even with perfect technology. Include the concepts of sensitive dependence, measurement uncertainty, and chaotic systems in your explanation.")
    ],
    "background_intro": "In 1961, meteorologist Edward Lorenz accidentally discovered one of the most profound principles in science. While running a weather simulation, he rounded an initial value from 0.506127 to 0.506 — a difference of less than 0.02%. The resulting forecast was completely different. This discovery — sensitive dependence on initial conditions — revealed that the atmosphere is a chaotic system with a fundamental prediction limit that no technology can ever overcome.",
    "background_sections": [
        ("How Weather Works", "All weather is driven by differential solar heating. The equator receives more solar energy per square meter than the poles, creating temperature gradients that drive atmospheric circulation. Warm air rises (convection), creating low pressure at the surface. Cool air sinks, creating high pressure. Air flows from high to low pressure (wind), carrying moisture evaporated from oceans. When moist air rises and cools, water vapor condenses into clouds and precipitation. This cycle — heating, convection, moisture transport, condensation — produces all weather."),
        ("Chaos Theory and Weather", "Chaotic systems are deterministic (governed by fixed physical laws) but unpredictable beyond a certain time horizon because they exhibit sensitive dependence on initial conditions. In the atmosphere, this means that two nearly identical starting states will diverge exponentially over time. The 'Lyapunov time' for the atmosphere — how long before small errors double — is approximately 2-3 days. After 5 doublings (~10-15 days), initial measurement errors have grown to the size of the weather features themselves, making the forecast meaningless."),
        ("Modern Weather Forecasting", "Today's forecasts use numerical weather prediction (NWP): supercomputers solve the Navier-Stokes equations and thermodynamic equations on a 3D grid covering the globe. Models divide the atmosphere into millions of cells, each about 3-10 km across and hundreds of meters tall. Every cell's temperature, pressure, humidity, and wind are updated every few minutes. To address chaos, forecasters run 'ensemble models' — 20-50 slightly different versions of the same forecast — and analyze how much they diverge to estimate confidence."),
        ("Forecast Accuracy by Lead Time", "Modern 1-day forecasts are about 95% accurate — essentially as good as they can get. 3-day forecasts are about 90% accurate, comparable to what 1-day forecasts were in the 1980s. 5-day forecasts are about 80% accurate, rivaling 3-day forecasts from 20 years ago. Beyond 10 days, accuracy drops below 60%. Beyond 14 days, forecasts provide only marginal improvement over using historical climate averages. The theoretical maximum useful forecast for the atmosphere is approximately 2-3 weeks.")
    ],
    "lever_L": "Students identify solar radiation input, air temperature, moisture content, wind speed, and storm probability as the key components of the atmospheric weather system.",
    "lever_E": "Students determine that solar radiation drives temperature, temperature differences drive wind, wind transports moisture, and the interaction of all four factors determines storm probability.",
    "lever_V": "Students build a computational model showing how atmospheric variables interact to produce weather patterns and how tiny changes in initial conditions cascade into different forecasts.",
    "lever_Ev": "Students run stable weather, approaching front, and butterfly effect scenarios to discover the limits of predictability in chaotic atmospheric systems.",
    "lever_R": "Students add pressure gradient, wind shear, or land-ocean contrast to model more realistic atmospheric dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic storm imagery", "say": "Your weather app says 70% chance of rain on Saturday. Saturday comes — it's sunny. Why? The answer involves one of the deepest discoveries in mathematics.", "do": "Quick poll: How far into the future do you trust a weather forecast? 1 day? 3 days? 7 days? Record responses.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're discovering WHY weather is so hard to predict — and it's not because meteorologists are bad at their jobs.", "do": "Have students read objectives. Pre-teach 'atmospheric convection' and 'sensitive dependence' with visual demonstrations.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Supercomputers vs. 10-day forecasts — why can't we win?", "say": "We have satellites watching every inch of the planet and supercomputers doing quadrillions of calculations per second. So why can't we get a 14-day forecast right?", "do": "Students hypothesize: Is it bad technology? Not enough data? Or something more fundamental?", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building a model of the atmosphere and then deliberately breaking it to discover the limits of predictability.", "do": "Preview LEVER steps. Emphasize that we're testing the LIMITS of the model, not just how it works.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for atmospheric model", "say": "What factors drive weather? Which one is the ultimate energy source for ALL atmospheric motion?", "do": "Guide sorting. Solar radiation is the only external input — everything else responds to it. Discuss why.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Relationship arrows between atmospheric variables", "say": "The sun heats the surface unevenly. That creates temperature differences. Temperature differences create wind. Wind carries moisture. Moisture creates storms. It's all connected.", "do": "Build the energy cascade from solar input to storms. Emphasize that every variable affects every other.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Diverging forecast comparison graphs", "say": "Now the fun part — let's change ONE number by 0.1% and see what happens to the 10-day forecast.", "do": "Students predict whether 0.1% matters. Run twin simulations. Watch the forecasts diverge. This is the butterfly effect.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Forecast accuracy decay curve", "say": "Edward Lorenz discovered this in 1961 by accident. He rounded a number from 0.506127 to 0.506, and the entire weather forecast changed. That 0.02% difference rewrote the future.", "do": "Show the accuracy decay curve: 95% at 1 day, 80% at 5 days, 50% at 10 days. Discuss the theoretical 2-3 week limit.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Severe weather alert system design", "say": "If you can't predict far ahead, you need to detect FAST. Design a system that gives your school maximum warning time for severe storms.", "do": "Groups design alert systems specifying sensors, thresholds, communication channels, and false alarm mitigation.", "time": "12 min"}
    ],
    "sort_reasoning": "Solar Radiation Input is the external component because it is the energy source that drives all atmospheric processes and varies based on astronomical and geographic factors independent of the atmosphere itself. Air Temperature, Moisture Content, Wind Speed, and Storm Probability are internal because they are atmospheric responses that emerge from the complex interactions driven by solar energy — they cannot be independently controlled but are determined by the physics of the atmospheric system.",
    "relationships": [
        ("Solar Radiation Input to Air Temperature", "POSITIVE (+)", "More solar radiation heats the surface and the air in contact with it. Differential heating by latitude, land/ocean, and cloud cover creates the temperature gradients that drive all atmospheric motion."),
        ("Air Temperature to Wind Speed", "POSITIVE (+)", "Greater temperature differences between air masses create steeper pressure gradients, which drive stronger winds. Temperature is the engine; wind is the motion. Without temperature differences, there would be no wind."),
        ("Moisture Content to Storm Probability", "POSITIVE (+)", "Higher moisture content provides more raw material for precipitation and more latent heat release during condensation. When moist air rises and cools, water vapor condenses, releasing energy that fuels thunderstorm updrafts, creating a positive feedback loop that intensifies storms.")
    ],
    "sim_answers": [
        ("Approaching Front Scenario", "When Moisture Content is high and Solar Radiation Input is strong, the model shows air temperature rising significantly, creating instability. Warm, moist air at the surface is overlain by cooler air aloft, promoting rapid convection. Wind speed increases as pressure gradients steepen. Storm Probability rises sharply as all ingredients for severe weather converge: instability, moisture, and lift. The model produces thunderstorm development within hours."),
        ("Butterfly Effect Scenario", "Two simulations run with Solar Radiation Input differing by just 0.1% produce nearly identical forecasts for the first 2-3 simulated days. By day 5, the forecasts begin to noticeably diverge — one predicts rain where the other predicts sun. By day 10, the forecasts are essentially unrelated — predicting different temperatures, wind patterns, and storm locations. This demonstrates that deterministic chaos makes long-range weather prediction fundamentally limited regardless of computational power.")
    ],
    "reflection_exemplars": [
        ("Why can't better technology solve this?", "The butterfly effect isn't a technology problem — it's a mathematical property of the atmospheric equations themselves. Even with perfect sensors measuring every molecule of air, the equations are chaotic: they amplify infinitesimally small differences exponentially over time. To produce a perfect 14-day forecast, you would need to measure the position and velocity of every molecule in the atmosphere with perfect precision — which is physically impossible (and forbidden by quantum mechanics at the smallest scales). Better computers improve short-range forecasts but cannot extend the fundamental predictability horizon."),
        ("How is chaos different from randomness?", "Chaotic systems are deterministic — they follow exact physical laws and the same initial conditions always produce the same result. They're not random. The problem is that infinitely small differences in initial conditions produce different results, and we can never measure initial conditions with infinite precision. Weather is governed by the Navier-Stokes equations — precise, deterministic physics — but the solutions to those equations diverge exponentially from nearby starting points. Randomness means no rules; chaos means rules that are exquisitely sensitive.")
    ],
    "stem_intro": "Present the challenge: A school district needs a severe weather alert system that provides maximum warning time for thunderstorms and tornadoes while avoiding the false alarm fatigue that makes people ignore alerts. Your team will design the monitoring sensors, alert thresholds, communication channels, and validation protocols.",
    "stem_concepts": [
        ("Nowcasting", "Very short-term forecasting (0-6 hours) that uses real-time observations — radar, satellite, lightning detection — rather than model predictions. Nowcasting is much more accurate than longer-range forecasting because it detects weather that has already formed rather than predicting weather that hasn't."),
        ("Ensemble Forecasting", "Running 20-50 slightly different versions of the same weather model to see how much the forecasts diverge. When all ensemble members agree, confidence is high. When they spread widely, uncertainty is high. This converts the chaos problem into a probability estimate."),
        ("False Alarm Mitigation", "When false alarm rates are too high, people stop responding to real alerts (the 'cry wolf' effect). The National Weather Service aims for a tornado warning false alarm rate of 70% — meaning 7 out of 10 tornado warnings are false alarms. Reducing this rate while maintaining detection capability is a critical engineering challenge.")
    ],
    "stem_eval": [
        ("Expert (4)", "System combines multiple data sources, specifies evidence-based alert thresholds, addresses false alarm rates with quantitative targets, includes communication redundancy, and uses model evidence to justify design decisions"),
        ("Proficient (3)", "System identifies appropriate data sources and alert thresholds with reasonable false alarm consideration"),
        ("Developing (2)", "System identifies some monitoring needs but lacks specific thresholds or false alarm management"),
        ("Beginning (1)", "System is incomplete or doesn't connect atmospheric science to alert system design")
    ],
    "support": [
        "Provide a severe weather ingredients checklist showing the atmospheric conditions that must combine for thunderstorm and tornado development",
        "Use a forecast accuracy chart showing how accuracy decreases with lead time as a reference for system design decisions",
        "Sentence frames: 'Our system triggers a __ alert when __ exceeds __ because our model shows this combination produces storms __% of the time'"
    ],
    "extensions": [
        "Research Edward Lorenz's original 1963 paper on deterministic chaos — how did a weather simulation error lead to one of the most important discoveries in mathematics?",
        "Investigate how artificial intelligence is being used to improve weather prediction — can machine learning extend the forecast horizon beyond the chaos theory limit?",
        "Compare weather prediction to earthquake prediction — why can we forecast weather 5 days out but not earthquakes 5 minutes out?"
    ],
    "cross_curr": [
        ("Math", "Explore exponential growth of errors: If measurement error doubles every 2.5 days and starts at 0.01°C, calculate the error after 5, 10, and 15 days. At what point does the error exceed the size of the weather feature being predicted?"),
        ("ELA", "Write a public communication piece explaining why weather forecasts are probabilistic, not certain. Target an audience that gets frustrated when forecasts are 'wrong' and help them understand what a '70% chance of rain' actually means."),
        ("History", "Research the Great Galveston Hurricane of 1900 (before modern forecasting killed 8,000 people) and compare to Hurricane Harvey in 2017 (advanced warning saved thousands). How much have forecasting improvements reduced weather-related deaths?")
    ],
    "misconceptions": [
        ("Weather apps are inaccurate because meteorologists are bad at their jobs", "Modern weather forecasting is one of the greatest achievements of computational science. A 5-day forecast today is as accurate as a 1-day forecast was in the 1980s. The remaining inaccuracy isn't due to incompetence — it's due to chaos theory, a fundamental mathematical property of the atmospheric equations. No amount of skill can overcome the butterfly effect beyond approximately 2 weeks.", "Show the improvement graph: 1-day forecast accuracy has gone from ~70% in 1970 to ~95% today. 5-day forecasts have improved from ~40% to ~80%. Progress is real but asymptotic — approaching a mathematical limit."),
        ("If we had enough data and computing power, we could predict weather perfectly", "This is the fundamental insight of chaos theory: perfect prediction requires perfect measurements of initial conditions, which is physically impossible. The atmosphere has approximately 10^44 molecules, each with position and velocity that would need to be measured with infinite precision. Even quantum mechanics (Heisenberg's uncertainty principle) prevents measurements below certain precision limits. Better computers and data improve short-range forecasts but cannot extend the fundamental prediction horizon.", "Thought experiment: To perfectly predict the weather 30 days out, you would need to account for every molecule of air on Earth. How many sensors would that require? More than the number of atoms in the sensor material itself — it's a logical impossibility."),
        ("Climate can't be predicted if weather can't", "Weather and climate are fundamentally different prediction problems. Weather is about the specific state of the atmosphere on a specific day — chaotic and unpredictable beyond ~2 weeks. Climate is about the statistical average of weather over decades — driven by well-understood energy balance physics and highly predictable. You can't predict which coin flip will be heads, but you can confidently predict that 1,000 flips will be close to 50% heads.", "Analogy: You can't predict exactly when a specific person will die (chaotic individual variation), but you can predict average life expectancy for a population with great accuracy (statistical trends). Climate prediction works the same way.")
    ]
}

L08 = {
    "id": "G10L1-L08",
    "title": "How Do We Know the Earth Is 4.5 Billion Years Old?",
    "subtitle": "Modeling Radioactive Decay, Radiometric Dating, and Deep Time",
    "ngss": "HS-ESS1-5, HS-ESS1-6",
    "ngss_desc": "Evaluate evidence of the past and current movements of continental and oceanic crust and the theory of plate tectonics to explain the ages of crustal rocks. Apply scientific reasoning and evidence from ancient Earth materials, meteorites, and other planetary surfaces to construct an account of Earth's formation and early history.",
    "big_question": "How can scientists confidently claim the Earth is 4.5 billion years old when no human has ever seen anything close to that old?",
    "objectives": [
        "Model how radioactive isotopes decay at constant, measurable rates that serve as natural clocks",
        "Explain how measuring the ratio of parent to daughter isotopes in a rock determines its age",
        "Predict the age of rock samples based on isotope ratios and known decay rates",
        "Analyze how multiple independent dating methods converge on the same age for Earth"
    ],
    "vocabulary": [
        ("Radioactive Isotope", "An unstable atom that spontaneously transforms into a different element by emitting radiation — the rate of decay is constant and unaffected by temperature, pressure, or chemical conditions"),
        ("Half-Life", "The time it takes for exactly half of a radioactive isotope to decay into its daughter product — uranium-238 has a half-life of 4.47 billion years, carbon-14 has 5,730 years"),
        ("Radiometric Dating", "The technique of measuring the ratio of parent radioactive isotope to daughter product in a rock to calculate how much time has passed since the rock formed"),
        ("Daughter Product", "The stable element produced when a radioactive parent isotope decays — for example, uranium-238 decays through a series of steps to become lead-206")
    ],
    "components": [
        ("Radioactive Isotope Amount", "The quantity of parent isotope remaining in the rock sample, which decreases by exactly half with each half-life period — the starting amount is locked in when the rock crystallizes", False),
        ("Decay Rate", "The constant rate at which the radioactive parent transforms into the daughter product, expressed as a half-life — this rate is fixed by nuclear physics and never changes", True),
        ("Rock Layer Age", "The time since the rock crystallized from magma or was deposited as sediment, during which radioactive decay has been continuously converting parent to daughter isotopes", False),
        ("Geological Event Timing", "The dates of major events in Earth's history — mountain building, mass extinctions, continental splitting — determined by dating the rocks associated with these events", False),
        ("Age Estimate Accuracy", "The precision and reliability of the age calculation, which depends on the isotope system used, the quality of the sample, and whether the rock system has remained closed (no leakage of parent or daughter)", False)
    ],
    "think_about_it": "If you find a rock where 75% of the original uranium has decayed to lead, how many half-lives have passed? If uranium-238's half-life is 4.47 billion years, how old is that rock? What makes you confident in that number?",
    "scenarios": [
        ("Young Rock Dating", "Set a rock with a high ratio of parent to daughter isotopes — calculate a young age of tens of millions of years using appropriate isotope systems"),
        ("Ancient Rock Dating", "Set a rock where most parent isotopes have decayed to daughters — calculate a multi-billion-year age and identify the isotope system needed"),
        ("Multiple Methods", "Apply uranium-lead, potassium-argon, and rubidium-strontium dating to the same sample — observe how independent methods converge on the same age")
    ],
    "sim_scenarios": [
        ("Young Rock", "Parent:Daughter ratio high | Short half-life isotope", "What age do you predict for a rock where 90% of the parent isotope remains?"),
        ("Ancient Rock", "Parent:Daughter ratio low | Long half-life isotope", "If only 6.25% of the original uranium remains in a rock, how many half-lives have passed and what is the rock's age?"),
        ("Multiple Methods", "Same rock | Three different isotope systems", "Do you predict that different isotope systems will give the same age for the same rock? Why or why not?")
    ],
    "discoveries": [
        "Radioactive decay follows a precise mathematical curve — after one half-life, 50% remains; after two, 25%; after three, 12.5% — and this rate is constant regardless of environmental conditions",
        "The parent-to-daughter ratio is a built-in clock that starts ticking when a rock crystallizes, and by measuring this ratio today, we can calculate exactly how long the clock has been running",
        "Multiple independent dating methods (uranium-lead, potassium-argon, rubidium-strontium) applied to the same rocks produce the same ages — this cross-validation is powerful evidence that the methods work",
        "The oldest Earth rocks are about 4.0 billion years old, but meteorites (from the same solar system formation event) date to 4.567 billion years, and our Moon's oldest samples are 4.51 billion years — all pointing to the same age"
    ],
    "answer": "We know Earth is 4.5 billion years old because radioactive isotopes are nature's most reliable clocks. When a rock crystallizes from magma, radioactive atoms are locked inside like a sealed hourglass. These atoms decay at absolutely constant rates — unaffected by temperature, pressure, or chemistry — converting parent isotopes to daughter products. By measuring the ratio of parent to daughter today, we calculate how many half-lives have passed. Uranium-lead dating of meteorites (which formed alongside Earth) gives 4.567 billion years. Multiple independent isotope systems all converge on the same answer. This isn't one measurement — it's thousands of independent measurements across dozens of isotope systems, all agreeing to within a fraction of a percent.",
    "stem_title": "Design a Rock Dating Laboratory Protocol",
    "stem_mission": "Design a laboratory protocol for dating an unknown rock sample using multiple radiometric methods, including quality control measures to ensure accuracy.",
    "stem_scenario": "A geological survey team has discovered rock formations that may contain evidence of an ancient mass extinction event. They need to determine the precise age of these rocks to correlate them with known extinction events. Your team must design the dating protocol — which isotope systems to use, how to prepare samples, what quality control checks to perform, and how to interpret the results.",
    "stem_questions": [
        "Which isotope systems are appropriate for the expected age range and why?",
        "What could contaminate the results and how will your protocol prevent this?",
        "How will you use multiple methods to cross-validate your age determination?"
    ],
    "stem_design_qs": [
        "What isotope systems will you analyze and what is the scientific basis for each choice?",
        "How will you prepare rock samples to avoid contamination of parent or daughter isotopes?",
        "What statistical methods will you use to calculate age and uncertainty from your measurements?",
        "How will you determine whether the rock system has remained 'closed' since formation?"
    ],
    "career": "Geochronologists specialize in determining the age of rocks, minerals, and geological events using radiometric and other dating techniques. They work at universities, geological surveys, and mining companies, earning $65,000–$120,000/year. Isotope Geochemists who develop new dating methods and study planetary formation earn $70,000–$140,000/year.",
    "images": {
        "cover": ("G10L1-L08-cover.png", "A photorealistic, cinematic image of dramatic geological rock layers in a canyon showing billions of years of Earth history, vibrant colored strata from red to tan to grey, dramatic sunset lighting casting warm tones"),
        "landscape": ("G10L1-L08-landscape.png", "A diverse group of 15-16 year old students in a modern geology lab examining rock samples with magnifying glasses and mineral identification tools, geological timeline posters on walls, engaged expressions"),
        "modeling": ("G10L1-L08-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of radioactive decay curves, screens showing half-life graphs and isotope ratio calculations, modern classroom"),
        "discussion": ("G10L1-L08-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about Earth's age, a radioactive decay curve and geological timeline displayed on a smartboard, students asking questions"),
        "stem": ("G10L1-L08-stem.png", "Diverse 15-16 year old students designing dating laboratory protocols on large poster boards with decay curve calculations, sample preparation flowcharts, and quality control checklists, collaborative science atmosphere")
    },
    "pre_assessment": [
        "How do you think scientists figured out the age of the Earth if no one was around to see it form?",
        "What do you know about radioactivity and how it might be used as a clock?",
        "Draw a diagram showing what you think happens to radioactive atoms over very long periods of time.",
        "Why do you think scientists say the Earth is 4.5 billion years old and not 4 billion or 5 billion?"
    ],
    "extend_components": [
        ("Isochron Analysis", "A graphical method that plots multiple minerals from the same rock to determine age without knowing the initial parent-daughter ratio — provides a built-in check on whether the system remained closed"),
        ("Concordance Testing", "Using two independent decay chains (U-235 to Pb-207 and U-238 to Pb-206) from the same sample — if both give the same age, the result is 'concordant' and highly reliable"),
        ("Metamorphic Resetting", "The process where heat and pressure can partially or completely reset a rock's radiometric clock by allowing isotopes to escape or re-equilibrate — dating metamorphic rocks requires understanding these resetting events")
    ],
    "reflections": [
        "How does your model demonstrate that radioactive decay is a reliable clock?",
        "Why is the convergence of multiple independent dating methods such powerful evidence for Earth's age?",
        "What would it mean if different dating methods gave significantly different ages for the same rock?",
        "How does understanding radiometric dating change your perception of time and Earth's history?",
        "What are the limitations of modeling radioactive decay with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Analyzing and Interpreting Data", "Students analyze isotope ratio data to calculate rock ages and evaluate the accuracy of age determinations from multiple independent methods."),
        ("Disciplinary Core Idea", "ESS1.C The History of Planet Earth / PS1.C Nuclear Processes", "Radioactive decay provides a way to establish absolute ages for Earth's rocks and history. Nuclear decay rates are constant and provide reliable chronometers for geological time."),
        ("Crosscutting Concept", "Patterns", "Students identify the mathematical pattern of exponential decay in radioactive isotopes and use this pattern to calculate ages and predict isotope ratios at different points in geological time.")
    ],
    "cast_items": [
        "Model radioactive decay as a constant-rate process and calculate rock ages from parent-daughter isotope ratios",
        "Evaluate the reliability of age determinations by comparing results from multiple independent isotope systems",
        "Construct an account of Earth's formation age using evidence from terrestrial rocks, meteorites, and lunar samples"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A rock sample contains 25% of its original uranium-238 and 75% daughter lead-206. If the half-life of U-238 is 4.47 billion years, what is the age of this rock?"),
        ("Constructed Response:", "Using your model, explain how scientists determined Earth's age is 4.567 billion years. Include the roles of radioactive decay, half-life, parent-daughter ratios, and multiple independent lines of evidence in your explanation. Why is it significant that meteorites, Moon rocks, and Earth's oldest minerals all yield consistent ages?")
    ],
    "background_intro": "The question 'How old is the Earth?' was unanswerable for most of human history. In 1862, Lord Kelvin calculated the Earth was 20-100 million years old based on cooling rates — but he didn't know about radioactivity. In 1953, Clair Patterson used uranium-lead dating of meteorites to determine the age of the Solar System — and Earth — at 4.55 billion years (later refined to 4.567 billion years). The key to this discovery was understanding that radioactive atoms are perfect clocks.",
    "background_sections": [
        ("Radioactive Decay as a Clock", "Radioactive decay is a quantum mechanical process where an unstable nucleus spontaneously transforms into a more stable configuration. This process follows a strict exponential decay curve: N(t) = N₀ × (1/2)^(t/t½). The half-life is absolutely constant — it cannot be changed by any known physical or chemical process. This constancy is what makes radioactive isotopes perfect clocks: they tick at the same rate regardless of temperature, pressure, or environment."),
        ("Uranium-Lead Dating", "The gold standard for dating ancient rocks. Uranium-238 decays to lead-206 with a half-life of 4.47 billion years, while uranium-235 decays to lead-207 with a half-life of 704 million years. Having two independent decay chains in the same element provides a built-in cross-check (concordia). When both U-Pb systems give the same age, the result is considered highly reliable. This system is ideal for dating rocks from millions to billions of years old."),
        ("Multiple Lines of Evidence", "Earth's age isn't based on a single measurement. Uranium-lead dating of meteorites gives 4.567 billion years. Potassium-argon dating of Moon rocks gives 4.51 billion years. Rubidium-strontium dating of early Earth rocks gives ages up to 4.0 billion years (the oldest Earth rocks were recycled, so none preserve the original formation age). Samarium-neodymium dating of Hadean zircons gives ages up to 4.4 billion years. All methods converge on the same answer."),
        ("The Scale of Deep Time", "4.5 billion years is almost impossible to comprehend. If Earth's history were compressed to 24 hours, the first life appears at 4:00 AM, complex animals appear at 9:00 PM, dinosaurs dominate from 10:40 to 11:39 PM, and all of human history occurs in the last 0.2 seconds before midnight. Understanding deep time is essential for understanding geology, evolution, and the processes that shaped our planet.")
    ],
    "lever_L": "Students identify radioactive isotope amount, decay rate, rock layer age, geological event timing, and age estimate accuracy as the key components of the radiometric dating system.",
    "lever_E": "Students determine that decay rate is fixed by nuclear physics, the ratio of parent to daughter isotopes reveals how many half-lives have passed, and age is calculated by multiplying half-lives elapsed by the half-life duration.",
    "lever_V": "Students build a computational model showing exponential decay curves and using parent-daughter ratios to calculate rock ages across geological timescales.",
    "lever_Ev": "Students run young rock, ancient rock, and multiple methods scenarios to calculate ages and discover that independent methods converge on consistent results.",
    "lever_R": "Students add isochron analysis, concordance testing, or metamorphic resetting to model more sophisticated dating techniques and their quality controls.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with dramatic rock layers image", "say": "4,500,000,000 years. That's the age of the Earth. But how can we possibly know that when the oldest human civilizations are only 6,000 years old?", "do": "Write 4.5 billion on the board. Ask: How would you even BEGIN to measure something this old? What kind of clock runs for billions of years?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today you're going to learn about nature's most perfect clock — one that has been running since Earth was born, and we can read it.", "do": "Have students read objectives. Pre-teach 'half-life' and 'radiometric dating' with the coin-flip analogy.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How do we know what we can't see?", "say": "No one was there 4.5 billion years ago. No written records. No photographs. So how can scientists be so CONFIDENT about this number?", "do": "Students list what evidence they think exists. Most will underestimate the strength of the evidence.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building a model of a clock that ticks for billions of years — and learning to read it.", "do": "Preview LEVER steps. Emphasize that this model is about EVIDENCE and CONVERGENCE of multiple independent measurements.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for radiometric dating model", "say": "What factors determine how we read the atomic clock inside a rock?", "do": "Guide sorting. Decay rate is the key external constant — set by physics, unchangeable by any known force.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Decay curve and parent-daughter ratio diagram", "say": "If you start with 100 uranium atoms and find 25 remaining and 75 lead atoms, how many half-lives passed?", "do": "Work through the math: 100→50→25 = 2 half-lives × 4.47 billion years = 8.94 billion year old rock. Build the calculation chain.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Decay curves and age calculations for different samples", "say": "Let's date three different rocks — and then check our answer with a completely different isotope system.", "do": "Students calculate ages from ratios. Then apply a second dating method to the same sample. Results should converge.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Convergence chart — multiple methods, one age", "say": "Meteorites, Moon rocks, and Earth's oldest minerals all point to the same age. That's not a coincidence — that's evidence.", "do": "Show the convergence of multiple independent methods. Discuss why convergence is the strongest form of scientific evidence.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Rock dating laboratory design challenge", "say": "A geological survey found rocks that might date a mass extinction. Design the lab protocol to nail down the age.", "do": "Groups design dating protocols specifying isotope systems, sample prep, quality controls, and cross-validation.", "time": "12 min"}
    ],
    "sort_reasoning": "Decay Rate is the external component because it is a fixed physical constant determined by nuclear physics — it cannot be changed or controlled and remains the same regardless of conditions. Radioactive Isotope Amount, Rock Layer Age, Geological Event Timing, and Age Estimate Accuracy are internal because they are measured or calculated values that depend on the decay process operating over time within the rock system.",
    "relationships": [
        ("Decay Rate to Radioactive Isotope Amount", "NEGATIVE (-) over time", "The constant decay rate continuously reduces the amount of parent radioactive isotope in the rock. After each half-life period, exactly half of the remaining parent atoms have transformed into daughter atoms. This exponential decrease is the fundamental clock mechanism."),
        ("Radioactive Isotope Amount to Rock Layer Age", "INVERSE CALCULATION", "The proportion of parent isotope remaining compared to the original amount directly reveals how many half-lives have elapsed. More parent remaining means younger rock; less parent remaining means older rock. The relationship follows: Age = half-life × log₂(N₀/N)."),
        ("Rock Layer Age to Geological Event Timing", "DETERMINES", "Dating specific rock layers places geological events — volcanic eruptions, asteroid impacts, mass extinctions, mountain building — on an absolute timeline. The age of a rock layer constrains the age of any fossils or geological features within or adjacent to it.")
    ],
    "sim_answers": [
        ("Ancient Rock Scenario", "When only 6.25% of the original parent isotope remains, the model calculates: 100%→50%→25%→12.5%→6.25% = 4 half-lives. For uranium-238 (half-life 4.47 billion years), the rock is approximately 17.9 billion years old — older than the universe itself, which would indicate an error in the sample or assumption. For potassium-40 (half-life 1.25 billion years), the age would be 5 billion years. This demonstrates why choosing the correct isotope system for the expected age range is critical."),
        ("Multiple Methods Scenario", "When three independent isotope systems (U-Pb, K-Ar, Rb-Sr) are applied to the same rock, the model shows all three converging on the same age within measurement uncertainty. This concordance is extremely powerful evidence because each system involves different elements, different decay mechanisms, and different half-lives. The probability of three independent methods accidentally giving the same wrong answer is vanishingly small.")
    ],
    "reflection_exemplars": [
        ("Why is convergence of multiple methods so important?", "A single measurement could potentially be wrong — contamination, sample alteration, or measurement error could produce an incorrect age. But when multiple independent methods using different elements and different decay chains all produce the same answer, the probability of all being wrong in exactly the same way is essentially zero. This is like asking three witnesses who don't know each other to describe a crime — if they all tell the same story independently, the story is almost certainly true. The convergence of U-Pb, K-Ar, and Rb-Sr dating on the same ages is among the strongest evidence in all of Earth science."),
        ("What makes radioactive decay a reliable clock?", "Radioactive decay is governed by quantum mechanics — specifically, the probability of a nucleus tunneling through its energy barrier. This probability is set by the fundamental forces of physics (the strong nuclear force and electromagnetic force) and cannot be altered by any known physical or chemical process. Temperature, pressure, chemical bonding, magnetism — nothing changes the decay rate. This is what makes it the most reliable clock in nature: it ticks at exactly the same rate whether the rock is at Earth's surface, deep in the mantle, or floating in space.")
    ],
    "stem_intro": "Present the challenge: A geological survey team needs to date rock formations potentially associated with a mass extinction event. Your team will design the laboratory dating protocol, selecting appropriate isotope systems, specifying sample preparation procedures, building in quality controls, and explaining how multiple methods will cross-validate the results.",
    "stem_concepts": [
        ("Concordia Diagrams", "Plotting U-235/Pb-207 age versus U-238/Pb-206 age on a graph. If both systems give the same age, the data point falls on the 'concordia curve.' Points that fall off this curve indicate the system has been disturbed (open system behavior), providing a built-in quality check."),
        ("Closed System Assumption", "Radiometric dating requires that no parent or daughter isotopes have been added or removed since the rock formed. Weathering, metamorphism, or fluid infiltration can violate this assumption. Quality protocols must assess whether the system remained closed by checking for alteration, using isochron methods, and testing mineral separates."),
        ("Zircon Dating", "Zircon crystals (ZrSiO₄) are the gold standard for U-Pb dating because they incorporate uranium but reject lead when they crystallize, giving a clean starting ratio. They are also extremely durable — surviving weathering, erosion, and even metamorphism. The oldest known zircons, from Jack Hills, Australia, are 4.4 billion years old.")
    ],
    "stem_eval": [
        ("Expert (4)", "Protocol selects appropriate isotope systems with justification, specifies sample preparation to avoid contamination, includes concordance testing and quality controls, and explains how results will be cross-validated"),
        ("Proficient (3)", "Protocol identifies appropriate isotope systems and includes basic quality control measures with some scientific justification"),
        ("Developing (2)", "Protocol identifies a dating method but lacks detail on sample preparation, quality control, or cross-validation"),
        ("Beginning (1)", "Protocol is incomplete or doesn't demonstrate understanding of radiometric dating principles")
    ],
    "support": [
        "Provide a half-life reference table showing common isotope systems and their useful dating ranges",
        "Use a visual decay curve with marked half-life intervals so students can read ages from parent-daughter ratios",
        "Sentence frames: 'We selected the __ isotope system because its half-life of __ years is appropriate for rocks in the __ age range'"
    ],
    "extensions": [
        "Research the controversy over the age of the Grand Canyon — how have radiometric dating methods been applied to different rock layers and what do they reveal about its formation?",
        "Investigate carbon-14 dating: Why is it limited to about 50,000 years, and how is it calibrated against tree ring records?",
        "Calculate: If Earth started with 10 kg of uranium-238, how much remains today after 4.5 billion years (approximately one half-life)?"
    ],
    "cross_curr": [
        ("Math", "Graph the exponential decay curve for U-238 over 20 billion years. Calculate the percentage remaining at 1, 2, 3, and 4 half-lives. If a rock has 12.5% parent remaining, solve for its age algebraically using the decay equation."),
        ("ELA", "Write a science narrative that makes the concept of 4.5 billion years comprehensible to a general audience. Use analogies, scale comparisons, and storytelling to convey the depth of geological time."),
        ("History", "Research the historical debate over Earth's age: from Archbishop Ussher's 1654 calculation (6,000 years) to Lord Kelvin's 1862 estimate (100 million years) to Patterson's 1956 measurement (4.55 billion years). How did each estimate reflect the scientific tools of its era?")
    ],
    "misconceptions": [
        ("Carbon dating proves the Earth is billions of years old", "Carbon-14 dating is only useful for organic materials up to about 50,000 years old — it says nothing about Earth's age. Earth's age comes from uranium-lead, potassium-argon, and rubidium-strontium dating of rocks and meteorites, which work on billion-year timescales. Different isotope systems have different useful ranges: C-14 for recent biology, K-Ar for millions of years, U-Pb for billions of years.", "Show the half-life comparison: C-14 (5,730 years) vs. U-238 (4.47 billion years). After 50,000 years, virtually no C-14 remains — it's useless for old rocks. Uranium is perfect because it's barely halfway through its first half-life at Earth's current age."),
        ("Radioactive decay rates could have been different in the past", "Radioactive decay rates are determined by the fundamental constants of nuclear physics — the strong force and electromagnetic force. These constants have been measured to be unchanged across the observable universe (through spectral analysis of distant stars and galaxies) and across billions of years of cosmic history. To change decay rates, you would need to change the fundamental forces that hold atomic nuclei together — and there is zero evidence this has ever happened.", "Evidence: The natural nuclear reactor at Oklo, Gabon, operated 2 billion years ago. Analysis of its fission products confirms that nuclear decay rates were identical then to what they are today. Nature ran the experiment for us."),
        ("Radiometric dating is just one guess", "Earth's age is not based on one measurement but on THOUSANDS of independent measurements using DOZENS of different isotope systems on rocks from EVERY continent, plus meteorites and Moon samples. Multiple independent methods all converge on the same age: 4.567 billion years. The probability of this convergence being coincidental is effectively zero. This is one of the most thoroughly verified measurements in all of science.", "Analogy: If one clock says 3:00 PM, it might be wrong. If 100 different clocks built by different people using different mechanisms all say 3:00 PM, what time is it? That's radiometric dating — overwhelming convergence from independent evidence.")
    ]
}

L09 = {
    "id": "G10L1-L09",
    "title": "Why Do Magnets Work Through Your Phone Case?",
    "subtitle": "Modeling Electromagnetic Fields, Force at a Distance, and Energy Storage",
    "ngss": "HS-PS2-3, HS-PS3-5",
    "ngss_desc": "Apply scientific and engineering ideas to design, evaluate, and refine a device that minimizes the force on a macroscopic object during a collision. Develop and use a model of two objects interacting through electric or magnetic fields to illustrate the forces between objects and the changes in energy of the objects due to the interaction.",
    "big_question": "How can a magnet pull on metal through solid materials — and where does the energy in a magnetic field actually come from?",
    "objectives": [
        "Model how magnetic field strength decreases with distance and interacts with different materials",
        "Explain how force at a distance works through the concept of electromagnetic fields",
        "Predict the force of attraction between a magnet and a ferromagnetic object at various distances and through different materials",
        "Analyze how energy is stored in magnetic fields and converted during interactions"
    ],
    "vocabulary": [
        ("Magnetic Field", "An invisible region of space around a magnet or current-carrying wire where magnetic forces can be detected — visualized using field lines that show direction and strength of the field"),
        ("Ferromagnetic Material", "A material (iron, nickel, cobalt, and their alloys) whose atomic magnetic domains can align with an external field, making it strongly attracted to magnets"),
        ("Inverse Square Law", "The mathematical relationship describing how field strength decreases with the SQUARE of the distance — doubling the distance reduces the force to one-quarter, not one-half"),
        ("Field Energy", "Energy stored in the magnetic field itself — when a magnet attracts an iron object, the stored field energy converts to kinetic energy of the moving object. The field is not just a description; it contains real, measurable energy")
    ],
    "components": [
        ("Magnetic Field Strength", "The intensity of the magnetic field produced by the source magnet, measured in Tesla — determined by the magnet's material, size, and magnetization. Neodymium magnets produce fields 10-100x stronger than ceramic magnets.", True),
        ("Distance from Magnet", "The separation between the magnet and the target object — force decreases approximately as the inverse cube of distance for magnetic dipoles, making the distance effect dramatic", True),
        ("Material Type", "The substance between the magnet and the target — non-ferromagnetic materials (plastic, glass, wood, aluminum) have negligible effect on the field, while ferromagnetic materials (iron, steel) redirect and shield it", True),
        ("Force of Attraction", "The pull exerted on a ferromagnetic object by the magnetic field — determined by field strength, distance, and the magnetic properties of the target material", False),
        ("Energy Stored in Field", "The total electromagnetic energy contained in the magnetic field surrounding the magnet — this energy is real, physical, and converts to kinetic energy when magnetic objects accelerate toward each other", False)
    ],
    "think_about_it": "Your phone case is made of plastic or silicone — nonmagnetic materials. Yet a magnet on the outside still locks onto the metal plate inside your case. If the force travels THROUGH the case, what does that tell us about what a field actually is?",
    "scenarios": [
        ("Direct Contact", "Set Distance from Magnet to minimum (touching) — observe maximum Force of Attraction and the energy state of the field"),
        ("Through Phone Case", "Set Distance from Magnet to the thickness of a phone case with plastic Material Type — observe how little the force changes compared to direct contact"),
        ("Distance Falloff", "Gradually increase Distance from Magnet from 1mm to 10cm — observe the dramatic inverse-cube decrease in Force of Attraction")
    ],
    "sim_scenarios": [
        ("Direct Contact", "Distance: 0mm | No intervening material", "What do you predict the Force of Attraction will be when the magnet is in direct contact with the metal?"),
        ("Through Phone Case", "Distance: 3mm | Material: Plastic", "Do you predict the phone case will significantly reduce the magnetic force? Why or why not?"),
        ("Distance Falloff", "Distance: 1mm → 100mm | Material: Air", "By how much do you predict the force will decrease when you double the distance? Triple it?")
    ],
    "discoveries": [
        "Magnetic fields pass through non-ferromagnetic materials (plastic, glass, wood, air, water) with virtually no reduction — the phone case is invisible to the magnetic field",
        "Force decreases with the cube of distance for magnetic dipoles — doubling the distance reduces force to about one-eighth, making the falloff extremely steep",
        "The magnetic field contains real energy that can do real work — when a magnet pulls a paperclip, the field's stored energy converts to the paperclip's kinetic energy",
        "Fields are not just mathematical descriptions — they are physical entities that carry energy, exert forces, and travel through space at the speed of light"
    ],
    "answer": "Magnets work through your phone case because magnetic fields are physical entities that permeate space and pass through non-ferromagnetic materials (like plastic, glass, or silicone) with almost no reduction. The field doesn't 'see' your phone case because plastic has no magnetic properties to interact with — the field passes through it the way light passes through glass. The force still reaches the metal plate inside because the field's strength depends primarily on distance, not on what non-magnetic material fills that distance. A 3mm plastic case reduces the force only by the amount that 3mm of additional distance causes — which, at close range, is quite small.",
    "stem_title": "Design a Magnetic Mounting System",
    "stem_mission": "Design a magnetic mounting system for a specific application (phone mount, tool holder, or cabinet latch) that provides sufficient holding force while remaining easy to detach when needed.",
    "stem_scenario": "A product design company wants to create a magnetic phone mount for cars that holds a phone securely during bumps and turns (force requirement: at least 2N) but can be removed with one hand (detach force: less than 8N). The mount must work through any standard phone case up to 5mm thick. Your team must specify the magnet type, size, and arrangement to meet these force requirements.",
    "stem_questions": [
        "What magnetic field strength is needed to hold a 200g phone securely against vibration and gravity?",
        "How does the phone case thickness affect your magnet selection?",
        "How will you ensure the magnet can be detached easily despite providing strong hold?"
    ],
    "stem_design_qs": [
        "What magnet material and size will provide the required field strength?",
        "How will you arrange multiple magnets to optimize the force profile — strong enough to hold but easy to slide off?",
        "What ferromagnetic metal plate should go inside the phone case, and how thick must it be?",
        "How will you test your prototype to verify it meets the force requirements?"
    ],
    "career": "Electromagnetic Engineers design systems that use magnetic and electric fields — from MRI machines in hospitals to maglev trains to the motors in electric vehicles. They work in medical device companies, automotive, energy, and defense sectors, earning $75,000–$140,000/year. Materials Scientists who develop new magnetic materials earn $70,000–$130,000/year.",
    "images": {
        "cover": ("G10L1-L09-cover.png", "A photorealistic, cinematic close-up of a smartphone attached to a magnetic car mount, visible magnetic field visualization lines passing through the phone case, sleek modern dashboard background, dramatic lighting"),
        "landscape": ("G10L1-L09-landscape.png", "A diverse group of 15-16 year old students in a modern physics lab experimenting with magnets, iron filings showing field lines on paper, force meters measuring magnetic force, engaged expressions"),
        "modeling": ("G10L1-L09-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of magnetic field strength and force, screens showing field line diagrams and force-distance graphs, modern classroom"),
        "discussion": ("G10L1-L09-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about electromagnetic fields, magnetic field visualization and inverse square law graph displayed on a smartboard, students experimenting with magnets"),
        "stem": ("G10L1-L09-stem.png", "Diverse 15-16 year old students designing magnetic mounting prototypes with various magnets, metal plates, force meters, and phone cases, collaborative engineering design atmosphere")
    },
    "pre_assessment": [
        "How can a magnet attract a paperclip without touching it? What is in the space between them?",
        "Why does a magnet stick to a refrigerator door through a piece of paper but not through a thick book?",
        "Draw what you think a magnetic field looks like around a bar magnet.",
        "Where does the energy come from when a magnet snaps onto metal?"
    ],
    "extend_components": [
        ("Magnetic Domain Alignment", "The degree to which atomic magnetic domains in a ferromagnetic material are aligned with the external field — randomly oriented domains produce no net magnetism, while aligned domains create a strong magnetic response"),
        ("Temperature Effects", "Heat disrupts magnetic domain alignment — above the Curie temperature (770°C for iron), ferromagnetic materials lose their magnetism entirely as thermal energy overwhelms magnetic ordering"),
        ("Electromagnetic Induction", "When a magnetic field changes through a conductor, it generates an electric current — this is the principle behind generators, transformers, and wireless charging, connecting magnetism to electricity")
    ],
    "reflections": [
        "How does your model demonstrate that magnetic fields are physical entities, not just mathematical descriptions?",
        "Why does the force drop so dramatically with distance while being unaffected by non-magnetic materials in between?",
        "What does it mean that the magnetic field stores real energy that can be converted to kinetic energy?",
        "How would your model change if you placed a ferromagnetic material (iron sheet) between the magnet and the target instead of plastic?",
        "What are the limitations of modeling electromagnetic interactions with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop and use models of magnetic field interactions to predict forces between objects at various distances and through different materials."),
        ("Disciplinary Core Idea", "PS2.B Types of Interactions / PS3.C Relationship Between Energy and Forces", "When two objects interact through magnetic fields, the force depends on their magnetic properties, distance, and orientation. Energy is stored in the field and converts during interactions."),
        ("Crosscutting Concept", "Systems and System Models", "Students model the magnet-field-material system to understand how invisible fields mediate forces between objects and store energy that can be transferred during interactions.")
    ],
    "cast_items": [
        "Model how magnetic field strength varies with distance and material type",
        "Predict the force of attraction between magnets and ferromagnetic objects under varying conditions",
        "Explain how energy is stored in magnetic fields and converted during magnetic interactions"
    ],
    "cast_questions": [
        ("Multiple Choice:", "A neodymium magnet holds a metal plate firmly through a 3mm plastic phone case. If the case is replaced with a 3mm iron plate, what will happen to the force on the metal plate behind it, and why?"),
        ("Constructed Response:", "Using your model, explain why a magnet can attract a paperclip through a wooden table but the force drops dramatically when you increase the distance by just a few centimeters. Include the roles of field permeation through materials, the inverse-distance relationship, and field energy in your explanation.")
    ],
    "background_intro": "Magnets are one of the most familiar yet least understood phenomena in everyday life. The fact that a magnet can exert force on metal through solid materials — without any physical connection — seems almost magical. But it reveals something profound about the nature of reality: space is not empty. It is filled with fields — invisible physical entities that carry energy, exert forces, and mediate every electromagnetic interaction in the universe.",
    "background_sections": [
        ("What Is a Magnetic Field?", "A magnetic field is a physical entity that exists in the space around any magnet or moving electric charge. It's not just a mathematical tool — it contains real energy, can exert real forces, and propagates through space at the speed of light. Field lines represent the direction a compass needle would point at each location. The field is strongest where lines are densest (near the poles) and weakest where they're spread apart (far from the magnet)."),
        ("Fields and Materials", "Magnetic fields interact differently with different materials. Ferromagnetic materials (iron, nickel, cobalt) have atomic magnetic domains that align with the field, concentrating and redirecting it — this is why iron shields and redirects magnetic fields. Diamagnetic and paramagnetic materials (plastic, wood, glass, water, air, aluminum) have virtually no interaction with the field — it passes through them as if they weren't there. This is why your phone case is invisible to a magnet."),
        ("The Distance Relationship", "For a magnetic dipole (bar magnet), the field strength decreases approximately as 1/r³ — the inverse CUBE of distance. This is even steeper than the inverse-square law of gravity. Doubling the distance reduces the force to about 1/8 (not 1/4). This explains why magnets seem to suddenly 'grab' when close — the force increases explosively as distance shrinks. At 1mm, a neodymium magnet might exert 5N; at 10mm, only about 0.005N — a thousand-fold decrease."),
        ("Energy in the Field", "The magnetic field stores energy — about B²/(2μ₀) joules per cubic meter. When a magnet attracts a paperclip, the total field energy decreases as the paperclip moves closer (a lower-energy configuration). This decrease in field energy converts to the kinetic energy of the accelerating paperclip. This is not abstract — the energy in the field is as real as the energy in a stretched spring. In fact, every electric motor, generator, and transformer works by converting energy between magnetic fields and mechanical motion.")
    ],
    "lever_L": "Students identify magnetic field strength, distance from magnet, material type, force of attraction, and energy stored in field as the key components of the magnetic interaction system.",
    "lever_E": "Students determine that field strength sets the maximum possible force, distance dramatically reduces force following the inverse cube relationship, and material type determines whether the field passes through unimpeded or is shielded.",
    "lever_V": "Students build a computational model showing how magnetic force varies with distance and material, and how field energy converts to kinetic energy during attraction.",
    "lever_Ev": "Students run direct contact, through-phone-case, and distance falloff scenarios to discover the inverse cube relationship and the transparency of non-magnetic materials to fields.",
    "lever_R": "Students add magnetic domain alignment, temperature effects, or electromagnetic induction to model more complete electromagnetic behavior.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with magnetic phone mount image", "say": "Your phone sticks to a magnetic mount through a plastic case. The magnet never touches the metal. How does force travel through solid material?", "do": "Pass around a strong magnet and various materials. Students test: Does the magnet work through paper? Wood? Plastic? Aluminum? Steel?", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're investigating one of the most fundamental questions in physics: how can objects push and pull each other without touching?", "do": "Have students read objectives. Pre-teach 'magnetic field' and 'inverse square law' with visual demonstrations.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "How does force travel through solid matter?", "say": "A magnet on the outside of your phone case pulls on metal inside the case. What is in the space between them that transmits this force?", "do": "Students draw what they think exists between a magnet and a paperclip. Most will draw 'nothing' — challenge this assumption.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're modeling the invisible — building a computational model of something you can't see but can definitely feel.", "do": "Preview LEVER steps. Emphasize we're exploring FIELDS — real physical entities that fill 'empty' space.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for magnetic interaction model", "say": "What determines how strongly a magnet pulls? Which factors can you change in a design?", "do": "Guide sorting. Field strength, distance, and material are design choices; force and energy are physics outcomes.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Force-distance curve and material comparison", "say": "Double the distance and the force drops to one-eighth. But a plastic case? Almost no effect. Why the difference?", "do": "Build the relationship map. Introduce the inverse cube law with numerical examples. Test materials.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Force-distance graphs and material comparison data", "say": "Let's measure exactly how force changes with distance — and prove that your phone case is invisible to the magnetic field.", "do": "Students predict force at various distances. Run simulations. Compare through air, plastic, glass, and iron.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings — field visualization and energy diagram", "say": "The space between a magnet and metal is NOT empty. It's filled with a field that carries real energy. When the paperclip flies to the magnet, that's field energy converting to motion.", "do": "Show iron filing field visualization. Discuss: The field is real. It carries energy. It's everywhere.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Magnetic mounting system design", "say": "Design a phone mount that holds securely through any case, survives bumpy roads, but comes off with one hand. Use your model data.", "do": "Groups specify magnet types, sizes, arrangements, and metal plate requirements. Test with force calculations.", "time": "12 min"}
    ],
    "sort_reasoning": "Magnetic Field Strength, Distance from Magnet, and Material Type are external components because they represent design variables that an engineer or experimenter can control — choosing the magnet strength, setting the distance, and selecting the intervening material. Force of Attraction and Energy Stored in Field are internal because they are physical outcomes determined by the laws of electromagnetism once the external variables are set.",
    "relationships": [
        ("Magnetic Field Strength to Force of Attraction", "POSITIVE (+)", "Stronger magnetic fields exert greater forces on ferromagnetic objects. A neodymium magnet (field ~1.2 Tesla) produces roughly 10-100 times more force than a ceramic magnet (~0.1 Tesla) at the same distance."),
        ("Distance from Magnet to Force of Attraction", "NEGATIVE (inverse cube)", "Force decreases approximately as the cube of distance for magnetic dipoles: F ∝ 1/r³. Doubling distance reduces force to about 1/8. This extremely steep falloff explains why magnets seem to 'grab' suddenly when close — the force increases explosively as distance shrinks."),
        ("Material Type to Force of Attraction", "CONDITIONAL", "Non-ferromagnetic materials (plastic, glass, wood, air) have negligible effect on the magnetic field — it passes through them transparently. Ferromagnetic materials (iron, steel) redirect and shield the field, potentially reducing the force on objects behind them. Material type acts as a gate: either transparent or opaque to the field.")
    ],
    "sim_answers": [
        ("Through Phone Case Scenario", "When a 3mm plastic phone case is placed between the magnet and metal plate, the model shows virtually no reduction in Force of Attraction beyond what the additional 3mm of distance would cause. The plastic is electromagnetically transparent — the field passes through it unimpeded. At close range (where the force-distance curve is steep), 3mm reduces the force by about 15-25%, not because of the material but purely because of the extra distance."),
        ("Distance Falloff Scenario", "As Distance increases from 1mm to 100mm, Force of Attraction drops by a factor of approximately 1,000,000 (one million). The inverse cube law means: at 1mm the force might be 5N; at 2mm about 0.63N; at 5mm about 0.04N; at 10mm about 0.005N; at 100mm about 0.000005N. This dramatic falloff explains why magnets seem to have a sharp 'on/off' boundary — they don't, but the force becomes imperceptible very quickly with distance.")
    ],
    "reflection_exemplars": [
        ("Are magnetic fields 'real' or just mathematical tools?", "Magnetic fields are absolutely real physical entities. They contain measurable energy (B²/2μ₀ joules per cubic meter), they exert real forces that can move objects and do work, and they propagate through space at the speed of light as electromagnetic waves (light, radio waves, X-rays are all electromagnetic fields). When a magnet accelerates a paperclip, the energy comes FROM the field — the field energy decreases by exactly the amount the paperclip's kinetic energy increases. You can't see fields, but you can't see air either — both are real, physical, and measurable."),
        ("Why does plastic not block a magnetic field?", "Magnetic fields interact with matter through the alignment of atomic magnetic moments — tiny current loops within atoms. In ferromagnetic materials, unpaired electrons create strong atomic magnets that align with external fields, concentrating the field and creating strong interactions. In non-ferromagnetic materials (plastic, glass, wood), all electrons are paired and their magnetic moments cancel. There's nothing for the field to interact with, so it passes through as if the material weren't there — like sound passing through air.")
    ],
    "stem_intro": "Present the challenge: A product design company needs a magnetic phone mount for cars that holds phones securely during driving (bumps, turns, sudden braking) but allows one-handed removal. Your team must specify magnet specifications, metal plate requirements, and arrangement geometry using your model data to meet the force requirements.",
    "stem_concepts": [
        ("Halbach Arrays", "A special arrangement of permanent magnets where the field is enhanced on one side and nearly cancelled on the other. This allows designers to direct magnetic force where it's needed while minimizing stray fields — used in MRI machines, refrigerator magnets, and maglev trains."),
        ("Shear vs. Pull Force", "Magnets resist being pulled apart (normal force) much more strongly than being slid apart (shear force). A mount designed so the phone slides off sideways (shear) requires much less detach force than one requiring pulling straight away (normal). This is the key to 'strong hold, easy removal.'"),
        ("Magnetic Circuit Design", "Like electrical circuits, magnetic fields follow paths of least resistance (highest permeability). Engineers design 'magnetic circuits' using iron backing plates to concentrate the field through the target area, increasing force without using a larger magnet. A thin iron backing plate can double the effective force of a magnet.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design specifies magnet type and dimensions, calculates holding force at expected distance through expected materials, addresses shear vs. pull force for easy detachment, and includes testing protocol"),
        ("Proficient (3)", "Design selects appropriate magnet specifications and addresses basic force requirements with some reference to model data"),
        ("Developing (2)", "Design identifies magnet needs but lacks specific calculations or doesn't address the hold-vs-detach trade-off"),
        ("Beginning (1)", "Design is incomplete or doesn't demonstrate understanding of magnetic field principles")
    ],
    "support": [
        "Provide a magnet specifications reference table showing field strength, size, and pull force for common magnet types",
        "Use a visual force-distance curve with marked points for typical phone case thicknesses",
        "Sentence frames: 'Our design uses a __ mm __ magnet because our model shows it provides __ N of force at __ mm distance through __'"
    ],
    "extensions": [
        "Research how MRI machines use superconducting magnets 30,000 times stronger than Earth's field to image inside the human body — how do magnetic fields interact with hydrogen atoms in your body?",
        "Investigate maglev trains: How do they use magnetic fields to levitate and propel a train at 375 mph with no friction? What's the engineering behind field-based transportation?",
        "Explore the physics of hard drives: How do tiny magnetic domains store billions of bits of data on a spinning disk, and why is this being replaced by solid-state storage?"
    ],
    "cross_curr": [
        ("Math", "Plot the inverse cube force-distance relationship: F = k/r³. Calculate the force at 1mm, 2mm, 5mm, and 10mm. Graph the curve. At what distance does the force drop below 1N? Below 0.01N? How does this inform mounting system design?"),
        ("ELA", "Write a scientific explanation for a general audience that answers: 'How can magnets push and pull things without touching them?' Use analogies and accessible language while maintaining scientific accuracy."),
        ("History/Technology", "Research the evolution of magnetic technology from ancient lodestones to neodymium supermagnets. How did understanding of electromagnetism (Faraday, Maxwell, Oersted) lead to motors, generators, MRI machines, and wireless charging?")
    ],
    "misconceptions": [
        ("Magnets push or pull through 'magic' with no mechanism", "Magnetic force is mediated by the magnetic field — a real, physical entity that fills the space around every magnet. The field contains energy, exerts forces, and obeys precise mathematical laws. There is nothing mysterious about it: the field is produced by moving charges (electron orbital motion and spin) and interacts with other magnetic materials through the alignment of atomic magnetic moments. Maxwell's equations describe this completely.", "Demonstration: Sprinkle iron filings around a magnet to VISUALIZE the field. The filings align along field lines, making the invisible visible. The field was always there — the filings just show us where."),
        ("Magnetic force goes through everything equally", "While magnetic fields pass through non-ferromagnetic materials (plastic, glass, air) with virtually no reduction, ferromagnetic materials (iron, steel) strongly interact with and redirect the field. An iron plate between a magnet and target will shield the target by 'absorbing' the field into itself. This is why steel is used for magnetic shielding. The field doesn't go through everything equally — it depends entirely on the material's magnetic properties.", "Test it: Hold a strong magnet near a paperclip with air between them — it sticks. Now slide a thick iron plate between them — the paperclip falls. The iron redirected the field. Try aluminum instead — no shielding at all."),
        ("Magnets eventually 'run out' of force or energy", "Permanent magnets don't 'run out' of magnetism through normal use. The magnetic field is maintained by the quantum mechanical spin of electrons in the magnet's crystal structure — this is an intrinsic property of the material, not a consumable resource. However, magnets CAN be demagnetized by excessive heat (above the Curie temperature), physical shock (disrupts domain alignment), or opposing magnetic fields. But under normal conditions, a neodymium magnet loses less than 1% of its field strength per century.", "Analogy: Gravity doesn't 'run out' — Earth has been attracting objects for 4.5 billion years without getting weaker. Magnetic fields are similar — they're properties of the material's structure, not fuel that gets consumed.")
    ]
}

L10 = {
    "id": "G10L1-L10",
    "title": "Why Can't Humans Photosynthesize?",
    "subtitle": "Modeling Energy Flow Between Photosynthesis and Cellular Respiration",
    "ngss": "HS-LS1-7, HS-LS2-5",
    "ngss_desc": "Use a model to illustrate that cellular respiration is a chemical process whereby the bonds of food molecules and oxygen molecules are broken and the bonds in new compounds are formed, resulting in a net transfer of energy. Develop a model to illustrate the role of photosynthesis and cellular respiration in the cycling of carbon among the biosphere, atmosphere, hydrosphere, and geosphere.",
    "big_question": "Plants convert sunlight into food using nothing but water and CO2. Why can't humans do the same — and what would happen if we could?",
    "objectives": [
        "Model how photosynthesis captures solar energy in glucose molecules and how cellular respiration releases that stored energy",
        "Explain why the energy output of photosynthesis is insufficient to power a human body",
        "Predict net energy balance for organisms with different metabolic rates and surface-area-to-volume ratios",
        "Analyze the complementary relationship between photosynthesis and cellular respiration in the global carbon cycle"
    ],
    "vocabulary": [
        ("Photosynthesis", "The process by which plants, algae, and cyanobacteria convert light energy, water, and CO2 into glucose and oxygen — 6CO2 + 6H2O + light → C6H12O6 + 6O2 — storing about 1% of incoming solar energy in chemical bonds"),
        ("Cellular Respiration", "The process by which all aerobic organisms break down glucose using oxygen to release stored chemical energy as ATP — C6H12O6 + 6O2 → 6CO2 + 6H2O + energy (ATP) — the reverse of photosynthesis"),
        ("ATP", "Adenosine triphosphate — the molecular 'energy currency' of all living cells. Cellular respiration produces about 36-38 ATP molecules per glucose molecule. A human body uses approximately 40 kg of ATP per day."),
        ("Surface-Area-to-Volume Ratio", "The relationship between an organism's surface area (which captures sunlight) and its volume (which consumes energy) — as organisms grow larger, volume increases faster than surface area, making photosynthesis increasingly insufficient for energy needs")
    ],
    "components": [
        ("Sunlight Intensity", "The amount of solar energy reaching the photosynthetic surface, varying by latitude, weather, time of day, and season — maximum solar energy at Earth's surface is about 1,000 watts per square meter", True),
        ("Chlorophyll Concentration", "The density of light-absorbing chlorophyll molecules in the photosynthetic tissue — determines what fraction of incoming light energy is captured and converted to chemical energy", True),
        ("Glucose Production Rate", "The rate at which photosynthesis produces glucose from CO2 and water using captured light energy — limited by chlorophyll concentration, sunlight intensity, CO2 availability, and temperature", False),
        ("Cellular Respiration Rate", "The rate at which cells break down glucose to produce ATP for metabolic functions — humans burn about 2,000-2,500 kilocalories per day just for basic survival", False),
        ("Net Energy Output", "The balance between energy captured by photosynthesis and energy consumed by cellular respiration — positive means surplus (growth), negative means deficit (starvation). For a hypothetical photosynthetic human, this balance is dramatically negative.", False)
    ],
    "think_about_it": "A leaf captures about 1% of the sunlight hitting it and converts it to glucose. A human needs about 2,000 kcal per day. Your body's total surface area is about 1.7 square meters. Is there any way the math works out?",
    "scenarios": [
        ("Optimal Plant", "Set Sunlight Intensity to maximum and Chlorophyll Concentration to high — observe how a typical leaf's Glucose Production Rate compares to a single plant cell's Cellular Respiration Rate"),
        ("Photosynthetic Human", "Imagine covering a human body with chlorophyll — set surface area to 1.7 m² and Cellular Respiration Rate to human levels (2,000 kcal/day). Calculate Net Energy Output."),
        ("Scaling Problem", "Compare the Net Energy Output for organisms of increasing size — bacteria, moss, tree leaf, entire human — observe when photosynthesis stops being sufficient")
    ],
    "sim_scenarios": [
        ("Optimal Plant", "Sunlight: Maximum | Chlorophyll: High | Plant scale", "What fraction of a plant cell's energy needs do you predict photosynthesis can provide under ideal conditions?"),
        ("Photosynthetic Human", "Surface area: 1.7m² | Respiration: 2,000 kcal/day", "If your entire skin were photosynthetic, what percentage of your daily energy needs could it provide?"),
        ("Scaling Problem", "Organisms from bacteria to human scale", "At what body size do you predict photosynthesis becomes insufficient to provide all needed energy?")
    ],
    "discoveries": [
        "Photosynthesis is remarkably inefficient at converting sunlight to chemical energy — only about 1-2% of incoming solar energy ends up stored in glucose molecules",
        "A photosynthetic human would produce only about 60-100 kcal per day from their skin surface area — roughly 3-5% of the 2,000 kcal needed for survival",
        "The surface-area-to-volume ratio is the fundamental constraint — as organisms get larger, their energy needs (proportional to volume) grow much faster than their ability to capture light (proportional to surface area)",
        "Photosynthesis and cellular respiration are complementary reactions that cycle carbon between organisms and the atmosphere — the glucose and O2 produced by one are consumed by the other"
    ],
    "answer": "Humans can't photosynthesize for a simple mathematical reason: our bodies need far more energy than our skin could ever capture from sunlight. Photosynthesis converts only 1-2% of incoming solar energy to glucose. Even if your entire 1.7 m² body surface were covered in chlorophyll under maximum sunlight, you'd produce about 60-100 kcal per day — roughly one banana's worth. You need 2,000 kcal. The surface-area-to-volume ratio makes it impossible: as organisms get larger, their volume (which consumes energy) grows much faster than their surface area (which captures light). Plants solve this by being flat (leaves maximize surface area) and metabolically slow. Humans are compact and metabolically fast — the geometry simply doesn't work.",
    "stem_title": "Design a Bio-Solar Energy Harvesting System",
    "stem_mission": "Design a biological or bio-inspired system that captures solar energy more efficiently than natural photosynthesis and converts it to usable energy for human applications.",
    "stem_scenario": "A biotech startup is exploring bio-solar energy — using biological or bio-inspired systems to capture sunlight more efficiently than traditional solar panels. Natural photosynthesis is only 1-2% efficient, while silicon solar cells reach 20-25%. Your team must design a system that bridges this gap — either by improving biological photosynthesis through bioengineering or by creating bio-inspired artificial systems.",
    "stem_questions": [
        "Why is natural photosynthesis only 1-2% efficient, and which steps lose the most energy?",
        "What would it take to engineer a more efficient photosynthetic organism?",
        "How does your design compare to existing solar technology in terms of efficiency, cost, and sustainability?"
    ],
    "stem_design_qs": [
        "Will your system use living organisms, bio-inspired materials, or a hybrid approach?",
        "What specific bottleneck in photosynthesis does your design address?",
        "How will you convert the captured energy into a form usable for human applications?",
        "What are the scalability and environmental implications of your design?"
    ],
    "career": "Bioenergy Researchers develop biological and bio-inspired systems for energy capture and conversion, including artificial photosynthesis, algal biofuels, and bio-solar cells. They work at universities, national laboratories, and biotech companies, earning $65,000–$130,000/year. Metabolic Engineers who redesign biological pathways for energy and chemical production earn $80,000–$150,000/year.",
    "images": {
        "cover": ("G10L1-L10-cover.png", "A photorealistic, cinematic split image: left side shows a vibrant green leaf with visible cellular structure and chloroplasts glowing with captured sunlight, right side shows a human hand under the same sunlight with visible skin cells — both illuminated by golden light, artistic science visualization"),
        "landscape": ("G10L1-L10-landscape.png", "A diverse group of 15-16 year old students in a modern biology lab conducting photosynthesis experiments with aquatic plants in beakers, oxygen bubbles visible, light intensity meters and data collection equipment, engaged expressions"),
        "modeling": ("G10L1-L10-modeling.png", "A diverse group of 15-16 year old students working on laptops building computational models of energy flow in photosynthesis and cellular respiration, classroom with cell biology posters and energy cycle diagrams"),
        "discussion": ("G10L1-L10-discussion.png", "A teacher leading a discussion with diverse 15-16 year old students about energy flow in ecosystems, a photosynthesis and respiration comparison diagram displayed on a smartboard, students engaged in debate"),
        "stem": ("G10L1-L10-stem.png", "Diverse 15-16 year old students designing bio-solar energy systems on large whiteboards with cell diagrams, energy efficiency charts, and biochemical pathway maps, collaborative biotech design atmosphere")
    },
    "pre_assessment": [
        "Why do plants need sunlight to grow but humans don't?",
        "What do you think would happen if human skin contained chlorophyll — could we skip eating?",
        "Draw a diagram showing how energy flows from the sun through a plant and eventually to a human.",
        "What is the relationship between the food you eat and the energy your cells use?"
    ],
    "extend_components": [
        ("CO2 Concentration", "The amount of carbon dioxide available for the Calvin cycle reactions — increasing CO2 up to a saturation point increases glucose production, but beyond that point, other factors become limiting"),
        ("Leaf Area Index", "The total photosynthetic surface area relative to ground area — forests have LAI of 6-8 (many overlapping leaf layers), while a flat human has an LAI of about 0.4, severely limiting light capture"),
        ("Metabolic Efficiency", "The percentage of glucose energy that is successfully converted to ATP during cellular respiration — approximately 38-40% in aerobic conditions, with the remaining 60% lost as heat")
    ],
    "reflections": [
        "How does your model demonstrate why large animals cannot survive on photosynthesis alone?",
        "What does the surface-area-to-volume ratio teach us about why plants and animals evolved such different body plans?",
        "How are photosynthesis and cellular respiration complementary reactions that drive the global carbon cycle?",
        "If a biotech company engineered human skin with chlorophyll, would it solve world hunger? Use your model to evaluate.",
        "What are the limitations of modeling the energy balance with only five components?"
    ],
    "dimensions": [
        ("Science Practice", "Developing and Using Models", "Students develop computational models to illustrate the energy transformations in photosynthesis and cellular respiration and the cycling of carbon through biological and geological systems."),
        ("Disciplinary Core Idea", "LS1.C Organization for Matter and Energy Flow in Organisms / LS2.B Cycles of Matter and Energy Transfer in Ecosystems", "Cellular respiration breaks glucose bonds to release energy for cellular work. Photosynthesis and respiration together cycle carbon among the biosphere, atmosphere, and geosphere."),
        ("Crosscutting Concept", "Energy and Matter", "Students track energy flow from sunlight through photosynthesis to glucose to cellular respiration to ATP, accounting for energy losses at each step and understanding why the cycle is not 100% efficient.")
    ],
    "cast_items": [
        "Model the energy transformations in photosynthesis and cellular respiration as complementary processes",
        "Calculate the energy budget for a hypothetical photosynthetic organism and predict the maximum viable body size",
        "Illustrate the role of photosynthesis and respiration in cycling carbon through biosphere and atmosphere"
    ],
    "cast_questions": [
        ("Multiple Choice:", "If photosynthesis converts 1.5% of incoming solar energy to glucose and a human body has 1.7 m² of surface area receiving 500 W/m² of sunlight for 8 hours, how much glucose energy would a photosynthetic human produce per day?"),
        ("Constructed Response:", "Using your model, explain why humans cannot photosynthesize by addressing: (1) the efficiency of photosynthesis, (2) the surface-area-to-volume constraint, (3) the energy demands of cellular respiration in humans, and (4) the complementary relationship between photosynthesis and respiration in the carbon cycle.")
    ],
    "background_intro": "Plants and animals have a deal: plants capture sunlight and store it in glucose, then animals eat the plants and burn that glucose for energy. This partnership — photosynthesis and cellular respiration — is the engine that drives virtually all life on Earth. But why can't animals cut out the middleman and photosynthesize for themselves? The answer reveals deep truths about energy, geometry, and the evolution of life.",
    "background_sections": [
        ("The Efficiency Problem", "Photosynthesis captures only about 1-2% of incoming solar energy as chemical energy in glucose. Of the sunlight hitting a leaf, about 50% is the wrong wavelength (chlorophyll absorbs mainly red and blue), 20% is reflected or transmitted, and most of the remaining energy is lost as heat during the chemical reactions. The theoretical maximum efficiency of photosynthesis is about 11%, but real plants achieve 1-2% under field conditions. After billions of years of evolution, this is still the best biology can do."),
        ("The Surface-Area-to-Volume Problem", "Energy capture is proportional to surface area; energy consumption is proportional to volume. For a sphere, surface area scales as r² while volume scales as r³. This means larger organisms have proportionally less surface area relative to their energy needs. A single-celled alga can meet ALL its energy needs with photosynthesis. A tree needs enormous flat leaves but has very low metabolic rate per unit mass. A human has too little surface area and too high a metabolic rate — the geometry is impossible."),
        ("The Numbers", "Calculation: Maximum solar intensity at Earth's surface = 1,000 W/m². Average over a day (accounting for angle, weather, night) ≈ 250 W/m². Human surface area ≈ 1.7 m². Energy captured at 1.5% efficiency = 1.7 × 250 × 0.015 = 6.4 W = 5,500 kcal per day... but wait, that's watts of SOLAR energy. At 1.5% photosynthetic efficiency, usable glucose energy ≈ 60-100 kcal/day. A human needs 2,000 kcal/day. You'd need to be 20-30 times your current surface area to survive — you'd need to be a flat sheet about 6 meters across."),
        ("The Carbon Cycle Connection", "Photosynthesis and cellular respiration are mirror-image reactions: 6CO2 + 6H2O + light → C6H12O6 + 6O2 (photosynthesis) and C6H12O6 + 6O2 → 6CO2 + 6H2O + energy (respiration). Together, they cycle carbon between the atmosphere (as CO2) and the biosphere (as organic molecules). Every carbon atom in your body was once CO2 in the air, captured by a plant, and will return to CO2 when that molecule is respired. This cycle has maintained atmospheric CO2 balance for hundreds of millions of years — until humans started burning fossil fuels faster than photosynthesis can absorb them.")
    ],
    "lever_L": "Students identify sunlight intensity, chlorophyll concentration, glucose production rate, cellular respiration rate, and net energy output as the key components of the photosynthesis-respiration energy system.",
    "lever_E": "Students determine that sunlight and chlorophyll drive glucose production, but cellular respiration consumes glucose at a rate determined by body size and metabolic demand, and the net energy output determines whether an organism can survive on photosynthesis alone.",
    "lever_V": "Students build a computational model showing energy flow from sunlight through photosynthesis to glucose to cellular respiration, calculating net energy balance for organisms of different sizes.",
    "lever_Ev": "Students run optimal plant, photosynthetic human, and scaling problem scenarios to discover the surface-area-to-volume constraint and calculate why photosynthetic humans are mathematically impossible.",
    "lever_R": "Students add CO2 concentration, leaf area index, or metabolic efficiency to model more complete energy balance and carbon cycling dynamics.",
    "slides_guide": [
        {"num": "Slide 1", "title": "Cover", "visual": "Title slide with leaf and human comparison image", "say": "A leaf turns sunlight into food using nothing but water and air. Why can't you? Imagine never having to eat again — just stand in the sun.", "do": "Ask: If you could photosynthesize, would you? How much time in the sun would you need? Let students speculate.", "time": "2 min"},
        {"num": "Slide 2", "title": "Learning Objectives", "visual": "Learning goals and vocabulary", "say": "Today we're running the numbers on a wild idea — and discovering why evolution chose eating over photosynthesizing for animals.", "do": "Have students read objectives. Pre-teach 'photosynthesis' and 'cellular respiration' as mirror reactions.", "time": "3 min"},
        {"num": "Slide 3", "title": "Big Question", "visual": "Why can't humans skip eating and just use sunlight?", "say": "Plants do it. Some sea slugs do it. Some salamander embryos sort of do it. So what's stopping us?", "do": "Students write their best hypothesis for why humans can't photosynthesize. Collect for later revisiting.", "time": "3 min"},
        {"num": "Slide 4", "title": "LEVER Framework", "visual": "LEVER steps overview", "say": "We're building an energy budget model — calculating exactly how much energy photosynthesis could give a human versus how much a human needs.", "do": "Preview LEVER steps. Emphasize this is a QUANTITATIVE question — the answer is in the numbers.", "time": "2 min"},
        {"num": "Slide 5", "title": "Activity 1: Components", "visual": "Component cards for energy balance model", "say": "What factors determine whether an organism can survive on photosynthesis? Which ones can biology control?", "do": "Guide sorting. Sunlight and chlorophyll are the inputs; glucose production and respiration rate determine the balance.", "time": "8 min"},
        {"num": "Slide 6", "title": "Activity 2: Connections", "visual": "Energy flow diagram — sun to glucose to ATP", "say": "Sunlight hits chlorophyll. Chlorophyll makes glucose. Your cells burn glucose for ATP. But at EVERY step, energy is lost. How much?", "do": "Build the energy cascade: 1000 W/m² solar → ~15 W/m² captured → glucose → ATP → work. Each arrow loses energy.", "time": "8 min"},
        {"num": "Slide 7", "title": "Activity 3: Simulation", "visual": "Energy budget calculations for plant vs. human", "say": "Let's run the math. Cover your entire body with chlorophyll. Stand in the sun all day. How many calories do you produce?", "do": "Students calculate photosynthetic output for 1.7 m² at 1.5% efficiency. Compare to 2,000 kcal daily need. Watch the deficit.", "time": "10 min"},
        {"num": "Slide 8", "title": "Discoveries", "visual": "Key findings — the impossible energy budget", "say": "About 60-100 calories from photosynthesis. You need 2,000. You'd have to be a flat green sheet 6 meters across. Evolution chose eating for a reason.", "do": "Revisit initial hypotheses. Most students will not have guessed the surface-area-to-volume problem. Discuss body plan evolution.", "time": "5 min"},
        {"num": "Slide 9", "title": "STEM Challenge", "visual": "Bio-solar energy design challenge", "say": "Natural photosynthesis is only 1-2% efficient. Silicon solar cells hit 25%. Can we build something biological that does better?", "do": "Groups design bio-solar systems — improved organisms, artificial photosynthesis, or bio-inspired materials. Present and evaluate.", "time": "12 min"}
    ],
    "sort_reasoning": "Sunlight Intensity and Chlorophyll Concentration are external components because they represent environmental and biological inputs that can be varied — sunlight depends on location and conditions, and chlorophyll depends on the amount of photosynthetic pigment present. Glucose Production Rate, Cellular Respiration Rate, and Net Energy Output are internal because they are metabolic outcomes determined by the interaction of inputs with an organism's biochemistry and body plan.",
    "relationships": [
        ("Sunlight Intensity to Glucose Production Rate", "POSITIVE (+) up to saturation", "Higher sunlight intensity drives more photosynthetic reactions, increasing glucose production — but only up to a saturation point where the photosynthetic machinery is running at maximum capacity. Beyond this point, additional light cannot be used."),
        ("Chlorophyll Concentration to Glucose Production Rate", "POSITIVE (+)", "Higher chlorophyll concentration allows more light photons to be captured and channeled into the light-dependent reactions, increasing the overall rate of glucose production. This is why leaves are densely packed with chloroplasts."),
        ("Glucose Production Rate to Net Energy Output", "POSITIVE (+)", "More glucose produced by photosynthesis increases the net energy available. Net Energy Output = glucose energy from photosynthesis - glucose energy consumed by respiration. When production exceeds consumption, the organism grows; when consumption exceeds production, it starves.")
    ],
    "sim_answers": [
        ("Photosynthetic Human Scenario", "With 1.7 m² of surface area, 250 W/m² average solar intensity (accounting for day/night, weather, angle), and 1.5% photosynthetic efficiency, the model calculates approximately 60-100 kcal/day of glucose production. Cellular Respiration Rate for a human is approximately 2,000 kcal/day. Net Energy Output is approximately -1,900 to -1,940 kcal/day — a massive deficit. The photosynthetic human would need to eat nearly as much as a normal human. Photosynthesis provides less than 5% of energy needs."),
        ("Scaling Problem Scenario", "The model reveals a clear scaling threshold. Single-celled organisms (surface area ≈ volume) can fully meet energy needs with photosynthesis. Small multicellular organisms like moss survive on photosynthesis because they're thin and metabolically slow. Trees work because leaves are flat (maximizing surface area) and wood is mostly dead tissue (low respiration). But compact, active animals like humans have too little surface area for their metabolic volume. The crossover point — where respiration exceeds photosynthetic capacity — occurs at roughly millimeter-scale for organisms with human-like metabolic rates.")
    ],
    "reflection_exemplars": [
        ("Why is 1-2% efficiency the best evolution can do?", "Photosynthesis has had 3 billion years of evolutionary optimization and still only achieves 1-2% efficiency under field conditions. The losses occur at multiple steps: chlorophyll absorbs only ~45% of the solar spectrum (red and blue light), not all absorbed energy reaches the reaction centers, the Calvin cycle requires significant ATP investment, and photorespiration wastes ~25% of fixed carbon in C3 plants. These aren't engineering failures — they're physical and chemical constraints. The quantum efficiency of individual photosystems is actually quite high (~95% for photon capture), but overall system efficiency is limited by the cumulative losses across many steps."),
        ("What does this teach about plant vs. animal body plans?", "Plants evolved to maximize surface-area-to-volume ratio: flat leaves, branching architecture, slow metabolism per unit mass. Animals evolved for mobility, coordination, and high metabolic rate — all of which require compact body plans with low surface-area-to-volume ratios. These are fundamentally incompatible strategies for energy acquisition. You cannot simultaneously be optimized for catching sunlight (flat, spread out, immobile) and catching prey (compact, fast, mobile). Evolution explored both strategies and they diverged into two completely different kingdoms of life.")
    ],
    "stem_intro": "Present the challenge: A biotech startup wants to create bio-solar energy systems that outperform natural photosynthesis. Your team will design a system that addresses the bottlenecks in natural photosynthesis — whether by engineering improved organisms, creating artificial photosynthetic materials, or developing bio-inspired solar technology.",
    "stem_concepts": [
        ("Artificial Photosynthesis", "Scientists are developing systems that mimic photosynthesis using synthetic catalysts to split water and produce hydrogen fuel using sunlight. These systems aim to exceed the 1-2% efficiency of natural photosynthesis by optimizing each step independently — some prototypes have reached 10-22% efficiency."),
        ("Algal Biofuels", "Microalgae are the most efficient natural photosynthesizers, converting 3-8% of solar energy to biomass. Grown in bioreactors, they can produce oils for biodiesel, hydrogen gas, or feedstock for bioethanol. The challenge is scaling production while maintaining efficiency and managing costs."),
        ("Photorespiration and C4 Engineering", "In C3 plants, the enzyme RuBisCO sometimes fixes oxygen instead of CO2 (photorespiration), wasting up to 25% of captured energy. C4 plants evolved a CO2 concentration mechanism that minimizes this loss. Bioengineers are working to install C4 pathways in C3 crop plants like rice and wheat to increase yield by 25-50%.")
    ],
    "stem_eval": [
        ("Expert (4)", "Design identifies specific photosynthetic bottlenecks, proposes a scientifically sound improvement mechanism, includes efficiency targets with calculations, and addresses scalability and environmental impact"),
        ("Proficient (3)", "Design addresses a real limitation of natural photosynthesis with a reasonable bio-inspired solution and some efficiency analysis"),
        ("Developing (2)", "Design identifies a photosynthetic limitation but lacks specific improvement mechanisms or efficiency calculations"),
        ("Beginning (1)", "Design is incomplete or doesn't demonstrate understanding of photosynthesis and respiration energy balance")
    ],
    "support": [
        "Provide an energy loss diagram for photosynthesis showing where the 98-99% of incoming solar energy is lost at each step",
        "Use a body plan comparison chart showing surface-area-to-volume ratios for bacteria, moss, tree leaf, and human",
        "Sentence frames: 'Photosynthesis cannot power a human because __ m² of surface area at __% efficiency produces only __ kcal, while cellular respiration requires __ kcal per day'"
    ],
    "extensions": [
        "Research the sea slug Elysia chlorotica, which steals chloroplasts from algae and uses them for months — is this true photosynthesis? What limits prevent it from working in larger animals?",
        "Investigate the Spotted Salamander (Ambystoma maculatum), whose embryos contain symbiotic algae that provide oxygen and some glucose — is this a step toward animal photosynthesis?",
        "Calculate: How large would a flat, green human need to be to survive entirely on photosynthesis? Design the 'optimal photosynthetic human' body plan and explain why it would be terrible at everything else humans do."
    ],
    "cross_curr": [
        ("Math", "Calculate the complete energy budget: 1,000 W/m² × 1.7 m² × 8 hours × 0.015 efficiency = ? kcal. Convert watts to kcal using 1 W = 0.86 kcal/hr. Compare to the 2,000 kcal daily requirement. What surface area would you need?"),
        ("ELA", "Write a creative science fiction short story about a world where humans CAN photosynthesize. What would society, agriculture, economics, and culture look like? Ground your fiction in the real science of your model."),
        ("Environmental Science", "Research how human disruption of the carbon cycle (fossil fuel burning) exceeds the capacity of global photosynthesis to absorb CO2. Use your model to explain why planting trees alone cannot solve climate change.")
    ],
    "misconceptions": [
        ("Plants get their mass from soil", "This is one of the oldest misconceptions in biology, dating back to ancient Greece. In reality, the vast majority of a plant's dry mass comes from CO2 in the air, not minerals from soil. Photosynthesis fixes atmospheric carbon into glucose, which is then used to build cellulose, lignin, and all other organic molecules. A tree is literally made of air and water. Soil provides only mineral nutrients (nitrogen, phosphorus, potassium) that make up a tiny fraction of plant mass.", "Historical experiment: Jan Baptist van Helmont (1648) grew a willow tree in a pot, carefully weighing the soil before and after. The tree gained 74 kg; the soil lost only 57 grams. The mass came from water and CO2, not soil."),
        ("Photosynthesis and respiration are opposites that cancel out", "While the CHEMICAL equations are mirror images (one produces glucose + O2, the other consumes them), they serve completely different biological functions and occur in different organelles. Photosynthesis CAPTURES and STORES solar energy in chemical bonds. Respiration RELEASES that stored energy for cellular work. A plant does BOTH simultaneously — photosynthesis in chloroplasts and respiration in mitochondria. During the day, photosynthesis exceeds respiration (net O2 producer). At night, only respiration occurs (net CO2 producer).", "Demonstration: Place an aquatic plant in light (O2 bubbles appear — photosynthesis exceeds respiration) then move it to dark (bubbles stop — only respiration occurs, consuming O2). Both processes run continuously; the balance shifts with light."),
        ("If humans had chlorophyll, we wouldn't need to eat", "Even with perfect chlorophyll coverage, a human body's 1.7 m² surface area at 1.5% photosynthetic efficiency would produce only 60-100 kcal per day — roughly 3-5% of the 2,000 kcal daily requirement. The fundamental problem is geometry: our metabolic needs (proportional to body volume) vastly exceed our light-capture capacity (proportional to surface area). You would need to be a flat green sheet about 6 meters in diameter to survive on photosynthesis alone.", "Run the math live: 1,000 W/m² × 1.7 m² × 0.015 × 8 hours × 0.86 kcal/W·hr ≈ 87.7 kcal. That's one small banana. Students immediately see why this doesn't work for an organism that needs 2,000 kcal/day.")
    ]
}

ALL_LESSONS = [L01, L02, L03, L04, L05, L06, L07, L08, L09, L10]
