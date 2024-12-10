map = []
#with open("inputTest.txt", 'r') as f:
with open("../Input/input10.txt", 'r') as f:
    for line in f.readlines():
        map.append( [int(c) for c in line.rstrip()] )

m = len(map)
n = len(map[0])

#find the starting spot:
starts = []
for r in range(m):
    for c in range(n):
        if map[r][c] == 0:
            starts.append((r,c))

def inMap(r,c):
    if 0 <= r < m and 0 <= c < n:
        return True
    return False

dirs = ((1,0),(0,-1),(-1,0),(0,1))
def dfs(r,c, seen):
    if map[r][c] == 9 and not (r,c) in seen:
        seen.add((r,c))
        return 1
    ret = 0
    for dr,dc in dirs:
        newR = r + dr
        newC = c + dc
        if inMap(newR,newC) and map[newR][newC] == map[r][c]+1:
            ret += dfs(newR,newC,seen)
    return ret

ret = 0
for r,c in starts:
    ret += dfs(r,c,set())


print(ret)