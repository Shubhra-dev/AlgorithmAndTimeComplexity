def find_sum_indices(array, S):
    i, j = 0, len(array) - 1

    while i < j:
        if array[i] + array[j] == S:
            return (i+1, j+1)
        elif array[i] + array[j] < S:
            i += 1
        else:
            j -= 1

    return -1

array = []
n = int(input("Enter N : "))
print("Elements - ")
for i in range(0, n):
    ele = int(input())
    array.append(ele)
S = int(input("Enter S : "))
result = find_sum_indices(array,S)

if(result == -1):
  print('Impossible')
else:
    print(result)
