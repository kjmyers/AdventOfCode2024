
def inBounds(row ,col, grid):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return True
    return False


def checkForXmas(row ,col, grid):
    dirs = ( (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1, 0), (1,1) )
    xmas = "XMAS"
    ret = 0
    
    for d in dirs:
        word = grid[row][col]
        curR = row
        curC = col
        for i in range(1,4):
            curR += d[0]
            curC += d[1]
            if inBounds(curR,curC,grid):
                word += grid[curR][curC]
                if word != xmas[:i+1]:
                    break
        if word == xmas:
            ret += 1
    return ret



with open("../Input/input4.txt", 'r') as f:
#with open("inputTest.txt", 'r') as f:
    grid = [line.rstrip() for line in f.readlines()]
ret = 0

ret = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'X':
            ret += checkForXmas(r,c,grid)

print(ret)