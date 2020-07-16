import random
from dice import *

# Obstacles Table - d10 Type
ObstacleType = [ "Lair", "Encounter", "Encounter", "Construct", "Passage", "Obstruction", "Hazard", "Weather", "Water", "Ruins" ] # d10

# Flying Ship Construct Table - d10 Type
FlyingShipType = [ "Monolith", "Barrow", "Pyramid", "Tower", "Spire", "Building", "Heap", "Signpost", "Isolated Farm", "Ruins" ]

# Passage d6
PassageType = [ "Track", "Path", "Trail", "Dirt Road", "Gravel Road", "Paved Road" ] #d6

#Lair Table - d6 Type
LairType = [ "Burrow, Cave, Ledge, Rock Pile, or Mound", "Trees (hollow or dwelling built in boughs/treetops)", "Construct", "Ruins", "Water, Shipwreck, Underwater Cave, or Sunken Ruin", "Floating Tower, Cloud Castle" ]

# Obstruction Jungle d8
ObstructionJungle = ["Crater", "Chasm", "Cliff", "Ravine", "Swamp", "Vegetation", "Quicksand/Dark Mud", "Insect Swarm", "Cloud of Fungus Spores"]

# Conctruct d10
ConstructionType = ["1 Monolith", "2 Barrow", "3 Pyramid", "4 Tower", "5 Spire", "6 Building", "7 Heap", "8 Signpost", "9 Isolated Farm", "10 Ruins"]

# Passage d6
PassageType = ["", "1 Track", "2 Path", "3 Trail", "4 Dirt Road", "5 Gravel Road", "6 Stone Road"]

def check_passage_type ():
    passage = PassageType[roll1d6()]
    return passage


# Obstruction Table
# | d6 | Clear      | Woods      | Desert | (d4) Swamp | (d3) Mountain Road |
# |----|------------|------------|--------|------------|--------------------|
# | 1  | Crater     | Crater     | Crater | Qksnd. Field Crater Stream1
# | 2  | Chasm      | Chasm      | Chasm  | Vegetation Chasm Chasm1
# | 3  | Cliff      | Cliff      | Cliff  | Dams Cliff Ravine1
# | 4  | Ravine     | Ravine     | Dry Ravine | - Ravine Road Block2
# | 5  | Swamp      | Swamp      |-       |-   | Volcanic Vents |Flooded
# | 6  | Vegetation | Vegetation |-       | -  | Vegetation | Vegetation

# 1: Indicates that a bridge is out for the listed feature. If in a swamp, any of these results indicate the road is flooded. In the desert, streams and ravines are treated as dry ravines.
# 2: Blocked by fallen tree in clear, woods, and swamp; blocked by rockslide in mountain; or road hidden by sand in desert.

def check_obstacle_type ():
    output = foo

# primary_type = (ObstacleType[roll1d10()])
print(check_passage_type())