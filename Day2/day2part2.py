def sameDir(numbers):
    increases = 0
    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i-1]:
            increases += 1
    if increases == len(numbers)-1:
        return True
    
    decreases = 0
    for i in range(1,len(numbers)):
        if numbers[i] < numbers[i-1]:
            decreases += 1
    if decreases == len(numbers)-1:
        return True
    return False

def diff(numbers):
    deltas = []
    for i in range(1,len(numbers)):
        dif = abs(numbers[i] - numbers[i-1])
        if 0 < dif < 4:
            deltas.append(True)
        else:
            deltas.append(False)
    return all(deltas)

def dampSameDir(numbers):
    checks = len(numbers)
    if sameDir(numbers):
        return True, numbers
    for position in range(checks):
        modified_numbers = [number for pos, number in enumerate(numbers) if pos != position]
        if sameDir(modified_numbers):
            return True, modified_numbers
    return False, numbers

def dampDiff(numbers):
    checks = len(numbers)
    if diff(numbers):
        return True, numbers
    for position in range(checks):
        modified_numbers = [
            number for pos, number in enumerate(numbers) if pos != position
        ]
        if diff(modified_numbers):
            return True, modified_numbers
    return False, numbers

def dampener(numbers):
    (worked, new_list) = dampSameDir(numbers)
    if worked and diff(new_list):
        return True
    (worked, new_list) = dampDiff(numbers)
    if  worked and sameDir(new_list):
            return True
    return False


with open("../Input/input2.txt", 'r') as f:
    input = [line.rstrip() for line in f.readlines()]
ret = 0
for row in input:
    split_row = [int(value) for value in row.split()]
    if dampener(split_row):
        ret += 1
print(ret)