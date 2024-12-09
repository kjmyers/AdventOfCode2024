from collections import defaultdict
import heapq

with open("../Input/input9.txt", 'r') as f:
#with open("inputTest.txt", 'r') as f:
    line = f.readlines()[0].rstrip()

print(line)
data = []
isfile = True
fid = 0
spaces = []
for c in line:
    if isfile:
        data += [str(fid)] * int(c)
        isfile = False
        fid += 1
    else:
        data += ['.'] * int(c)
        for ind in range( len(data) - int(c) ,len(data)):
            heapq.heappush(spaces, ind)
            #spaces.append(ind)
        isfile = True

print("".join(data))
print(spaces)

ind = 0
fileInd = len(data)-1

#while spaceInd < len(spaces): # and fileInd <
#for ind in spaces:
while fileInd > spaces[0] and spaces:
    ind = heapq.heappop(spaces)
    while data[fileInd] == '.':
        fileInd -= 1
    data[ind] = data[fileInd]
    data[fileInd] = '.'
    heapq.heappush(spaces, fileInd)

print("".join(data))

ret = 0
i = 0
while data[i] != '.':
    ret += int(data[i]) * i
    i += 1

print(ret)