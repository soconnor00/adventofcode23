import re

MAX_R = 12
MAX_G = 13
MAX_B = 14

def count_valid(count):
    # Extract number and color from count
    number, color = count.split(' ', 1)
    # Check each color for violation
    match color:
        case 'red':
            if int(number) > MAX_R:
                return False
        case 'green':
            if int(number) > MAX_G:
                return False
        case 'blue':
            if int(number) > MAX_B:
                return False
    return True

def round_valid(round):
    # Validate each count in round
    for count in round.split(', ', 2):
        if not count_valid(count):
            return False
    return True

def game_valid(game):
    # Validate each round in game
    for round in game[1:]:
        if not round_valid(round):
            return False
    return True

def main():
    with open('input.txt', 'r') as f:
        sum = 0
        for line in f:
            # Split into id and round info
            game = re.split('; |: ', line.rstrip('\n'))
            # Get game id
            id = game[0].split()[1]
            # Check rounds of game for violations
            if game_valid(game):
                sum += int(id)
    print(sum)

if __name__ == "__main__":
    main()