def printunion(arr1,arr2,n1,n2):
    hs = set()
    for i in range(0,n1):
        hs.add(arr1[i])
    
    for i in range(0,n2):
        hs.add(arr2[i])
    
    for i in hs:
        print(i,end=" ")

def printintersection(arr1,arr2,n1,n2):
    hs = set()
    for i in range(0,n1):
        hs.add(arr1[i])
        
    for i in range(0,n2):
        if arr2[i] in hs:
            print(arr2[i],end=" ")


arr1 = [1,2,3,5,7]
arr2 = [1,2,3,6,9]

printunion(arr1,arr2,len(arr1),len(arr2))
print("\n")
printintersection(arr1,arr2,len(arr1),len(arr2))


        
