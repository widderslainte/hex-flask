import random

def standard_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    return total

def roll1d8():
    dice1 = random.randint(1,8)
    return dice1

def roll1d10():
    dice1 = random.randint(1,10)
    return dice1

def roll1d12():
    dice1 = random.randint(1,12)
    return dice1

def roll1d20():
    dice1 = random.randint(1,20)
    return dice1