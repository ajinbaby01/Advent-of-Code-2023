import re

sum = 0

file_path = 'Day 2/day2_cube_conundrum_input.txt'
pattern_find_all = r'\b\d+\b|\b\w+\b|[;]'
with open(file_path, 'r') as f:
    for line in f:
        line = re.findall(pattern_find_all, line)
        blue = red = green = 0
        for i in range(2, len(line)):
            if line[i].isdigit():
                num = int(line[i])
                if line[i+1] == 'blue':
                    blue = max(blue, num)
                elif line[i+1] == 'red':
                    red = max(red, num)
                elif line[i+1] == 'green':
                    green = max(green, num)
        sum += blue*green*red
print(sum)
