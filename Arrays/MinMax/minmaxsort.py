def minmax(arr):
    arr.sort()
    mm = {"min": arr[0], "max": arr[-1]}
    return mm

array = [12,45,91,29,1,34]
mima = minmax(array)

print("Minimun element is ", mima["min"])
print("Maximum element is ", mima["max"])