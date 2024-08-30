def rotation(arr,n):
    i=0
    j=n-1
    
    while i != j:
      arr[i],arr[j] = arr[j],arr[i]
      i+=1
    pass

arr = [1,2,3,4]
n = len(arr)

print("Array \n")
for i in range(0,n):
    print(arr[i], end='')

rotation(arr,n)

print("\n \nRotated Array \n")
for i in range(0,n):
    print(arr[i], end='')
