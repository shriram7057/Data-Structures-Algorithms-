MAX = 6
intArray = [0] * MAX
front = 0
rear = -1
itemCount = 0
def isFull():
    return itemCount == MAX
def isEmpty():
    return itemCount == 0
def insert(data):
    global rear, itemCount
    if not isFull():
        if rear == MAX-1:
            rear = -1
        rear += 1
        intArray[rear] = data
        itemCount += 1
def removeData():
    global front, itemCount
    data = intArray[front]
    if front == MAX-1:
        front = 0
    else:
        front += 1
    itemCount -= 1
    return data
insert(3);
insert(5);
insert(9);
insert(1);
insert(12);
insert(15);
print("Queue: ")
for i in range(MAX):
    print(intArray[i], end = " ")
num = removeData()
print("\nElement removed: ", num)
print("Updated Queue: ")
while(not isEmpty()):
    n = removeData()
    print(n, end = " ")