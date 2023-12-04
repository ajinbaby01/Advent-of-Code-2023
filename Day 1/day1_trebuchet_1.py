file_path = 'Day 1/day1_trebuchet_input.txt'

with open(file_path, 'r') as f:
    total_sum = 0
    for line in f:
        digits = [int(digit) for digit in line if digit.isdigit()]
        total_sum += digits[0] * 10 + digits[-1]

print(total_sum)
