import re

with open("../Input/input3.txt", 'r') as f:
    input = f.read()

input = re.sub('\n', '', input)

ret = 0
row = input
row += 'do()'
row = re.sub(r'don\'t\(\).+?do\(\)', '', row)
valList = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', row)
for a,b in valList:
    print(a,b)
    ret += int(a)*int(b)
        
print(ret)