map = []
#with open("inputTest.txt", 'r') as f:
with open("../Input/input12.txt", 'r') as f:
    for line in f.readlines():
        map.append( [c for c in line.rstrip()] )

m = len(map)
n = len(map[0])

def inMap(r,c):
    if 0 <= r < m and 0 <= c < n:
        return True
    return False

dirs = ((1,0),(0,-1),(-1,0),(0,1))

def dfs(r,c):
    seen.add((r,c))
    addedArea = 1
    addedPerm = 0
    for dr,dc in dirs:
        newR = r + dr
        newC = c + dc
        if not inMap(newR,newC) or map[newR][newC] != map[r][c]:
            addedPerm += 1
        else:
            if (newR,newC) not in seen:
                newA, newP = dfs(newR,newC)
                addedArea += newA
                addedPerm += newP
    return (addedArea, addedPerm)

print(map)
seen = set()
ret = 0
for r in range(m):
    for c in range(n):
        if (r,c) not in seen:
            a, p = dfs(r,c)
            ret += a * p


print(ret)