import re

def parse_count(count):
    count_r, count_g, count_b = 0, 0, 0
    # Extract number and color from count
    number, color = count.split(' ', 1)
    # Assign number to location in tuple based on color
    match color:
        case 'red':
            count_r = number
        case 'green':
            count_g = number
        case 'blue':
            count_b = number
    return count_r, count_g, count_b

def round_counts(round):
    # Get min number of cubes required for this round
    round_count_r, round_count_g, round_count_b = 0, 0, 0
    for count in round.split(', ', 2):
        parsed_count = parse_count(count)
        round_count_r += int(parsed_count[0])
        round_count_g += int(parsed_count[1])
        round_count_b += int(parsed_count[2])
    return round_count_r, round_count_g, round_count_b

def set_power(game):
    # Get min number cubes required for each game
    max_r, max_g, max_b = 0, 0, 0
    for round in game[1:]:
        counts = round_counts(round)
        max_r = max(max_r, counts[0])
        max_g = max(max_g, counts[1])
        max_b = max(max_b, counts[2])
    return max_r * max_g * max_b

def main():
    with open('input.txt', 'r') as f:
        sum = 0
        for line in f:
            # Split into id and round info
            game = re.split('; |: ', line.rstrip('\n'))
            # Get power of set
            sum += set_power(game)
    print(sum)

if __name__ == "__main__":
    main()