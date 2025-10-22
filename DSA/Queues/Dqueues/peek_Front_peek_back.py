#Python Program
SIZE = 5
deque = [0] * SIZE
front = -1
rear = -1
# Check if the deque is full
def isFull():
   if (front == 0 and rear == SIZE - 1) or front == rear + 1: return True
   return False
# Check if the deque is empty
def isEmpty():
   if front == -1: return True
   return False
# Insert element at the back
def push_back(element):
   global front
   global rear
   if isFull(): print("Deque is full")
   else:
      if front == -1: front = 0
      if rear == SIZE - 1: rear = 0
      else: rear = rear + 1
      deque[rear] = element
      print("Inserted ->", element)
# Get the element from the front
def peek_front():
   if isEmpty():
      print("Deque is empty")
      return -1
   else:
      return deque[front]
# Get the element from the back
def peek_back():
   if isEmpty():
      print("Deque is empty")
      return -1
   else:
      return deque[rear]
push_back(1)
push_back(2)
push_back(3)
push_back(4)
push_back(5)
print("\nElement at front:", peek_front())
print("Element at back:", peek_back())