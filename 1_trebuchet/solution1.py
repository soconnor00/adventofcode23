with open('input.txt', 'r') as f:
    sum = 0
    for line in f:
        # Get list of digits in line
        digits = [int(i) for i in line if i.isdigit()]
        first, last = digits[0], digits[-1]
        # Combine first and last digits of line into int
        cal_value = int(str(first) + str(last))
        sum += cal_value
print(sum)