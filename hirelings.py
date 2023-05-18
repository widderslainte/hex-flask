from dice import *
hd = 6

# Village or Small Town
## Number available
## Determine hireling or henchmen

# Large Town or City
## Number available
## Determine hireling or henchmen

# Determine hireling type
def check_hireling_type():
    # roll = roll1d6()
    # if roll <= 2:
    #     hireling_type="Man-at-arms"
    # elif roll == 6:
    #     hireling_type="War dog"
    # else:
    #     hireling_type="Torchbearer"
    # return hireling_type
    hireling = {
        'War dog': 8,
        'Man-at-arms': 6,
        'Man-at-arms': 6,
        'Torchbearer': 4,
        'Torchbearer': 4,
        'Torchbearer': 4,
    }
    hireling_type = random.choice(list(hireling.keys()))
    hit_points = random.randint(1, hireling[hireling_type]) + (hireling[hireling_type] // 2)
    return "Type: " + hireling_type, 'HP: ' + str(hit_points)


# Determine henchmen type
def check_character_class():
    roll = roll1d10()
    if roll == 1:
        character_class="Magician"
        hd = 4
    elif roll == 2:
        character_class="Priest"
        hd = 8
    elif roll == 3:
        character_class="Priest"
        hd = 8
    elif 4 < roll <= 6:
        character_class="Burglar"
        hd = 6
    else:
        character_class="Warrior"
        hd = 10
    return 'Class: ' + character_class  

# Ancestry
def check_common_ancestry():
    roll = roll1d10()
    if roll == 1:
        ancestry="Ancestry: Maetah"
    elif roll == 2:
        ancestry="Ancestry: Chlendi"
    elif roll == 3:
        ancestry="Ancestry: Heteri"
    elif roll == 4:
        ancestry="Ancestry: Mindat"
    elif roll == 5:
        ancestry="Ancestry: Eskla"
    else:
        ancestry="Ancestry: Dominant for Region"
    return ancestry   

# HP
def check_hp():
    hp = str(random.randint(1,hd))
    return 'HP: ' + hp

# Sex	
def check_gender():
    roll = roll1d6()
    if roll < 4:
        alignment="Gender: Female"
    else:
        alignment="Gender: Male"
    return alignment

# Weapon	
# Armor	

def check_alignment():
    Alignment	= ["Chaos", "Neutral", "Law"]
    roll = roll1d6()
    if roll == 1:
        alignment="Alignment: Chaos"
    elif roll == 6:
        alignment="Alignment: Law"
    else:
        alignment="Alignment: Neutral"
    return alignment

# Background	
# Possessions & Knowledge	
# Notable Features

# Name
## http://discourseanddragons.blogspot.com/2010/01/hireling-name-generator-revised.html
# 
#  