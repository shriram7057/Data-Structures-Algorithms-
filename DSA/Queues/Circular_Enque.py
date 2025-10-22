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

# Driver Code
ob = CircularQueue(5)
ob.enQueue(1)
ob.enQueue(2)
ob.enQueue(3)
ob.enQueue(4)
ob.enQueue(5)
ob.enQueue(6) # Fails to insert because front == 0 && rear == SIZE - 1
ob.display()