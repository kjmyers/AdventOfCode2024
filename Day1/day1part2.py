from collections import Counter 

with open('input.txt','r') as f:
    list1 = []
    list2 = []
    for line in f:
        nums = line.split(" ")
        list1.append(int(nums[0]))
        list2.append(int(nums[-1]))
    
    freq = Counter(list2)
    print(freq)

    ret = 0
    for num in list1:
        ret += num * freq[num]
    
    print(ret)