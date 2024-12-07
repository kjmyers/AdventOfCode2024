from collections import defaultdict

with open("../Input/input7.txt", 'r') as f:
#with open("inputTest.txt", 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

equations = []

for line in lines:
    ans, equ = line.split(":")
    equations.append( [int(ans)] + [int(x) for x in equ.strip().split(" ")] )

def bt(val, i, nums):
    if i == len(nums):
        if val == nums[0]:
            return True
        else:
            return False
    
    return bt(val + nums[i],i+1, nums) or bt(val * nums[i],i+1, nums)


ret = 0
for line in equations:
    if bt(line[1], 2, line):
        ret += line[0]
    
print(ret)