def insertion_sort(array, size):
   for i in range(size):
      imin = i
      for j in range(i+1, size):
         if arr[j] < arr[imin]:
            imin = j
      temp = array[i];
      array[i] = array[imin];
      array[imin] = temp;

arr = [12, 19, 55, 2, 16]
n = len(arr)
print("Array before Sorting: ")
print(arr)
insertion_sort(arr, n);
print("Array after Sorting: ")
print(arr)