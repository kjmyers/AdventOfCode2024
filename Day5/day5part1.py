from collections import defaultdict
from graphlib import TopologicalSorter

with open("../Input/input5.txt", 'r') as f:
#with open("inputTest.txt", 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

graph = defaultdict(list)
updates = []

for line in lines:
    if '|' in line:
        (before, after) = [int(x) for x in line.split('|')]
        graph[before].append(after)
    elif ',' in line:
        updates.append([int(x) for x in line.split(',')])

print(graph)
print(updates)

def checkCorrect(up):
    seen = set()
    needsSort = False
    for page in up:
        for rule in graph[page]:
            if rule in seen:
                return 0
        seen.add(page)
    return up[len(up)//2]

ret = 0
for update in updates:
    middle = checkCorrect(update)
    ret += middle
        
print(ret)
