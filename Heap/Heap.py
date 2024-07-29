def maxHeapify(arr, i):
    parent = (i - 1) // 2
    if parent >= 0:
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            maxHeapify(arr, parent)


def insertNode(
    arr,
    key,
):

    arr.append(key)
    n = len(arr)

    maxHeapify(arr, n - 1)


def deleteFromHeap(arr):
    arr[0] = arr[-1]

    arr.pop()

    i = 0
    while i < len(arr):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if arr[i] < arr[left_index]:
            arr[i], arr[left_index] = arr[left_index], arr[i]
            i = left_index
        elif arr[i] < arr[right_index]:
            arr[i], arr[right_index] = arr[right_index], arr[i]
            i = right_index

        else:
            return


def heapify(arr, n, i):
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and arr[i] < arr[left_index]:
        largest = left_index

    if right_index < n and arr[i] < arr[right_index]:
        if arr[right_index] > arr[left_index]:
            largest = right_index

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def heapSort(arr, n):
    i = n - 1
    while i > 0:
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        i -= 1


arr = []
insertNode(arr, 10)
insertNode(arr, 4)
insertNode(arr, 3)
insertNode(arr, 2)
insertNode(arr, 1)
insertNode(arr, 7)
print("array", arr)
deleteFromHeap(arr)
print("deleted array", arr)


arr = [4, 1, 5, 2, 3, 7, 6]
print("array", arr)
n = len(arr)
for i in range((n // 2) - 1, -1, -1):
    heapify(arr, n, i)

print("heapified", arr)

arr = [5, 3, 4, 2, 1]
print("array", arr)
heapSort(arr, len(arr))
print("sorted", arr)
