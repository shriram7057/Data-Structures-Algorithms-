def merge_sort(a, n):
   if n > 1:
      m = n // 2
      #divide the list in two sub lists
      l1 = a[:m]
      n1 = len(l1)
      l2 = a[m:]
      n2 = len(l2)
      #recursively calling the function for sub lists
      merge_sort(l1, n1)
      merge_sort(l2, n2)
      i = j = k = 0
      while i < n1 and j < n2:
         if l1[i] <= l2[j]:
            a[k] = l1[i]
            i = i + 1
         else:
            a[k] = l2[j]
            j = j + 1
         k = k + 1
      while i < n1:
         a[k] = l1[i]
         i = i + 1
         k = k + 1    
      while j < n2:
         a[k]=l2[j]
         j = j + 1
         k = k + 1

a = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 0]
n = len(a)
print("Array before Sorting")
print(a)
merge_sort(a, n)
print("Array after Sorting")
print(a)