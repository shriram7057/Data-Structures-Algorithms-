def binary_search(a, low, high, key):
   mid = (low + high) // 2
   if (low <= high):
      if(a[mid] == key):
         print("The element is present at index:", mid)
      elif(key < a[mid]):
         binary_search(a, low, mid-1, key)
      elif (a[mid] < key):
         binary_search(a, mid+1, high, key)
   if(low > high):
      print("Unsuccessful Search")

a = [6, 12, 14, 18, 22, 39, 55, 182]
n = len(a)
low = 0
high = n-1
key = 22
binary_search(a, low, high, key)
key = 54
binary_search(a, low, high, key)