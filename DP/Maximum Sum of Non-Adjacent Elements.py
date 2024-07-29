# Memoization
def func(ind, arr, dp):
    if ind==0:
        return arr[ind]
    if ind<0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    pick = arr[ind] + func(ind-2, arr, dp)
    notPick = 0 + func(ind-1, arr, dp)
    

    dp[ind] =  max(pick, notPick)
    return dp[ind]


# Tabulation
def tablutionFunc(dp, arr):
    dp[0] = arr[0]
    
    for i in range(1, len(arr)):
        take = arr[i]
        if i>1:
            take+=dp[i-2]
        notTake = 0 + dp[i-1]

        dp[i] = max(take, notTake)
    
    return dp[n-1]

# Space Optimized
def spaceOptimizedFunc(dp, arr):
    prev2=0
    prev=arr[0]

    for i in range(1, len(arr)):
        take = arr[i]
        if i>1:
            take+=prev2
        notTake = 0 + prev

        curr = max(take, notTake)

        prev2=prev
        prev=curr

    return prev

arr = [4,2,4,9]
n = len(arr)
dp = [-1]*n
print(tablutionFunc(dp, arr))

print(func(n-1, arr, dp))

print(spaceOptimizedFunc(dp,arr))
