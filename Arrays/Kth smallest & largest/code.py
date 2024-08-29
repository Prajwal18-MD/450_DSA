import random

def kthSmallest(arr, l, r, k):
    if 0 < k <= r - l + 1:
        pos = randomPartition(arr, l, r)
        
        if pos - l == k - 1:
            return arr[pos]
        elif pos - l > k - 1:
            return kthSmallest(arr, l, pos - 1, k)
        else:
            return kthSmallest(arr, pos + 1, r, k - pos + l - 1)
    
    return float('inf')  


def kthLargest(arr, l, r, k):
    n = r - l + 1
    return kthSmallest(arr, l, r, n - k + 1)


def randomPartition(arr, l, r):
    pivot_index = random.randint(l, r)
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
    
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


if __name__ == '__main__':
    
    arr = [12,4,6,8,1,2]
    
    k = 3
    
    print("K'th smallest element is", kthSmallest(arr, 0, len(arr) - 1, k))
    print("K'th largest element is", kthLargest(arr, 0, len(arr) - 1, k))
    
