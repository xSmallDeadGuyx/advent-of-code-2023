import re

input_file = open('input.txt', 'r')

seed_ranges = []
current_map = []

def applyCurrentMap():
    global seed_ranges, current_map
    
    if len(current_map) == 0:
        return
    
    new_converted_seeds = []

    i = 0
    while i < len(seed_ranges):
        seed_range = seed_ranges[i]

        for mapping in current_map:
            conversion = mapping[2] - mapping[0]
            
            if seed_range[0] >= mapping[0] and seed_range[1] <= mapping[1]:
                # Seeds contained wholly withing mapping range
                seed_ranges[i] = (seed_range[0] + conversion, seed_range[1] + conversion)
                break # No more mapping left to do
            elif seed_range[0] < mapping[0] and seed_range[1] >= mapping[0]:
                # Start is before mapping start but end is after
                if seed_range[1] <= mapping[1]:
                    # Ranges overlap but not wholly contained, split into two where the latter is converted
                    seed_ranges[i] = (seed_range[0], mapping[0] - 1)
                    new_converted_seeds.append((mapping[0] + conversion, seed_range[1] + conversion))
                else:
                    # Mapping is wholly contained within seed range, split into three where only the middle is converted
                    seed_ranges[i] = (seed_range[0], mapping[0] - 1)
                    new_converted_seeds.append((mapping[0] + conversion, mapping[1] + conversion))
                    seed_ranges.insert(i + 1, (mapping[1] + 1, seed_range[1]))
            elif seed_range[0] >= mapping[0] and seed_range[0] <= mapping[1]:
                # Ranges overlap but not wholly contained, split into two where the former is converted
                new_converted_seeds.append((seed_range[0] + conversion, mapping[1] + conversion))
                seed_ranges[i] = (mapping[1] + 1, seed_range[1])
                
            seed_range = seed_ranges[i]
        i += 1
        # break

    seed_ranges.extend(new_converted_seeds)

    current_map = []

for line in input_file:
    line = line.rstrip('\n')
    
    if len(seed_ranges) == 0:
        split_line = line.split()
        for i in range(int(len(split_line) / 2)):
            range_start = int(split_line[i*2 + 1])
            range_end = range_start + int(split_line[i*2 + 2]) - 1
            seed_ranges.append((range_start, range_end))
        continue
    
    split_line = line.split()
    if len(split_line) == 3:
        mapping_start = int(split_line[1])
        mapping_end = mapping_start + int(split_line[2]) - 1
        mapping_to = int(split_line[0])
        current_map.append((mapping_start, mapping_end, mapping_to))
    else:
        applyCurrentMap()

applyCurrentMap()

print(min([x[0] for x in seed_ranges]))