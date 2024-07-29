arr = [2,4,1,3]
l=len(arr)
for i in range(l-1):
    for j in range(l-i-1):

        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
print(arr)


"""
HOW IT WORKS:

-> Compare the first two elements.
-> Swap them if the first is greater than the second.
-> Move to the next pair of elements, compare them, and swap if necessary.
-> Continue this process for the entire list.
-> Repeat the above steps for all elements, reducing the range of comparison by one each time, because the largest element will be at the end of the list after each pass. 

TIME COMPLEXITY:

-> Best Case: O(n), when list is already sorted
-> Avg Case: O(n^2)
-> Worst Case: O(n^2)

"""