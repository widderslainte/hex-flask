import random
from dice import *

# #### Uod General Encounter Tables, OSR Use
# _use Uod sub-tables for '-type' specific results_
 
uod_generic_civilized_region = ["0", "0", "Dragon-type", "Weird", "Outsider", "Monster-type", "Local Faction", "Cult-type", "Local Faction", "Local Fauna", "Humanoid", "Weird", "Wizard-type"]
uod_generic_wilderness_region = ["0", "0", "Dragon-type", "Weird", "Outsider", "Monster-type", "Local Faction", "Local Fauna", "Local Faction", "Cult-type", "Humanoid", "Weird", "Wizard-type"]
uod_generic_subterranean_region = ["0", "0", "Dragon-type", "Weird", "Outsider", "Monster-type", "Local Faction", "Cult-type", "Local Faction", "Humanoid", "Monster-tyepe", "Weird", "Wizard-type"]


# #### Uod General Encounter Tables, Jungle
# _use Uod sub-tables for '-type' specific results_
uod_jungle_civilized_region = ["0", "0", "Dragon-type", "Weird", "Outsider", "Monster-type", "Local Faction", "Cult-type", "Local Faction", "Local Fauna","Humanoid", "Weird", "Wizard-type"]

uod_jungle_bug_region = ["0", "0", "Dragon-type", "Weird", "Outsider", "Monster-type", "Local Faction", "Local Fauna",
"Local Faction", "Cult-type", "Metal Snail", "Weird", "Wizard-type" ]

uod_jungle_lizardfolk_region = ["0", "0",
"Dragon-type",
"Weird",
"Outsider",
"giant frog/snake",
"Local Faction",
"Insect Swarm",
"Local Faction",
"Cult-type",
"Boar"
"Weird",
"Wizard-type"
]

region_4_array = ["0", "0",
"bug zombie",
"insect swarm"
"stirges",
"giant snapping turtles",
"insect, common",
"animal, small",
"giant leeches",
"malicious fish",
"throat leeches",
"snake, poisonous/constrictor",
"shambling mound"
]

region_3_array = ["0", "0",
"dinosaur, common",
"humanoid, common",
"animal",
"giant turtle",
"giant leeches",
"stirges",
"insect swarm",
"crocodiles",
"giant animal",
"pterodactyl",
"snake"
]

region_2_array = ["0", "0",
"metal snail",
"bug zombie",
"forest snail",
"insects, tiny",
"insects, giant",
"monkeys",
"jaguar",
"wild boars",
"fish - 50% malicious",
"shambling mound",
"god whale"
]

region_1_array = ["0", "0",
"wizard-type",
"cannibals",
"gator",
"herd",
"pterodactyl",
"pirate scout",
"insect, giant",
"crab, giant",
"snakes",
"walking tree",
"wood golem"
]

jungle_array_1 = [ "0", "0",
"rhakasha",
"ooze",
"giant frog",
"pterodactyl",
"bombardier beetle",
"insect swarm",
"centipede, huge",
"boar, giant",
"jaguar",
"mongrelman",
"dragon-type"
]

array2 = [ "0",
"Spiny Beetle Spiny 1d6",
"Bat 2d4",
"killer bees 3d2",
"stirges d6",
"giant snake",
"Candlethieves d12",
"centipedes - giant d6",
"Swamp Snakes d8", 
"shambling plants - vine horrors",
"giant frog"
]

array2 = [ "0",
"bug zombie",
"shambling mound",
"giant snapping turtle",
"giant leeches",
"stirges",
"insect swarm",
"crocodiles",
"malicious fish",
"other fish",
"Snake, Constrictor",
"Snake, Poisonous",
"Throat Leech"
]

x = standard_roll()
print(x)
print("")

encounter=uod_jungle_lizardfolk_region[x]

print(encounter)
