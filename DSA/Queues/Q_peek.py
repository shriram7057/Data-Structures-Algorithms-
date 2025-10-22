MAX = 6
intArray = [0] * MAX
front = 0
rear = -1
itemCount = 0
def peek():
    return intArray[front]
def isFull():
    return itemCount == MAX
def insert(data):
    global rear, itemCount
    if(not isFull()):
        if(rear == MAX-1):
            rear = -1
        rear  = rear + 1
        intArray[rear] = data
        itemCount+1
insert(3);
insert(5);
insert(9);
insert(1);
insert(12);
insert(15);
print("Queue: ")
for i in range(MAX):
    print(intArray[i], end = " ")
print("\nElement at front: ", peek())