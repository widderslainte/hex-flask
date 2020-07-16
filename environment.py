import random
from dice import *

# Determine temperature
def check_temperature():
    rolls = roll1d8()
    if rolls == 1:
        return 'Temperature:  Hot and sticky, (roll was: ' + str(rolls) + ')'
    elif rolls == 2:
        return 'Temperature:  Similar but more sticky, (roll was: ' + str(rolls) + ')'
    elif rolls == 3:
        return 'Temperature:  Similar but hotter, (roll was: ' + str(rolls) + ')'
    elif rolls == 4:
        return 'Temperature:  Slightly cooler and less sticky, (roll was: ' + str(rolls) + ')'
    elif rolls == 5:
        return 'Temperature:  Similar but wetter somehow, (roll was: ' + str(rolls) + ')'
    elif rolls == 6:
        return 'Temperature:  hotter but drier, (roll was: ' + str(rolls) + ')'
    elif rolls == 7:
        return 'Temperature:  Much cooler, (roll was: ' + str(rolls) + ')'
    else:
        return 'Temperature:  Remains the same, (roll was: ' + str(rolls) + ')'

# Determine weather
def check_weather():
    rolls = roll1d10()
    if rolls == 1:
        return 'Weather:  Still, (roll was: ' + str(rolls) + ')'
    elif rolls == 2:
        return 'Weather:  Breezy, (roll was: ' + str(rolls) + ')'
    elif rolls == 3:
        return 'Weather:  Gutsy, (roll was: ' + str(rolls) + ')'
    elif rolls == 4:
        return 'Weather:  Overcast, (roll was: ' + str(rolls) + ')'
    elif rolls == 5:
        return 'Weather:  Light rain, (roll was: ' + str(rolls) + ')'
    elif rolls == 6:
        return 'Weather:  Heavy rain, (roll was: ' + str(rolls) + ')'
    elif rolls == 7:
        return 'Weather:  Thunderstorm, (roll was: ' + str(rolls) + ')'
    elif rolls == 8:
        return 'Weather:  Foggy, (roll was: ' + str(rolls) + ')'
    elif rolls == 9:
        return 'Weather:  Misty and muggy, (roll was: ' + str(rolls) + ')'
    else:
        return 'Weather:  Remains the same, (roll was: ' + str(rolls) + ')'

def check_weather_change():
    rolls = roll2d6()
    if rolls < 7:
        return 'The weather gets worse, roll was: ' + str(rolls)
    elif rolls == 7:
        return 'The weather stays the same, roll was: ' + str(rolls)        
    else:
        return 'The weather gets milder, roll was: ' + str(rolls)

# # Determine local terrain
# def check_local_terrain():
#     rolls = roll2d6()

# # Determine sounds
# def check_sounds():
#     rolls = roll2d6()

# Determine odors
def check_odors():
    rolls = roll1d10()
    if rolls == 1:
        return 'Odors:  Nothing too foul, (roll was: ' + str(rolls) + ')'
    elif rolls == 2:
        return 'Odors:  Sulfur smell and rotten onions, (roll was: ' + str(rolls) + ')'
    elif rolls == 3:
        return 'Odors:  Decay and death, (roll was: ' + str(rolls) + ')'
    elif rolls == 4:
        return 'Odors:  Sweaty feet, (roll was: ' + str(rolls) + ')'
    elif rolls == 5:
        return 'Odors:  Rich like compost pile, (roll was: ' + str(rolls) + ')'
    elif rolls == 6:
        return 'Odors:  Headache causing odorless gas, (roll was: ' + str(rolls) + ')'
    elif rolls == 7:
        return 'Odors:  Metal scent and taste in air, (roll was: ' + str(rolls) + ')'
    elif rolls == 8:
        return 'Odors:  Faint smoke and ash, (roll was: ' + str(rolls) + ')'
    elif rolls == 9:
        return 'Odors:  Floral and sickly sweet, (roll was: ' + str(rolls) + ')'
    else:
        return 'Odors:  Very foul, (roll was: ' + str(rolls) + ')'

