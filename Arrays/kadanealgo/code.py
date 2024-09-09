def subsum(arr):
    res = 0
    
    for i in range(len(arr)):
        cursum = 0
        
        for j in range(i,len(arr)):
            cursum = cursum + arr[j]
            
        
        res = max(res,cursum)
    
    return res

arr = [1,-1,3,4,6,7,-8]
res = subsum(arr)

print(res)
            