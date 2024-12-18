from collections import deque 

blocks = []
#with open("inputTest.txt", 'r') as f:
with open("../Input/input18.txt", 'r') as f:
    for line in f.readlines():
        l = line.rstrip().split(',')
        blocks.append([int(l[0]),int(l[1])])

n = 71
space = [['.'] * n for _ in range(n)]

def inMap(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

dirs = ((0,1),(-1,0),(0,-1),(1,0))

def bfs():
    q = deque([(0,0,0)])
    visited = set()
    visited.add((0,0))
    while q:
        for _ in range(len(q)):
            r,c,steps = q.popleft()
            if r == n-1 and c == n-1:
                return steps
            for dir in dirs:
                newR = r + dir[0]
                newC = c + dir[1]
                if inMap(newR,newC) and space[newR][newC] == '.' and (newR,newC) not in visited:
                    q.append([newR,newC,steps+1])
                    visited.add((newR,newC))


for i in range(3451):
    col,row = blocks[i]
    space[row][col] = '#'
    if bfs() == None:
        print(row,col)
        break