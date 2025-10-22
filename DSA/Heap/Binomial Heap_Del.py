class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = self.child = None
        self.left = self.right = self
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.nodeCount = 0

    def insert(self, key):
        x = Node(key)
        if self.min is None:
            self.min = x
        else:
            x.right = self.min.right
            x.left = self.min
            self.min.right.left = x
            self.min.right = x
            if x.key < self.min.key:
                self.min = x
        self.nodeCount += 1

    def printHeap(self):
        if self.min is None:
            print("Heap is empty!")
            return
        temp = self.min
        print("Fibonacci Heap Root List: ", end="")
        while True:
            print(temp.key, end=" ")
            temp = temp.right
            if temp == self.min:
                break
        print()

fibHeap = FibonacciHeap()
fibHeap.insert(10)
fibHeap.insert(3)
fibHeap.insert(15)
fibHeap.insert(7)
fibHeap.printHeap()
print("Minimum value in heap:", fibHeap.min.key)