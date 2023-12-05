import re

input_file = open('input.txt', 'r')

seeds = []
current_map = []

def applyCurrentMap():
    global seeds, current_map
    
    if len(current_map) == 0:
        return
    
    for i, seed in enumerate(seeds):
        for mapping in current_map:
            if seed >= mapping[1] and seed < mapping[1] + mapping[2]:
                seeds[i] = mapping[0] + seed - mapping[1]
                break
    
    current_map = []

for line in input_file:
    line = line.rstrip('\n')
    
    if len(seeds) == 0:
        seeds = list(map(int, re.findall(r'[0-9]+', line)))
        continue
    
    split_line = line.split()
    if len(split_line) == 3:
        current_map.append(list(map(int, split_line)))
    else:
        applyCurrentMap()

applyCurrentMap()

print(min(seeds))