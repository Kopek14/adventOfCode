import re

with open("numbers.txt") as file:
    lines = file.readlines()
    
def mul(first_number, second_number):
    return first_number * second_number

pattern = r"mul\(\d+,\d+\)"

result = 0

for line in lines:
    matches = re.findall(pattern, line)
    
    for match in matches:
        result += eval(match)

print(result)