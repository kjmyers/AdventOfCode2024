
with open('../Input/input22.txt', 'r') as f:
    initSecrets = [int(l.strip()) for l in f.readlines()]

print(initSecrets)

ret = 0

def getNextSecret(num):
    numx64 = num * 64
    newNum = num ^ numx64
    step1 = newNum % 16777216

    numdiv32 =  round(step1 / 32)
    newNum = num ^ numdiv32
    step2 = newNum % 16777216

    numx2048 =  step2 * 2048
    newNum = num ^ numx2048
    step3 = newNum % 16777216
    return step3


def randomNumber(seed):
    seed = ((seed << 6) ^ seed) % 16777216
    seed = ((seed >> 5) ^ seed) % 16777216
    seed = ((seed << 11) ^ seed) % 16777216
    return seed


    
total = 0
for num in initSecrets:
    curNum = num
    for i in range(2000):
        curNum = randomNumber(curNum)
    total += curNum

print(total)