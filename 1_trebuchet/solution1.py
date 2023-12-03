# 1. Read each line from file
# 2. Get list of digits in line
# 3. Combine first and last digits
# 4. Add to sum
# 5. Print sum

with open('input.txt', 'r') as f:
    sum = 0
    for line in f:
        digits = [int(i) for i in line if i.isdigit()]
        first, last = digits[0], digits[-1]
        cal_value = int(str(first) + str(last))
        sum += cal_value
print(sum)