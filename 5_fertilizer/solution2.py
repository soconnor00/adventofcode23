# Note: this took about 8 hours to run on my macbook air m2
# One of the threads took 8 hours of CPU time
# I highly recommend running this on good hardware

import re
from multiprocessing import Pool

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

def closest_location_in_range(maps, seed_range):
    closest_location_in_range = float('inf')
    range_start, range_length = seed_range.split()
    # Convert each seed in range to locations using map
    for seed in range(int(range_start), int(range_start) + int(range_length)):
        # Keep track of closest location
        closest_location_in_range = min(closest_location_in_range, map_seed_to_location(maps, seed))
    print('closest location in range: ' + str(closest_location_in_range))
    return closest_location_in_range

def get_closest_location(maps, seed_ranges):
    seed_range_list = re.findall(r'\d+ \d+', seed_ranges)
    # Multithread, one thread per seed range
    with Pool(len(seed_range_list)) as pool:
        return min(pool.starmap(
            closest_location_in_range, 
            [(maps, seed_range) for seed_range in seed_range_list]
        ))

def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        # Split data based on category
        split_data = re.split(r'\n\n.+\:\n', data)
        # Pull maps out of data
        maps = split_data[1:]
        # Pull seed ranges out of data
        seed_ranges = split_data[0].strip('seeds: ')
        # Get closest location using seed ranges and maps
        closest_location = get_closest_location(maps, seed_ranges)
        print(closest_location)

if __name__ == "__main__":
    main()