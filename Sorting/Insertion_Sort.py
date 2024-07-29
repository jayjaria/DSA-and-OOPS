arr = [3,1,4,5,2]

l=len(arr)
for i in range(1,l):
    if arr[i]<arr[i-1]:
        j=i
        while(j!=0 and arr[j]<arr[j-1]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1

print(arr)


"""
HOW IT WORKS:

-> We start from second element and checks if this element is at correct place by comparing to the previous elements.
-> And we will repeat this process for every element

TIME COMPLEXITY:

Best case: O(n), when list is already sorted
Avg case: O(n^2)
Worst case: O(n^2)

"""