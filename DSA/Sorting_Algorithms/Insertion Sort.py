def insertion_sort(array, size):
   for i in range(1, size):
      key = array[i]
      j = i
      while (j > 0) and (array[j-1] > key):
         array[j] = array[j-1]
         j = j-1
      array[j] = key
      
arr = [67, 44, 82, 17, 20]
n = len(arr)
print("Array before Sorting: ")
print(arr)
insertion_sort(arr, n);
print("Array after Sorting: ")
print(arr)