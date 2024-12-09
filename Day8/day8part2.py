from collections import defaultdict

with open("../Input/input8.txt", 'r') as f:
#with open("inputTest.txt", 'r') as f:
    lines = [list(line.rstrip()) for line in f.readlines()]

m = len(lines)
n = len(lines[0])
sig = defaultdict(list)
nodes = 0
for r in range(m):
    for c in range(n):
        if lines[r][c] != '.':
            sig[lines[r][c]].append((r,c))
            nodes += 1

def inMap(r,c):
    if 0 <= r < m and 0 <= c < n:
        return True
    return False


print(sig)
ret = 0

for key, locs in sig.items():
    for curPair in range(len(locs)):
        for other in range(len(locs)):
            if curPair != other:
                newR = locs[curPair][0] #+ (locs[curPair][0] - locs[other][0])
                newC = locs[curPair][1] #+ (locs[curPair][1] - locs[other][1])
                while inMap(newR, newC): # and lines[newR][newC] != key and lines[newR][newC] != '#':
                    if lines[newR][newC] == '.':
                        lines[newR][newC] = '#'
                        ret += 1
                    newR += (locs[curPair][0] - locs[other][0])
                    newC += (locs[curPair][1] - locs[other][1])


for line in lines:
    print(line)

print(ret + nodes)