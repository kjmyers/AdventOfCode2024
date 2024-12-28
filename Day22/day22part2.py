
with open('../Input/input22.txt', 'r') as f:
    initSecrets = [int(l.strip()) for l in f.readlines()]

print(initSecrets)

ret = 0

def randomNumber(seed):
    seed = ((seed << 6) ^ seed) % 16777216
    seed = ((seed >> 5) ^ seed) % 16777216
    seed = ((seed << 11) ^ seed) % 16777216
    return seed


    
total = 0
ranges = {}
for num in initSecrets:
    curNum = num
    visited = set()
    changes = []
    
    for i in range(2000):
        nextNum = randomNumber(curNum)
        changes.append((nextNum % 10) - (curNum % 10))
        curNum = nextNum

        if len(changes) == 4:
            key = ",".join(map(str, changes))
            if key not in visited:
                if key not in ranges:
                    ranges[key] = []
                ranges[key].append(nextNum % 10)
                visited.add(key)
            changes.pop(0)

print(max(sum(rangeValues) for rangeValues in ranges.values()))