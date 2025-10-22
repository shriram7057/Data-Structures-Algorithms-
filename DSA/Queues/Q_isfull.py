#python code for isFull in Queue
MAX = 6
intArray = [None] * MAX
front = 0
rear = -1
itemCount = 0

def isFull():
    return itemCount == MAX

def insert(data):
    global rear, itemCount
    if not isFull():
        if rear == MAX-1:
            rear = -1
        rear += 1
        intArray[rear] = data
        itemCount += 1
#inserting 5 items into the Queue
insert(3)
insert(5)
insert(9)
insert(1)
insert(12)
insert(15)
print("Queue: ", end="")
for i in range(MAX):
    print(intArray[i], end=" ")
print()
if isFull():
    print("Queue is full!")