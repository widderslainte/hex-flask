from flask import Flask, render_template
import random
from encounter import *

app = Flask(__name__)

# Load the configuration from the instance folder
# app.config.from_pyfile('config.py')

def roll2d6():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    return total

def weathertype():
    rolls = roll2d6()
    if rolls < 7:
        return 'The forecast is bad, roll was: ' + str(rolls)
    else:
        return 'The forecast is good, roll was: ' + str(rolls)

def terraintype():
    rolls = roll2d6()
    if rolls < 7:
        return 'The terrain is jungle, roll was: ' + str(rolls)
    else:
        return 'The terrain is horrible jungle, roll was: ' + str(rolls)

def encounterdie():
    die = random.randint(1,6)
    if die == 1:
        return 'Wandering monster attacks!'
    elif die == 2:
        return 'Encounter a hazard.'
    else:
        return 'The day passes uneventfully.'

@app.route('/')
def hello_world():
    return render_template('index.html', message="Dungeon Science")

@app.route('/2d6')
def sample_2d6():
    sample = roll2d6()
    return 'Sample roll was: ' + str(sample)

@app.route('/weather/')
def sample_weather():
    weather = weathertype()
    return weather

@app.route('/jungle/')
def jungle():
    return 'You\'re in the jungle, baby!'

@app.route('/hex/')
def hexday():
    section = 'Hex Status'
    temperature = roll2d6()
    weather = weathertype()
    terrain = terraintype()
    encounter = encounterdie()
    return render_template('generic.html', title=section, status=temperature, weather=weather, terrain=terrain, encounter=encounter)

@app.route('/encounter/')
def encounter_generation():
    section = 'Encounter Layout'
    visibility = check_visibility()
    # print(check_elevation())
    elevation = check_elevation()
    # print(check_cover())
    cover = check_cover()
    # print(check_distance())
    distance = check_distance()
    # print(check_motivation())
    motivation = check_motivation()
    # print(check_reaction())
    reaction = check_reaction()
    return render_template('encounter.html', title=section, section=section, elevation=elevation, visibility=visibility, cover=cover, distance=distance, motivation=motivation, reaction=reaction)
