
import random

def quickselect(arr, k):
    if k < 1 or k > len(arr):
        return None
    
    pivot = random.choice(arr)
    left, middle, right = partition(arr, pivot)
    
    if k <= len(left):
        return quickselect(left, k)
    elif k == len(left) + 1:
        return pivot
    else:
        return quickselect(right, k - len(left) - 1)

def partition(arr, pivot):

    left, middle, right = [], [], []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return left, middle, right

with open('input.txt', 'r') as f:
    arr = list(map(int, f.readline().strip().split()))
    print(arr)
    for line in f:
        k = int(line.strip())
        result = quickselect(arr, k)
        print(f"The {k}th smallest element in the array is {result}.")
