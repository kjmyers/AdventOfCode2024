
with open('../Input/input2.txt','r') as f:
    ret = 0
    for line in f:
        nums = line.split(" ")
        inc = 0
        add = 1
        for i in range(1, len(nums)):
            diff = int(nums[i]) - int(nums[i-1])
            if diff == 0 or abs(diff) > 3:
                add = 0
                break
            
            if inc == 0:
                if diff > 0:
                    inc = 1
                else:
                    inc = -1
            
            if diff > 0 and inc != 1:
                add = 0
                break
            if diff < 0 and inc != -1:
                add = 0
                break

        ret += add
    
    print(ret)