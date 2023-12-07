import re

with open('input.txt', 'r') as f:
    data = list(f)
    copy_counts = [1 for _ in range(len(data))]
    for line in data:
        # Get line number for this line
        split_line = re.split(':', line.rstrip('\n'))
        line_num = int(split_line[0].split()[1])
        # Split line into your numbers and winning numbers
        numbers_str = re.split(r'\|', split_line[1])
        winning_numbers = re.findall(r'\d+', numbers_str[0])
        our_numbers = re.findall(r'\d+', numbers_str[1])
        # Get overlap between winning numbers and our numbers
        overlap = set(winning_numbers).intersection(our_numbers)
        score = len(overlap)
        # Iterate copy counts for next lines
        for i in range(score):
            copy_counts[line_num + i] += copy_counts[line_num - 1]
    # Print total number of cards
    print(sum(copy_counts))