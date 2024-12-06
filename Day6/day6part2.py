# from collections import defaultdict
# import bisect

# #with open("../Input/input6.txt", 'r') as f:
# with open("inputTest.txt", 'r') as f:
#     map = [line.rstrip() for line in f.readlines()]

# m = len(map)
# n = len(map[0])

# # Find the starting spot:
# curR = 0
# curC = 0
# obsR = defaultdict(list)
# obsC = defaultdict(list)
# for r in range(m):
#     for c in range(n):
#         if map[r][c] == '^':
#             curR = r
#             curC = c
#         if map[r][c] == '#':
#             obsR[r].append(c)
#             obsC[c].append(r)

# # print("Row Obstacles: ", obsR)
# # print("Col Obstacles: ", obsC)
# def inMap(r,c):
#     if 0 <= r < m and 0 <= c < n:
#         return True
#     return False

# dirs = ( (-1,0), (0,1), (1,0), (0,-1) )

# def tryLoop(curR, curC, curDir):
#     newObstacle = (curR + dirs[curDir][0], curC + dirs[curDir][1])
#     seen = set()
#     seen.add((curR, curC, curDir))
#     curDir = curDir+1 if curDir < 3 else 0
#     while inMap(curR,curC):
#         if (curR,curC,curDir) in seen:
#             return (True, newObstacle)
#         seen.add((curR, curC, curDir))
#         nextR = curR + dirs[curDir][0]
#         nextC = curC + dirs[curDir][1]
#         if inMap(nextR,nextC) and map[nextR][nextC] == '#' or (nextR,nextC) == newObstacle:
#             curDir = curDir+1 if curDir < 3 else 0
#             nextR = curR + dirs[curDir][0]
#             nextC = curC + dirs[curDir][1]
#         curR = nextR
#         curC = nextC
#     return (False, (0,0))

# curDir = 0
# ret = set()
# while inMap(curR,curC):
#     nextR = curR + dirs[curDir][0]
#     nextC = curC + dirs[curDir][1]
    
#     if inMap(nextR,nextC) and map[nextR][nextC] == '#':
#         curDir = curDir+1 if curDir < 3 else 0
#         nextR = curR + dirs[curDir][0]
#         nextC = curC + dirs[curDir][1]
#     else:
#         (success, newObs) = tryLoop(curR, curC, curDir)
#         if success:
#             ret.add(newObs)
    
#     curR = nextR
#     curC = nextC

# print(len(ret))


# 1957 too high
# 1939 should be correct


def find_looped_route(start_pos, next_row, next_col, grid):
    row_count = len(grid)
    col_count = len(grid[0])
    curr_row, curr_col = start_pos
    visited = set()

    while True:
        # Add coords to visited
        visited.add((curr_row, curr_col, next_row, next_col))
        # Bounds check (is guard gonna leave)
        if curr_row + next_row < 0 or curr_row + next_row >= row_count or curr_col + next_col < 0 or curr_col + next_col >= col_count:
            break
        # Check for obstacle else move
        if grid[curr_row + next_row][curr_col + next_col] == "#":
            next_col, next_row = -next_row, next_col
        else:
            curr_row += next_row
            curr_col += next_col
        # Check if looped
        if (curr_row, curr_col, next_row, next_col) in visited:
            return True

total = 0
visited = set()
loopers = set()
with open("../Input/input6.txt", 'r') as f:
    data_input = [line.rstrip() for line in f.readlines()]
grid = [list(row) for row in data_input]

# Get start position of guard
start_pos = None
for row_idx, row in enumerate(grid):
    if "^" in row:
        col_idx = row.index("^")
        start_pos = (row_idx, col_idx)
    
next_row, next_col = -1, 0
# Loop the rows and columns, adding an obstacle and check for looped route
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != ".":
            continue
        grid[row][col] = "#"
        if find_looped_route(start_pos, next_row, next_col, grid):
            total += 1
        grid[row][col] = "."

print(total)