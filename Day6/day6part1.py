from collections import defaultdict
from graphlib import TopologicalSorter

with open("../Input/input6.txt", 'r') as f:
#with open("inputTest.txt", 'r') as f:
    map = [line.rstrip() for line in f.readlines()]

m = len(map)
n = len(map[0])
print(map)

#find the starting spot:
curR = 0
curC = 0
for r in range(m):
    for c in range(n):
        if map[r][c] == '^':
            curR = r
            curC = c

def inMap(r,c):
    if 0 <= r < m and 0 <= c < n:
        return True
    return False

seen = set()
dirs = ( (-1,0), (0,1), (1,0), (0,-1) )
curDir = 0

while inMap(curR,curC):
    seen.add((curR,curC))
    nextR = curR + dirs[curDir][0]
    nextC = curC + dirs[curDir][1]
    if inMap(nextR,nextC) and map[nextR][nextC] == '#':
        curDir = curDir+1 if curDir < 3 else 0
        nextR = curR + dirs[curDir][0]
        nextC = curC + dirs[curDir][1]
    curR = nextR
    curC = nextC

print(seen)
ret = len(seen)
print(ret)
