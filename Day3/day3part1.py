
import re
with open("../Input/input3.txt", 'r') as f:
    input = [line.rstrip() for line in f.readlines()]
ret = 0
for row in input:
    valList = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', row)
    for a,b in valList:
        ret += int(a)*int(b)
        
print(ret)