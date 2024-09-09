"Imagine you are adjusting the heights of platforms in a theme park so that the"
"difference between the tallest and shortest platforms is as small as possible." 
"You can raise or lower the platforms by a maximum of 6 units. The initial platform heights are"
"[7, 4, 8, 8, 8, 9]. The algorithm helps you adjust the platforms in such a way that the difference"
"between the tallest and shortest platforms is minimized to 5 units."

def minmaxdiff(arr, n ,k):
    arr.sort()
    ans = arr[n-1]-arr[0]
    
    tempmin = arr[0]
    tempmax = arr[n-1]
    
    for i in range(1,n):
        if arr[i]<k:
            continue
        
        tempmin = min(arr[0]+k,arr[i]-k)
        tempmax = max(arr[i-1]+k, arr[n-1]-k)
        
        ans = min(ans, tempmax-tempmin)
    
    return ans

k = 3
arr = [1,5,15,10]
n = len(arr)

result = minmaxdiff(arr,n,k)
print(result)