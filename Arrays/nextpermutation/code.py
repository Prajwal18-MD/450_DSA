def next_permutation(s:str)->str:
    arr=list(s)
    n = len(arr)
    i = n-2
    
    while i>=0 and arr[i]>=arr[i+1]:
        i-=1
        
    if i<0:
        print("No Permutation Available")
    
    j = n-1
    
    while j>=0 and arr[j]<=arr[i]:
        j-=1
    
    arr[i], arr[j]= arr[j], arr[i]
    
    arr[i+1:] = reversed(arr[i+1:])
    
    return ''.join(arr)

s = "abb"
print(next_permutation(s))