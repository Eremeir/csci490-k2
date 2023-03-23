from . import data

def hp_diff(name1, name2):
    return get_mon(name1)['hp'] - get_mon(name2)['hp']

def attack_diff(name1, name2):
    return get_mon(name1)['attack'] - get_mon(name2)['attack']
    
def defense_diff(name1, name2):
    return get_mon(name1)['defense'] - get_mon(name2)['defense']
    
def get_mon(name):
    mons = data.get_data()
    for mon in mons:
        if mon['name'].lower() == name.lower():
            return mon
    raise ValueError(f'Pokemon {name} not found in pokedex')

def get_combat_power(mon):
    Attack = 2 * round(mon['attack']**0.5 * mon['sp_attack']**0.5 + mon['speed']**0.5)
    Defense = 2 * round(mon['defense']**0.5 * mon['sp_defense']**0.5 + mon['speed']**0.5)
    return float((Attack + 15) * (Defense + 15)**0.5 * ((mon['hp'] * 2) + 15)**0.5 * 0.7903001**2 / 10)

def combat_power_diff(name1, name2):
    cpwr1 = get_combat_power(get_mon(name1))
    cpwr2 = get_combat_power(get_mon(name2))
    
    return round(cpwr1 - cpwr2, 6)