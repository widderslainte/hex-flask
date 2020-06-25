from flask import Flask, render_template
import random

from encounter import *
from environment import *
from random_encounters import *
from factions import *
from monsters_jungle import *

app = Flask(__name__)
source = '/app.py'

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
    return render_template('index.html', message="Dungeon Science", source=source)

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
    section = 'Encounter Scene Layout'
    visibility = check_visibility()
    elevation = check_elevation()
    cover = check_cover()
    distance = check_distance()
    motivation = check_motivation()
    reaction = check_reaction()
    return render_template('encounter.html', title=section, section=section, elevation=elevation, visibility=visibility, cover=cover, distance=distance, motivation=motivation, reaction=reaction)

@app.route('/environment/')
def enviroment_generation():
    section = 'Environment Generation'
    temp = check_temperature()
    weather = check_weather()
    odors = check_odors()
    return render_template('environment.html', title=section, section=section, item1=temp, item2=weather, item3=odors)

@app.route('/check')
def check():
    section = "Check for Random Encounters"
    explored = check_explored()
    unexplored = check_unexplored()
    obstacle = check_obstacle()
    encounter_time = check_encounter_time()
    wander_activity = check_wander_activity()
    return render_template('generic5.html', title=section, section=section, item1=explored, item2=unexplored, item3=obstacle, item4=encounter_time, item5=wander_activity)

@app.route('/factions')
def faction_connection():
    section = "Faction Connection"
    faction = check_faction()
    item2 = ""
    item3 = ""
    item4 = ""
    item5 = ""
    return render_template('generic5.html', title=section, section=section, item1=faction, item2=item2, item3=item3, item4=item4, item5=item5)

@app.route('/monster')
def check_monster():
    section = "Random Monster Result"
    explored = check_uod_jungle_civilized_region()
    unexplored = check_uod_jungle_bug_region()
    obstacle = check_array_1_region()
    check_lc_region = check_uod_jungle_lizardfolk_region()
    wander_activity = check_wander_activity()
    # print(check_uod_jungle_bug_region())
    # print(check_array_1_region())
    output2 = (check_array_2_region())
    output3 = (check_array_3_region())
    output4 = (check_array_4_region())
    # print(check_uod_jungle_civilized_region())
    # print(check_uod_jungle_lizardfolk_region())
    return render_template('generic8.html', title=section, section=section, item1=explored, item2=unexplored, item3=check_lc_region, item4=obstacle, item5=output2, item6=output3, item7=output4, item8=wander_activity)

