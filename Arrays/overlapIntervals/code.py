def overlap(arr):
    arr.sort(key=lambda x: x[0])
    res = [arr[0][:]]

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        if curr[0] < last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr[:])

    return res

arr = [[2,11],[1,3]]
res = overlap(arr)

print("Original array:", arr)
print("Merged intervals:", res)
