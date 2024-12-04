with open('input.txt','r') as f:
    list1 = []
    list2 = []
    for line in f:
        nums = line.split(" ")
        list1.append(int(nums[0]))
        list2.append(int(nums[-1]))
    
    list1.sort()
    list2.sort()

    diff = 0
    
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])
    
    print(diff)