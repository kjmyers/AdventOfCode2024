import functools

#with open("inputTest.txt", 'r') as f:
with open("../Input/input11.txt", 'r') as f:
    stones = list(map(int, f.read().rstrip().split(" ")))
    print(stones)


dic = {}

#@functools.lru_cache
def operate(stone, times):
    if (stone,times) in dic:
        return dic[(stone,times)]
    
    if times == 0:
        return 1
    
    if stone == 0:
        return operate(1, times - 1)
    
    c = str(stone)
    if len(c) % 2 == 0:
        ret = operate(int(c[:len(c)//2]), times - 1) + operate(int(c[len(c)//2:]), times - 1)
        dic[(stone, times)] = ret
        return ret
    return operate(int(stone) * 2024, times - 1)

print(sum([operate(x, 75) for x in stones]))
