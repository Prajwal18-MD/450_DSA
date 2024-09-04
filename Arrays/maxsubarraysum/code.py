from sys import maxsize

def subarraysum(a,size):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end =0
    s=0
    
    for i in range(0,size):
        max_ending_here += a[i]
        
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i 
        
        if max_ending_here < 0:
            max_ending_here = 0
            s=i+1
    
    print("Max Sum of subarray \n")
    print(max_so_far)
    
    print("Start Index\n")
    print(start)
    
    print("End Index\n")
    print(end)

a = [1,-5,8,-2,1,2]
subarraysum(a,len(a))
