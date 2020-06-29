import random
from dice import *


moss_potion_avail = "50"
moss_potion_amount = 3
moss_potion_cost = "500sp"
moss_poultice_avail = "50"
moss_poultice_amount = 3
moss_poultice_cost = "250sp"
apothecary_potion_avail = "50"
apothecary_potion_amount = 3
apothecary_potion_cost = "400sp"
apothecary_poultice_avail = "50"
apothecary_poultice_amount = 3
apothecary_poultice_cost = "250sp"

def check_moss():
    if roll1d100() < int(moss_potion_avail):
        num_potions = str(rolltbd(moss_potion_amount))
    else:
        num_potions = str(0)
    return 'Grandmother Moss has: ' + num_potions + ' healing potions at ' + moss_potion_cost

def check_moss_poultice():
    if roll1d100() < int(moss_poultice_avail):
        num_poultices = str(rolltbd(moss_poultice_amount))
    else:
        num_poultices = str(0)
    return 'Grandmother Moss has: ' + num_poultices + ' healing poultices at ' + moss_poultice_cost

def check_apoth():
    if roll1d100() < int(apothecary_potion_avail):
        num_potions = str(rolltbd(apothecary_potion_amount))
    else:
        num_potions = str(0)
    return 'Tuloi Apothecary has: ' + num_potions + ' healing potions at ' + apothecary_potion_cost

def check_apoth_poultice():
    if roll1d100() < int(moss_poultice_avail):
        num_poultices = str(rolltbd(apothecary_poultice_amount))
    else:
        num_poultices = str(0)
    return 'Tuloi Apothecary has: ' + num_poultices + ' healing poultices at ' + apothecary_poultice_cost


print(check_moss())
print(check_moss_poultice())
print(check_apoth())
print(check_apoth_poultice())