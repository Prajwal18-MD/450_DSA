def sort012(arr):
    c0 = 0
    c1 = 0
    c2 = 0

    
    for i in arr:
        if i == 0:
            c0 += 1
        elif i == 1:
            c1 += 1
        else:
            c2 += 1

    x = 0  

    
    for i in range(c0):
        arr[x] = 0
        x += 1  

    
    for i in range(c1):
        arr[x] = 1
        x += 1  

    
    for i in range(c2):
        arr[x] = 2
        x += 1  


a = [1,1,0,0,2,2]
sort012(a)

for x in a:
    print(x,end='')

