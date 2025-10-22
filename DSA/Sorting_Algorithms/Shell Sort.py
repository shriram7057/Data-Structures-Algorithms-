def shell_sort(array,n):
   gap = n//2 #using floor division to avoid float values as result
   while gap > 0:
      for i in range(int(gap),n):
         temp = array[i]
         j = i
         while j >= gap and array[j-gap] >temp:
            array[j] = array[j-gap]
            j -= gap
            array[j] = temp
      gap = gap // 2 #using floor division to avoid float values as result

arr = [33, 45, 62, 12, 98]
n = len(arr)
print("Array before Sorting: ")
print(arr)
shell_sort(arr, n);
print("Array after Sorting: ")
print(arr)