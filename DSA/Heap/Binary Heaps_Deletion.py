#Python Program to perform Delete Operation on Binary Heap

def insert(heap, n, key):
   n = n + 1
   heap.append(key)
   i = n
   while i != 0 and heap[(i-1)//2] > heap[i]:
      heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
      i = (i-1)//2
   return n

def delete(heap, n):
   root = heap[0]
   heap[0] = heap[n-1]
   n = n - 1
   i = 0
   while 2*i + 1 < n:
      left = 2*i + 1
      right = 2*i + 2
      min = left
      if right < n and heap[right] < heap[left]:
         min = right
      if heap[i] > heap[min]:
         heap[i], heap[min] = heap[min], heap[i]
         i = min
      else:
         break
   return n

heap = [10, 20, 15, 40, 50, 100, 25]
n = 7
print("Heap before Delete Operation: ", end = "")
for i in range(n):
   print(heap[i], end = " ")
print()
n = delete(heap, n)
print("Heap after Delete Operation: ", end = "")
for i in range(n):
   print(heap[i], end = " ")