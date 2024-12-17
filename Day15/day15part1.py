map = []
moves = []
#with open("inputTest2.txt", 'r') as f:
with open("../Input/input15.txt", 'r') as f:
    for line in f.readlines():
        if line[0] == '#':
            map.append( [c for c in line.rstrip()] )
        if line[0] in '<^>v':
            moves += [c for c in line.rstrip()]

for g in map:
    print(g)
print(moves)
print()
m = len(map)
n = len(map[0])

# find the starting spot:
curR = 0
curC = 0
for r in range(m):
    for c in range(n):
        if map[r][c] == '@':
            curR = r
            curC = c
            break


def inMap(r,c):
    if 0 <= r < m and 0 <= c < n:
        return True
    return False

dirs = ((1,0),(0,-1),(-1,0),(0,1))

def checkMove(r, c, dir, obj):
    if map[r][c] == '#':
        return False
    if map[r][c] == '.' or checkMove(r+dir[0],c+dir[1],dir,'O'):
        map[r][c] = obj
        return True


for move in moves:
    print("Trying... ", move)
    if move == '<':
        dir = (0,-1)
    elif move == '^':
        dir = (-1,0)
    elif move == '>':
        dir = (0,1)
    else: # 'v'
        dir = (1,0)
    if checkMove(curR+dir[0], curC+dir[1], dir, '@'):
        map[curR][curC] = '.'
        curR += dir[0]
        curC += dir[1]
    
    for g in map:
        print("".join(g))
    print()

gps = 0
for r in range(m):
    for c in range(n):
        if map[r][c] == 'O':
            gps += (r*100) + c

print("Final Count: ", gps)