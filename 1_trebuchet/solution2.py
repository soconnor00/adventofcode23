# List of valid spelled out numbers
numbers_spelled = ['one', 'two', 'three', 'four', 'five', 'six',
                   'seven', 'eight', 'nine']

with open('input.txt', 'r') as f:
    sum = 0
    for line in f:
        # Replace spelled numbers with integer
        # Have to keep first and last characters in case of overlap
        for (i, s) in enumerate(numbers_spelled):
            line = line.replace(s, s[0] + str(i + 1) + s[-1])
        # Same steps as part 1
        digits = [int(i) for i in line if i.isdigit()]
        first, last = digits[0], digits[-1]
        cal_value = int(str(first) + str(last))
        sum += cal_value
print(sum)