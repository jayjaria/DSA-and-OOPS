arr = [3,1,6,1,6,5]
l=len(arr)
k=2
dp=[-1]*(l)
# Memoization
# def kjumps(ind,arr):
#     if ind==0:
#         return 0
#     if dp[ind]!=-1:
#         return dp[ind]
#     min_steps = 999999
#     for j in range(1,k+1):
#         if ind-j>=0:
#             jump = kjumps(ind-j,arr)+abs(arr[ind]-arr[ind-j])
#         min_steps = min(min_steps,jump)
#     dp[ind] = min_steps
#     return dp[ind]

# min_steps = kjumps(l-1,arr)
# print(min_steps)

# Tabulation
dp[0]=0
def kjumps(arr):
    for i in range(1,l):
        min_steps = 999999
        for j in range(1,k+1):
            if i-j>=0:
                jump = dp[i-j] + abs(arr[i]-arr[i-j])
            min_steps = min(min_steps,jump)
        dp[i] = min_steps
    return dp[i]

min_steps = kjumps(arr)
print(min_steps)