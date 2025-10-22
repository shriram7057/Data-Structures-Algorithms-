import math
def jump_search(a, n, key):
   i = 0
   m = int(math.sqrt(n))
   k = m
   while(a[m] <= key and m < n):
      i = m
      m += k
      if(m > n - 1):
         return -1
   for j in range(m):
      if(arr[j] == key):
         return j
   return -1

arr = [0, 6, 12, 14, 19, 22, 48, 66, 79, 88, 104, 126]
n = len(arr);
print("Array elements are: ")
for i in range(n):
   print(arr[i], end = " ")
key = 66
print("\nThe element to be searched: ", key)
index = jump_search(arr, n, key)
if(index >= 0):
   print("The element is found at position: ", (index+1))
else:
   print("\nUnsuccessful Search")