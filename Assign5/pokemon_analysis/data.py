import os
import json

pokedex = None

def get_data():
    global pokedex
    if pokedex != None:
        return pokedex
    
    fname = os.path.join(os.path.dirname(__file__), 'pokemon.json')
    pokedex = json.load(open(fname))
    return pokedex