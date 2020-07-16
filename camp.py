import random
from dice import *

array_camp_features = [ "",
    "water (stream, pond)",
    "boulders", 
    "hollow tree (strangler fig)",
    "fallen tree",
    "thorn bushes",
    "cliff or ledge",
    "sink hole",
    "quicksand",
    "insects",
    "tangle of vines"
]

def check_camp():
    # if roll1d100() < int(moss_potion_avail):
    #     num_potions = str(rolltbd(moss_potion_amount))
    # else:
    #     num_potions = str(0)
    features = ""
    num_features = range(int(roll1d4()))
    for i in num_features:
        features = features + array_camp_features[roll1d10()] + ", "

    return 'Camp has: ' + features

# print(check_camp())
