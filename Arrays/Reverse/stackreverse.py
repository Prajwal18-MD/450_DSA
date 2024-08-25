def array_stack(arr):
    stack= []
    
    for i in arr:
        stack.append(i)
    
    for j in range(len(arr)):
        a[j]= stack.pop()

a = [1,2,34,5,6,]
array_stack(a)
print(a)