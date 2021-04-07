def ArrayJumping(arr):
    
    ht = {}
    max_index = arr.index(max(arr))
    L = len(arr)    
    
    for i in range(L):
        ht[i] = (left(L,i,arr[i]),right(L,i,arr[i]))
    
    # print(ht)
    if max_index in ht[max_index]:
        return 1
    
    travel_set = set(ht[max_index]) 
    # print(travel_set)
    
    for step in range(2,L+1):
        for val in tuple(travel_set):
            travel_set.add(ht[val][0])
            travel_set.add(ht[val][1])
        print(travel_set)
        if max_index in travel_set:
            return step
    return -1
        

def left(length,index,number):
    left = number % length
    if left > index:
        left = length + index - left
    else:
        left = index - left
    return left

def right(length,index,number):
    right = number % length
    if right > length - index - 1:
        right = right + index - length
    else:
        right = right + index
    return right

print(ArrayJumping([1,2,3,4,2]))