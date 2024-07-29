def func(arr):
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


arr=[2,3,2]
n = len(arr)
res = max(func(arr[1:]),func(arr[0:n-1]))
print(res)