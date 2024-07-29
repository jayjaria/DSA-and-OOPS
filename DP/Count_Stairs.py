def memo(n, dp):
    if n==0 or n==1:
        dp[n]=1
    
    if dp[n]!=-1:
        return dp[n]

    dp[n] = memo(n-1, dp)+memo(n-2, dp)
    return dp[n]

def tab(n):
    dp[0]=1
    dp[1]=1

    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[-1]

n=4
dp = [-1]*(n+1)
res = memo(n,dp)
print("memo",res)
print(dp)

dp = [-1]*(n+1)
res = tab(n)

print("tab",res)