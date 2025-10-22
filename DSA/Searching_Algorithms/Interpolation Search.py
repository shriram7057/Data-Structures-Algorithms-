def interpolation_search( data, arr):
   lo = 0
   hi = len(arr) - 1
   mid = -1
   comparisons = 1
   index = -1
   while(lo <= hi):
      print("Comparison ", comparisons)
      print("lo : ", lo)
      print("list[", lo, "] = ")
      print(arr[lo])
      print("hi : ", hi)
      print("list[", hi, "] = ")
      print(arr[hi])
      comparisons = comparisons + 1

      #probe the mid point
      mid = lo + (((hi - lo) * (data - arr[lo])) // (arr[hi] - arr[lo]))
      print("mid = ", mid)

      #data found
      if(arr[mid] == data):
         index = mid
         break
      else:
         if(arr[mid] < data):
            
            #if data is larger, data is in upper half
            lo = mid + 1
         else:

            #if data is smaller, data is in lower half
            hi = mid - 1
   print("Total comparisons made: ")
   print(comparisons-1)
   return index

arr = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
#find location of 33
location = interpolation_search(33, arr)

#if element was found
if(location != -1):
   print("Element found at location: ", (location+1))
else:
   print("Element not found.")