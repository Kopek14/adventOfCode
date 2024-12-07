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

totalPart1 = 0

for i in range(len(numbers_column1)):
    totalPart1 += abs(numbers_column1[i] - numbers_column2[i])

#Result 1 day part 1
print(f"Total part 1: {totalPart1}")

totalPart2 = 0

for i in range(len(numbers_column1)):
    number = numbers_column1[i]
    totalSameNumbers = 0

    for i in range(len(numbers_column2)):

        if numbers_column2[i] == number:
            totalSameNumbers += 1
    totalPart2 += number * totalSameNumbers

print(f"Total part 2: {totalPart2}")