with open("numbers.txt") as file:
    lines = file.readlines()

twoDArray = []

for line in lines:
    numbers = line.strip().split()
    for i, number in enumerate(numbers):
        numbers[i] = int(number)
    twoDArray.append(numbers)
        
def increasing(array):
    return all(i == 0 or num > array[i - 1] and num - array[i - 1] < 4  for i, num in enumerate(array))

def decreasing(array):
     return all(i == 0 or num < array[i - 1] and array[i - 1] - num < 4 for i, num in enumerate(array))

def checkResults(twoDArray):
    safeResults = 0
    
    for array in twoDArray:
        positive = (
            increasing(array) or
            decreasing(array)
        )
        if(positive):
            safeResults += 1
    return safeResults

print("Solution part 1: ", checkResults(twoDArray))

def cut(array, i):
    return array[0: i] + array[i + 1: len(array)]

def everyButOne(arr, f):
    if(f(arr)):
        return True
    return any(f(cut(arr, i)) for i, num in enumerate(arr))

resultPart2 =  len(list(filter(bool, map(lambda row: everyButOne(row, decreasing) or everyButOne(row, increasing), twoDArray))))

print("resultPart2: ", resultPart2)