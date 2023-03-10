#Function
def mergeSort(array):
    if len(array) > 1:

        #array divide
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


array = []
  
# number of elements as input
n = int(input("Enter N : "))
print("Elements - ")
for i in range(0, n):
    ele = int(input())
    array.append(ele)
    56
mergeSort(array)

print("Sorted array is: ")
for i in range(len(array)):
   print(array[i], end=" ")
   print()
