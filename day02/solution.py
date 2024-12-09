with open("numbers.txt") as file:
    lines = file.readlines()
print(len(lines))

twoDArray = []

for line in lines:
    numbers = line.strip().split()
    for i, number in enumerate(numbers):
        numbers[i] = int(number)
    twoDArray.append(numbers)

safeReports = 0

for array in twoDArray:
    iOrD = 'i'
    safe = True
    for i, number in enumerate(array):
        if(i == 0):
            continue
        if(i == 1 and array[i - 1] > number):
            iOrD = 'd'
        if(iOrD == 'i' and array[i - 1] >= number):
            safe = False
            break
        if(iOrD == 'd' and array[i - 1] <= number):
            safe = False
            break
        if(abs(array[i - 1] - number) > 3):
            safe = False
            break
    if(safe == True):
        safeReports += 1 
        
print(f'safeReports: {safeReports}')