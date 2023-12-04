# 12 red cubes, 13 green cubes, and 14 blue cubes
import re

RED = 12
GREEN = 13
BLUE = 14

sum = 0

file_path = 'Day 2/day2_cube_conundrum_input.txt'
# pattern_split = r'[:,;\s]'
pattern_find_all = r'\b\d+\b|\b\w+\b|[;]'
with open(file_path, 'r') as f:
    for line in f:
        # line = re.split(pattern_split, line)
        line = re.findall(pattern_find_all, line)
        # for i in range(3, len(line)):
        for i in range(2, len(line)):
            if line[i].isdigit():
                num = int(line[i])
                if num > RED and line[i+1] == 'red':
                    break
                if num > GREEN and line[i+1] == 'green':
                    break
                if num > BLUE and line[i+1] == 'blue':
                    break
        if i == len(line) - 1:
            sum += int(line[1])
print(sum)
