import re

with open('input.txt', 'r') as f:
    total_value = 0
    for line in f:
        # Split line into your numbers and winning numbers
        numbers_str = re.split(r'\|', re.split(r':', line.rstrip('\n'))[1])
        winning_numbers = re.findall(r'\d+', numbers_str[0])
        our_numbers = re.findall(r'\d+', numbers_str[1])
        # Get overlap between winning numbers and our numbers
        overlap = set(winning_numbers).intersection(our_numbers)
        # Add value of this scratchcard to total
        if len(overlap) != 0: total_value += 2 ** (len(overlap) - 1)
    print(total_value)