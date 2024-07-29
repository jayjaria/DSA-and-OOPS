def jump(ind, arr, dp):
    if ind==0:
        return 0
    
    if dp[ind]!=-1:
        return dp[ind]
    left = jump(ind-1, arr, dp) + abs(arr[ind] - arr[ind-1])

    right = float("inf")
    if ind>1:
        right = jump(ind-2, arr, dp) + abs(arr[ind]-arr[ind-2])
        
    dp[ind] = min(left, right)
    return dp[ind]
    


arr = [3,1,6,1,6,5]
l = len(arr)
dp = [-1]*l
res = jump(l-1,arr, dp)
print(res)


def jump(arr, l):
    prev, prev2 = 0, 0
    
    for i in range(1,l):

        oneStep = prev + abs(arr[i]-arr[i-1])

        twoStep = float("inf")
        if i>1:
            twoStep = prev2 + abs(arr[i]-arr[i-2])

        curr = min(oneStep, twoStep)

        prev2 = prev
        prev = curr

    return prev

res = jump(arr, l)
print(res)
