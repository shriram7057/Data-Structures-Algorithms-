class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def isFull(self):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            return True
        return False

    def isEmpty(self):
        if self.front == -1:
            return True
        return False

    def enQueue(self, data):
        if self.isFull():
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print("Inserted ->", data)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            print("Deleted ->", data)

    def display(self):
        if self.isEmpty():
            print("Empty Queue")
        else:
            print("Items")
            i = self.front
            while True:
                print(self.queue[i], end = " ")
                i = (i + 1) % self.size
                if i == (self.rear + 1) % self.size:
                    break
            print()
#Driver Code
ob = CircularQueue(5)
ob.deQueue() # Fails because front = -1
ob.enQueue(1)
ob.enQueue(2)
ob.enQueue(3)
ob.display()
ob.deQueue()
ob.display()