"""
CS 2302
Mark Williams
Lab 5 - Option B
Diego Aguirre/Manoj Saha
11-21-18
Purpose: Create a heap data structure and use it to implement heapsort
         on an array (list).
"""


import random
from Heap import Heap


def main():
  heap = Heap()
  array = list()
  size = 100
  for i in range(size):
    array.append(random.randint(0, size))
  print("Array before heapsort:")
  print(array)
  
  for value in array:
    heap.insert(value)
  del array
  print("Heap of array:")
  print(heap.heap_array)
  
  sorted_array = list()
  while len(heap.heap_array) > 0:
    sorted_array.append(heap.extract_min())
  print("Sorted array:")
  print(sorted_array)


main()
