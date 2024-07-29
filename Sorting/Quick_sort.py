def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

arr = [3,2,1,5,4]
arr = quick_sort(arr)
print(arr)

"""

HOW IT WORKS:

-> Find a pivot element, then put all the smaller elements in left array, larger elements in right array
   and store pivot element inside middle array.
-> Then Recursively do same things for sub-arrays(left and right)

TIME COMPLEXITY:
-> Best Case: O(nlog(n))
-> Average Case: O(nlog(n))
-> Worst Case: O(n^2), when the smallest or largest element is always chosen as a Pivot element

"""