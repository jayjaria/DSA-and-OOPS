arr = [1,4,2,5,3]

l=len(arr)
for i in range(l):
        min_index = i  # Assume the minimum is the first element
        for j in range(i + 1, l):
            if arr[j] < arr[min_index]:
                min_index = j  # Update the index of the minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap

print(arr)

"""
HOW IT WORKS:

-> Get the minimum element first then swap it with the first element of the array.
-> Then repeat the process for next minimum element and swap it with the second element of the array and carry till the end of the array.

TIME COMPLEXITY:

-> Best Case: O(n^2)
-> Average Case: O(n^2)
-> Worst Case: O(n^2)

"""
    