import re

def calculate_race_dist(velocity, time_moving):
    return velocity * time_moving

def num_ways_to_win(time, distance):
    num_ways_to_win = 0
    # Loop through all permuations of race
    for time_charging in range(time):
        # Problem constraints dictate velocity in mm/ms == ms spent charging
        velocity = time_charging
        time_moving = time - time_charging
        race_dist = calculate_race_dist(velocity, time_moving)
        if (race_dist > distance):
            num_ways_to_win += 1
    return num_ways_to_win

def main():
    with open('input.txt', 'r') as f:
        multiplied_numbers = 1
        data = list(f)
        times = re.findall(r'\d+', data[0])
        distances = re.findall(r'\d+', data[1])
        for (time, distance) in zip(times, distances):
            multiplied_numbers *= num_ways_to_win(int(time), int(distance))
        print(multiplied_numbers)

if __name__ == "__main__":
    main()