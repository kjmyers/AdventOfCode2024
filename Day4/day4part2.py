
def inBounds(row ,col, grid):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return True
    return False


def checkForXmas(row ,col, grid):
    dirs = ( (-1,-1), (-1,1) )  #, (1,-1), (1,1)
    xmas = "MAS"

    cross = []
    for d in dirs:
        word = grid[row][col]
        if inBounds(row+d[0],col+d[1],grid) and inBounds(row - d[0],col - d[1],grid):
            word = grid[row+d[0]][col+d[1]] + word
            word = word + grid[row-d[0]][col-d[1]]
            cross.append(word)

    ret = 0
    if len(cross) == 2 and (cross[0] == xmas or cross[0][::-1] == xmas) and (cross[1] == xmas or cross[1][::-1] == xmas):
        ret += 1
    return ret



with open("../Input/input4.txt", 'r') as f:
#with open("inputTest.txt", 'r') as f:
    grid = [line.rstrip() for line in f.readlines()]
ret = 0

ret = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'A':
            ret += checkForXmas(r,c,grid)

print(ret)