# import re
# import numpy as np
# import math

# ret = 0
# #with open("inputTest.txt", 'r') as f:
# with open("../Input/input13.txt", 'r') as f:
#     while True:
#         # Read A
#         a = f.readline().rstrip()
#         if not a:
#             break
#         v = re.search(r'\+([0-9]+).*\+([0-9]+)', a)
#         a1 = int(v.group(1))
#         a2 = int(v.group(2))
#         # Read B
#         b = f.readline().rstrip()
#         v = re.search(r'\+([0-9]+).*\+([0-9]+)', b)
#         b1 = int(v.group(1))
#         b2 = int(v.group(2))

#         eq = np.array([[a1, b1], [a2, b2]])

#         # Read Prize
#         prize = f.readline().rstrip()
#         v = re.search(r'=([0-9]+).*=([0-9]+)', prize)
#         p1 = int(v.group(1))
#         p2 = int(v.group(2))
#         ans = np.array([[p1], [p2]])
        
#         x = np.linalg.solve(eq, ans)

#         if math.isclose(x[0][0], math.floor(x[0][0]), rel_tol=0.0001) and math.isclose(x[1][0], math.floor(x[1][0]), rel_tol=0.0001):
#             print(a,b)
#             ret += math.floor(x[0][0]) * 3 + math.floor(x[1][0])

#         # Skip line
#         f.readline()

# print(ret)

# 24583 too low


import itertools as it, functools as ft, re

games = [tuple(map(int, it.chain(*map(ft.partial(re.findall, r'\d+'), game)))) for game in it.batched(open('../Input/input13.txt').read().splitlines(),4)]
for p, total in (0,0), (10000000000000,0):
    for ax, ay, bx, by, X, Y in games:
        A = int(round(((X+p)-bx*(B:=int(round(((Y+p)-(ay*(X+p))/ax)/(by-(ay*bx)/ax), 0))))/ax, 0))
        total+=A*3+B if A*ax+B*bx==(X+p) and A*ay+B*by==(Y+p) else 0
    print(total)