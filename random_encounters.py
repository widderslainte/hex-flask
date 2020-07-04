import random
from dice import *
# Hazard	Roll on the appropriate terrain table for a non-monster hazard or hardship	
# Wandering	Roll on the appropriate region Wandering Monster table below and consult that entry in the rulebook for number appearing	
# Monster Lair	Same as above but use lair numbers.  These are the locations that must be dealt with to change a hex to 'Civilized' as below	
# Locale	A dungeon or prepared adventure location or feature of note.  Replaced with Monster Lair if the DM determines that the hex has no more Locales	

# Grab forbidden lands mishaps, scarlet heroes?

# Unexplored
def check_unexplored():
    array_unexplored = [ "0", "1) Nothing", "2) Nothing", "3) Nothing", "4) Nothing", "5) Nothing","6) Hazard", "7) Hazard", "8) Wandering", "9) Wandering", "10) Hazard and Wandering", "11) Monster Lair", "12) Locale" ]
    return 'Unexplored Hex encounter: ' + array_unexplored[roll1d12()]

# Explored
def check_explored():
    array_explored = [ "0", "1) Nothing", "2) Nothing", "3) Nothing", "4) Nothing", "5) Nothing", "6) Nothing", "7) Nothing", "8) Hazard", "9) Wandering", "10) Hazard and Wandering", "11) Monster Lair", "12) Locale" ]
    return 'Explored Hex encounter: ' + array_explored[roll1d12()]

# Obstacle
def check_obstacle():
    array_obstacle = [ "0", "1) Canal, no bridge or guarded bridge", "2) Central square with lots of movement and activity, very exposed", "3) Giant workplace (leather, rope, wood, stone, food prep)", "4) Overgrowth - detour or hack through (extra encounter check)", "5) Collapsed buildings, climb or detour", "6) Cleared road, wall rigged to collapse, 1d4 Giants in hiding nearby", "7) Giants digging into building for treasure, few outside on break", "8) Marketplace - Urgruk giants trading magic baubles with Dorraan for food & tools", "9) Fallen sky bridge - climb (roll resource depletion) or detour for new encounter check","10) Tunnel rigged to collapse, nasty fall (dex14/19/23 for med/large/huge, 3d8 dmg and Covered with rock, str dc 25 to clear, or  str dc 20 and 3 checks)", "11) quicksand, darkmud, or recent mudslide", "12) hazardous plant - poison, irritant, or thorn", "13) hazardous plant - carnivorous", "14) insect swarm - mundane", "15) water hazard - waterfilled region or waterway ravine", "16) avoidable dangerous fauna - sleeping, eating, unaware", "17)...", "18)...", "19)..." ]
    return 'Obstacle: ' + array_obstacle[roll1d20()]

# Encounter time
def check_encounter_time():
    array_encounter_time = ["0", "1) Morning at-camp", "2) Morning", "3) Morning", "4) Afternoon at-rest", "5) Afternoon", "6) Afternoon", "7) Evening - making camp", "8) Evening", "9) Evening", "10) Night - First Watch", "11) Night - Second Watch", "12) Night - Third Watch" ]
    return 'Encounter Time: ' + array_encounter_time[roll1d12()]

# Wanderng Activities 2d4
def check_wander_activity():
    array_wander_activity = [ "0", "Lost", "Resting/wounded", "Exploring", "Hunting", "Eating", "Sleeping", "Fleeing", "8...", "9...", "10..." ]
    return 'Wandering Monster Activity: ' + array_wander_activity[roll1d10()]

# The encounter area should have something interesting about it. 
# Visually memorable. Something that presents threat, opportunity, beauty, or revulsion. 
# A threat is pretty obvious: a dragon slumbering on the other side of a rope-bridged chasm, 
# visible by the embers of his breath, a gauntlet of facing statues holding stone halberds aloft, etc. 