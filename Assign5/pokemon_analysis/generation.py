from . import data
from collections import Counter

def generation_types(gen_num):
    mons = data.get_data()
    types = [mon['primary_type'] for mon in mons if mon['generation'] == gen_num]
    return dict(Counter(types))

def generation_ranges(gen_num):
    mons = data.get_data()
    gen_mon_stats = [(mon['hp'], mon['attack'], mon['defense']) for mon in mons if mon['generation'] == gen_num]

    health, attack, defense = zip(*gen_mon_stats)
    return {'hp': (min(health), max(health)), 'attack': (min(attack), max(attack)),'defense': (min(defense), max(defense))}