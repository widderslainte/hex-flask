from dice import *

# Village or Small Town
## Number available
## Determine hireling or henchmen

# Large Town or City
## Number available
## Determine hireling or henchmen

# Determine hireling type
# * Torchbearer
# * Man-at-arms
# * War dog

# Determine henchmen type
def check_character_class():
    roll = roll1d10()
    if roll == 1:
        character_class="Magician"
    elif roll == 2:
        character_class="Priest"
    elif roll == 3:
        character_class="Priest"
    elif 4 < roll <= 6:
        character_class="Burglar"
    else:
        character_class="Warrior"  

# Ancestry
# def check_common_ancestry():
#     roll = roll1d10()
#     if roll == 1:
#         then ancestry="Ancestry: Maetah"
#     elif roll == 2:
#         then ancestry="Ancestry: Chlendi"
#     elif roll == 3:
#         then ancestry="Ancestry: Heteri"
#     elif roll == 4:
#         then ancestry="Ancestry: Mindat"
#     elif roll == 5:
#         then ancestry="Ancestry: Eskla"
#     else:
#         then ancestry="Ancestry: Dominant for Region"   

# HP
# def check_hp():	

# Sex	
# def check_alignment():
#     roll = roll1d6()
#     if roll < 4:
#         then alignment="Sex: Female"
#     else:
#         then alignment="Sex: Make"

# Weapon	
# Armor	
# Alignment	= ["Chaos", "Neutral", "Law"]

# def check_alignment():
#     roll = roll1d6()
#     if roll == 1:
#         then alignment="Alignment: Chaos"
#     elif roll == 6:
#         then alignment="Alignment: Law"
#     else:
#         then alignment="Alignment: Neutral"

# Background	
# Possessions & Knowledge	
# Notable Features

# Name
## http://discourseanddragons.blogspot.com/2010/01/hireling-name-generator-revised.html
# 
#  