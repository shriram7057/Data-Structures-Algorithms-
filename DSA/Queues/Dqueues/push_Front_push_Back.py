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
# Remove element from the front
def pop_front():
   global front
   global rear
   if isEmpty(): print("Deque is empty")
   else:
      print("Deleted from front ->", deque[front])
      if front == rear: front = rear = -1
      else: front = (front + 1) % SIZE
# Remove element from the back
def pop_back():
   global front
   global rear
   if isEmpty(): print("Deque is empty")
   else:
      print("Deleted from back ->", deque[rear])
      if front == rear: front = rear = -1
      elif rear == 0: rear = SIZE - 1
      else: rear = rear - 1
# Display the deque
def display():
   i = front
   if isEmpty(): print("Empty Deque")
   else:
      print("Elements ->", end = " ")
      while True:
         print(deque[i], end = " ")
         if i == rear: break
         i = (i + 1) % SIZE
      print(deque[rear])
push_back(1)
push_back(2)
push_back(3)
push_back(4)
push_back(5)
pop_front()
pop_back()
display()