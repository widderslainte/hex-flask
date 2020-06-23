import random
from dice import *

# Obstacles Table - d10 Type
[ "Lair", "Encounter", "Encounter", "Construct", "Passage", "Obstruction", "Hazard", "Weather", "Water", "Ruins" ]

#Lair Table - d6 Type
[ "Burrow, Cave, Ledge, Rock Pile, or Mound",
"Trees (hollow or dwelling built in boughs/treetops)",
"Construct",
"Ruins",
"Water, Shipwreck, Underwater Cave, or Sunken Ruin",
"Floating Tower, Cloud Castle" ]

# Flying Ship Construct Table - d10 Type
[ "Monolith", "Barrow", "Pyramid", "Tower", "Spire", "Building", "Heap", "Signpost", "Isolated Farm", "Ruins" ]

# Passage Table - d6 Type
[ "Track", "Path", "Trail", "Dirt Road", "Gravel Road", "Paved Road" ]

# Obstruction Table
# | d6 | Clear      | Woods      | Desert | (d4) Swamp | (d3) Mountain Road |
# |----|------------|------------|--------|------------|--------------------|
# | 1  | Crater     | Crater     | Crater | Qksnd. Field Crater Stream1
# | 2  | Chasm      | Chasm      | Chasm  | Vegetation Chasm Chasm1
# | 3  | Cliff      | Cliff      | Cliff  | Dams Cliff Ravine1
# | 4  | Ravine     | Ravine     | Dry Ravine | - Ravine Road Block2
# | 5  | Swamp      | Swamp      |-       |-   | Volcanic Vents |Flooded
# | 6  | Vegetation | Vegetation |-       | -  | Vegetation | Vegetation


# Obstruction Jungle d6
["Crater", "Chasm", "Cliff", "Ravine", "Swamp", "Vegetation", "Quicksand/Mud"]

# 1: Indicates that a bridge is out for the listed feature. If in a swamp, any of these results indicate the road is flooded. In the desert, streams and ravines are treated as dry ravines.
# 2: Blocked by fallen tree in clear, woods, and swamp; blocked by rockslide in mountain; or road hidden by sand in desert.

# Conctruct d10
["1 Monolith", "2 Barrow", "3 Pyramid", "4 Tower", "5 Spire", "6 Building", "7 Heap", "8 Signpost", "9 Isolated Farm", "10 Ruins"]

# Passage d6
["1 Track", "2 Path", "3 Trail", "4 Dirt Road", "5 Gravel Road", "6 Paved Road"]