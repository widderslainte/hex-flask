from flask import Flask, render_template
import random

from describe_encounter import *
from environment import *
from random_encounters import *
from factions import *
from monsters_jungle import *
from treasure import *
from healing import *
from camp import *
from spoor import *
from dice import *

app = Flask(__name__)
source = '/app.py'

# Load the configuration from the instance folder
# app.config.from_pyfile('config.py')

def terraintype():
    rolls = roll2d6()
    if rolls < 4:
        return 'The terrain is low lying (roll was: ' + str(rolls) + ')'
    elif 4 <= rolls <= 7:
        return 'The terrain is just more jungle, roll was: ' + str(rolls)
    elif rolls > 10:
        return 'The terrain is hilly or raised, roll was: ' + str(rolls)
    else:
        return 'The terrain is horrible jungle, roll was: ' + str(rolls)

def encounterdie():
    die = random.randint(1,6)
    if die == 1:
        return '1: Wandering monster attacks!'
    elif die == 2:
        return '2: Encounter a hazard.'
    elif die == 6:
        return '6: The day passes uneventfully'
    else:
        spoor = check_spoor()
        return spoor

@app.route('/')
def hello_world():
    return render_template('index.html', message="Dungeon Science", source=source)

@app.route('/2d6')
def sample_2d6():
    sample = roll2d6()
    return 'Sample roll was: ' + str(sample)

@app.route('/reaction')
def reaction():
    outcome = check_reaction()
    return outcome

@app.route('/jungle/')
def jungle():
    return 'You\'re in the jungle, baby!'

@app.route('/hex/')
def hexday():
    section = 'Hex Status'
    temperature = roll2d6()
    weather = check_weather_change()
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
    section = 'Environment Generation: New Day:'
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

@app.route('/treasure')
def check_treasure():
    section = "Treasure"
    gem_ornamental = check_ornamental() 
    gem_semiprecious = check_semiprecious() 
    gem_fancy = check_fancy()  
    output4 = "foo"
    output5 = "bar"
    return render_template('generic5.html', title=section, section=section, item1=gem_ornamental, item2=gem_semiprecious, item3=gem_fancy, item4=output4, item5=output5)

@app.route('/healing')
def check_healing():
    section = "Healing"
    moss_potion = check_moss()
    moss_poultice = check_moss_poultice()
    apoth_potion = check_apoth()
    apoth_poultice = check_apoth_poultice()
    return render_template('generic5.html', title=section, section=section, item1=moss_potion, item2=moss_poultice, item3=apoth_potion, item4=apoth_poultice, item5="")

@app.route('/camp')
def check_camp_features():
    output = check_camp()
    return output

@app.route('/encounter-roll')
def check_encounter_roll():
    output = check_unexplored()
    return output

@app.route('/hazard')
def check_hazard():
    output = check_unexplored()
    return output

@app.route('/spoor')
def route_spoor():
    output = check_spoor()
    return output