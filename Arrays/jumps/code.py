def minJumps(arr, n):
    if (n <= 1):
        return 0

    if (arr[0] >= n-1):
        return 1

    if (arr[0] == 0):
        return -1

    maxReach = arr[0]
    step = arr[0]
    jump = 1

    for i in range(1, n):
        if (i == n-1):
            return jump

        if (arr[i] >= (n-1) - i):
            return jump + 1

        maxReach = max(maxReach, i + arr[i])
        step -= 1

        if (step == 0):
            jump += 1

            if(i >= maxReach):
                return -1

            step = maxReach - i

    return -1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)

print("Minimum number of jumps to reach end is % d " % minJumps(arr, size))
