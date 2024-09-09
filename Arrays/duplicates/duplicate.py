def duplicate(arr):
    freq_value = {}
    result=[]
    
    for num in arr:
        freq_value[num] = freq_value.get(num,0)+1
    
    for key,value in freq_value.items():
        if value > 1:
            result.append(key)
    
    if not result:
        return -1
    
    result.sort()
    
    return result


a = [1,1,2,2,3,4,5,6,6,7]
result = duplicate(a)
for i in result:
    print(i , end=" ")
    
        