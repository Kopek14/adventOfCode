with open('numbers.txt', 'r') as file:
    lines = file.readlines()

numbers_column1 = []
numbers_column2 = []
for line in lines:
    numbers = line.strip().split()
    
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            numbers_column1.append(int(num))
        else:
            numbers_column2.append(int(num))

numbers_column1.sort()
numbers_column2.sort()

total = 0

for i in range(len(numbers_column1)):
    total = total + abs(numbers_column1[i] - numbers_column2[i])

print(total)