def quickSort(arr, low, high):
    """
    Sorts a subarray of arr from index low to index high using the quick sort algorithm
    """
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    return arr

def partition(arr, low, high):
    """
    Partitions a subarray of arr from index low to index high around a pivot element
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().strip().split()))
    sorted_arr = quickSort(arr, 0, len(arr) - 1)
    print(sorted_arr)
