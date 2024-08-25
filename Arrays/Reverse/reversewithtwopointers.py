def reversepointer (arr, start, end):
    while start < end:
        arr[start], arr[end]= arr[end], arr[start]
        start +=1
        end -=1

array = [1,2,3,4,6,9]
reversepointer(array,0,5)
print(array)