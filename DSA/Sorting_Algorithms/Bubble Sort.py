def bubble_sort(array, size):
   for i in range(size):
      swaps = 0;
      for j in range(0, size-i-1):
         if(arr[j] > arr[j+1]):
            temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
            swaps = 1;
      if(swaps == 0):
         break;

arr = [67, 44, 82, 17, 20]
n = len(arr)
print("Array before Sorting: ")
print(arr)
bubble_sort(arr, n);
print("Array after Sorting: ")
print(arr)