# def fib(n, dp):
#     if n<=1:
#         dp[n]=n
    
#     if dp[n]!=-1:
#         return dp[n]
    
#     dp[n] = fib(n-1,dp)+fib(n-2,dp)
#     return dp[n]


# n=7
# dp=[-1]*(n+1)

# res = fib(n, dp)
# print(res)

def fib(n):
    prev=0
    curr=1

    for i in range(2,n+1):
        res = prev+curr
        prev = curr
        curr = res
    
    return curr

n=5
res = fib(n)
print(res)