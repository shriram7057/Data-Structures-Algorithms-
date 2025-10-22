import math
def exponential_search(a, n, key):
   i = 1
   m = int(math.pow(2, i))
   if(a[0] == key):
      return 0
   while(a[m] <= key and m < n):
      i = i + 1
      m = int(math.pow(2, i))
      low = 0
      high = n - 1
      while (low <= high):
         mid = (low + high) // 2
         if(a[mid] == key):
            return mid
         elif(a[mid] < key):
            low = mid + 1
         else:
            high = mid - 1
   return -1
   
arr = [6, 11, 19, 24, 33, 54, 67, 81, 94, 99]
n = len(arr);
print("Array elements are: ")
for i in range(len(arr)):
   print(arr[i], end = " ")
key = 67
print("\nThe element to be searched: ", key)
index = exponential_search(arr, n, key)
if(index >= 0):
   print("The element is found at index: ", (index))
else:
   print("\nUnsuccessful Search")