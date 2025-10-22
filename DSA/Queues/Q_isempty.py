#python code for isFull in Queue
MAX = 6
intArray = [None] * MAX
front = 0
rear = -1
itemCount = 0

def isEmpty():
    return itemCount == 0

print("Queue: ", end="")
for i in range(MAX):
    print(intArray[i], end=" ")
print()
if isEmpty():
    print("Queue is empty!")