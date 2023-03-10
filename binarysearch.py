
def binary_search(arr, target):
    # Set the initial left and right boundaries of the search
    left = 0
    right = len(arr) - 1
    
    # Continue searching until the left boundary surpasses the right boundary
    while left <= right:
        # Find the midpoint of the current range
        mid = (left + right) // 2
        
        # Check if the target is equal to the midpoint element
        if arr[mid] == target:
            return mid
        
        # If the target is less than the midpoint element, search the left half
        elif arr[mid] > target:
            right = mid - 1
        
        # If the target is greater than the midpoint element, search the right half
        else:
            left = mid + 1
            
    # If the target is not found, return -1
    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9]
target = 5
result = binary_search(my_list, target)
if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print("Element is not present in the array")
