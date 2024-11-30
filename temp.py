import random

# Define the hit point rules for each character class
hit_dice = {
    'barbarian': 12,
    'bard': 8,
    'cleric': 8,
    'druid': 8,
    'fighter': 10,
    'monk': 8,
    'paladin': 10,
    'ranger': 10,
    'rogue': 8,
    'sorcerer': 6,
    'warlock': 8,
    'wizard': 6
}

# Randomly select a character class
char_class = random.choice(list(hit_dice.keys()))

# Roll hit points based on the character class
hit_points = random.randint(1, hit_dice[char_class]) + (hit_dice[char_class] // 2)

# Print the results
print(f"You are a {char_class} with {hit_points} hit points.")
