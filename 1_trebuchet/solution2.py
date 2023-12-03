# Same as solution 1, but replace spelled numbers with their actual number
# Have to keep first and last digit from each spelled out number in string in case of overlap

numbers_spelled = ['one', 'two', 'three', 'four', 'five', 'six',
                   'seven', 'eight', 'nine']

with open('input.txt', 'r') as f:
    sum = 0
    for line in f:
        for (i, s) in enumerate(numbers_spelled):
            line = line.replace(s, s[0] + str(i + 1) + s[-1])
        digits = [int(i) for i in line if i.isdigit()]
        first, last = digits[0], digits[-1]
        cal_value = int(str(first) + str(last))
        sum += cal_value
print(sum)