import random
from dice import *

def check_faction():
    array_faction = [ "0:...", "mindat", "heteri", "pirates", "lizardfolk", "mad tree god", "bugs", "centipede god", "chaos", "anteater alien", "jellyfish alien" ]
    return 'Faction Connection: ' + array_faction[roll1d10()]
