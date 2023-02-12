# -*- coding: utf-8 -*-
"""Find two indeices from list whose sum is equal to S in 0(n) time complexity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PL17XeGysHT7OhdGK9sgf19GF9fl6_u-

Find two indeices from list whose sum is equal to S in 0(n) time complexity.
"""

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