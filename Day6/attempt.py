from collections import defaultdict
import bisect

#with open("../Input/input6.txt", 'r') as f:
with open("inputTest.txt", 'r') as f:
    map = [line.rstrip() for line in f.readlines()]

m = len(map)
n = len(map[0])

#find the starting spot:
curR = 0
curC = 0
obsR = defaultdict(list)
obsC = defaultdict(list)
for r in range(m):
    for c in range(n):
        if map[r][c] == '^':
            curR = r
            curC = c
        if map[r][c] == '#':
            obsR[r].append(c)
            obsC[c].append(r)

print("Row Obstacles: ", obsR)
print("Col Obstacles: ", obsC)
def inMap(r,c):
    if 0 <= r < m and 0 <= c < n:
        return True
    return False

dirs = ( (-1,0), (0,1), (1,0), (0,-1) )

def obsToRight(r,c, dir):
    # Horizontal vector, check vertical
    if dirs[dir][0] == 0:
        if dirs[dir][1] == -1:
            if bisect.bisect(obsC[c], r) != 0:
                return True
            return False
        if dirs[dir][1] == 1:
            if bisect.bisect(obsC[c], r) != len(obsC[c]):
                return True
            return False
    # Vertical vector, check horizontal
    if dirs[dir][1] == 0:
        if dirs[dir][0] == -1:
            if bisect.bisect(obsR[r], c) != len(obsR[r]):
                return True
            return False
        if dirs[dir][0] == 1:
            if bisect.bisect(obsR[r], c) != 0:
                return True
            return False

    return True


def tryLoop(curR, curC, curDir):
    newObstacle = (curR + dirs[curDir][0], curC + dirs[curDir][1])
    seen = set()
    seen.add((curR, curC, curDir))
    curDir = curDir+1 if curDir < 3 else 0
    while inMap(curR,curC):
        if (curR,curC,curDir) in seen:
            return (True, newObstacle)
        seen.add((curR, curC, curDir))
        nextR = curR + dirs[curDir][0]
        nextC = curC + dirs[curDir][1]
        if inMap(nextR,nextC) and map[nextR][nextC] == '#' or (nextR,nextC) == newObstacle:
            curDir = curDir+1 if curDir < 3 else 0
            nextR = curR + dirs[curDir][0]
            nextC = curC + dirs[curDir][1]
        curR = nextR
        curC = nextC
    return (False, (0,0))

curDir = 0
ret = set()
while inMap(curR,curC):
    nextR = curR + dirs[curDir][0]
    nextC = curC + dirs[curDir][1]
    
    if obsToRight(curR,curC, curDir):
        print("Trying... ", curR,curC,curDir, dirs[curDir])
        (success, newObs) = tryLoop(curR, curC, curDir)
        if success:
            ret.add(newObs)
    
    if inMap(nextR,nextC) and map[nextR][nextC] == '#':
        curDir = curDir+1 if curDir < 3 else 0
        nextR = curR + dirs[curDir][0]
        nextC = curC + dirs[curDir][1]
    
    curR = nextR
    curC = nextC

print(len(ret))


# 1957 too high
# 1939 should be correct