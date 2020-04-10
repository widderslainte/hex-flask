from flask import render_template
from app import app
import random

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
@app.route('/index')
 
@app.route('/')
def hello_world():
   return render_template('index.html', message="Dungeon Science")
 
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
 
@app.route('/2d6')
def basic_roll():
    result = roll2d6()
    return render_template('roll.html', message=result)

# @app.route('/spencer')
# def basic_roll():
#     return 'Hi Spencer'