task = [[2,1,3],[3,4,6],[10,1,6],[8,3,7]]
# task = [[10,50,1],[5,100,11]]
l=len(task)
dp=[[-1]*(4)]*(l)

def func(day,last):
    maxi=0
    if day==0:
        for i in range(0,3):
            if i!=last:
                maxi = max(maxi,task[0][i])
        return maxi
    
    if dp[day][last]!=-1:
        return dp[day][last]
    
    maxi=0
    for i in range(0,3):
        if i!=last:
            points = task[day][i] + func(day-1,i)
            maxi = max(maxi,points)
            dp[day][last]=maxi
    return dp[day][last]
    
res = func(l-1,3)
print(res)