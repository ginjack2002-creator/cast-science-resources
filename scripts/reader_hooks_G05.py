#!/usr/bin/env python3
"""
Reader Hooks for Grade 5 Differentiated Readers
Each lesson has: scientist character (DIFFERENT from lesson slide careers),
spotlight topic (timeless, factual, non-divisive), extend_components for
the "What Else?" section, and a data source for the Data Detective activity.
"""

READER_HOOKS = {
    "G05-L01": {
        "scientist": {
            "name": "Dr. Keisha Williams",
            "title": "Fire Behavior Analyst",
            "workplace": "U.S. Forest Service, Predictive Services",
            "salary": "$80K-$125K/year",
            "education": "B.S. in Forestry or Environmental Science, M.S. in Fire Science",
            "what_they_model": "Where wildfires will spread next based on wind, moisture, and fuel load"
        },
        "additional_career": {
            "name": "Remote Sensing Technician",
            "description": "Uses satellite imagery and drones to map fire-prone areas and track active wildfires in real time.",
            "salary": "$55K-$90K/year",
            "education": "B.S. in Geography, GIS, or Environmental Technology"
        },
        "spotlight": {
            "title": "Yellowstone 1988: The Fire That Changed Everything We Knew",
            "narrative": "In the summer of 1988, Yellowstone National Park experienced the largest wildfire in its recorded history. Over 793,000 acres burned — nearly 36% of the entire park. Scientists had predicted the fires would burn out on their own, but dry conditions and strong winds created a firestorm that no model had anticipated. After the fires, researchers were astonished: within just one year, wildflowers bloomed across the burned landscape. Lodgepole pine cones, which need extreme heat to open, released millions of seeds. The fire didn't destroy the ecosystem — it reset it. Today, fire ecologists use Yellowstone 1988 as the foundation for understanding how fire is a natural part of healthy forests.",
            "discussion_prompt": "Why did scientists change their thinking about forest fires after Yellowstone 1988?"
        },
        "extend_components": [
            ("Fuel Moisture Content", "Dr. Williams checks this every morning — how much water is inside living and dead plants. Below 25%? Fire moves fast."),
            ("Topography (Slope)", "Fire races uphill. A 30-degree slope can double a fire's speed. Dr. Williams maps every hill and canyon."),
            ("Ember Transport", "Burning embers fly up to 2 miles ahead of the fire front. This is how fires jump highways and rivers.")
        ],
        "data": {
            "title": "California Wildfire Acres Burned (2015-2024)",
            "type": "table",
            "headers": ["Year", "Acres Burned", "Structures Destroyed"],
            "rows": [
                ["2015", "893,362", "3,075"],
                ["2017", "1,248,606", "10,280"],
                ["2018", "1,893,913", "24,226"],
                ["2020", "4,397,809", "10,488"],
                ["2021", "2,569,009", "3,629"],
                ["2023", "56,601", "214"]
            ],
            "prompts": [
                "What pattern do you notice in the acres burned over time?",
                "2023 had far fewer acres burned. What factors might explain this?",
                "If you were Dr. Williams, which year would you study most closely? Why?"
            ]
        }
    },

    "G05-L02": {
        "scientist": {
            "name": "Dr. Marcus Chen",
            "title": "Bioremediation Engineer",
            "workplace": "Environmental cleanup firm, Terranova Solutions",
            "salary": "$85K-$130K/year",
            "education": "B.S. in Environmental Engineering, M.S. in Microbiology",
            "what_they_model": "How fast contaminated soil breaks down different pollutants using decomposer organisms"
        },
        "additional_career": {
            "name": "Composting Systems Manager",
            "description": "Designs and operates large-scale composting facilities that turn city food waste into rich soil for farms and gardens.",
            "salary": "$50K-$80K/year",
            "education": "B.S. in Environmental Science or Agriculture"
        },
        "spotlight": {
            "title": "The Great Pacific Garbage Patch: Why Some Trash Never Decomposes",
            "narrative": "In the middle of the Pacific Ocean, there's a floating collection of trash twice the size of Texas. But it's not an island you can walk on — it's more like a plastic soup. Sunlight breaks plastic into tiny pieces called microplastics, but decomposers can't eat most plastic. A banana peel disappears in 2 weeks. A plastic bottle? Over 450 years. Dr. Marcus Chen's work shows that understanding what CAN decompose — and what can't — is the key to solving waste problems. His team is engineering bacteria that might one day be able to break down plastics the way fungi break down a fallen tree.",
            "discussion_prompt": "Why can decomposers break down a fallen tree but not a plastic bottle?"
        },
        "extend_components": [
            ("Temperature", "Decomposers slow down in cold — Dr. Chen factors this into every cleanup timeline"),
            ("Oxygen Level", "Underground contamination decomposes differently because there's less oxygen"),
            ("Material Type", "Plastic takes 450+ years; a banana peel takes 2 weeks — the model needs to know WHAT is decomposing")
        ],
        "data": {
            "title": "How Long Does It Take to Decompose?",
            "type": "table",
            "headers": ["Material", "Time to Decompose", "Can Decomposers Break It Down?"],
            "rows": [
                ["Banana peel", "2 weeks", "Yes — bacteria and fungi"],
                ["Newspaper", "6 weeks", "Yes — cellulose-eating bacteria"],
                ["Cotton shirt", "5 months", "Yes — slowly"],
                ["Leather shoe", "25-40 years", "Partially"],
                ["Aluminum can", "200 years", "No — must be recycled"],
                ["Plastic bottle", "450+ years", "No (not yet)"]
            ],
            "prompts": [
                "What do the items that decompose quickly have in common?",
                "Why do you think leather takes so much longer than cotton?",
                "If Dr. Chen could engineer bacteria to eat one material on this list, which should he choose? Why?"
            ]
        }
    },

    "G05-L03": {
        "scientist": {
            "name": "Dr. Amara Okafor",
            "title": "Bioenergy Systems Engineer",
            "workplace": "National Renewable Energy Laboratory (NREL)",
            "salary": "$90K-$140K/year",
            "education": "B.S. in Chemical Engineering, Ph.D. in Bioenergy",
            "what_they_model": "How to convert plant biomass into fuel by optimizing energy transfer from sunlight to usable energy"
        },
        "additional_career": {
            "name": "Greenhouse Operations Scientist",
            "description": "Manages controlled-environment agriculture, optimizing light, temperature, and CO2 to maximize plant growth and food production.",
            "salary": "$55K-$85K/year",
            "education": "B.S. in Horticulture or Plant Biology"
        },
        "spotlight": {
            "title": "The World's Deepest Cave Ecosystem: Life Without Sunlight",
            "narrative": "In Romania's Movile Cave, sealed off from sunlight for 5.5 million years, scientists found 48 species living in total darkness. How do they survive without the sun? Instead of photosynthesis, bacteria in the cave use chemical energy from hydrogen sulfide gas — a process called chemosynthesis. These bacteria are the base of the food chain, just like plants are above ground. Dr. Amara Okafor studies both systems because understanding ALL the ways energy enters an ecosystem helps her design better bioenergy systems. If bacteria can power a whole cave ecosystem from chemicals, what else might be possible?",
            "discussion_prompt": "How is chemosynthesis similar to and different from photosynthesis?"
        },
        "extend_components": [
            ("Water Availability", "Plants close their stomata when water is scarce, shutting down photosynthesis even if sunlight is abundant"),
            ("CO2 Concentration", "Dr. Okafor's lab increases CO2 levels to boost plant growth rates for biofuel crops"),
            ("Chlorophyll Health", "Diseased or nutrient-starved plants produce less chlorophyll, reducing their ability to capture light energy")
        ],
        "data": {
            "title": "Energy Transfer Efficiency in Nature",
            "type": "table",
            "headers": ["Energy Step", "Energy Available", "Efficiency"],
            "rows": [
                ["Sunlight hitting a leaf", "100%", "—"],
                ["Captured by photosynthesis", "1-2%", "1-2%"],
                ["Stored in plant as sugar", "0.5-1%", "~50% of captured"],
                ["Transferred to herbivore", "0.05-0.1%", "~10% of plant"],
                ["Transferred to carnivore", "0.005-0.01%", "~10% of herbivore"]
            ],
            "prompts": [
                "Why does so much energy get 'lost' at each step?",
                "Based on this data, why do ecosystems have more plants than herbivores, and more herbivores than carnivores?"
            ]
        }
    },

    "G05-L04": {
        "scientist": {
            "name": "Dr. Rafael Morales",
            "title": "Glacier Hydrologist",
            "workplace": "U.S. Geological Survey (USGS), Water Resources Division",
            "salary": "$75K-$115K/year",
            "education": "B.S. in Earth Science, M.S. in Hydrology",
            "what_they_model": "How snowpack and glacier melt timing affects downstream water supply for millions of people"
        },
        "additional_career": {
            "name": "Water Treatment Plant Operator",
            "description": "Monitors and operates the systems that clean and purify water before it reaches homes, schools, and businesses.",
            "salary": "$45K-$75K/year",
            "education": "Associate's degree + state certification"
        },
        "spotlight": {
            "title": "The Aral Sea: How an Entire Sea Disappeared",
            "narrative": "In 1960, the Aral Sea in Central Asia was one of the four largest lakes on Earth. Then the rivers feeding it were diverted for cotton farming. By 2014, the eastern section was completely dry. Fishing villages that once sat on the shoreline are now 60 miles from the nearest water. Dr. Rafael Morales uses the Aral Sea as a case study in his models because it shows exactly what happens when water inputs drop below water losses. The system doesn't slowly shrink — it collapses. Today, some restoration efforts are bringing water back to parts of the sea, but the ecosystem will never fully recover.",
            "discussion_prompt": "What would a model of the Aral Sea look like? What components and relationships would you include?"
        },
        "extend_components": [
            ("Snowpack Depth", "Dr. Morales measures mountain snowpack every winter — it's like a frozen water savings account for summer"),
            ("Groundwater Recharge Rate", "Underground aquifers refill slowly. If communities pump faster than they recharge, wells go dry"),
            ("Agricultural Demand", "Farms use 70% of all fresh water. During droughts, cities and farms compete for the same supply")
        ],
        "data": {
            "title": "Aral Sea Surface Area Over Time",
            "type": "table",
            "headers": ["Year", "Surface Area (sq km)", "% of Original"],
            "rows": [
                ["1960", "68,000", "100%"],
                ["1980", "55,700", "82%"],
                ["1990", "36,800", "54%"],
                ["2000", "25,500", "37%"],
                ["2007", "10,300", "15%"],
                ["2014", "7,300", "11%"]
            ],
            "prompts": [
                "Between which two decades did the Aral Sea shrink the fastest?",
                "If you graphed this data, what shape would the line make? Why isn't it a straight line?",
                "What would you predict for 2030 if nothing changed?"
            ]
        }
    },

    "G05-L05": {
        "scientist": {
            "name": "Dr. Priya Nair",
            "title": "Materials Characterization Scientist",
            "workplace": "3M Innovation Center",
            "salary": "$85K-$135K/year",
            "education": "B.S. in Chemistry, Ph.D. in Materials Science",
            "what_they_model": "How matter changes form during manufacturing — tracking every atom to ensure nothing is lost or wasted"
        },
        "additional_career": {
            "name": "Quality Control Chemist",
            "description": "Tests products during manufacturing to verify that the right amounts of materials are present — conservation of matter in action every day.",
            "salary": "$50K-$75K/year",
            "education": "B.S. in Chemistry or Chemical Engineering"
        },
        "spotlight": {
            "title": "The Mystery of the Shrinking Candle: Where Does the Wax Go?",
            "narrative": "Light a candle and watch it for an hour. The wax gets shorter. The wick gets shorter. But where does the mass go? It seems to vanish into thin air — and that's exactly right. The wax melts, then vaporizes, then combusts. The carbon and hydrogen atoms in the wax combine with oxygen in the air to form carbon dioxide (CO2) and water vapor (H2O). If you could capture every molecule of gas and water leaving the candle and weigh it all, plus the remaining wax and ash, the total mass would be exactly the same as what you started with. Dr. Priya Nair uses this exact principle every day: in her lab, she tracks atoms through manufacturing processes to eliminate waste.",
            "discussion_prompt": "If mass is always conserved, why does a burning log seem to weigh less when it turns to ash?"
        },
        "extend_components": [
            ("Gas Production", "Dr. Nair tracks invisible gases like CO2 produced during reactions — mass doesn't disappear, it changes form"),
            ("Reaction Speed", "Temperature affects how fast matter changes form, but the total mass before and after stays the same"),
            ("Surface Area", "Crushing a sugar cube makes it dissolve faster, but the mass of sugar doesn't change")
        ],
        "data": {
            "title": "Mass Before and After: Tracking Matter Through Changes",
            "type": "table",
            "headers": ["Change", "Starting Mass", "Ending Mass (visible)", "\"Missing\" Mass", "Where It Went"],
            "rows": [
                ["Ice melting", "100g", "100g", "0g", "Still there as liquid"],
                ["Sugar dissolving", "10g sugar + 200g water", "210g solution", "0g", "Sugar is in the water"],
                ["Wood burning", "500g log", "50g ash", "450g", "CO2 + water vapor in the air"],
                ["Baking soda + vinegar", "50g total", "50g total", "0g (in closed system)", "CO2 gas trapped in container"]
            ],
            "prompts": [
                "Which change LOOKS like matter disappeared but actually didn't?",
                "Why does a closed container show zero 'missing' mass for baking soda + vinegar?",
                "Design an experiment to prove that the 'missing' mass from a burning log still exists."
            ]
        }
    },

    "G05-L06": {
        "scientist": {
            "name": "Dr. Tomoko Hashimoto",
            "title": "Forest Carbon Scientist",
            "workplace": "NASA Jet Propulsion Laboratory (JPL)",
            "salary": "$95K-$150K/year",
            "education": "B.S. in Ecology, Ph.D. in Earth System Science",
            "what_they_model": "How much carbon dioxide forests absorb from the atmosphere and convert into wood, leaves, and roots"
        },
        "additional_career": {
            "name": "Arborist (Tree Care Specialist)",
            "description": "Diagnoses tree health, manages urban forests, and ensures trees have the conditions they need to grow and absorb carbon.",
            "salary": "$40K-$65K/year",
            "education": "Associate's or B.S. in Forestry, Arboriculture, or Horticulture"
        },
        "spotlight": {
            "title": "Van Helmont's Willow Tree: The Experiment That Baffled Scientists for 350 Years",
            "narrative": "In 1648, a Belgian scientist named Jan Baptist van Helmont planted a 5-pound willow tree in a pot with exactly 200 pounds of dried soil. For five years, he added nothing but water. When he pulled the tree out, it weighed 169 pounds — but the soil had lost only 2 ounces. Where did 164 pounds of tree come from? Van Helmont guessed it was from the water. He was wrong. It took scientists another 200 years to figure out that most of a tree's mass comes from carbon dioxide in the air. Trees are literally made of air. Dr. Tomoko Hashimoto uses satellites to measure this process across every forest on Earth.",
            "discussion_prompt": "Why was Van Helmont's experiment brilliant even though his conclusion was wrong?"
        },
        "extend_components": [
            ("Root Biomass", "Dr. Hashimoto estimates that 20-30% of a tree's total mass is underground — roots that nobody sees"),
            ("Seasonal Growth Rate", "Trees grow faster in spring/summer when days are longer, capturing more CO2 during these months"),
            ("Leaf Surface Area", "More leaves = more photosynthesis. Dr. Hashimoto's satellites measure 'leaf area index' from space")
        ],
        "data": {
            "title": "Where Does a 1,000 kg Tree's Mass Come From?",
            "type": "table",
            "headers": ["Source", "Mass Contribution", "Percentage"],
            "rows": [
                ["Carbon from CO2 in air", "450 kg", "45%"],
                ["Oxygen from CO2 in air", "400 kg", "40%"],
                ["Hydrogen from water", "60 kg", "6%"],
                ["Oxygen from water", "60 kg", "6%"],
                ["Minerals from soil", "30 kg", "3%"]
            ],
            "prompts": [
                "What percentage of a tree's mass comes from the AIR vs. from the SOIL?",
                "Why do most people guess 'soil' when asked where trees get their mass?",
                "If CO2 levels in the atmosphere increase, what might happen to tree growth? Why?"
            ]
        }
    },

    "G05-L07": {
        "scientist": {
            "name": "Dr. Jabari Osei",
            "title": "Soil Microbiome Researcher",
            "workplace": "Smithsonian Tropical Research Institute, Panama",
            "salary": "$70K-$110K/year",
            "education": "B.S. in Biology, Ph.D. in Microbial Ecology",
            "what_they_model": "How mycorrhizal fungi networks distribute nutrients between trees and what controls network health"
        },
        "additional_career": {
            "name": "Mushroom Cultivation Specialist",
            "description": "Grows edible and medicinal mushrooms by recreating the conditions fungi need to thrive — applying the same science from the forest to a farm.",
            "salary": "$40K-$70K/year",
            "education": "B.S. in Biology, Agriculture, or self-taught with certification"
        },
        "spotlight": {
            "title": "The Mother Tree: How One Tree Feeds an Entire Forest",
            "narrative": "In the forests of British Columbia, ecologist Dr. Suzanne Simard discovered something remarkable: the oldest, largest trees in a forest — she calls them 'Mother Trees' — send extra sugar through fungal networks to younger trees growing in the shade. They even send MORE sugar to their own offspring. When a Mother Tree is dying, it dumps its remaining carbon into the network, feeding its neighbors one last time. Dr. Jabari Osei studies similar networks in tropical forests, where a single tree can be connected to hundreds of neighbors through miles of fungal threads thinner than a human hair.",
            "discussion_prompt": "Why would a Mother Tree 'choose' to share food with other trees instead of keeping it all?"
        },
        "extend_components": [
            ("Network Age", "Dr. Osei has found that older networks transfer nutrients more efficiently — a 100-year-old network outperforms a 10-year-old one"),
            ("Fungal Species Diversity", "Forests with more fungal species have more resilient networks. If one species dies, others can take over"),
            ("Phosphorus Availability", "Fungi are especially important for delivering phosphorus to trees — roots alone can't absorb enough")
        ],
        "data": {
            "title": "Mycorrhizal Network Connections in a Forest Plot",
            "type": "table",
            "headers": ["Tree Type", "Age (years)", "Fungal Connections", "Sugar Shared (g/day)"],
            "rows": [
                ["Mother Douglas Fir", "250", "47 other trees", "12.5"],
                ["Adult Douglas Fir", "80", "22 other trees", "4.8"],
                ["Young Douglas Fir", "15", "8 other trees", "0.3 (receives 3.2)"],
                ["Seedling", "2", "3 other trees", "0 (receives 1.8)"],
                ["Paper Birch", "60", "19 other trees", "2.1 (cross-species)"]
            ],
            "prompts": [
                "Which tree shares the most sugar? Which receives the most?",
                "Why might it benefit the Mother Tree to keep seedlings alive?",
                "The Paper Birch is a completely different species. What does its connection tell you about the network?"
            ]
        }
    },

    "G05-L08": {
        "scientist": {
            "name": "Dr. Fatima Al-Rashid",
            "title": "Antimicrobial Surfaces Engineer",
            "workplace": "Johns Hopkins Applied Physics Laboratory",
            "salary": "$90K-$140K/year",
            "education": "B.S. in Biomedical Engineering, Ph.D. in Surface Chemistry",
            "what_they_model": "How antimicrobial coatings on surfaces destroy bacteria and viruses on contact, and how to make surfaces self-cleaning"
        },
        "additional_career": {
            "name": "Infection Prevention Specialist",
            "description": "Works in hospitals to design handwashing protocols and monitor how well soap and sanitizer reduce infection rates.",
            "salary": "$55K-$90K/year",
            "education": "B.S. in Nursing or Public Health + certification"
        },
        "spotlight": {
            "title": "The Doctor Who Proved Handwashing Saves Lives — And Was Ignored",
            "narrative": "In 1847, Dr. Ignaz Semmelweis noticed that women in his hospital ward were dying at five times the rate of women in another ward. The only difference? His ward was staffed by doctors who came straight from performing autopsies — without washing their hands. When Semmelweis required handwashing with chlorine solution, death rates dropped from 18% to under 2%. But other doctors were offended by the suggestion that their hands were dirty. They rejected his findings, and Semmelweis lost his job. It took another 20 years — and the germ theory work of Louis Pasteur and Joseph Lister — before the medical world finally accepted that handwashing saves lives.",
            "discussion_prompt": "Why did doctors reject Semmelweis's evidence even though the data clearly showed handwashing worked?"
        },
        "extend_components": [
            ("Water Temperature", "Dr. Al-Rashid found that warm water helps soap work faster by increasing molecular movement — but even cold water works with enough time"),
            ("Scrubbing Friction", "Physical scrubbing helps soap reach virus particles trapped in skin folds and under fingernails"),
            ("Viral Load", "The number of virus particles on your hands determines how much soap and time you need — more viruses means more washing time")
        ],
        "data": {
            "title": "Virus Survival After Handwashing Methods",
            "type": "table",
            "headers": ["Method", "Time", "% Viruses Remaining"],
            "rows": [
                ["No washing", "0 sec", "100%"],
                ["Water only", "20 sec", "65%"],
                ["Soap + water", "5 sec", "40%"],
                ["Soap + water", "10 sec", "15%"],
                ["Soap + water", "20 sec", "0.1%"],
                ["Hand sanitizer (60% alcohol)", "20 sec", "1%"]
            ],
            "prompts": [
                "How much more effective is 20 seconds of soap vs. 5 seconds of soap?",
                "Why does water alone still remove some viruses?",
                "Based on this data, why do health experts recommend 20 seconds — not 10?"
            ]
        }
    },

    "G05-L09": {
        "scientist": {
            "name": "Dr. James Whitehorse",
            "title": "Atmospheric Dispersion Modeler",
            "workplace": "National Oceanic and Atmospheric Administration (NOAA)",
            "salary": "$80K-$125K/year",
            "education": "B.S. in Atmospheric Science, M.S. in Environmental Modeling",
            "what_they_model": "How air pollutants move through cities based on wind patterns, building heights, and emission sources"
        },
        "additional_career": {
            "name": "Air Quality Monitoring Technician",
            "description": "Installs and maintains sensors that measure pollution levels in real time, providing data communities use to protect their health.",
            "salary": "$40K-$65K/year",
            "education": "Associate's degree in Environmental Technology"
        },
        "spotlight": {
            "title": "The Great Smog of London: The Fog That Killed 12,000 People",
            "narrative": "In December 1952, London experienced five days of fog so thick you couldn't see your own feet. But it wasn't ordinary fog — it was a deadly mix of coal smoke, vehicle exhaust, and cold air that trapped pollution close to the ground. Visibility dropped to one foot. People got lost in their own neighborhoods. Over 12,000 people died from breathing the toxic air, mostly the elderly and those with lung conditions. The disaster led to the world's first Clean Air Act in 1956. Dr. James Whitehorse studies events like this to build models that predict when pollution will get trapped — so cities can issue warnings before it becomes dangerous.",
            "discussion_prompt": "What conditions created the 'perfect storm' that trapped pollution in London? How is this similar to your air quality model?"
        },
        "extend_components": [
            ("Temperature Inversion", "Dr. Whitehorse watches for these — when warm air sits on top of cold air, it acts like a lid, trapping pollution near the ground"),
            ("Building Height/Density", "Tall buildings in cities can block wind and create 'street canyons' where pollution concentrates"),
            ("Time of Day", "Morning rush hour + cold air + no wind = worst air quality. Dr. Whitehorse's models predict this down to the hour")
        ],
        "data": {
            "title": "Air Quality Index (AQI) by Distance from Highway",
            "type": "table",
            "headers": ["Distance from Highway", "Average AQI", "Health Category"],
            "rows": [
                ["0-100 meters", "142", "Unhealthy for Sensitive Groups"],
                ["100-200 meters", "108", "Unhealthy for Sensitive Groups"],
                ["200-500 meters", "78", "Moderate"],
                ["500-1000 meters", "52", "Moderate"],
                ["1000+ meters", "35", "Good"]
            ],
            "prompts": [
                "How does AQI change as you move farther from the highway?",
                "At what distance does the air quality become 'Good'?",
                "If you were planning where to build a school, what would this data tell you?"
            ]
        }
    },

    "G05-L10": {
        "scientist": {
            "name": "Dr. Aisha Patel",
            "title": "Exoplanet Characterization Scientist",
            "workplace": "NASA Goddard Space Flight Center",
            "salary": "$95K-$155K/year",
            "education": "B.S. in Physics, Ph.D. in Planetary Science",
            "what_they_model": "How to determine the size, temperature, and atmosphere of planets orbiting distant stars — using only the light that reaches us"
        },
        "additional_career": {
            "name": "Planetarium Educator",
            "description": "Designs and presents immersive shows that teach people about stars, light, and the universe using dome projections and real NASA data.",
            "salary": "$40K-$65K/year",
            "education": "B.S. in Astronomy, Physics, or Science Education"
        },
        "spotlight": {
            "title": "Hubble Deep Field: The Photo That Changed How We See the Universe",
            "narrative": "In 1995, astronomer Robert Williams pointed the Hubble Space Telescope at the emptiest, darkest patch of sky anyone could find — a spot no bigger than a grain of sand held at arm's length. Other scientists thought it was a waste of telescope time. After 10 days of exposure, the image revealed over 3,000 galaxies, each containing billions of stars. Some of these galaxies were so far away that their light had been traveling for over 12 billion years. Dr. Aisha Patel studies light from distant stars to find planets orbiting them — planets that might have conditions similar to Earth. Every photon she captures is a message from the past.",
            "discussion_prompt": "When we look at a galaxy 12 billion light-years away, we see it as it was 12 billion years ago. Why is that both amazing and limiting for scientists?"
        },
        "extend_components": [
            ("Star Color/Temperature", "Dr. Patel reads a star's temperature from its color — blue stars are hottest (30,000°C), red stars coolest (3,000°C)"),
            ("Interstellar Dust", "Dust between stars dims and reddens light. Dr. Patel must subtract this 'dust effect' to measure true brightness"),
            ("Star Age", "Young stars burn brighter. As stars age, their luminosity changes — Dr. Patel's models account for this")
        ],
        "data": {
            "title": "How Long Does Light Take to Reach Earth?",
            "type": "table",
            "headers": ["Light Source", "Distance", "Travel Time"],
            "rows": [
                ["The Sun", "93 million miles", "8 minutes 20 seconds"],
                ["The Moon (reflected)", "238,900 miles", "1.3 seconds"],
                ["Proxima Centauri (nearest star)", "4.24 light-years", "4 years 3 months"],
                ["Sirius (brightest star)", "8.6 light-years", "8 years 7 months"],
                ["Betelgeuse", "700 light-years", "700 years"],
                ["Andromeda Galaxy", "2.5 million light-years", "2.5 million years"]
            ],
            "prompts": [
                "If Betelgeuse exploded right now, when would we see it?",
                "The light from Andromeda left before humans existed. What does that tell you about the scale of the universe?",
                "Why does Dr. Patel say she's 'looking back in time' when she studies distant stars?"
            ]
        }
    }
}
