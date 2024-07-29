m=3
n=3
# p = [[-1]*(n)]*(m)
# def f(i,j):
#     if i==0 and j==0:
#         return 1
#     if i<0 or j<0:
#         return 0
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     l = f(i-1,j)
#     r = f(i,j-1)

#     dp[i][j] = l+r
#     return l+r
# i=m-1
# j=n-1
# res = f(i,j)
# print(res)

# In Recursion: Time Complexity is 2^(m*n) [Exponential, bcoz every box has two choice upward or left], Space Complexity is O(Path Length)
# After Memoization: TC is O(m*n)[Bcoz the max number of call will be m*n], SC is O((m-1)+(n-1))[Path Length] + O(n*m)[Stack Space]


# TABULATION
dp = [[0 for j in range(n)] for i in range(m)]
# def f(i,j):
#     for i in range(m):
#         for j in range(n):
#             if i==0 and j==0:
#                 dp[0][0]=1
#             else:
#                 l,r=0,0
#                 if i>0:
#                     l = dp[i-1][j]
#                 if j>0:
#                     r = dp[i][j-1]

#                 dp[i][j] = l+r

#     return dp[m-1][n-1]

# AFTER SPACE OPTIMIZATION(We just used prev and curr 1D arrays to store the values.(i-1) means the prev row.)
def f(i,j):
    prev = [0]*n
    for i in range(m):
        curr = [0]*n
        for j in range(n):
            if i==0 and j==0:
                curr[j] = 1
            else:
                l,r=0,0
                if i>0:
                    l = prev[j]
                if j>0:
                    r = curr[j-1]
                curr[j] = l + r
        prev = curr

    return prev[n-1]

i,j=0,0
res = f(i,j)
print(res)