# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

Find two indeices from list whose sum is equal to S in 0(n^2) time complexity.
"""

def find_sum_indices(array, S):
  flag = 0
  for i in range(0,len(array)-1):
    for j in range(i+16,len(array)):
      print(array[i] + array[j])
      if (array[i] + array[j] == S):
        return [i+1,j+1]
  
  return("Imposible")

array = []
  
# number of elements as input
n = int(input("Enter N : "))
print("Elements - ")
for i in range(0, n):
    ele = int(input())
    array.append(ele)
S = int(input("Enter S : "))
result = find_sum_indices(array,S)
print(result)