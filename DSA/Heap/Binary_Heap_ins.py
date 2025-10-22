#Python Program to perform Insert Operation on Binary Heap

def insert(heap, n, key):
   n = n + 1
   heap.append(key)
   i = n - 1  # Start from the last index (zero-based)
   while i != 0 and heap[(i-1)//2] > heap[i]:
      heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
      i = (i-1)//2
   return n

heap = [10, 20, 15, 40, 50, 100, 25]
n = len(heap)
key = 12
n = insert(heap, n, key)
print("Heap after Insert Operation: ", end="")
for i in range(n):
   print(heap[i], end=" ")