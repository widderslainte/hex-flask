import random
from dice import *

# Cover
def check_cover():
    rolls = roll2d6()
    if rolls == 2:
        return 'Cover:       Monster - hard, (roll was: ' + str(rolls) + ')'
    elif rolls == 3:
        return 'Cover:       Monster - soft, (roll was: ' + str(rolls) + ')'
    elif rolls == 4:
        return 'Cover:       Left (of PCs) - hard, (roll was: ' + str(rolls) + ')'
    elif rolls == 5:
        return 'Cover:       Left (of PCs) - soft, (roll was: ' + str(rolls) + ')'
    elif rolls == 9:
        return 'Cover:       Right (of PCs) - soft, (roll was: ' + str(rolls) + ')'
    elif rolls == 10:
        return 'Cover:       Right (of PCs) - hard, (roll was: ' + str(rolls) + ')'
    elif rolls == 11:
        return 'Cover:       PCs - soft, (roll was: ' + str(rolls) + ')'
    elif rolls == 12:
        return 'Cover:       PCs - hard, (roll was: ' + str(rolls) + ')'
    else:
        return 'Cover:       None, (roll was: ' + str(rolls) + ')'

# Distance
def check_distance():
    rolls = roll2d6() * 10
    return 'Distance:    ' + str(rolls) + ' feet/yards'

# Elevation
def check_elevation():
    rolls = roll2d6()
    if 2 <= rolls <= 3:
        return 'Elevation:   Monster higher, (roll was: ' + str(rolls) + ')'
    elif rolls == 4:
        return 'Elevation:   Center higher, (roll was: ' + str(rolls) + ')'
    elif rolls == 5:
        return 'Elevation:   Left higher, (roll was: ' + str(rolls) + ')'
    elif rolls == 9:
        return 'Elevation:   Center lower, (roll was: ' + str(rolls) + ')'
    elif rolls == 10:
        return 'Elevation:   Right higher, (roll was: ' + str(rolls) + ')'
    elif 11 <= rolls <= 12:
        return 'Elevation:   Character higher, (roll was: ' + str(rolls) + ')'
    else:
        return 'Elevation:   Elevation level, (roll was: ' + str(rolls) + ')'

# Motivation
def check_motivation():
    rolls = roll2d6()
    if rolls == 2:
        return 'Motivation:  Lost or escaping, (roll was: ' + str(rolls) + ')'
    elif 3 <= rolls <= 4:
        return 'Motivation:  Overcoming obstacle, (roll was: ' + str(rolls) + ')'
    elif 5 <= rolls <= 6:
        return 'Motivation:  Resting, (roll was: ' + str(rolls) + ')'
    elif 9 <= rolls <= 10:
        return 'Motivation:  Searching for lost person or item, (roll was: ' + str(rolls) + ')'
    elif rolls == 11:
        return 'Motivation:  Guarding or near lair, (roll was: ' + str(rolls) + ')'
    elif rolls == 12:
        return 'Motivation:  Fleeing encounter, (roll was: ' + str(rolls) + ')'
    else:
        return 'Motivation:  Seeking food/shelter, (roll was: ' + str(rolls) + ')'

# Reaction
def check_reaction():
    rolls = roll2d6()
    if rolls == 2:
        return 'Reaction:    Immediate Attack, (roll was: ' + str(rolls) + ')'
    elif rolls == 12:
        return 'Reaction:    Enthusiastic Friendship, (roll was: ' + str(rolls) + ')'
    elif 3 <= rolls <= 5:
        return 'Reaction:    Hostile - Possible Attack, (roll was: ' + str(rolls) + ')'
    elif 9 <= rolls <= 11:
        return 'Reaction:    No Attack - Leaves or Considers Offers, (roll was: ' + str(rolls) + ')'
    else:
        return 'Reaction:    Uncertain or Confused, (roll was: ' + str(rolls) + ')'

# Visibility
def check_visibility():
    rolls = roll2d6()
    if rolls < 4:
        return 'Visibility:  Misty/Smoke/Foliage  (roll was: ' + str(rolls) + ')'
    else:
        return 'Visibility:  Clear  (roll was: ' + str(rolls) + ')'

