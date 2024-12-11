#with open("inputTest.txt", 'r') as f:
with open("../Input/input11.txt", 'r') as f:
    stones = f.read().rstrip().split(" ")
    print(stones)

def operate(stone):
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        return [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
    
    return [str(int(stone) * 2024)]

for _ in range(25):
    newStones = []
    for s in stones:
        newStones += operate(s)
    stones = newStones

print(stones)

print(len(stones))