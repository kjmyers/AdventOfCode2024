import re
import numpy as np
import math


ret = 0
bots = []

numRows = 103
numCols = 101

# numRows = 7
# numCols = 11

#with open("inputTest.txt", 'r') as f:
with open("../Input/input14.txt", 'r') as f:
    for line in f.readlines():
        bots.append( [ int(x) for x in re.findall(r'-?\d+', line.strip())] )

#print(bots)

grid = [ ['.'] * numCols for _ in range(numRows) ]
# for g in grid:
#     print(g)

for c,r,dc,dr in bots:
    #print(c,r,dc,dr)
    print(r,c)
    if grid[r][c] == '.':
        grid[r][c] = '1'
    else:
        grid[r][c] = str(int(grid[r][c]) + 1)


for g in grid:
    print(g)

endgrid = [ ['.'] * numCols for _ in range(numRows) ]

quads = [0,0,0,0]

for c,r,dc,dr in bots:
    newR = (r + (dr*100)) % numRows
    newC = (c + (dc*100)) % numCols

    if 0 <= newR < numRows//2:
        if 0 <= newC < numCols//2:
            quads[0] += 1
        elif numCols//2 < newC < numCols:
            quads[1] += 1
    elif numRows//2 < newR < numRows:
        if 0 <= newC < numCols//2:
            quads[2] += 1
        elif numCols//2 < newC < numCols:
            quads[3] += 1

    if endgrid[newR][newC] == '.':
        endgrid[newR][newC] = '1'
    else:
        endgrid[newR][newC] = str(int(endgrid[newR][newC]) + 1)
print()
for g in endgrid:
    print(g)

ans = quads[0]
for q in quads[1:]:
    ans *= q

print(ans)