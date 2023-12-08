import re

def map_num(mapping, num):
    mapped_num = num
    changed = False
    dest_start, source_start, range_len = [int(i) for i in mapping.split(' ', 3)]
    # If seed is in range of this mapping
    if source_start <= mapped_num < source_start + range_len:
        # Set mapped seed to newly mapped value
        mapped_num = dest_start + (mapped_num - source_start)
        changed = True
    return mapped_num, changed

def traverse_map(map, num):
    mapped_num = num
    mappings = map.split('\n')
    # Check mapped seed against each mapping of this map
    for mapping in mappings:
        mapped_num, changed = map_num(mapping, num)
        # If we find a mapping, return it immediately
        if (changed):
            break
    return mapped_num

def map_seed_to_location(maps, seed):
    num = seed
    # Pull mappings out of maps
    for map in maps:
        num = traverse_map(map, num)
    return num

def get_closest_location(maps, seeds):
    closest_location = float('inf')
    # Convert each seed to locations using map
    for seed in seeds:
        # Keep track of closest location
        closest_location = min(closest_location, map_seed_to_location(maps, seed))
    return closest_location

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        # Split data based on category
        split_data = re.split(r'\n\n.+\:\n', data)
        # Pull maps out of data
        maps = split_data[1:]
        # Pull seeds out of data
        seeds = [int(i) for i in split_data[0].strip('seeds: ').split()]
        # Get closest location using seeds and maps
        closest_location = get_closest_location(maps, seeds)
        print(closest_location)

if __name__ == "__main__":
    main()