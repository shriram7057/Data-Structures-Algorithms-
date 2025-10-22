#Python Program
SIZE = 5
deque = [0] * SIZE
front = -1
rear = -1

# Check if the deque is full
def isFull():
   if (front == 0 and rear == SIZE - 1) or (front == rear + 1):
      return True
   return False

# Check if the deque is empty
def isEmpty():
   if front == -1:
      return True
   return False

# Insert element at the back
def push_back(element):
   global front, rear
   if isFull():
      print("Deque is full")
   else:
      if front == -1:  # Initial insertion
         front = 0
         rear = 0
      elif rear == SIZE - 1 and front != 0:  # Wrap around
         rear = 0
      else:  # Normal case
         rear += 1
      deque[rear] = element
      print("Inserted ->", element)

# Display the deque
def display():
   global front, rear
   if isEmpty():
      print("Empty Deque")
   else:
      print("Elements ->", end=" ")
      i = front
      while True:
         print(deque[i], end=" ")
         if i == rear:  # Stop when we reach the last element
            break
         i = (i + 1) % SIZE  # Move to the next index, circularly
      print()

# Test the deque
push_back(1)
push_back(2)
push_back(3)
push_back(4)
push_back(5)
display()
