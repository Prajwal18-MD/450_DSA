def merge(arr1,arr2,n1,n2,arr3):
    i=0 
    j=0
    k=0
    
    while i<n1:
        arr3[k] = arr1[i]
        i+=1
        k+=1
    
    while j<n2:
        arr3[k] = arr2[j]
        j+=1
        k+=1
    
    arr3.sort()

arr1 = [1,3,5,6,7,8]
arr2 = [1,3,4,9]

n1=len(arr1)
n2=len(arr2)

arr3=[0 for i in range(n1+n2)]

merge(arr1,arr2,n1,n2,arr3)

for i in arr3:
    print(i,end=" ")

