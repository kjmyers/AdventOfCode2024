# from collections import deque 
# from trie import Trie, TrieNode

# patterns = []
# with open("inputTest.txt", 'r') as f:
# #with open("../Input/input19.txt", 'r') as f:
#     colorLine = [ x.strip() for x in f.readline().rstrip().split(',')]
#     f.readline()
#     for line in f.readlines():
#         patterns.append(line.rstrip())

# print(colorLine)
# print(patterns)

# # Add to trie and search

# t = Trie()
# for color in colorLine:
#     t.insert(color)

# print(t.search("ab"))

from functools import cache

words = set()
patterns = []

@cache
def isValid(pattern):
    if not pattern:
        return True
    
    for i in range(1, len(pattern) + 1):
        prefix = pattern[0:i]
        suffix = pattern[i:]
        
        if prefix in words and isValid(suffix):
            return True        
    
    return False
    

file_path = '../Input/input19.txt'

with open(file_path, 'r') as f:
    file = f.readlines()
    words = set(file[0].strip().split(", "))
    patterns = [pattern.strip() for pattern in file[2:]]

count = 0
for pattern in patterns:
    count += isValid(pattern)
print(count)