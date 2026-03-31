#!/usr/bin/env python3
"""
Reader Hooks for Level 2 Differentiated Readers (Grades 4-8)
Each lesson has: scientist character (DIFFERENT from lesson slide careers),
spotlight topic (timeless, factual, non-divisive), extend_components for
the "What Else?" section, and a data source for the Data Detective activity.

35 lessons total: G04L2-L01 through G08L2-L07
"""

READER_HOOKS_L2 = {

    # =========================================================================
    # GRADE 4 LEVEL 2 (7 lessons)
    # =========================================================================

    "G04L2-L01": {
        # The Energy Roller Coaster: Where Does Speed Come From?
        "scientist": {
            "name": "Dr. Mei-Ling Huang",
            "title": "Roller Coaster Dynamics Engineer",
            "workplace": "Walt Disney Imagineering, R&D Division",
            "salary": "$95K-$145K/year",
            "education": "B.S. in Mechanical Engineering, M.S. in Vehicle Dynamics",
            "what_they_model": "How energy transforms between potential, kinetic, and thermal forms on every ride — ensuring thrills without danger"
        },
        "additional_career": {
            "name": "Energy Auditor",
            "description": "Inspects buildings and machines to find where energy is being wasted as heat from friction, then recommends fixes to save money and reduce waste.",
            "salary": "$50K-$80K/year",
            "education": "B.S. in Energy Engineering or Environmental Science"
        },
        "spotlight": {
            "title": "The Steel Phantom: The Coaster That Terrified Its Own Engineers",
            "narrative": "In 1991, Kennywood Park in Pittsburgh opened the Steel Phantom, which held the record for the longest and steepest drop of any roller coaster in the world — a 225-foot plunge that converted massive potential energy into terrifying kinetic energy. But engineers hadn't fully accounted for friction and vibration at the bottom of the drop. Riders experienced forces so intense that some blacked out. The coaster had to be redesigned to add friction brakes and smoother curves that converted energy more gradually. Today, every coaster is modeled on computers first, calculating exactly how much energy transforms at every point on the track.",
            "discussion_prompt": "Why did the Steel Phantom's engineers need to ADD friction to the ride instead of removing it?"
        },
        "extend_components": [
            ("Air Resistance", "Dr. Huang measures how air pushing against the coaster car steals kinetic energy at high speeds — faster cars lose more energy to drag"),
            ("Coaster Mass", "A fully loaded coaster car weighs more than an empty one, which means more potential energy at the top but also more friction at every contact point"),
            ("Loop Radius", "Tighter loops require more kinetic energy to complete — if friction has stolen too much energy, the coaster won't make it around")
        ],
        "data": {
            "title": "Energy at Different Points on a Roller Coaster Track",
            "type": "table",
            "headers": ["Track Position", "Height (m)", "Speed (m/s)", "Potential Energy (%)", "Kinetic Energy (%)", "Heat Loss (%)"],
            "rows": [
                ["Top of first hill", "50", "0", "95%", "0%", "5%"],
                ["Bottom of first drop", "2", "31", "4%", "88%", "8%"],
                ["Top of second hill", "30", "18", "57%", "30%", "13%"],
                ["Bottom of second drop", "2", "28", "4%", "76%", "20%"],
                ["End of ride (brakes)", "2", "5", "4%", "3%", "93%"]
            ],
            "prompts": [
                "What happens to heat loss as the coaster moves through the track?",
                "Why is the coaster slower at the bottom of the second drop than the first?",
                "If you added up PE + KE + Heat Loss at every row, what would you get? Why?"
            ]
        }
    },

    "G04L2-L02": {
        # Can Sound Travel Through Space?
        "scientist": {
            "name": "Dr. James Carter",
            "title": "Acoustic Engineer",
            "workplace": "Bose Corporation, Research Division",
            "salary": "$85K-$130K/year",
            "education": "B.S. in Physics, M.S. in Acoustical Engineering",
            "what_they_model": "How sound waves behave in different materials — from concert halls to noise-canceling headphones"
        },
        "additional_career": {
            "name": "Audiologist",
            "description": "Tests people's hearing and designs solutions for hearing loss, understanding how sound waves interact with the delicate structures of the human ear.",
            "salary": "$60K-$95K/year",
            "education": "Doctorate of Audiology (Au.D.)"
        },
        "spotlight": {
            "title": "The Bell Jar Experiment: Proving That Space Is Silent",
            "narrative": "In 1660, scientist Robert Boyle placed a ticking watch inside a glass jar and slowly pumped out the air. As the air disappeared, the ticking got quieter and quieter until — silence. The watch was still ticking, but with no air molecules to carry the vibrations, no sound could reach the listener. This simple experiment proved what scientists had suspected: sound needs a medium to travel. In space, where there is no air, no water, and no solid material, sound cannot travel at all. When astronauts work outside the International Space Station, they communicate by radio waves — which are electromagnetic, not sound — because even shouting into space produces absolute silence.",
            "discussion_prompt": "If sound can't travel through space, how do astronauts communicate during spacewalks?"
        },
        "extend_components": [
            ("Material Elasticity", "Dr. Carter tests how 'springy' a material is — elastic materials like steel transmit sound faster because molecules bounce back quickly"),
            ("Sound Frequency", "High-pitched sounds are absorbed faster than low-pitched sounds, which is why you can hear bass through walls but not treble"),
            ("Distance from Source", "Sound energy spreads out in all directions, so loudness decreases with the square of the distance — twice as far means one-quarter the volume")
        ],
        "data": {
            "title": "Speed of Sound in Different Materials",
            "type": "table",
            "headers": ["Material", "Density", "Speed of Sound (m/s)", "Can You Hear Through It?"],
            "rows": [
                ["Vacuum (space)", "None", "0", "No — no molecules"],
                ["Air (20°C)", "Low", "343", "Yes — normal hearing"],
                ["Water", "Medium", "1,482", "Yes — 4x faster than air"],
                ["Wood", "Medium-High", "3,850", "Yes — press ear to desk"],
                ["Steel", "High", "5,960", "Yes — 17x faster than air"],
                ["Diamond", "Very High", "12,000", "Yes — fastest known"]
            ],
            "prompts": [
                "What pattern do you notice between density and the speed of sound?",
                "Why does sound travel fastest in diamond and not at all in a vacuum?",
                "A train is coming from far away. Would you hear it sooner by pressing your ear to the rail or listening through the air? Why?"
            ]
        }
    },

    "G04L2-L03": {
        # Why Do Some Animals Survive Winter?
        "scientist": {
            "name": "Dr. Rosa Gutierrez",
            "title": "Wildlife Thermoregulation Biologist",
            "workplace": "University of Alaska Fairbanks, Institute of Arctic Biology",
            "salary": "$70K-$110K/year",
            "education": "B.S. in Wildlife Biology, Ph.D. in Physiological Ecology",
            "what_they_model": "How Arctic animals regulate body temperature and energy use to survive months of extreme cold and darkness"
        },
        "additional_career": {
            "name": "Zookeeper (Cold Climate Specialist)",
            "description": "Cares for arctic and subarctic animals in zoos, creating habitats that match the temperature and food conditions these animals need to stay healthy.",
            "salary": "$35K-$55K/year",
            "education": "B.S. in Zoology or Animal Science"
        },
        "spotlight": {
            "title": "The Wood Frog: The Animal That Freezes Solid and Comes Back to Life",
            "narrative": "Every winter in Alaska, wood frogs do something that seems impossible: they freeze solid. Their hearts stop beating, their blood stops flowing, and ice crystals form between their cells. To any observer, the frog is dead. But the wood frog has a secret weapon — it floods its cells with glucose (sugar), which acts like antifreeze and prevents the ice from destroying the cells from the inside. When spring arrives and temperatures rise, the frog's heart restarts, its blood begins flowing again, and it hops away as if nothing happened. Dr. Rosa Gutierrez studies this process because understanding how the frog survives freezing could help doctors preserve human organs for transplant.",
            "discussion_prompt": "How is the wood frog's glucose strategy similar to how humans use antifreeze in car radiators?"
        },
        "extend_components": [
            ("Hibernation Depth", "Dr. Gutierrez monitors how deeply animals slow their metabolism — some bears reduce their heart rate from 40 beats per minute to just 8"),
            ("Day Length", "Many animals use shortening days as a signal to start building fat stores and growing thicker fur weeks before the cold arrives"),
            ("Social Huddling", "Emperor penguins rotate positions in a huddle of thousands, sharing body heat so the group loses 50% less energy than individuals alone")
        ],
        "data": {
            "title": "Winter Survival Strategies Across Species",
            "type": "table",
            "headers": ["Animal", "Strategy", "Body Temp in Winter", "Metabolic Rate Reduction", "Survival Rate"],
            "rows": [
                ["Arctic Fox", "Thick fur + fat", "38°C (normal)", "0% — stays active", "92%"],
                ["Black Bear", "Hibernation", "31°C (mild drop)", "75% reduction", "95%"],
                ["Ground Squirrel", "Deep hibernation", "2°C (near freezing)", "98% reduction", "88%"],
                ["Wood Frog", "Freeze tolerance", "−3°C (frozen!)", "100% (heart stops)", "65%"],
                ["Monarch Butterfly", "Migration", "N/A — leaves cold", "Moderate (in flight)", "~10% reach destination"]
            ],
            "prompts": [
                "Which strategy reduces metabolic rate the most? Which reduces it the least?",
                "The monarch butterfly has the lowest survival rate. Why might migration still be a successful strategy for the species?",
                "If you could combine two strategies, which two would you pick and why?"
            ]
        }
    },

    "G04L2-L04": {
        # The Mountain That Used to Be an Ocean
        "scientist": {
            "name": "Dr. Kwame Asante",
            "title": "Paleontologist and Stratigrapher",
            "workplace": "Smithsonian National Museum of Natural History",
            "salary": "$75K-$120K/year",
            "education": "B.S. in Geology, Ph.D. in Paleontology",
            "what_they_model": "How ancient ocean fossils ended up thousands of meters above sea level by tracing the history of tectonic plate movements"
        },
        "additional_career": {
            "name": "Geotechnical Driller",
            "description": "Drills deep into rock layers to collect core samples that reveal millions of years of Earth's history — each layer telling a different story.",
            "salary": "$45K-$75K/year",
            "education": "Associate's degree in Drilling Technology or Geology"
        },
        "spotlight": {
            "title": "Seashells on Mount Everest: The Ocean Floor That Became the Roof of the World",
            "narrative": "At the summit of Mount Everest, 8,849 meters above sea level, climbers have found limestone packed with the fossils of ancient sea creatures called crinoids. These animals lived on the floor of the Tethys Sea approximately 450 million years ago. When the Indian tectonic plate began crashing into the Eurasian plate about 50 million years ago, the ocean floor between them was slowly squeezed upward like toothpaste from a tube. The Himalayas are still rising today — about 1 centimeter per year — because the plates are still pushing together. Dr. Kwame Asante uses these fossils to calculate exactly when and how fast the mountains rose.",
            "discussion_prompt": "If the Himalayas are still growing 1 cm per year, how much taller will they be in 1,000 years? In 1 million years? Why might they not actually get that tall?"
        },
        "extend_components": [
            ("Erosion Rate", "Dr. Asante factors in how rain, wind, and ice wear mountains down — the Himalayas grow 1 cm per year but erode almost as fast"),
            ("Sediment Thickness", "Thicker ocean floor sediment creates thicker mountain layers — Dr. Asante measures sediment depth to predict mountain structure"),
            ("Plate Angle", "Plates that collide head-on build taller mountains than plates that slide at an angle — the collision geometry matters")
        ],
        "data": {
            "title": "Fossils Found at Different Elevations",
            "type": "table",
            "headers": ["Location", "Elevation", "Fossil Found", "Original Environment", "Age (millions of years)"],
            "rows": [
                ["Mount Everest summit", "8,849 m", "Crinoid sea lilies", "Shallow ocean floor", "450"],
                ["Rocky Mountains, CO", "4,200 m", "Ammonite shells", "Deep ocean", "70"],
                ["Appalachian Mtns, WV", "1,200 m", "Coral reef fossils", "Tropical reef", "350"],
                ["Swiss Alps", "3,500 m", "Fish skeletons", "Ocean basin", "200"],
                ["Andes Mountains, Peru", "5,000 m", "Whale bone fragments", "Open ocean", "15"]
            ],
            "prompts": [
                "What do all of these mountain fossils have in common about their original environment?",
                "The Andes whale bones are only 15 million years old while the Everest fossils are 450 million years old. What does this tell you about when these mountains formed?",
                "If you found a fish fossil at 2,000 meters elevation, what could you conclude about the land's history?"
            ]
        }
    },

    "G04L2-L05": {
        # Can We Power a City with Wind?
        "scientist": {
            "name": "Dr. Sarah Mitchell",
            "title": "Wind Resource Assessment Engineer",
            "workplace": "National Renewable Energy Laboratory (NREL)",
            "salary": "$85K-$135K/year",
            "education": "B.S. in Meteorology, M.S. in Renewable Energy Engineering",
            "what_they_model": "Where to place wind farms by predicting wind speed patterns across landscapes using terrain, weather, and atmospheric data"
        },
        "additional_career": {
            "name": "Wind Turbine Technician",
            "description": "Climbs 300-foot wind turbines to maintain generators, replace parts, and ensure each turbine captures maximum wind energy safely.",
            "salary": "$50K-$80K/year",
            "education": "Associate's degree in Wind Energy Technology"
        },
        "spotlight": {
            "title": "Block Island: The First Offshore Wind Farm in America",
            "narrative": "In 2016, five massive wind turbines began spinning three miles off the coast of Block Island, Rhode Island, creating America's first offshore wind farm. Before the turbines, Block Island relied entirely on diesel generators shipped from the mainland, paying some of the highest electricity rates in the country. Now, the five turbines generate enough electricity to power the entire island with clean energy. On calm days, an undersea cable connects the island to the mainland grid for backup power. The project proved that offshore winds — which blow stronger and more consistently than onshore winds — could reliably power communities. Dr. Sarah Mitchell's models predicted the wind patterns that made this location ideal.",
            "discussion_prompt": "Why are offshore winds stronger and more reliable than onshore winds? Think about what slows wind down on land."
        },
        "extend_components": [
            ("Turbine Height", "Dr. Mitchell knows that wind speeds increase with height — a turbine at 100 meters catches 25% more wind than one at 50 meters"),
            ("Energy Storage Capacity", "Batteries store excess wind energy for calm days, but current batteries can only hold a few hours of city power"),
            ("Grid Interconnection", "Connecting wind farms to the power grid requires transformers and transmission lines that can handle fluctuating supply")
        ],
        "data": {
            "title": "Wind Farm Performance Data by Location",
            "type": "table",
            "headers": ["Wind Farm", "Location", "Avg Wind Speed (mph)", "Turbines", "Homes Powered", "Capacity Factor"],
            "rows": [
                ["Block Island", "Rhode Island (offshore)", "22", "5", "17,000", "48%"],
                ["Alta Wind Center", "California (mountain pass)", "19", "586", "450,000", "32%"],
                ["Shepherds Flat", "Oregon (plateau)", "17", "338", "235,000", "28%"],
                ["Roscoe Wind Farm", "Texas (plains)", "16", "627", "265,000", "26%"],
                ["Fowler Ridge", "Indiana (farmland)", "14", "355", "200,000", "22%"]
            ],
            "prompts": [
                "What is the relationship between average wind speed and capacity factor?",
                "Block Island has only 5 turbines but a 48% capacity factor. Why is offshore wind so efficient?",
                "If you were Dr. Mitchell, where would you recommend building the next wind farm? What data supports your choice?"
            ]
        }
    },

    "G04L2-L06": {
        # Building for the Big One: Earthquake Engineering
        "scientist": {
            "name": "Dr. Takeshi Yamamoto",
            "title": "Earthquake Resilience Engineer",
            "workplace": "Pacific Earthquake Engineering Research Center (UC Berkeley)",
            "salary": "$90K-$145K/year",
            "education": "B.S. in Civil Engineering, Ph.D. in Structural Dynamics",
            "what_they_model": "How buildings respond to earthquake shaking — testing whether structures bend safely or break catastrophically"
        },
        "additional_career": {
            "name": "Building Inspector",
            "description": "Evaluates whether buildings meet earthquake safety codes by checking foundations, walls, and connections for structural weaknesses.",
            "salary": "$45K-$75K/year",
            "education": "Associate's degree + state certification in Building Inspection"
        },
        "spotlight": {
            "title": "The 2011 Japan Earthquake: The Building That Swayed But Never Broke",
            "narrative": "On March 11, 2011, a magnitude 9.0 earthquake struck Japan — the fourth most powerful earthquake ever recorded. Tokyo's skyscrapers swayed dramatically for six full minutes, with the tops of some buildings moving 5 feet back and forth. But virtually no modern building in Tokyo collapsed. The secret? Japanese engineers had spent decades designing buildings with flexible steel frames, energy-absorbing dampers, and base isolation systems that let the building move WITH the earthquake instead of fighting against it. One 52-story building in Shinjuku swayed so gently that workers on the upper floors barely felt the quake. Dr. Takeshi Yamamoto studies these designs to help other earthquake-prone cities protect their people.",
            "discussion_prompt": "Why is it safer for a building to sway during an earthquake than to stay completely rigid?"
        },
        "extend_components": [
            ("Base Isolation", "Dr. Yamamoto's favorite technology — rubber and steel pads under a building that let it slide during a quake, absorbing 90% of the shaking force"),
            ("Soil Type", "Buildings on soft clay shake more violently than those on solid bedrock — the same earthquake can cause different damage depending on the ground"),
            ("Building Height", "Tall buildings sway more at the top but handle earthquakes differently than short buildings — each has a natural vibration frequency that can amplify shaking")
        ],
        "data": {
            "title": "Building Damage vs. Design Features in Earthquakes",
            "type": "table",
            "headers": ["Building Type", "Design Feature", "Earthquake Magnitude", "Damage Level", "Occupant Injuries"],
            "rows": [
                ["Unreinforced brick", "Rigid, no flexibility", "6.0", "Collapsed", "Many"],
                ["Basic concrete frame", "Some flexibility", "6.0", "Severe cracking", "Moderate"],
                ["Steel moment frame", "Flexible joints", "7.0", "Minor damage", "Few"],
                ["Base-isolated hospital", "Rubber bearings", "7.0", "Negligible", "Zero"],
                ["Japanese high-rise", "Dampers + flex frame", "9.0", "Cosmetic only", "Zero"]
            ],
            "prompts": [
                "Which building types survived the strongest earthquakes with the least damage?",
                "The base-isolated hospital had zero injuries in a 7.0 earthquake. How does base isolation work based on what you know about energy transfer?",
                "If you were designing a school in earthquake country, which features would you include and why?"
            ]
        }
    },

    "G04L2-L07": {
        # Chain Reaction: When Energy Moves Object to Object
        "scientist": {
            "name": "Dr. Anika Washington",
            "title": "Collision Physics Researcher",
            "workplace": "Sandia National Laboratories, Impact Physics Division",
            "salary": "$90K-$140K/year",
            "education": "B.S. in Physics, Ph.D. in Mechanical Engineering",
            "what_they_model": "How energy transfers between objects during collisions — from car crashes to asteroid impacts"
        },
        "additional_career": {
            "name": "Crash Test Engineer",
            "description": "Designs and analyzes vehicle crash tests to understand how collision energy transfers through car structures and affects passenger safety.",
            "salary": "$65K-$100K/year",
            "education": "B.S. in Mechanical or Automotive Engineering"
        },
        "spotlight": {
            "title": "Newton's Cradle: The 350-Year-Old Toy That Still Stumps Physics Students",
            "narrative": "In 1687, Isaac Newton described what would become the world's most famous desk toy: Newton's cradle. When you pull back one ball and release it, one ball on the other end flies out. Pull back two balls, and two fly out. It seems like magic, but it's pure energy transfer. The kinetic energy from the first ball passes through the middle balls as a compression wave — like dominoes made of energy. The middle balls barely move because the energy passes THROUGH them. But here's what most people don't notice: over time, the balls swing less and less. Where does the energy go? Sound and heat. Each click you hear is energy leaving the system forever. Dr. Anika Washington uses this same principle to model how energy transfers in real collisions.",
            "discussion_prompt": "In Newton's cradle, the middle balls don't move much. Does that mean energy skips over them, or does something else happen?"
        },
        "extend_components": [
            ("Material Hardness", "Dr. Washington tests how material hardness affects energy transfer — steel balls transfer energy more efficiently than rubber balls because less energy is absorbed"),
            ("Collision Angle", "Head-on collisions transfer energy differently than glancing blows — the angle determines how much energy goes forward vs. sideways"),
            ("Number of Objects in Chain", "Each object in the chain absorbs a tiny bit of energy as sound and heat, so longer chains deliver less energy to the final object")
        ],
        "data": {
            "title": "Energy Transfer Through Collision Chains",
            "type": "table",
            "headers": ["Chain Length", "Initial Energy (J)", "Final Object Energy (J)", "Energy Lost (%)", "Main Loss Type"],
            "rows": [
                ["2 objects", "10.0", "9.2", "8%", "Sound + Heat"],
                ["3 objects", "10.0", "8.5", "15%", "Sound + Heat"],
                ["5 objects", "10.0", "7.1", "29%", "Sound + Heat"],
                ["8 objects", "10.0", "5.3", "47%", "Sound + Heat"],
                ["12 objects", "10.0", "3.4", "66%", "Sound + Heat"]
            ],
            "prompts": [
                "What pattern do you notice as the chain gets longer?",
                "Why does the final object always receive less energy than the first object had?",
                "If you wanted to transfer the MOST energy to the last object, what would you change about the chain?"
            ]
        }
    },

    # =========================================================================
    # GRADE 5 LEVEL 2 (7 lessons)
    # =========================================================================

    "G05L2-L01": {
        # The Carbon Cycle: Where Does Your Breath Go?
        "scientist": {
            "name": "Dr. Carlos Rivera",
            "title": "Carbon Flux Scientist",
            "workplace": "Lawrence Berkeley National Laboratory",
            "salary": "$85K-$135K/year",
            "education": "B.S. in Environmental Science, Ph.D. in Biogeochemistry",
            "what_they_model": "How much carbon moves between the atmosphere, forests, soils, and oceans every day — tracking the planet's carbon budget"
        },
        "additional_career": {
            "name": "Carbon Credit Analyst",
            "description": "Calculates how much carbon dioxide a forest or farm removes from the atmosphere, helping companies offset their emissions by investing in nature.",
            "salary": "$55K-$90K/year",
            "education": "B.S. in Environmental Science or Economics"
        },
        "spotlight": {
            "title": "The Keeling Curve: The Graph That Changed the World",
            "narrative": "In 1958, a chemist named Charles David Keeling set up a CO2 monitor on top of Mauna Loa volcano in Hawaii, far from any city or factory. He expected to find a steady number. Instead, he discovered something remarkable: CO2 levels rise and fall every year in a zigzag pattern — up in winter when Northern Hemisphere trees lose their leaves and stop absorbing CO2, down in summer when they grow leaves and absorb it again. The Earth literally breathes. But Keeling also noticed something alarming: the average was creeping upward every year. In 1958, CO2 was 315 parts per million. Today it exceeds 420 ppm. The 'Keeling Curve' became the most important graph in climate science.",
            "discussion_prompt": "Why does the Keeling Curve zigzag every year? What does this tell us about how forests affect the atmosphere?"
        },
        "extend_components": [
            ("Ocean CO2 Absorption", "Dr. Rivera tracks how oceans absorb about 25% of human-emitted CO2, but this makes ocean water more acidic, threatening coral reefs and shellfish"),
            ("Fossil Fuel Combustion", "Burning coal, oil, and gas releases carbon that was stored underground for millions of years — putting ancient carbon back into the modern atmosphere"),
            ("Soil Microbe Activity", "Billions of soil bacteria break down dead plants and release CO2 — warmer soils decompose faster, creating a climate feedback loop")
        ],
        "data": {
            "title": "Atmospheric CO2 Concentration Over Time (Keeling Curve Data)",
            "type": "table",
            "headers": ["Year", "CO2 (parts per million)", "Annual Increase (ppm)", "Primary Cause"],
            "rows": [
                ["1960", "317", "0.7", "Early industrialization"],
                ["1980", "339", "1.4", "Growing fossil fuel use"],
                ["2000", "369", "1.5", "Global economic growth"],
                ["2010", "390", "2.1", "China/India industrialization"],
                ["2020", "414", "2.4", "Continued fossil fuel use"],
                ["2024", "424", "2.5", "Record emissions"]
            ],
            "prompts": [
                "Is CO2 increasing at a steady rate, or is the rate itself increasing? What does this mean?",
                "Between 1960 and 2024, CO2 rose from 317 to 424 ppm. Calculate the total increase and the average annual change.",
                "If Dr. Rivera's carbon cycle model shows that forests absorb CO2, why is the total still going up every year?"
            ]
        }
    },

    "G05L2-L02": {
        # Solar vs. Fossil: The Energy Showdown
        "scientist": {
            "name": "Dr. Patricia Okonkwo",
            "title": "Solar Energy Systems Researcher",
            "workplace": "Fraunhofer Institute for Solar Energy Systems",
            "salary": "$80K-$130K/year",
            "education": "B.S. in Electrical Engineering, Ph.D. in Photovoltaic Science",
            "what_they_model": "How solar panel efficiency, weather patterns, and grid demand interact to determine whether solar can replace fossil fuels in a region"
        },
        "additional_career": {
            "name": "Solar Panel Installer",
            "description": "Designs and installs rooftop and ground-mounted solar systems for homes and businesses, calculating the optimal angle and placement for maximum energy production.",
            "salary": "$40K-$65K/year",
            "education": "Technical certificate or Associate's in Solar Technology"
        },
        "spotlight": {
            "title": "The Solar Impulse: Flying Around the World on Sunlight Alone",
            "narrative": "In 2016, a plane called Solar Impulse 2 completed the first-ever solar-powered flight around the world — 26,000 miles without a single drop of fuel. Its 17,000 solar cells powered four electric motors and charged batteries for nighttime flying. The plane flew so slowly (about 45 mph) that the journey took 16 months. But pilot Bertrand Piccard wasn't trying to break speed records. He was proving a point: the technology exists to power transportation with sunlight alone. Dr. Patricia Okonkwo's models show that solar energy is now cheaper than coal in most of the world, and efficiency keeps improving — modern solar panels convert 25% of sunlight to electricity, up from just 6% in the 1960s.",
            "discussion_prompt": "Solar Impulse flew at only 45 mph. What does this tell us about the current limitations of solar power for transportation?"
        },
        "extend_components": [
            ("Panel Degradation Rate", "Dr. Okonkwo tracks how solar panels slowly lose efficiency over time — most panels produce 80% of original capacity after 25 years"),
            ("Cloud Cover Percentage", "Clouds block direct sunlight but panels still generate about 25% power from diffuse light on cloudy days"),
            ("Battery Storage Efficiency", "Storing solar energy in batteries loses about 10-15% of the energy, which matters for nighttime electricity supply")
        ],
        "data": {
            "title": "Cost of Electricity by Source (2010-2024)",
            "type": "table",
            "headers": ["Year", "Solar (cents/kWh)", "Coal (cents/kWh)", "Natural Gas (cents/kWh)", "Wind (cents/kWh)"],
            "rows": [
                ["2010", "35.9", "11.1", "8.3", "13.5"],
                ["2014", "17.7", "10.9", "7.5", "8.0"],
                ["2018", "8.5", "11.2", "5.8", "5.6"],
                ["2022", "4.9", "12.8", "6.5", "3.8"],
                ["2024", "4.2", "13.5", "7.1", "3.5"]
            ],
            "prompts": [
                "What happened to the cost of solar between 2010 and 2024? How does this compare to coal?",
                "In what year did solar become cheaper than coal? What might have caused this crossover?",
                "If you were a city planner, which energy source would you invest in for the next 20 years based on this data?"
            ]
        }
    },

    "G05L2-L03": {
        # The Water Crisis
        "scientist": {
            "name": "Dr. Kevin Tran",
            "title": "Groundwater Hydrologist",
            "workplace": "U.S. Geological Survey (USGS), California Water Science Center",
            "salary": "$75K-$120K/year",
            "education": "B.S. in Geology, M.S. in Hydrogeology",
            "what_they_model": "How underground water reserves fill up from rain and get depleted by wells — predicting when aquifers will run dry"
        },
        "additional_career": {
            "name": "Water Conservation Specialist",
            "description": "Works with cities and farms to reduce water waste through better irrigation, drought-resistant landscaping, and recycling systems.",
            "salary": "$45K-$75K/year",
            "education": "B.S. in Environmental Science or Water Resource Management"
        },
        "spotlight": {
            "title": "The Ogallala Aquifer: The Underground Ocean That's Disappearing",
            "narrative": "Beneath eight U.S. states stretches the Ogallala Aquifer, one of the largest underground water reserves on Earth. It took millions of years to fill with ancient rainwater. Since the 1950s, farmers have been pumping it to irrigate crops across the Great Plains — America's breadbasket. The problem? They're pumping water out 10 times faster than rain refills it. In parts of Kansas and Texas, the water table has dropped over 150 feet. Some wells have already gone dry. Scientists estimate that at current rates, 70% of the Ogallala could be depleted by 2060. Dr. Kevin Tran builds models to help communities understand exactly how much water they can use without emptying the aquifer forever.",
            "discussion_prompt": "If the Ogallala Aquifer took millions of years to fill but could be emptied in 100 years, what does that tell you about the relationship between input and output in this system?"
        },
        "extend_components": [
            ("Evapotranspiration Rate", "Dr. Tran calculates how much water plants release back into the air through their leaves — hot, dry regions lose enormous amounts of water this way"),
            ("Soil Permeability", "Sandy soil lets rain soak down to aquifers quickly, but clay soil blocks water, sending it away as runoff instead of recharging underground reserves"),
            ("Agricultural Irrigation Efficiency", "Flood irrigation wastes 50% of water to evaporation, while drip irrigation delivers 95% directly to plant roots")
        ],
        "data": {
            "title": "Ogallala Aquifer Water Level Changes",
            "type": "table",
            "headers": ["State", "1950 Depth to Water (ft)", "2020 Depth to Water (ft)", "Change (ft)", "Estimated Years Remaining"],
            "rows": [
                ["Nebraska", "20", "35", "−15", "200+"],
                ["Colorado", "60", "110", "−50", "80"],
                ["Kansas", "50", "130", "−80", "40"],
                ["Oklahoma", "45", "100", "−55", "60"],
                ["Texas (panhandle)", "40", "190", "−150", "15"]
            ],
            "prompts": [
                "Which state has the biggest drop in water level? Which has the smallest?",
                "Texas has only 15 years of water remaining at current rates. What could they do to extend this?",
                "Why does Nebraska have 200+ years remaining while Texas has only 15, even though they share the same aquifer?"
            ]
        }
    },

    "G05L2-L04": {
        # Phase Changes: When Matter Transforms
        "scientist": {
            "name": "Dr. Hannah Johansson",
            "title": "Phase Transition Physicist",
            "workplace": "MIT Lincoln Laboratory",
            "salary": "$95K-$150K/year",
            "education": "B.S. in Physics, Ph.D. in Condensed Matter Physics",
            "what_they_model": "How matter transitions between solid, liquid, and gas states — and the exotic states of matter that exist at extreme temperatures"
        },
        "additional_career": {
            "name": "Cryogenics Technician",
            "description": "Works with materials at extremely cold temperatures, using liquid nitrogen and helium to study superconductors and preserve biological samples.",
            "salary": "$45K-$70K/year",
            "education": "Associate's or B.S. in Physics or Engineering Technology"
        },
        "spotlight": {
            "title": "Triple Point: The Temperature Where Ice, Water, and Steam Exist at the Same Time",
            "narrative": "At exactly 0.01°C and a very specific low pressure, water does something seemingly impossible: it exists as ice, liquid water, and water vapor all at the same time. This is called the triple point, and it's so precisely defined that scientists use it to calibrate thermometers worldwide. At the triple point, you can watch ice melting into water while water simultaneously evaporates into steam, all in the same container. Dr. Hannah Johansson studies triple points of different materials because they reveal the fundamental rules governing how matter changes form. Every substance has its own triple point — for CO2, it's at −56.6°C and 5.2 times normal atmospheric pressure, which is why dry ice goes straight from solid to gas (sublimation) under normal conditions.",
            "discussion_prompt": "Dry ice (solid CO2) turns directly into gas without becoming liquid first. Using the triple point concept, why does this happen at normal air pressure?"
        },
        "extend_components": [
            ("Impurities in the Substance", "Dr. Johansson knows that salt lowers water's freezing point — which is why we salt roads in winter and why ocean water freezes at −2°C instead of 0°C"),
            ("Surface Area Exposed", "A thin layer of water evaporates faster than a deep pool because more molecules are at the surface where they can escape into the air"),
            ("Container Pressure", "In a pressure cooker, increased pressure raises water's boiling point above 100°C, which is why food cooks faster inside one")
        ],
        "data": {
            "title": "Phase Change Temperatures for Common Substances",
            "type": "table",
            "headers": ["Substance", "Melting Point (°C)", "Boiling Point (°C)", "Range as Liquid (°C)", "State at Room Temp (20°C)"],
            "rows": [
                ["Water", "0", "100", "100", "Liquid"],
                ["Mercury", "−39", "357", "396", "Liquid"],
                ["Iron", "1,538", "2,862", "1,324", "Solid"],
                ["Oxygen", "−219", "−183", "36", "Gas"],
                ["Ethanol (alcohol)", "−114", "78", "192", "Liquid"],
                ["Tungsten", "3,422", "5,555", "2,133", "Solid"]
            ],
            "prompts": [
                "Which substance has the largest liquid range? What makes this useful for manufacturing?",
                "Mercury is a liquid at room temperature. Based on its melting point, why?",
                "If you heated a room to 100°C, which substances on this list would change state? Which would not?"
            ]
        }
    },

    "G05L2-L05": {
        # The Food Web Puzzle
        "scientist": {
            "name": "Dr. Andre Baptiste",
            "title": "Marine Food Web Ecologist",
            "workplace": "Monterey Bay Aquarium Research Institute (MBARI)",
            "salary": "$75K-$115K/year",
            "education": "B.S. in Marine Biology, Ph.D. in Ecosystem Ecology",
            "what_they_model": "How energy flows from microscopic plankton to great white sharks — and what happens when any link in the chain breaks"
        },
        "additional_career": {
            "name": "Wildlife Habitat Restoration Specialist",
            "description": "Rebuilds damaged ecosystems by reintroducing native plants and animals in the right proportions to restore natural food web relationships.",
            "salary": "$45K-$75K/year",
            "education": "B.S. in Conservation Biology or Ecology"
        },
        "spotlight": {
            "title": "The Wolves of Yellowstone: How Predators Changed a River",
            "narrative": "When wolves were eliminated from Yellowstone National Park in the 1920s, the elk population exploded. With no predators, elk grazed riverside willows and aspens down to nothing. Without tree roots to hold the soil, riverbanks eroded and streams widened into shallow, braided channels. In 1995, 41 wolves were reintroduced. Elk began avoiding open riverbanks where they were vulnerable. Willows and aspens grew back. Roots stabilized the banks. Rivers narrowed and deepened. Beavers returned to build dams. Songbirds came back to nest in the new trees. The wolves didn't just change the elk — they literally changed the shape of the rivers. Scientists call this a trophic cascade.",
            "discussion_prompt": "How did removing one predator species end up changing the physical shape of rivers? What does this tell you about food web connections?"
        },
        "extend_components": [
            ("Invasive Species Pressure", "Dr. Baptiste studies how invasive species disrupt food webs by competing with native species for the same position — sometimes outcompeting them entirely"),
            ("Seasonal Availability", "Many food web connections change with seasons — salmon runs provide massive energy pulses to bears, eagles, and even forest soil"),
            ("Scavenger Recycling", "Vultures, beetles, and bacteria consume dead organisms, recycling nutrients that would otherwise be locked away from the food web")
        ],
        "data": {
            "title": "Yellowstone Ecosystem Changes After Wolf Reintroduction (1995-2020)",
            "type": "table",
            "headers": ["Ecosystem Measure", "Before Wolves (1990)", "After Wolves (2020)", "Change"],
            "rows": [
                ["Elk population", "20,000", "6,000", "−70%"],
                ["Willow height (avg)", "< 1 meter", "4+ meters", "+300%"],
                ["Beaver colonies", "1", "12", "+1,100%"],
                ["Songbird species", "Few", "Many — multiple new species", "Significant increase"],
                ["Riverbank erosion rate", "High", "Low — stabilized by roots", "Major reduction"],
                ["Grizzly bear berry food", "Scarce", "Abundant — berry bushes returned", "Recovery"]
            ],
            "prompts": [
                "The elk population dropped 70%, but why was this actually GOOD for the ecosystem?",
                "How did wolves affect beavers even though wolves don't eat beavers?",
                "If Dr. Baptiste built a food web model of Yellowstone, how many levels of connection would exist between wolves and songbirds?"
            ]
        }
    },

    "G05L2-L06": {
        # Earth Systems Collide
        "scientist": {
            "name": "Dr. Yuki Tanaka",
            "title": "Volcanologist and Climate Modeler",
            "workplace": "USGS Hawaiian Volcano Observatory",
            "salary": "$80K-$130K/year",
            "education": "B.S. in Geology, Ph.D. in Volcanology",
            "what_they_model": "How volcanic eruptions change Earth's climate by injecting gases and particles into the atmosphere — from local effects to global cooling"
        },
        "additional_career": {
            "name": "Atmospheric Chemist",
            "description": "Analyzes the chemical composition of Earth's atmosphere, tracking how gases from volcanoes, factories, and forests interact to affect climate and air quality.",
            "salary": "$60K-$100K/year",
            "education": "B.S. in Chemistry, M.S. in Atmospheric Science"
        },
        "spotlight": {
            "title": "The Year Without a Summer: When a Volcano Froze the World",
            "narrative": "In April 1815, Mount Tambora in Indonesia erupted with the force of 10,000 nuclear bombs — the most powerful volcanic eruption in recorded history. It blasted 36 cubic miles of rock and ash into the atmosphere. The sulfur dioxide gas formed a global haze that blocked sunlight for over a year. In 1816, known as 'The Year Without a Summer,' snow fell in June in New England. Crops failed across Europe, causing famine. The strange, colorless sunlight inspired Mary Shelley to write Frankenstein during the gloomy summer. Dr. Yuki Tanaka studies how Tambora's sulfur particles reflected sunlight back into space, temporarily cooling the entire planet by 3°C.",
            "discussion_prompt": "How can a single volcanic eruption affect weather on the opposite side of the planet? What does this tell you about how Earth's systems are connected?"
        },
        "extend_components": [
            ("Sulfur Dioxide Emissions", "Dr. Tanaka measures how SO2 from eruptions forms tiny particles in the upper atmosphere that reflect sunlight, cooling the surface for months or years"),
            ("Ocean Heat Absorption", "Oceans absorb excess heat slowly, which means volcanic cooling effects are delayed and prolonged by the ocean's thermal inertia"),
            ("Ash Particle Size", "Large ash particles fall out of the atmosphere in days, but tiny sulfate particles can stay suspended for 2-3 years, extending climate effects")
        ],
        "data": {
            "title": "Major Volcanic Eruptions and Climate Effects",
            "type": "table",
            "headers": ["Volcano", "Year", "Material Ejected", "Global Temp Change", "Effects Duration"],
            "rows": [
                ["Mount Tambora", "1815", "36 cubic miles", "−3.0°C", "3 years"],
                ["Krakatoa", "1883", "6 cubic miles", "−1.2°C", "5 years"],
                ["Mount Pinatubo", "1991", "2.4 cubic miles", "−0.5°C", "2 years"],
                ["Eyjafjallajokull", "2010", "0.06 cubic miles", "~0°C", "Weeks"],
                ["Mount St. Helens", "1980", "0.67 cubic miles", "~0°C", "Months"]
            ],
            "prompts": [
                "What is the relationship between the amount of material ejected and the global temperature change?",
                "Why did Eyjafjallajokull and Mount St. Helens barely affect global temperature despite being major eruptions?",
                "If a volcano erupted that was twice the size of Tambora, what might happen to global agriculture?"
            ]
        }
    },

    "G05L2-L07": {
        # Starlight and Distance
        "scientist": {
            "name": "Dr. Lena Kowalski",
            "title": "Stellar Luminosity Researcher",
            "workplace": "Space Telescope Science Institute (STScI), Baltimore",
            "salary": "$90K-$145K/year",
            "education": "B.S. in Astrophysics, Ph.D. in Observational Astronomy",
            "what_they_model": "How to determine a star's true brightness and distance by analyzing the light that reaches Earth's telescopes"
        },
        "additional_career": {
            "name": "Telescope Operations Specialist",
            "description": "Operates and maintains research telescopes, ensuring that astronomers get the clearest possible images of distant stars and galaxies.",
            "salary": "$45K-$75K/year",
            "education": "B.S. in Physics or Astronomy + technical training"
        },
        "spotlight": {
            "title": "Henrietta Leavitt: The Woman Who Measured the Universe",
            "narrative": "In 1912, astronomer Henrietta Swan Leavitt discovered something that revolutionized our understanding of the universe. While studying variable stars — stars that pulse brighter and dimmer over regular cycles — she noticed a pattern: the brighter a variable star truly was, the longer its pulsing cycle took. This meant that by timing how fast a star pulsed, she could calculate its actual brightness. Then, by comparing its actual brightness to how bright it appeared from Earth, she could calculate its distance. Her discovery gave astronomers a cosmic ruler. Edwin Hubble later used Leavitt's method to prove that other galaxies existed beyond the Milky Way. Without her work, we wouldn't know the size of the universe.",
            "discussion_prompt": "Henrietta Leavitt couldn't directly measure how far away a star was. How did she use brightness and pulsing to figure it out indirectly?"
        },
        "extend_components": [
            ("Atmospheric Distortion", "Dr. Kowalski accounts for how Earth's atmosphere bends and distorts starlight, which is why stars twinkle — and why space telescopes see more clearly"),
            ("Red Shift", "Light from stars moving away from Earth gets stretched to redder wavelengths — farther and faster-moving stars appear redder, which helps measure distance"),
            ("Stellar Classification", "Stars are classified by color and temperature (O, B, A, F, G, K, M) — knowing a star's class helps Dr. Kowalski estimate its true brightness before calculating distance")
        ],
        "data": {
            "title": "Comparing Star Brightness: Actual vs. Apparent",
            "type": "table",
            "headers": ["Star", "Distance (light-years)", "Actual Brightness (solar luminosities)", "Apparent Magnitude", "Appears Bright or Dim?"],
            "rows": [
                ["Sun", "0.000016", "1", "−26.7", "Extremely bright"],
                ["Sirius", "8.6", "25", "−1.46", "Brightest night star"],
                ["Betelgeuse", "700", "126,000", "+0.42", "Moderately bright"],
                ["Deneb", "2,600", "196,000", "+1.25", "Visible but dimmer"],
                ["Rigel", "860", "120,000", "+0.13", "Bright"],
                ["Polaris", "433", "2,500", "+1.98", "Moderately dim"]
            ],
            "prompts": [
                "Deneb is the most luminous star on this list but appears dimmer than Sirius. Why?",
                "If you could move Betelgeuse to Sirius's distance (8.6 light-years), how would it appear in our sky compared to the Sun?",
                "Why is apparent magnitude a misleading way to judge how powerful a star really is?"
            ]
        }
    },

    # =========================================================================
    # GRADE 6 LEVEL 2 (7 lessons)
    # =========================================================================

    "G06L2-L01": {
        # Who Eats Who? Energy Flow Through Food Webs
        "scientist": {
            "name": "Dr. Marcus Johnson",
            "title": "Ecosystem Energy Modeler",
            "workplace": "Cary Institute of Ecosystem Studies, New York",
            "salary": "$80K-$125K/year",
            "education": "B.S. in Ecology, Ph.D. in Ecosystem Science",
            "what_they_model": "How energy flows through entire ecosystems — measuring exactly how much energy is lost at each step of the food web"
        },
        "additional_career": {
            "name": "Fisheries Biologist",
            "description": "Manages fish populations by calculating how many fish can be harvested without collapsing the food web, using the 10% energy rule to set catch limits.",
            "salary": "$50K-$85K/year",
            "education": "B.S. in Marine Biology or Fisheries Science"
        },
        "spotlight": {
            "title": "The Cod Collapse: When Overfishing Broke an Entire Ocean Food Web",
            "narrative": "For 500 years, the Grand Banks off Newfoundland held the richest fishing grounds on Earth. Atlantic cod were so abundant that fishermen said you could walk across their backs. By the 1980s, factory trawlers were pulling out cod faster than they could reproduce. In 1992, the cod population crashed by 99%, and Canada declared a moratorium on cod fishing. But the damage went far beyond cod. Without cod eating them, shrimp and crab populations exploded. Without small fish controlling them, algae bloomed. The entire food web reorganized into a new, less productive state. Thirty years later, the cod still haven't recovered. Dr. Marcus Johnson uses this collapse as a warning about what happens when humans remove too much from one trophic level.",
            "discussion_prompt": "Why hasn't the cod population recovered even after 30 years of no fishing? What does this tell you about food web stability?"
        },
        "extend_components": [
            ("Detritus Production", "Dr. Johnson measures dead organic matter that falls to the ocean floor — this 'marine snow' feeds deep-sea ecosystems that never see sunlight"),
            ("Trophic Level Efficiency", "Not all ecosystems transfer 10% of energy — warm-blooded predators waste more energy as heat, sometimes transferring only 1-2%"),
            ("Nutrient Upwelling", "Deep ocean currents bring nutrient-rich water to the surface, fueling phytoplankton blooms that are the base of marine food webs")
        ],
        "data": {
            "title": "Energy Transfer Through a Marine Food Web",
            "type": "table",
            "headers": ["Trophic Level", "Example Organism", "Energy Available (kcal/m²/yr)", "% of Original", "Biomass (g/m²)"],
            "rows": [
                ["Producer", "Phytoplankton", "20,000", "100%", "500"],
                ["Primary Consumer", "Zooplankton", "2,000", "10%", "50"],
                ["Secondary Consumer", "Small fish", "200", "1%", "5"],
                ["Tertiary Consumer", "Tuna", "20", "0.1%", "0.5"],
                ["Apex Predator", "Shark", "2", "0.01%", "0.05"]
            ],
            "prompts": [
                "By the time energy reaches sharks, what percentage of the original solar energy remains?",
                "Why does biomass decrease at each level just like energy does?",
                "If overfishing removed all the tuna, what would happen to small fish AND sharks?"
            ]
        }
    },

    "G06L2-L02": {
        # Why Does Your Coffee Get Cold?
        "scientist": {
            "name": "Dr. Isabel Vega",
            "title": "Thermal Systems Engineer",
            "workplace": "NASA Johnson Space Center, Thermal Protection Division",
            "salary": "$90K-$140K/year",
            "education": "B.S. in Aerospace Engineering, M.S. in Thermal Sciences",
            "what_they_model": "How heat transfers between spacecraft and the extreme temperatures of space — protecting astronauts from both scorching sun and freezing shadow"
        },
        "additional_career": {
            "name": "HVAC Design Engineer",
            "description": "Designs heating and cooling systems for buildings, calculating heat transfer rates to keep indoor temperatures comfortable year-round.",
            "salary": "$55K-$90K/year",
            "education": "B.S. in Mechanical Engineering"
        },
        "spotlight": {
            "title": "The Thermos Flask: The Invention That Fights All Three Types of Heat Transfer",
            "narrative": "In 1892, Scottish scientist Sir James Dewar invented a container with a double wall and a vacuum between the walls. His Dewar flask (later marketed as a 'Thermos') fights heat transfer in three ways at once: the vacuum eliminates conduction and convection (no molecules to carry heat), and a reflective silver coating reflects radiation back inside. A good thermos can keep coffee hot for 12 hours or keep ice frozen for 24. Dr. Isabel Vega uses the same principles on spacecraft — the International Space Station experiences temperature swings from +250°F in sunlight to −250°F in shadow, and multi-layered insulation based on Dewar's design protects the crew.",
            "discussion_prompt": "A thermos fights conduction, convection, AND radiation. Why does your coffee still eventually get cold even in a thermos?"
        },
        "extend_components": [
            ("Surface Color", "Dr. Vega paints spacecraft surfaces white or silver to reflect radiant heat — dark surfaces absorb heat and warm up faster"),
            ("Container Material", "Metal cups cool coffee faster than ceramic mugs because metal conducts heat away from the liquid more quickly"),
            ("Liquid Volume", "A full cup of coffee stays hot longer than a half-full cup because the greater mass holds more thermal energy relative to its surface area")
        ],
        "data": {
            "title": "Coffee Cooling Experiment: Temperature Over Time",
            "type": "table",
            "headers": ["Time (minutes)", "Metal Cup (°C)", "Ceramic Mug (°C)", "Thermos (°C)", "Room Temp (°C)"],
            "rows": [
                ["0", "90", "90", "90", "22"],
                ["5", "72", "82", "89", "22"],
                ["15", "48", "64", "86", "22"],
                ["30", "30", "44", "81", "22"],
                ["60", "23", "28", "72", "22"],
                ["120", "22", "22", "58", "22"]
            ],
            "prompts": [
                "Which container reached room temperature fastest? Why?",
                "The coffee cools quickly at first but slows down later. Why does the cooling rate change?",
                "At 120 minutes, the thermos coffee is still 58°C while the others are at room temperature. What makes the thermos so effective?"
            ]
        }
    },

    "G06L2-L03": {
        # Plate Tectonics: Predicting Where Earth Will Crack Next
        "scientist": {
            "name": "Dr. David Kim",
            "title": "Seismologist and Plate Boundary Modeler",
            "workplace": "Caltech Seismological Laboratory",
            "salary": "$85K-$135K/year",
            "education": "B.S. in Geophysics, Ph.D. in Seismology",
            "what_they_model": "Where stress builds up along tectonic plate boundaries, using seismic wave data to forecast where the next major earthquake might strike"
        },
        "additional_career": {
            "name": "Seismic Monitoring Technician",
            "description": "Installs and maintains networks of earthquake sensors that detect ground motion 24/7, providing real-time data to scientists and emergency services.",
            "salary": "$45K-$70K/year",
            "education": "B.S. in Geology or Geophysics + field experience"
        },
        "spotlight": {
            "title": "The San Andreas Fault: California's 800-Mile Time Bomb",
            "narrative": "The San Andreas Fault stretches 800 miles through California, marking where the Pacific and North American plates grind past each other. In some sections, the plates creep smoothly, producing small earthquakes constantly. But in other sections, the plates are locked — stuck together by friction while stress builds year after year. The locked section near Los Angeles hasn't produced a major earthquake since 1857, over 165 years ago. Scientists estimate that this section has accumulated enough stress for a magnitude 7.8 earthquake. Dr. David Kim uses GPS stations along the fault to measure how much the ground has shifted, calculating stress with millimeter precision to understand when the locked section might finally rupture.",
            "discussion_prompt": "Why is a section of the San Andreas Fault that has been quiet for 165 years MORE dangerous than a section that produces small earthquakes regularly?"
        },
        "extend_components": [
            ("Fault Depth", "Dr. Kim monitors earthquake depth because shallow quakes (less than 20 km deep) cause more surface damage than deep ones, even at the same magnitude"),
            ("Seismic Wave Speed", "Different rock types transmit earthquake waves at different speeds — Dr. Kim maps underground rock layers by measuring how fast waves travel through them"),
            ("Aftershock Probability", "After a major earthquake, stress transfers to nearby faults, increasing the probability of additional quakes for months or years")
        ],
        "data": {
            "title": "Earthquake Frequency by Plate Boundary Type",
            "type": "table",
            "headers": ["Boundary Type", "Example Location", "Avg Magnitude", "Quakes per Year (M>4)", "Volcano Risk"],
            "rows": [
                ["Convergent (collision)", "Himalayas", "6.0-8.9", "150+", "Moderate"],
                ["Convergent (subduction)", "Japan Trench", "7.0-9.1", "200+", "Very High"],
                ["Divergent (spreading)", "Mid-Atlantic Ridge", "4.0-6.5", "50", "High (underwater)"],
                ["Transform (sliding)", "San Andreas Fault", "5.0-7.8", "100", "None"],
                ["Hotspot (intraplate)", "Hawaii", "3.0-5.0", "20", "Very High"]
            ],
            "prompts": [
                "Which boundary type produces the strongest earthquakes? Why?",
                "Transform boundaries have NO volcano risk. Based on how transform faults work, why not?",
                "Japan is on a subduction boundary with 200+ earthquakes per year. How does this explain why they lead the world in earthquake engineering?"
            ]
        }
    },

    "G06L2-L04": {
        # Inside the Cell
        "scientist": {
            "name": "Dr. Amina Hassan",
            "title": "Cellular Metabolism Researcher",
            "workplace": "Broad Institute of MIT and Harvard",
            "salary": "$90K-$145K/year",
            "education": "B.S. in Biochemistry, Ph.D. in Cell Biology",
            "what_they_model": "How cells convert nutrients and oxygen into energy — and what goes wrong in diseases where this process breaks down"
        },
        "additional_career": {
            "name": "Medical Laboratory Scientist",
            "description": "Runs blood and tissue tests in hospitals, analyzing cells under microscopes to help doctors diagnose diseases based on cellular function.",
            "salary": "$50K-$80K/year",
            "education": "B.S. in Medical Laboratory Science + certification"
        },
        "spotlight": {
            "title": "The Mighty Mitochondria: The Bacteria That Became Part of You",
            "narrative": "About 2 billion years ago, a large cell swallowed a smaller bacterium — but instead of digesting it, the two formed a partnership. The small bacterium was extremely good at using oxygen to produce energy. The large cell provided protection and nutrients. Over billions of years, the bacterium became the mitochondria — the powerhouse organelles inside nearly every cell in your body. The evidence? Mitochondria still have their own DNA, separate from your cell's DNA, and they reproduce by dividing in half, just like bacteria. You have about 10 million billion mitochondria in your body, and they produce your body weight in ATP energy every single day. Dr. Amina Hassan studies how mitochondrial dysfunction leads to diseases like Parkinson's and diabetes.",
            "discussion_prompt": "If mitochondria have their own DNA and divide like bacteria, what does this evidence suggest about their origin?"
        },
        "extend_components": [
            ("ATP Recycling Rate", "Dr. Hassan measures how fast cells recycle ATP — your body contains only about 250 grams of ATP at any moment, but you use and regenerate about 70 kg of it daily"),
            ("Oxygen Debt", "During intense exercise, cells burn energy faster than oxygen arrives, creating an oxygen debt that causes muscle fatigue and heavy breathing"),
            ("Cellular pH Level", "Waste products like lactic acid lower cell pH, which slows enzyme function and reduces mitochondria efficiency — this is why muscles 'burn' during exercise")
        ],
        "data": {
            "title": "Cell Energy Production Under Different Conditions",
            "type": "table",
            "headers": ["Condition", "Oxygen Available", "Glucose Available", "ATP Produced per Glucose", "Waste Products"],
            "rows": [
                ["Normal (aerobic)", "Plenty", "Plenty", "36-38 ATP", "CO2 + Water"],
                ["Low oxygen (anaerobic)", "None", "Plenty", "2 ATP", "Lactic acid"],
                ["Starvation", "Plenty", "None", "0 ATP", "Cell uses stored fat"],
                ["Exercise (moderate)", "Some", "Plenty", "30-34 ATP", "CO2 + Water + some lactate"],
                ["Exercise (intense)", "Not enough", "Plenty", "2-10 ATP", "Lactic acid buildup"]
            ],
            "prompts": [
                "Aerobic respiration produces 36-38 ATP while anaerobic produces only 2. Why is oxygen so important for energy?",
                "During intense exercise, why do your muscles burn and you breathe harder? Use the data to explain.",
                "If Dr. Hassan blocked a cell's mitochondria, which row in this table would best describe what happens?"
            ]
        }
    },

    "G06L2-L05": {
        # Atoms Rearrange: Modeling Chemical Reactions
        "scientist": {
            "name": "Dr. Michael Torres",
            "title": "Computational Chemist",
            "workplace": "Dow Chemical Company, Reaction Engineering Division",
            "salary": "$90K-$140K/year",
            "education": "B.S. in Chemistry, Ph.D. in Chemical Engineering",
            "what_they_model": "How atoms rearrange during chemical reactions — predicting which reactions will happen, how fast, and how much product they'll make"
        },
        "additional_career": {
            "name": "Pharmaceutical Quality Analyst",
            "description": "Tests medicines during manufacturing to verify the right chemical reactions occurred and the correct products formed in the right amounts.",
            "salary": "$55K-$85K/year",
            "education": "B.S. in Chemistry or Pharmaceutical Science"
        },
        "spotlight": {
            "title": "The Haber Process: The Chemical Reaction That Feeds Half the World",
            "narrative": "In 1909, German chemist Fritz Haber figured out how to combine nitrogen from the air with hydrogen to make ammonia — the key ingredient in synthetic fertilizer. Before Haber's process, the world's food supply was limited by the amount of natural nitrogen in soil. His invention allowed farmers to grow enough food to feed billions more people. Today, the Haber process uses 1-2% of the entire world's energy supply and produces 175 million tons of ammonia per year. Without it, scientists estimate that half the world's population would not have enough food. Dr. Michael Torres optimizes industrial chemical reactions like this one, using models to find the perfect temperature and pressure that maximize product while minimizing waste.",
            "discussion_prompt": "The Haber process uses 1-2% of all the world's energy. Is it worth it? What would happen if we stopped?"
        },
        "extend_components": [
            ("Catalyst Presence", "Dr. Torres adds catalysts — substances that speed up reactions without being consumed — iron catalysts make the Haber process 1,000 times faster"),
            ("Activation Energy", "Every reaction needs a minimum energy input to start, like a match needing friction to light — higher activation energy means the reaction is harder to trigger"),
            ("Equilibrium Point", "Some reactions reach a balance where products form as fast as they break apart — Dr. Torres adjusts conditions to push equilibrium toward more products")
        ],
        "data": {
            "title": "Reaction Rate Under Different Conditions",
            "type": "table",
            "headers": ["Condition", "Temperature", "Reactant Concentration", "Catalyst?", "Reaction Rate (relative)", "Product Yield"],
            "rows": [
                ["Cold, dilute, no catalyst", "20°C", "Low", "No", "1x", "5%"],
                ["Room temp, concentrated", "25°C", "High", "No", "4x", "20%"],
                ["Warm, dilute, no catalyst", "40°C", "Low", "No", "3x", "15%"],
                ["Warm, concentrated", "40°C", "High", "No", "12x", "55%"],
                ["Warm, concentrated + catalyst", "40°C", "High", "Yes", "48x", "92%"]
            ],
            "prompts": [
                "What has the biggest effect on reaction rate: temperature, concentration, or catalyst?",
                "Adding a catalyst increased the rate from 12x to 48x. Why don't all industrial reactions use catalysts?",
                "If Dr. Torres needed to produce the most product in the least time, which conditions would he choose?"
            ]
        }
    },

    "G06L2-L06": {
        # The Invisible Plant Factory: Photosynthesis Deeper
        "scientist": {
            "name": "Dr. Christina Park",
            "title": "Plant Physiology Researcher",
            "workplace": "Donald Danforth Plant Science Center, St. Louis",
            "salary": "$75K-$120K/year",
            "education": "B.S. in Botany, Ph.D. in Plant Physiology",
            "what_they_model": "How light, CO2, and water interact inside a leaf to produce sugar and oxygen — and how to make crops more efficient at photosynthesis"
        },
        "additional_career": {
            "name": "Vertical Farm Manager",
            "description": "Manages indoor farms where LED lights, controlled CO2, and hydroponic water systems optimize photosynthesis to grow food year-round without soil or sunlight.",
            "salary": "$50K-$85K/year",
            "education": "B.S. in Agricultural Science or Horticulture"
        },
        "spotlight": {
            "title": "The Oxygen Catastrophe: When Photosynthesis Almost Destroyed All Life",
            "narrative": "About 2.4 billion years ago, cyanobacteria — the first organisms to perform photosynthesis — flooded Earth's atmosphere with a gas that was toxic to nearly every living thing: oxygen. Before photosynthesis, Earth's atmosphere had almost no oxygen. The cyanobacteria changed everything. Most organisms that couldn't tolerate oxygen went extinct in what scientists call the Great Oxidation Event. It was the largest mass extinction in Earth's history — caused by a waste product of photosynthesis. Eventually, new organisms evolved that could USE oxygen for energy (aerobic respiration), and life as we know it became possible. Dr. Christina Park reminds her students that oxygen — the gas we depend on — was once a deadly pollutant.",
            "discussion_prompt": "Oxygen was once a toxic pollutant that caused a mass extinction. What does this tell you about how the same substance can be harmful or helpful depending on context?"
        },
        "extend_components": [
            ("Stomata Opening", "Dr. Park studies how tiny pores on leaves open and close — open stomata let CO2 in for photosynthesis but also let water vapor escape, creating a constant tradeoff"),
            ("Chloroplast Density", "Leaves with more chloroplasts (the organelles where photosynthesis happens) capture more light but also need more water and CO2 to keep up"),
            ("Light Wavelength", "Plants absorb red and blue light most efficiently but reflect green light — which is why leaves look green to our eyes")
        ],
        "data": {
            "title": "Photosynthesis Rate Under Different Conditions",
            "type": "table",
            "headers": ["Condition", "Light", "CO2", "Water", "Glucose Produced (mg/hr)", "O2 Released (mL/hr)"],
            "rows": [
                ["All optimal", "High", "High", "Plenty", "12.5", "8.4"],
                ["Low light", "Low", "High", "Plenty", "3.1", "2.1"],
                ["No light", "Zero", "High", "Plenty", "0", "0"],
                ["Low CO2", "High", "Low", "Plenty", "4.2", "2.8"],
                ["No water", "High", "High", "None", "0", "0"],
                ["Low light + low CO2", "Low", "Low", "Plenty", "1.4", "0.9"]
            ],
            "prompts": [
                "Which input, when removed completely, stops photosynthesis entirely?",
                "Under 'all optimal' conditions, the plant makes 12.5 mg/hr of glucose. Under 'low light + low CO2,' it makes only 1.4. Why is the combined effect worse than either alone?",
                "If Dr. Park wanted to grow the most food in a vertical farm, which input should she maximize first based on this data?"
            ]
        }
    },

    "G06L2-L07": {
        # Engineering a Solution: The Design Process
        "scientist": {
            "name": "Dr. Robert Nakamura",
            "title": "Engineering Design Process Researcher",
            "workplace": "Stanford d.school (Hasso Plattner Institute of Design)",
            "salary": "$85K-$135K/year",
            "education": "B.S. in Mechanical Engineering, Ph.D. in Design Science",
            "what_they_model": "How the engineering design process — defining problems, researching, prototyping, testing, and iterating — produces better solutions over time"
        },
        "additional_career": {
            "name": "Product Development Engineer",
            "description": "Takes ideas from concept to reality by designing, prototyping, and testing products through multiple iterations until they work reliably.",
            "salary": "$65K-$110K/year",
            "education": "B.S. in Engineering (any field)"
        },
        "spotlight": {
            "title": "The Dyson Vacuum: 5,127 Failures Before Success",
            "narrative": "In 1978, British engineer James Dyson was frustrated that his vacuum cleaner kept losing suction as the bag filled with dust. He had an idea: replace the bag with a cyclone separator that spins air to fling dust out. It took Dyson 15 years and 5,127 prototypes to get the design right. Each prototype taught him something new — why a certain angle didn't work, why a particular material cracked, why the cyclone needed to be a specific diameter. Prototype number 5,128 worked perfectly. When established vacuum companies refused to license his design, Dyson manufactured it himself. Today, Dyson is a billionaire, and his company sells millions of bagless vacuums worldwide. Dr. Robert Nakamura uses Dyson's story to teach that failure isn't the opposite of success — it's the path to it.",
            "discussion_prompt": "Why did Dyson need 5,127 failed prototypes? Couldn't he have just designed it right the first time?"
        },
        "extend_components": [
            ("User Feedback Quality", "Dr. Nakamura insists that testing prototypes with REAL users reveals problems that designers can't see — engineers often love features that users find confusing"),
            ("Material Selection", "Choosing the right material can make or break a design — the strongest material isn't always best if it's too heavy, too expensive, or can't be manufactured"),
            ("Constraint Identification", "Every engineering problem has constraints — budget, time, materials, safety regulations — and the best designs work within constraints rather than ignoring them")
        ],
        "data": {
            "title": "Prototype Performance Improvement Through Iteration",
            "type": "table",
            "headers": ["Iteration #", "Problem Addressed", "Performance Score (1-100)", "Cost per Unit", "Time to Build"],
            "rows": [
                ["1 (first attempt)", "Basic concept only", "22", "$85", "3 weeks"],
                ["3 (after testing)", "Fixed structural weakness", "41", "$70", "2 weeks"],
                ["5 (user feedback)", "Improved usability", "58", "$55", "10 days"],
                ["8 (optimization)", "Reduced materials waste", "74", "$38", "5 days"],
                ["12 (refined)", "Fine-tuned all systems", "89", "$32", "3 days"],
                ["15 (final)", "Production-ready", "95", "$28", "2 days"]
            ],
            "prompts": [
                "What happens to both performance score AND cost as iterations increase?",
                "The biggest performance jump happened between iterations 1 and 5. Why do early iterations improve the most?",
                "If you could only do 3 iterations instead of 15, which three would give you the best result for the time invested?"
            ]
        }
    },

    # =========================================================================
    # GRADE 7 LEVEL 2 (7 lessons)
    # =========================================================================

    "G07L2-L01": {
        # The Invisible War: How Your Immune System Fights Back
        "scientist": {
            "name": "Dr. Elena Rodriguez",
            "title": "Immunologist and Vaccine Development Researcher",
            "workplace": "National Institutes of Health (NIH), National Institute of Allergy and Infectious Diseases",
            "salary": "$95K-$155K/year",
            "education": "B.S. in Microbiology, M.D./Ph.D. in Immunology",
            "what_they_model": "How the immune system mounts a defense against new pathogens, and how to design vaccines that train immunity without causing disease"
        },
        "additional_career": {
            "name": "Epidemiologist",
            "description": "Investigates disease outbreaks to determine how pathogens spread through populations and designs public health interventions to stop them.",
            "salary": "$60K-$100K/year",
            "education": "M.P.H. (Master of Public Health) in Epidemiology"
        },
        "spotlight": {
            "title": "The Smallpox Eradication: How Vaccines Eliminated a Disease That Killed 500 Million People",
            "narrative": "Smallpox killed an estimated 500 million people in the 20th century alone and had a 30% fatality rate. In 1796, Edward Jenner discovered that milkmaids who had caught cowpox — a mild disease from cows — never got smallpox. He deliberately infected a boy with cowpox, then exposed him to smallpox. The boy didn't get sick. This was the world's first vaccine (from 'vacca,' Latin for cow). Nearly 200 years later, in 1980, the World Health Organization declared smallpox completely eradicated — the only human disease ever wiped out by vaccination. Dr. Elena Rodriguez studies how this success can be replicated for diseases like malaria and HIV, where the pathogens are far trickier to target.",
            "discussion_prompt": "Smallpox was eradicated through global vaccination. Why haven't we been able to do the same for influenza (the flu)?"
        },
        "extend_components": [
            ("Memory Cell Lifespan", "Dr. Rodriguez studies how long immune memory lasts — some vaccines provide lifelong protection, while others (like tetanus) need boosters every 10 years"),
            ("Antigenic Drift", "Flu viruses constantly mutate their surface proteins, which is why last year's flu vaccine doesn't work this year — the immune system doesn't recognize the new 'disguise'"),
            ("Cytokine Storm", "Sometimes the immune system overreacts, producing too many inflammatory signals that damage the body's own tissues — this is how some people die from COVID-19")
        ],
        "data": {
            "title": "Immune Response Timeline: Vaccinated vs. Unvaccinated",
            "type": "table",
            "headers": ["Days After Exposure", "Unvaccinated Antibody Level", "Vaccinated Antibody Level", "Unvaccinated Symptoms", "Vaccinated Symptoms"],
            "rows": [
                ["Day 0", "0", "0", "None", "None"],
                ["Day 3", "Low", "Moderate (memory cells activate)", "Fever begins", "None"],
                ["Day 5", "Low", "High (rapid production)", "High fever, body aches", "Mild fatigue"],
                ["Day 7", "Moderate (finally ramping up)", "Very high (peak)", "Severe symptoms", "None — cleared"],
                ["Day 14", "High (peak, but late)", "Returning to normal", "Recovering", "Fully recovered"],
                ["Day 21", "Declining", "Low (memory cells remain)", "Mostly recovered", "Immune memory stored"]
            ],
            "prompts": [
                "How many days does it take the unvaccinated person to reach peak antibodies? The vaccinated person?",
                "Why does the vaccinated person clear the infection by Day 7 while the unvaccinated person is still severely ill?",
                "On Day 21, the vaccinated person has low antibody levels. Does this mean the vaccine stopped working? Explain."
            ]
        }
    },

    "G07L2-L02": {
        # DNA Decoded
        "scientist": {
            "name": "Dr. William Chang",
            "title": "Epigenetics Researcher",
            "workplace": "Johns Hopkins School of Medicine, Center for Epigenetics",
            "salary": "$85K-$140K/year",
            "education": "B.S. in Genetics, Ph.D. in Molecular Biology",
            "what_they_model": "How environmental factors like diet, stress, and pollution switch genes on and off without changing the DNA sequence itself"
        },
        "additional_career": {
            "name": "Genetic Counselor",
            "description": "Helps families understand genetic test results and make informed decisions about inherited conditions, translating complex DNA data into clear guidance.",
            "salary": "$65K-$100K/year",
            "education": "M.S. in Genetic Counseling"
        },
        "spotlight": {
            "title": "Identical Twins Who Look Different: The Power of Epigenetics",
            "narrative": "Identical twins share 100% of the same DNA. So why do some identical twins develop different diseases, have different body types, or even look slightly different as they age? The answer is epigenetics. While twins start with the same genetic blueprint, their different life experiences — what they eat, where they live, how much stress they face — cause different genes to be switched on or off. Dr. William Chang studied pairs of identical twins where one twin developed cancer and the other didn't. He found that the twins' epigenetic markers had diverged significantly over time. The twin who developed cancer had certain tumor-suppressing genes switched OFF. Same DNA, different gene expression, different health outcomes.",
            "discussion_prompt": "If identical twins have the same DNA but can develop different diseases, what does this tell you about the relationship between genes and environment?"
        },
        "extend_components": [
            ("Nutritional Intake", "Dr. Chang found that a mother's diet during pregnancy affects which genes are switched on in her child — folic acid, for example, activates genes that prevent spinal cord defects"),
            ("Generational Inheritance", "Some epigenetic changes can be passed to children and grandchildren — a grandmother's famine experience can affect her grandchild's metabolism"),
            ("Gene Silencing by Methylation", "Chemical tags called methyl groups attach to DNA and silence specific genes — Dr. Chang maps these tags across the genome to understand which genes are active or quiet")
        ],
        "data": {
            "title": "Gene Expression Differences in Identical Twins Over Time",
            "type": "table",
            "headers": ["Twin Age", "Shared Epigenetic Patterns", "Different Epigenetic Patterns", "Health Differences Observed"],
            "rows": [
                ["3 years", "97%", "3%", "Virtually none"],
                ["10 years", "92%", "8%", "Minor (allergies, height)"],
                ["25 years", "80%", "20%", "Moderate (weight, fitness)"],
                ["50 years", "65%", "35%", "Significant (disease risk)"],
                ["70 years", "50%", "50%", "Major (different diseases, different aging)"]
            ],
            "prompts": [
                "What happens to the percentage of shared epigenetic patterns as twins age?",
                "At age 3, twins share 97% of their epigenetic patterns. By 70, only 50%. What causes this divergence?",
                "If genes were the only thing that mattered, would identical twins always get the same diseases? What does this data tell you?"
            ]
        }
    },

    "G07L2-L03": {
        # Ocean Currents and Climate
        "scientist": {
            "name": "Dr. Fatima Al-Zahrani",
            "title": "Physical Oceanographer",
            "workplace": "Woods Hole Oceanographic Institution (WHOI)",
            "salary": "$80K-$130K/year",
            "education": "B.S. in Ocean Sciences, Ph.D. in Physical Oceanography",
            "what_they_model": "How ocean currents distribute heat around the globe — and what happens to climate patterns when currents weaken or shift"
        },
        "additional_career": {
            "name": "Climate Data Analyst",
            "description": "Processes satellite and buoy data to track ocean temperatures, current speeds, and ice coverage, providing critical input for climate models.",
            "salary": "$55K-$90K/year",
            "education": "B.S. in Data Science, Environmental Science, or Oceanography"
        },
        "spotlight": {
            "title": "The Gulf Stream: Why London Is Warmer Than Montreal",
            "narrative": "London, England sits at 51°N latitude — the same latitude as Calgary, Canada, where winter temperatures regularly drop to −20°C. Yet London rarely sees temperatures below 0°C. The reason is the Gulf Stream, a massive ocean current that carries warm water from the Gulf of Mexico across the Atlantic to Europe. This current transfers enough heat to warm Western Europe by 5-10°C compared to what it would be without the current. It's like a giant underwater heating system. Dr. Fatima Al-Zahrani monitors the Gulf Stream because climate models show it may be weakening. If Greenland's ice sheet melts, the influx of cold freshwater could disrupt the current, paradoxically making parts of Europe COLDER even as the rest of the world warms.",
            "discussion_prompt": "How could global warming actually make parts of Europe colder? Use what you know about ocean currents and heat distribution."
        },
        "extend_components": [
            ("Salinity Gradient", "Dr. Al-Zahrani measures ocean saltiness because salty water is denser and sinks, driving deep ocean circulation — melting glaciers add freshwater that disrupts this process"),
            ("Coriolis Effect", "Earth's rotation curves ocean currents to the right in the Northern Hemisphere and left in the Southern — without this, currents would flow in straight lines"),
            ("Thermohaline Circulation", "The 'global conveyor belt' takes about 1,000 years for water to complete one full loop around the world's oceans, distributing heat from equator to poles")
        ],
        "data": {
            "title": "Cities at Similar Latitudes: Temperature Comparison",
            "type": "table",
            "headers": ["City", "Latitude", "Nearest Ocean Current", "Average January Temp (°C)", "Average July Temp (°C)"],
            "rows": [
                ["London, UK", "51°N", "Gulf Stream (warm)", "5°C", "18°C"],
                ["Calgary, Canada", "51°N", "None (inland)", "−8°C", "16°C"],
                ["Paris, France", "49°N", "North Atlantic Drift (warm)", "4°C", "20°C"],
                ["Winnipeg, Canada", "50°N", "None (inland)", "−17°C", "20°C"],
                ["Seattle, USA", "48°N", "North Pacific Current (warm)", "5°C", "19°C"],
                ["Newfoundland, Canada", "48°N", "Labrador Current (cold)", "−4°C", "16°C"]
            ],
            "prompts": [
                "London and Calgary are at the same latitude. Why is London 13°C warmer in January?",
                "Newfoundland and Seattle are also at the same latitude, but Newfoundland is much colder. What current is responsible?",
                "Based on this data, would you rather live near a warm ocean current or a cold one? What tradeoffs might exist?"
            ]
        }
    },

    "G07L2-L04": {
        # Newton's Laws
        "scientist": {
            "name": "Dr. Jerome Williams",
            "title": "Aerospace Dynamics Engineer",
            "workplace": "SpaceX, Flight Dynamics Division",
            "salary": "$100K-$160K/year",
            "education": "B.S. in Aerospace Engineering, M.S. in Applied Physics",
            "what_they_model": "How Newton's laws govern rocket launches, orbital maneuvers, and spacecraft landings — calculating the precise forces needed for every mission"
        },
        "additional_career": {
            "name": "Biomechanics Technician",
            "description": "Applies Newton's laws to human movement, using motion capture and force plates to analyze athletes' performance and prevent injuries.",
            "salary": "$45K-$75K/year",
            "education": "B.S. in Kinesiology or Biomedical Engineering"
        },
        "spotlight": {
            "title": "The Falcon 9 Landing: Newton's Laws Make the Impossible Routine",
            "narrative": "On December 21, 2015, SpaceX's Falcon 9 rocket launched 11 satellites into orbit, then did something that had never been done before: the first-stage booster turned around, reignited its engines, and landed vertically back on the launch pad. This impossible-seeming feat is pure Newton's laws in action. Newton's Third Law: the engines push exhaust gas downward, and the exhaust pushes the rocket upward with equal force. Newton's Second Law: the thrust force must be precisely calculated relative to the rocket's changing mass (it gets lighter as fuel burns). Newton's First Law: without engine corrections, the rocket would continue in whatever direction it was moving. Dr. Jerome Williams calculates these forces to within fractions of a second for every SpaceX mission.",
            "discussion_prompt": "As a rocket burns fuel, it gets lighter. According to Newton's Second Law (F=ma), what happens to its acceleration if the force stays the same but the mass decreases?"
        },
        "extend_components": [
            ("Aerodynamic Drag", "Dr. Williams accounts for air resistance that opposes rocket motion — drag increases with speed squared, so doubling speed means four times the drag"),
            ("Gravitational Pull Variation", "Gravity weakens with altitude — at the International Space Station's orbit (400 km up), gravity is still 89% of surface gravity, not zero"),
            ("Momentum Conservation", "In space with no friction, objects keep moving forever (Newton's First Law) — Dr. Williams uses this to plan fuel-free coasting phases between engine burns")
        ],
        "data": {
            "title": "Force, Mass, and Acceleration: Newton's Second Law in Action",
            "type": "table",
            "headers": ["Object", "Force Applied (N)", "Mass (kg)", "Acceleration (m/s²)", "What's Happening"],
            "rows": [
                ["Shopping cart", "20", "10", "2.0", "Easy to push"],
                ["Shopping cart (full)", "20", "40", "0.5", "Much harder to push"],
                ["Soccer ball (kick)", "1,000", "0.45", "2,222", "Flies fast!"],
                ["Bowling ball (same kick)", "1,000", "7.0", "143", "Moves, but slowly"],
                ["Falcon 9 at launch", "7,607,000", "549,000", "13.8", "Liftoff (1.4g)"],
                ["Falcon 9 (nearly empty)", "7,607,000", "100,000", "76.1", "Much faster acceleration"]
            ],
            "prompts": [
                "When the same force is applied, what happens as mass increases? Write the pattern as a rule.",
                "The Falcon 9's acceleration increases from 13.8 to 76.1 m/s² during flight. Its force stays the same. What changed?",
                "If you could triple the force on a shopping cart, what would the new acceleration be? Show your calculation using F=ma."
            ]
        }
    },

    "G07L2-L05": {
        # Evolution in Action
        "scientist": {
            "name": "Dr. Sophia Nikolaou",
            "title": "Evolutionary Biologist",
            "workplace": "American Museum of Natural History, Sackler Institute",
            "salary": "$75K-$120K/year",
            "education": "B.S. in Biology, Ph.D. in Evolutionary Biology",
            "what_they_model": "How populations change over generations in response to environmental pressures — tracking evolution as it happens in real time"
        },
        "additional_career": {
            "name": "Bioinformatics Scientist",
            "description": "Uses computer algorithms to compare DNA sequences across species, mapping evolutionary relationships and identifying genes under selection pressure.",
            "salary": "$70K-$115K/year",
            "education": "B.S. in Biology + M.S. in Computer Science or Bioinformatics"
        },
        "spotlight": {
            "title": "The Peppered Moths: Watching Evolution Happen in Real Time",
            "narrative": "Before the Industrial Revolution in England, most peppered moths were light-colored with dark speckles, well camouflaged against pale lichen-covered tree bark. Dark moths existed but were rare — birds spotted and ate them easily. Then factories blackened trees with soot. Suddenly, light moths stood out against dark bark, and birds ate THEM instead. Within just 50 years, dark moths went from 2% to 95% of the population. When clean air laws reduced pollution and lichen grew back in the 1960s, the trend reversed — light moths became common again. Dr. Sophia Nikolaou uses the peppered moth as a textbook example of natural selection because the entire process was observed and documented within a human lifetime.",
            "discussion_prompt": "The peppered moth population shifted from 98% light to 95% dark in just 50 years. Did individual moths change color, or did the population change? What's the difference?"
        },
        "extend_components": [
            ("Mutation Rate", "Dr. Nikolaou tracks random DNA mutations that introduce new traits into populations — most are neutral, some are harmful, and rarely, one is beneficial"),
            ("Gene Flow Between Populations", "When individuals migrate between groups, they bring new genetic variations — isolated populations evolve differently from connected ones"),
            ("Sexual Selection", "Not all selection is about survival — peacock tails, bird songs, and bright colors evolved because they attract mates, even though they may reduce survival")
        ],
        "data": {
            "title": "Peppered Moth Population Changes Over Time",
            "type": "table",
            "headers": ["Year", "Tree Bark Color", "Light Moths (%)", "Dark Moths (%)", "Pollution Level"],
            "rows": [
                ["1848", "Light (lichen-covered)", "98%", "2%", "Low (pre-industrial)"],
                ["1895", "Dark (soot-covered)", "50%", "50%", "High"],
                ["1920", "Very dark (heavy soot)", "5%", "95%", "Very high"],
                ["1960", "Dark (still polluted)", "10%", "90%", "Moderate (clean air acts)"],
                ["1990", "Light (lichen returning)", "60%", "40%", "Low"],
                ["2020", "Light (clean)", "85%", "15%", "Very low"]
            ],
            "prompts": [
                "What caused the dark moth percentage to rise from 2% to 95% between 1848 and 1920?",
                "After the Clean Air Act, the population shifted back toward light moths. Did dark moths 'evolve back' into light moths? Explain what actually happened.",
                "If pollution returned tomorrow, what would you predict would happen to the moth population? How fast?"
            ]
        }
    },

    "G07L2-L06": {
        # Electromagnetic Spectrum
        "scientist": {
            "name": "Dr. Raj Patel",
            "title": "Radio Frequency Engineer",
            "workplace": "NASA Jet Propulsion Laboratory (JPL), Deep Space Network",
            "salary": "$95K-$150K/year",
            "education": "B.S. in Electrical Engineering, Ph.D. in Electromagnetic Theory",
            "what_they_model": "How electromagnetic waves of different frequencies travel through space, atmosphere, and matter — enabling communication with spacecraft billions of miles away"
        },
        "additional_career": {
            "name": "Medical Imaging Technologist",
            "description": "Operates X-ray, MRI, and CT machines that use different parts of the electromagnetic spectrum to see inside the human body without surgery.",
            "salary": "$50K-$80K/year",
            "education": "Associate's or B.S. in Radiologic Technology"
        },
        "spotlight": {
            "title": "The Voyager Golden Record: A Message Carried by Electromagnetic Waves",
            "narrative": "In 1977, NASA launched Voyager 1 and Voyager 2 into space, each carrying a golden record with sounds and images representing life on Earth — greetings in 55 languages, music from Beethoven to Chuck Berry, and nature sounds from whale songs to thunder. Today, Voyager 1 is over 15 billion miles from Earth. The only way it can communicate with us is through radio waves, a form of electromagnetic radiation traveling at the speed of light. Even at light speed, Voyager's signals take over 22 hours to reach Earth, and they arrive with the power of a 20-watt light bulb spread across a sphere bigger than the solar system. Dr. Raj Patel's 230-foot radio dishes can detect these impossibly faint signals and decode the data.",
            "discussion_prompt": "Voyager's radio signal takes 22 hours to reach Earth at the speed of light. If you sent a question, how long would you wait for an answer? Why?"
        },
        "extend_components": [
            ("Atmospheric Absorption", "Dr. Patel knows that Earth's atmosphere blocks most UV, X-rays, and gamma rays — which protects us but also means space telescopes are needed to observe these wavelengths"),
            ("Antenna Size vs. Wavelength", "Radio waves can be meters long, so radio telescopes must be enormous — the Arecibo dish was 305 meters wide, while optical telescopes need only be meters across"),
            ("Doppler Shift", "When a wave source moves away, its frequency decreases (redshift); when it approaches, frequency increases (blueshift) — Dr. Patel uses this to measure spacecraft speed")
        ],
        "data": {
            "title": "The Electromagnetic Spectrum: From Radio to Gamma",
            "type": "table",
            "headers": ["EM Wave Type", "Frequency (Hz)", "Wavelength", "Energy Level", "Common Use"],
            "rows": [
                ["Radio", "10³-10⁹", "Meters to km", "Lowest", "Communication, radio"],
                ["Microwave", "10⁹-10¹²", "Millimeters to cm", "Low", "Cooking, cell phones"],
                ["Infrared", "10¹²-10¹⁴", "Micrometers", "Moderate", "Heat sensing, remotes"],
                ["Visible Light", "4-8 × 10¹⁴", "400-700 nm", "Moderate", "Human vision"],
                ["Ultraviolet", "10¹⁵-10¹⁶", "Nanometers", "High", "Sunburn, sterilization"],
                ["X-ray", "10¹⁶-10¹⁹", "Picometers", "Very High", "Medical imaging"],
                ["Gamma Ray", "10¹⁹+", "Sub-picometers", "Highest", "Cancer treatment"]
            ],
            "prompts": [
                "As frequency increases across the spectrum, what happens to wavelength? What happens to energy?",
                "Why can radio waves pass through walls but gamma rays can pass through your body? How does energy relate to penetration?",
                "Your eyes can only detect visible light. What percentage of the electromagnetic spectrum can you actually see?"
            ]
        }
    },

    "G07L2-L07": {
        # Rock Cycle Deep Dive
        "scientist": {
            "name": "Dr. Laura Mendez",
            "title": "Petrologist (Rock Formation Scientist)",
            "workplace": "U.S. Geological Survey (USGS), Geology, Minerals, Energy, and Geophysics Division",
            "salary": "$75K-$120K/year",
            "education": "B.S. in Geology, Ph.D. in Petrology",
            "what_they_model": "How rocks transform between igneous, sedimentary, and metamorphic types over millions of years — and how to read Earth's history from rock layers"
        },
        "additional_career": {
            "name": "Mining Geologist",
            "description": "Locates valuable mineral deposits by understanding which rock types and formation processes create concentrations of gold, copper, lithium, and other resources.",
            "salary": "$65K-$110K/year",
            "education": "B.S. in Geology + field certification"
        },
        "spotlight": {
            "title": "The Marble Parthenon: A Metamorphic Masterpiece 2,500 Years Old",
            "narrative": "The Parthenon in Athens, Greece, was built in 438 BC from marble quarried on Mount Pentelicus. But marble isn't just any rock — it started as limestone, formed from the compressed shells of ancient sea creatures millions of years ago. Then tectonic forces pushed that limestone deep underground, where intense heat and pressure transformed it into marble, a metamorphic rock with interlocking crystals that gleam in sunlight. The same marble that Athenian sculptors carved into stunning statues began as tiny ocean organisms, was buried and crushed into limestone, then cooked into marble. Dr. Laura Mendez traces these transformations to understand how the rock cycle connects the ocean floor to mountain temples.",
            "discussion_prompt": "Marble started as sea creature shells, became limestone, then became marble. What would need to happen for that marble to become sedimentary rock again?"
        },
        "extend_components": [
            ("Mineral Composition", "Dr. Mendez analyzes the specific minerals in each rock to determine its history — granite contains quartz and feldspar, while basalt contains pyroxene and olivine"),
            ("Cooling Rate", "Igneous rocks that cool slowly underground (granite) have large visible crystals, while those that cool quickly at the surface (basalt) have tiny crystals or glassy texture"),
            ("Burial Depth", "The deeper a sedimentary rock is buried, the more heat and pressure it experiences — at about 200°C and several kilometers deep, metamorphism begins")
        ],
        "data": {
            "title": "Rock Types and Formation Conditions",
            "type": "table",
            "headers": ["Rock", "Type", "Formed By", "Temperature", "Pressure", "Time to Form"],
            "rows": [
                ["Granite", "Igneous (intrusive)", "Magma cooling underground", "700-900°C", "Moderate", "Thousands of years"],
                ["Basalt", "Igneous (extrusive)", "Lava cooling at surface", "1,000-1,200°C", "Low", "Days to weeks"],
                ["Sandstone", "Sedimentary", "Sand grains cemented", "Surface temp", "Low-Moderate", "Millions of years"],
                ["Limestone", "Sedimentary", "Shell/coral compression", "Surface temp", "Low-Moderate", "Millions of years"],
                ["Marble", "Metamorphic", "Limestone + heat/pressure", "200-800°C", "High", "Millions of years"],
                ["Slate", "Metamorphic", "Shale + heat/pressure", "200-500°C", "Moderate-High", "Millions of years"]
            ],
            "prompts": [
                "What is the main difference between how igneous and sedimentary rocks form?",
                "Granite and basalt are both igneous but look very different. What causes this difference?",
                "Trace the journey from sand on a beach to slate. How many rock cycle steps are involved?"
            ]
        }
    },

    # =========================================================================
    # GRADE 8 LEVEL 2 (7 lessons)
    # =========================================================================

    "G08L2-L01": {
        # Survival of the Fittest: Can You Outrun Natural Selection?
        "scientist": {
            "name": "Dr. Terrence Brooks",
            "title": "Population Genetics Researcher",
            "workplace": "Harvard University, Department of Organismic and Evolutionary Biology",
            "salary": "$85K-$140K/year",
            "education": "B.S. in Biology, Ph.D. in Population Genetics",
            "what_they_model": "How trait frequencies shift across generations under different selection pressures — predicting which populations will adapt and which will face extinction"
        },
        "additional_career": {
            "name": "Wildlife Genetics Lab Technician",
            "description": "Extracts and analyzes DNA from wildlife samples to measure genetic diversity in endangered populations, helping conservationists make data-driven decisions.",
            "salary": "$40K-$65K/year",
            "education": "B.S. in Biology or Genetics"
        },
        "spotlight": {
            "title": "The Cheetah Bottleneck: When a Species Nearly Lost the Race Against Extinction",
            "narrative": "About 10,000 years ago, a climate catastrophe killed nearly all cheetahs on Earth. The few that survived — perhaps fewer than 500 — became the ancestors of every cheetah alive today. This 'genetic bottleneck' left cheetahs with almost no genetic diversity. Modern cheetahs are so genetically similar that a skin graft from any cheetah will be accepted by any other cheetah without rejection — their immune systems can't tell the difference. This lack of diversity makes the entire species vulnerable: a single disease could potentially wipe out all 7,000 remaining cheetahs because none have unique resistance genes. Dr. Terrence Brooks studies genetic bottlenecks to help conservation programs prevent the same fate in other endangered species.",
            "discussion_prompt": "Why does a genetic bottleneck make a species MORE vulnerable to extinction, not less? Think about what diversity provides."
        },
        "extend_components": [
            ("Founder Effect", "Dr. Brooks studies how small groups that colonize new areas carry only a fraction of the original population's genetic diversity — like starting a new country with only 10 families"),
            ("Selective Breeding vs. Natural Selection", "Humans artificially select for specific traits in dogs and crops, but this REDUCES overall genetic diversity, making breeds vulnerable to disease"),
            ("Genetic Rescue", "Introducing individuals from a different population can restore genetic diversity — Florida panthers were saved from inbreeding by bringing in Texas cougars")
        ],
        "data": {
            "title": "Genetic Diversity and Species Vulnerability",
            "type": "table",
            "headers": ["Species", "Population Size", "Genetic Diversity Index", "Known Bottleneck?", "Extinction Risk"],
            "rows": [
                ["Cheetah", "7,000", "Very Low (0.01)", "Yes — 10,000 years ago", "Vulnerable"],
                ["Mountain Gorilla", "1,063", "Low (0.05)", "Yes — recent habitat loss", "Endangered"],
                ["Florida Panther", "230", "Very Low (0.02)", "Yes — isolation", "Critically Endangered"],
                ["White-tailed Deer", "30,000,000", "High (0.72)", "No", "Least Concern"],
                ["Gray Wolf", "300,000", "Moderate (0.45)", "Partial — regional", "Least Concern"],
                ["Tasmanian Devil", "25,000", "Low (0.08)", "Yes — facial tumor disease", "Endangered"]
            ],
            "prompts": [
                "What is the relationship between genetic diversity index and extinction risk?",
                "The white-tailed deer has 30 million individuals AND high genetic diversity. Why are BOTH numbers important for species survival?",
                "If Dr. Brooks could choose one species to receive genetic rescue first, which should it be based on this data? Justify your choice."
            ]
        }
    },

    "G08L2-L02": {
        # Trophic Cascades
        "scientist": {
            "name": "Dr. Jasmine Osei-Mensah",
            "title": "Trophic Cascade Ecologist",
            "workplace": "Yellowstone Center for Resources, National Park Service",
            "salary": "$70K-$115K/year",
            "education": "B.S. in Environmental Science, Ph.D. in Community Ecology",
            "what_they_model": "How adding or removing one species at the top of a food web creates ripple effects that transform entire ecosystems — from wolves changing rivers to sharks shaping seagrass"
        },
        "additional_career": {
            "name": "Wildlife Reintroduction Coordinator",
            "description": "Plans and manages programs that return species to ecosystems where they've been eliminated, monitoring the cascading effects on the entire food web.",
            "salary": "$50K-$85K/year",
            "education": "B.S. in Wildlife Management or Conservation Biology"
        },
        "spotlight": {
            "title": "Sea Otters, Sea Urchins, and Kelp Forests: A Cascade in the Pacific",
            "narrative": "Along the Pacific coast, sea otters eat sea urchins. Sea urchins eat kelp. When fur traders nearly hunted sea otters to extinction in the 1800s, sea urchin populations exploded and devoured entire kelp forests, turning lush underwater jungles into barren 'urchin barrens.' When sea otters were reintroduced and protected, they ate the urchins, and kelp forests grew back within a decade. Those kelp forests then provided habitat for hundreds of species — fish, crabs, seals, and seabirds. Scientists even discovered that kelp forests absorb enormous amounts of CO2, meaning that sea otters indirectly help fight climate change. Dr. Jasmine Osei-Mensah calls this a 'trophic cascade with climate benefits.'",
            "discussion_prompt": "How can protecting sea otters help fight climate change? Trace the chain of connections from otters to atmospheric CO2."
        },
        "extend_components": [
            ("Mesopredator Release", "Dr. Osei-Mensah studies what happens when apex predators disappear and medium-sized predators (mesopredators) take over, often causing even more damage to prey populations"),
            ("Landscape of Fear", "Prey animals change their behavior when predators are present — elk avoid open areas near rivers, allowing vegetation to grow back even before many elk are killed"),
            ("Ecosystem Engineer Effects", "Some species physically reshape their environment — beavers create wetlands, elephants knock over trees creating grasslands, and whales fertilize surface waters")
        ],
        "data": {
            "title": "Yellowstone Ecosystem Changes: Wolves Removed (1926) vs. Wolves Restored (1995)",
            "type": "table",
            "headers": ["Ecosystem Indicator", "1920 (Wolves Present)", "1990 (No Wolves)", "2020 (Wolves Restored)", "Direction of Change"],
            "rows": [
                ["Elk population", "8,000", "20,000", "6,000", "Returned to natural level"],
                ["Willow/aspen coverage", "Widespread", "Nearly gone", "Recovering strongly", "Major recovery"],
                ["Beaver colonies", "Many", "0-1", "12+", "Dramatic return"],
                ["Songbird species count", "High", "Declining", "Increasing", "Recovery underway"],
                ["Streambank erosion", "Low", "Severe", "Low — stabilizing", "Reversal"],
                ["Coyote population", "Low (wolves control)", "Very high", "Moderate", "Rebalanced"]
            ],
            "prompts": [
                "When wolves were removed, why did the COYOTE population also increase? What relationship do wolves and coyotes have?",
                "Beavers returned to Yellowstone after wolves were reintroduced, even though wolves don't interact with beavers directly. Trace the chain.",
                "Based on this data, would you say removing ONE species affected just prey, or the ENTIRE ecosystem? What evidence supports your answer?"
            ]
        }
    },

    "G08L2-L03": {
        # Why Baking Soda Explodes
        "scientist": {
            "name": "Dr. Nathan Kim",
            "title": "Reaction Kinetics Chemist",
            "workplace": "Argonne National Laboratory, Chemical Sciences Division",
            "salary": "$85K-$135K/year",
            "education": "B.S. in Chemistry, Ph.D. in Physical Chemistry",
            "what_they_model": "How fast chemical reactions occur and what controls the speed — temperature, concentration, surface area, and catalysts"
        },
        "additional_career": {
            "name": "Forensic Chemist",
            "description": "Analyzes chemical evidence from crime scenes — identifying unknown substances, matching explosive residues, and testifying in court about chemical reactions.",
            "salary": "$50K-$85K/year",
            "education": "B.S. in Chemistry or Forensic Science"
        },
        "spotlight": {
            "title": "The Hindenburg Disaster: When a Chemical Reaction Destroyed the World's Largest Airship",
            "narrative": "On May 6, 1937, the hydrogen-filled airship Hindenburg caught fire while landing in New Jersey. In just 34 seconds, the 804-foot airship was completely destroyed. For decades, scientists debated what started the fire. In 1997, NASA engineer Addison Bain proved that the fabric skin of the Hindenburg was coated with chemicals remarkably similar to rocket fuel — iron oxide and aluminum powder. A spark of static electricity ignited the skin, and the hydrogen gas inside provided endless fuel. The reaction was: 2H₂ + O₂ → 2H₂O (plus enormous heat). The water produced by burning hydrogen was invisible — what everyone saw as 'fire' was actually the fabric burning. Dr. Nathan Kim uses the Hindenburg as a lesson in how surface area (thin fabric), temperature (a spark), and reactant availability (pure hydrogen) can turn a mild reaction into a catastrophe.",
            "discussion_prompt": "The Hindenburg burned in 34 seconds. If the same amount of hydrogen were stored in a solid metal tank instead of spread across fabric skin, would it have burned as fast? Why or why not?"
        },
        "extend_components": [
            ("Gas Pressure in Sealed Systems", "Dr. Kim measures how gas production in a sealed container increases pressure — if pressure exceeds the container's strength, it explodes"),
            ("Exothermic vs. Endothermic", "Baking soda + vinegar is endothermic (absorbs heat, feels cold), while combustion reactions are exothermic (releases heat, feels hot) — both conserve mass"),
            ("Stoichiometric Ratios", "Dr. Kim calculates the exact ratio of reactants needed — too much baking soda or too much vinegar leaves unreacted material behind")
        ],
        "data": {
            "title": "Baking Soda + Vinegar Reaction: Variables and Results",
            "type": "table",
            "headers": ["Trial", "Baking Soda (g)", "Vinegar (mL)", "CO2 Produced (mL)", "Mass Before (g)", "Mass After (g)", "Mass of CO2 Gas"],
            "rows": [
                ["1", "5", "50", "610", "55.0", "53.8", "1.2 g"],
                ["2", "10", "50", "610", "60.0", "58.8", "1.2 g"],
                ["3", "5", "100", "1,220", "105.0", "102.6", "2.4 g"],
                ["4", "10", "100", "1,220", "110.0", "107.6", "2.4 g"],
                ["5 (sealed)", "5", "50", "610 (trapped)", "55.0", "55.0", "0 g (still inside)"]
            ],
            "prompts": [
                "In trials 1 and 2, the same amount of CO2 was produced even though trial 2 had twice the baking soda. Why?",
                "Compare trial 1 (open) and trial 5 (sealed). Why does the sealed container show zero mass loss?",
                "If mass is conserved, where did the 'missing' 1.2 grams go in trial 1? Did matter actually disappear?"
            ]
        }
    },

    "G08L2-L04": {
        # Climate Feedback Loops
        "scientist": {
            "name": "Dr. Kenji Nakamura",
            "title": "Climate Feedback Modeler",
            "workplace": "National Center for Atmospheric Research (NCAR), Boulder",
            "salary": "$90K-$145K/year",
            "education": "B.S. in Atmospheric Science, Ph.D. in Climate Physics",
            "what_they_model": "How feedback loops in the climate system can amplify small temperature changes into major shifts — identifying tipping points where change becomes irreversible"
        },
        "additional_career": {
            "name": "Sustainability Consultant",
            "description": "Helps businesses and cities measure their carbon footprint and develop plans to reduce emissions, using climate models to set science-based targets.",
            "salary": "$55K-$95K/year",
            "education": "B.S. in Environmental Science + MBA or sustainability certification"
        },
        "spotlight": {
            "title": "The Permafrost Time Bomb: 1.5 Trillion Tons of Carbon Waiting to Escape",
            "narrative": "Beneath the frozen tundra of Siberia, Alaska, and northern Canada lies permafrost — ground that has been frozen for thousands of years. Locked inside this permafrost is approximately 1.5 trillion tons of dead plants and animals that never decomposed because it was too cold. That's twice as much carbon as is currently in the entire atmosphere. As global temperatures rise, permafrost is thawing. When it thaws, bacteria begin decomposing the ancient organic matter, releasing CO2 and methane — a greenhouse gas 80 times more potent than CO2 over 20 years. This is a positive feedback loop: warming thaws permafrost, which releases greenhouse gases, which causes more warming, which thaws more permafrost. Dr. Kenji Nakamura's models suggest that if global temperatures rise 2°C above pre-industrial levels, enough permafrost could thaw to release carbon equivalent to decades of human emissions.",
            "discussion_prompt": "Why is the permafrost feedback loop called a 'positive feedback' even though its effects are negative for the climate? What does 'positive' mean in systems science?"
        },
        "extend_components": [
            ("Water Vapor Feedback", "Dr. Nakamura tracks how warming increases evaporation, putting more water vapor in the atmosphere — water vapor is a greenhouse gas, so this amplifies warming"),
            ("Cloud Feedback", "Clouds both cool Earth (reflecting sunlight) and warm it (trapping heat) — whether warming creates more cooling or warming clouds is climate science's biggest uncertainty"),
            ("Ocean Heat Absorption", "Oceans have absorbed 90% of the extra heat from climate change, but warmer oceans absorb less CO2, weakening nature's carbon sink over time")
        ],
        "data": {
            "title": "Climate Feedback Loops: Amplifying vs. Stabilizing",
            "type": "table",
            "headers": ["Feedback Loop", "Type", "Mechanism", "Effect on Warming", "Strength"],
            "rows": [
                ["Ice-albedo", "Amplifying (+)", "Less ice → less reflection → more warming", "Amplifies warming", "Strong"],
                ["Permafrost carbon", "Amplifying (+)", "Warming → thaw → CO2/CH4 release → more warming", "Amplifies warming", "Potentially massive"],
                ["Water vapor", "Amplifying (+)", "Warming → more evaporation → more greenhouse gas", "Amplifies warming", "Strong"],
                ["Plant growth", "Stabilizing (−)", "More CO2 → more photosynthesis → CO2 removed", "Reduces warming", "Moderate"],
                ["Weathering", "Stabilizing (−)", "Warming → more rain → rocks absorb more CO2", "Reduces warming", "Weak (slow)"]
            ],
            "prompts": [
                "Are there more amplifying or stabilizing feedbacks in this table? What does this suggest about the climate system's response to warming?",
                "Plant growth is a stabilizing feedback. Why isn't it strong enough to stop warming on its own?",
                "Dr. Nakamura calls permafrost a 'tipping point.' Based on the mechanism, why is it so dangerous once it starts?"
            ]
        }
    },

    "G08L2-L05": {
        # Potential to Kinetic: The Energy Transformation Chain
        "scientist": {
            "name": "Dr. Brianna Jackson",
            "title": "Energy Systems Physicist",
            "workplace": "Oak Ridge National Laboratory, Energy Transformation Division",
            "salary": "$85K-$140K/year",
            "education": "B.S. in Physics, Ph.D. in Energy Science",
            "what_they_model": "How energy transforms from one form to another in complex systems — from hydroelectric dams to regenerative braking in electric cars"
        },
        "additional_career": {
            "name": "Power Plant Operations Engineer",
            "description": "Monitors and controls energy conversion systems in power plants, ensuring maximum efficiency as chemical, thermal, and mechanical energy transform into electricity.",
            "salary": "$60K-$95K/year",
            "education": "B.S. in Electrical or Mechanical Engineering"
        },
        "spotlight": {
            "title": "Regenerative Braking: How Electric Cars Turn Stopping Energy Into Driving Energy",
            "narrative": "In a traditional car, when you press the brakes, friction pads clamp onto the wheels and convert all that kinetic energy into heat — wasted energy that dissipates into the air. Electric cars do something remarkable: when you lift your foot off the accelerator, the electric motor runs in reverse, becoming a generator. Instead of wasting kinetic energy as heat, it converts the car's motion back into electrical energy and stores it in the battery. This is regenerative braking, and it can recover 60-70% of the energy that would otherwise be lost. In stop-and-go city driving, regenerative braking can extend an electric car's range by 20-30%. Dr. Brianna Jackson models these energy transformations to design more efficient systems.",
            "discussion_prompt": "In a traditional car, braking wastes energy as heat. In an electric car, braking recovers energy. Why can't regenerative braking recover 100% of the energy?"
        },
        "extend_components": [
            ("Elastic vs. Inelastic Collisions", "Dr. Jackson distinguishes between collisions where kinetic energy is conserved (elastic, like billiard balls) and those where it's converted to heat and sound (inelastic, like car crashes)"),
            ("Energy Conversion Efficiency", "No real energy conversion is 100% efficient — gas engines convert only 25% of fuel energy to motion, while electric motors convert 90%"),
            ("Gravitational Potential Energy Storage", "Pumped hydro storage lifts water uphill when electricity is cheap, then lets it flow downhill through turbines when electricity is needed — storing energy as height")
        ],
        "data": {
            "title": "Energy Transformation Efficiency in Common Systems",
            "type": "table",
            "headers": ["System", "Input Energy", "Useful Output", "Efficiency", "Where 'Lost' Energy Goes"],
            "rows": [
                ["Incandescent bulb", "Electrical", "Light", "5%", "95% becomes heat"],
                ["LED bulb", "Electrical", "Light", "40%", "60% becomes heat"],
                ["Gas car engine", "Chemical (fuel)", "Kinetic (motion)", "25%", "75% heat + exhaust"],
                ["Electric motor", "Electrical", "Kinetic (motion)", "90%", "10% heat"],
                ["Solar panel", "Light", "Electrical", "22%", "78% heat + reflection"],
                ["Human body", "Chemical (food)", "Kinetic + thermal", "25%", "75% heat (body warmth)"]
            ],
            "prompts": [
                "Which system is most efficient? Which is least? Why do you think there's such a big range?",
                "An LED bulb is 8 times more efficient than an incandescent bulb. If both use 60 watts, how much light energy does each produce?",
                "Your body is only 25% efficient at converting food to motion. Where does the other 75% go? Is that energy truly 'wasted'?"
            ]
        }
    },

    "G08L2-L06": {
        # Genetic Mutations
        "scientist": {
            "name": "Dr. Michelle Liu",
            "title": "Cancer Genetics Researcher",
            "workplace": "Memorial Sloan Kettering Cancer Center",
            "salary": "$95K-$155K/year",
            "education": "B.S. in Molecular Biology, M.D./Ph.D. in Cancer Genetics",
            "what_they_model": "How DNA mutations accumulate over a person's lifetime and how specific mutations transform normal cells into cancer cells"
        },
        "additional_career": {
            "name": "Genetic Testing Lab Scientist",
            "description": "Analyzes patient DNA samples to identify mutations linked to inherited diseases, drug sensitivities, and cancer risk, providing data that guides treatment decisions.",
            "salary": "$55K-$85K/year",
            "education": "B.S. in Genetics or Molecular Biology + certification"
        },
        "spotlight": {
            "title": "The Tasmanian Devil: A Cancer That's Contagious",
            "narrative": "In the mid-1990s, Tasmanian devils began dying from a horrifying disease: Devil Facial Tumor Disease (DFTD). Unlike human cancers, DFTD is contagious — it spreads when devils bite each other's faces during fights. The tumor cells from one devil can survive in another devil's body because Tasmanian devils have such low genetic diversity (from a population bottleneck) that their immune systems can't tell the difference between their own cells and the invading tumor cells. Since 1996, DFTD has killed over 80% of the Tasmanian devil population. Dr. Michelle Liu studies DFTD because it reveals how genetic diversity protects against disease — if the devils had more diverse immune system genes, their bodies would recognize and destroy the foreign tumor cells.",
            "discussion_prompt": "Why can DFTD spread between Tasmanian devils but human cancers can't spread between people? What role does genetic diversity play?"
        },
        "extend_components": [
            ("DNA Repair Mechanisms", "Dr. Liu studies the proteins that fix DNA copying errors — your cells fix about 99.99% of mistakes, but the remaining 0.01% can accumulate over decades"),
            ("Tumor Suppressor Genes", "Certain genes act as 'brakes' on cell division — when these genes are mutated (like BRCA1 or p53), cells can grow uncontrollably"),
            ("Environmental Mutagens", "Beyond UV radiation, chemicals in cigarette smoke, industrial pollution, and even charred meat can damage DNA and increase mutation rates")
        ],
        "data": {
            "title": "Mutation Types and Their Effects on Organisms",
            "type": "table",
            "headers": ["Mutation Type", "What Happens to DNA", "Effect on Protein", "Effect on Organism", "Example"],
            "rows": [
                ["Silent", "Base changes, same amino acid", "No change", "None", "Most mutations"],
                ["Missense", "Base changes, different amino acid", "Slightly altered", "Usually mild", "Sickle cell trait (1 copy)"],
                ["Nonsense", "Creates early stop signal", "Truncated (shortened)", "Often harmful", "Some muscular dystrophies"],
                ["Frameshift", "Insertion/deletion shifts reading", "Completely wrong", "Usually severe", "Cystic fibrosis (some forms)"],
                ["Beneficial", "Changes that improve function", "Enhanced", "Advantageous", "Lactose tolerance in adults"]
            ],
            "prompts": [
                "Most mutations are 'silent' — they don't change the protein. Why would this be important for species survival?",
                "Sickle cell trait (one mutated copy) provides malaria resistance but sickle cell disease (two copies) is harmful. How can the same mutation be both beneficial and harmful?",
                "Lactose tolerance in adults is a beneficial mutation that spread through human populations. Using natural selection, explain why."
            ]
        }
    },

    "G08L2-L07": {
        # Wave Properties
        "scientist": {
            "name": "Dr. Antonio Reyes",
            "title": "Acoustical Physicist",
            "workplace": "Penn State Applied Research Laboratory, Underwater Acoustics Division",
            "salary": "$80K-$130K/year",
            "education": "B.S. in Physics, Ph.D. in Acoustics",
            "what_they_model": "How sound waves and other mechanical waves travel through different media — enabling everything from submarine sonar to earthquake early warning systems"
        },
        "additional_career": {
            "name": "Audio Engineer",
            "description": "Designs concert venues, recording studios, and sound systems by applying wave physics — controlling how sound reflects, absorbs, and resonates in different spaces.",
            "salary": "$45K-$85K/year",
            "education": "B.S. in Audio Engineering, Physics, or Music Technology"
        },
        "spotlight": {
            "title": "The Tacoma Narrows Bridge: The Day a Bridge Danced Itself to Death",
            "narrative": "On November 7, 1940, just four months after opening, the Tacoma Narrows Bridge in Washington State began swaying wildly in 40 mph winds. The bridge's roadway twisted and undulated in waves so dramatic that the last car to cross was tossed from lane to lane. Then the bridge tore itself apart and collapsed into Puget Sound. The cause? Resonance. The wind created vortices that pushed the bridge at its natural frequency — the specific frequency at which it naturally vibrated. Each push added more energy to the wave, like pushing a swing at just the right moment. The amplitude grew and grew until the bridge could no longer hold together. Dr. Antonio Reyes studies resonance to ensure that modern bridges, buildings, and aircraft are designed to avoid this catastrophic frequency matching.",
            "discussion_prompt": "Why does pushing a swing at its natural frequency make it go higher, but pushing at random times doesn't? How is this the same principle that destroyed the Tacoma Narrows Bridge?"
        },
        "extend_components": [
            ("Wave Interference", "Dr. Reyes models how two waves meeting can combine constructively (bigger wave) or destructively (waves cancel out) — noise-canceling headphones use destructive interference"),
            ("Resonance Frequency", "Every object has a natural vibration frequency — when an external force matches it, energy builds up dramatically, which can be useful (musical instruments) or destructive (bridges)"),
            ("Wave Diffraction", "Waves bend around obstacles and through openings — this is why you can hear someone around a corner, and why AM radio reaches farther than FM")
        ],
        "data": {
            "title": "Wave Properties in Different Media",
            "type": "table",
            "headers": ["Property", "Sound in Air", "Sound in Water", "Sound in Steel", "Light in Vacuum", "Light in Glass"],
            "rows": [
                ["Speed (m/s)", "343", "1,482", "5,960", "299,792,458", "200,000,000"],
                ["Can humans detect?", "Yes (20-20,000 Hz)", "Muffled", "Press ear to surface", "Yes (visible)", "Yes (visible)"],
                ["Blocked by?", "Walls, dense objects", "Not easily", "Not at all", "Opaque objects", "Opaque objects"],
                ["Frequency change in medium?", "No", "No", "No", "No", "No"],
                ["Wavelength change?", "N/A (source)", "Increases", "Increases", "N/A (source)", "Decreases"],
                ["Energy loss over distance", "High", "Low", "Very low", "Almost none", "Moderate"]
            ],
            "prompts": [
                "When sound enters water from air, its speed increases but its frequency stays the same. What must happen to the wavelength?",
                "Light slows down in glass but its frequency doesn't change. Using the wave equation (speed = frequency x wavelength), what happens to wavelength?",
                "Sound loses energy quickly in air but slowly in water. Why might whales use sound to communicate across entire ocean basins?"
            ]
        }
    }
}
