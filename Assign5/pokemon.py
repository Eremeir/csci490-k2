#Matt Borek z1951125
import sys
from pokemon_analysis import generation, compare

def usage():
    USAGE = "Usage: python -m pokemon_analysis [generation <num> | types <num> | compare <hp | atk | def | pwr> <name1> <name2>]"
    print(USAGE)
    exit(1)

def main():
    args = sys.argv[1:]
    
    if not args:
        usage()
    
    if args[0] == 'generation':
        if len(args) != 2:
            usage()
        
        try:
            gen_num = int(args[1])
            if gen_num < 1 or gen_num > 8:
                raise ValueError("Generation must be betwen 1 and 8.")
        except ValueError:
            print(f'Invalid generation provided:', args[1])
            usage()
        
        
    elif args[0] == 'types':
        if len(args) != 2:
            usage()
        
        try:
            gen_num = int(args[1])
            if gen_num < 1 or gen_num > 8:
                raise ValueError("Generation must be betwen 1 and 8.")
        except ValueError:
            print(f'Invalid generation provided:', args[1])
            usage()
        gen_type_count = generation.generation_types(gen_num)
        print(f'Generation {gen_num}:')
        for type, count in gen_type_count.items():
            print(f'  {type}: {count}')
            

    elif args[0] == 'compare':
        if len(args) != 4:
            usage()
        
        name1, name2 = args[2], args[3]
        
        if args[1] == 'pwr': 
            try:
                power_diff = compare.combat_power_diff(name1, name2)
                print(f'{name1} has {power_diff:+} combat power than {name2}')
            except ValueError as no_mon:
                print(no_mon)
                usage()
                
        elif args[1] == 'hp': 
            try:
                power_diff = compare.hp_diff(name1, name2)
                print(f'{name1} has {power_diff:+} health than {name2}')
            except ValueError as no_mon:
                print(no_mon)
                usage()
                
        elif args[1] == 'atk': 
            try:
                power_diff = compare.attack_diff(name1, name2)
                print(f'{name1} has {power_diff:+} attack than {name2}')
            except ValueError as no_mon:
                print(no_mon)
                usage()
                
        elif args[1] == 'def': 
            try:
                power_diff = compare.defense_diff(name1, name2)
                print(f'{name1} has {power_diff:+} defense than {name2}')
            except ValueError as no_mon:
                print(no_mon)
                usage()  
                
        else:
            usage()
        
        
    else:
        usage()  
    
if __name__ == '__main__':
    main()