#Implementation of circular queue using linked list in python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front
        print("Inserted ->", data)

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        elif self.front == self.rear:
            temp = self.front
            self.front = None
            self.rear = None
            return temp.value
        else:
            temp = self.front
            self.front = self.front.next
            self.rear.next = self.front
            return temp.value

    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            while True:
                print(temp.value, end = " ")
                temp = temp.next
                if temp == self.front:
                    break
            print()

# Driver Code
ob = CircularQueue()
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(6)
print("Initial Queue")
ob.display()
print("Element Removed= ", ob.dequeue())
print("Queue after deletion an element:")
ob.display()
ob.enqueue(9)
print("Rear Element ", ob.rear.value)
ob.enqueue(20)
print("Front Element ", ob.front.value)
print("Final Queue")
ob.display()