import random
from dice import *

# #### Uod General Encounter Tables, OSR Use
# _use Uod sub-tables for '-type' specific results_
 
uod_generic_civilized_region = ["0", "0", "Dragon-type", "Weird", "Outsider", "Monster-type", "Local Faction", "Cult-type", "Local Faction", "Local Fauna", "Humanoid", "Weird", "Wizard-type"]
uod_generic_wilderness_region = ["0", "0", "Dragon-type", "Weird", "Outsider", "Monster-type", "Local Faction", "Local Fauna", "Local Faction", "Cult-type", "Humanoid", "Weird", "Wizard-type"]
uod_generic_subterranean_region = ["0", "0", "Dragon-type", "Weird", "Outsider", "Monster-type", "Local Faction", "Cult-type", "Local Faction", "Humanoid", "Monster-tyepe", "Weird", "Wizard-type"]


# #### Uod General Encounter Tables, Jungle
# _use Uod sub-tables for '-type' specific results_
uod_jungle_civilized_region = ["0", "0", "2: Dragon-type", "3: Weird", "4: Outsider", "5: Monster-type", "6: Local Faction", "7: Cult-type", "8: Local Faction", "9: Local Fauna", "10: Humanoid", "11: Weird", "12: Wizard-type"]
uod_jungle_bug_region = ["0", "0", "2: Dragon-type", "3: Weird", "4: Outsider", "5: Monster-type", "6: Local Faction", "7: Local Fauna", "8: Local Faction", "9: Cult-type", "10: Metal Snail", "11: Weird", "12: Wizard-type" ]
uod_jungle_lizardfolk_region = ["0", "0", "2: Dragon-type", "3: Weird", "4: Outsider", "5: Giant frog/snake", "6: Local Faction", "7: Insect Swarm", "8: Local Faction", "9: Cult-type", "10: Boar", "11: Weird", "12: Wizard-type" ]
region_4_array = ["0", "0", "2: bug zombie", "3: insect swarm" "4: stirges", "5: giant snapping turtles", "6: insect, common", "7: animal, small", "8: giant leeches", "9: malicious fish", "10: throat leeches", "11: snake, poisonous/constrictor", "12: Shambling mound" ]
region_3_array = ["0", "0", "2: dinosaur, common", "3: humanoid, common", "4: Animal", "5: Giant turtle", "6: Giant Leeches", "7: Stirges", "insect swarm", "crocodiles", "giant animal", "pterodactyl", "12: snake" ]
region_2_array = ["0", "0", "2: metal snail", "3: bug zombie", "forest snail", "insects, tiny", "insects, giant", "monkeys", "jaguar", "wild boars", "fish - 50% malicious", "shambling mound", "12: god whale" ]
region_1_array = ["0", "0", "2: wizard-type", "3: cannibals", "gator", "herd", "pterodactyl", "pirate scout", "insect, giant", "crab, giant", "snakes", "walking tree", "12: wood golem" ]
jungle_array_1 = ["0", "0", "2: rhakasha", "3: ooze", "giant frog", "pterodactyl", "bombardier beetle", "insect swarm", "centipede, huge", "boar, giant", "jaguar", "mongrelman", "12: dragon-type" ]
array2 = ["0", "2: Spiny Beetle Spiny 1d6", "3: Bat 2d4", "killer bees 3d2", "stirges d6", "giant snake", "Candlethieves d12", "centipedes - giant d6", "Swamp Snakes d8",  "shambling plants - vine horrors", "12: giant frog" ]
array3 = ["0", "2: Bug zombie", "3: shambling mound", "giant snapping turtle", "giant leeches", "stirges", "insect swarm", "crocodiles", "malicious fish", "other fish", "Snake, Constrictor", "Snake, Poisonous", "12: Throat Leech" ]

def check_uod_jungle_civilized_region():
    return 'Civilized Region Encounter: ' + uod_jungle_civilized_region[standard_roll()]

def check_uod_jungle_bug_region():
    return 'Bug Region Encounter: ' + uod_jungle_bug_region[standard_roll()]

def check_uod_jungle_lizardfolk_region():
    return 'Lizardfolk Region Encounter: ' + uod_jungle_lizardfolk_region[standard_roll()]

def check_array_1_region():
    return 'Array 1 Region Encounter: ' + region_1_array[standard_roll()]

def check_array_2_region():
    return 'Array 2 Region Encounter: ' + region_2_array[standard_roll()]

def check_array_3_region():
    return 'Array 3 Region Encounter: ' + region_3_array[standard_roll()]

def check_array_4_region():
    return 'Array 4 Region Encounter: ' + region_4_array[standard_roll()]

# print(check_uod_jungle_bug_region())
# print(check_array_1_region())
# print(check_array_2_region())
# print(check_array_3_region())
# print(check_array_4_region())
# print(check_uod_jungle_civilized_region())
# print(check_uod_jungle_lizardfolk_region())

# A. Encounter Type (ex. Intelligent, Beast, Lizardman, Plant)
# B. Specific Thing (roll on the appropriate subtable like "Beast")
# C. Motivation (ie subtable to determine if the beast is eating, sleeping, mating
# D. Ecology subtable: (modify the numbers if you want more enounters that are the signs of the creature and fewer actual encounters)
# 	1-3. You encounter the thing, then roll to determine if its in its lair
# 	4-5. Spoor (droppings, nest, torn up trees, etc.)
# 	6. Tracks