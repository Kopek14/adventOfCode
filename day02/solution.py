with open("numbers.txt") as file:
    lines = file.readlines()

twoDArray = []

for line in lines:
    numbers = line.strip().split()
    for i, number in enumerate(numbers):
        numbers[i] = int(number)
    twoDArray.append(numbers)
        

def checkResults(twoDArray):
    safeResults = 0
    for array in twoDArray:
        positive = (
            all(i == 0 or num > array[i - 1] and num - array[i - 1] < 4  for i, num in enumerate(array)) or
            all(i == 0 or num < array[i - 1] and array[i - 1] - num < 4 for i, num in enumerate(array))
        )
        if(positive):
            safeResults += 1
    return safeResults

print("Solution part 1: ", checkResults(twoDArray))