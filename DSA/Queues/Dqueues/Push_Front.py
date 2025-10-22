SIZE = 5
deque = [0] * SIZE
front = -1
rear = -1

# Check if the deque is full
def isFull():
    return (front == 0 and rear == SIZE - 1) or (front == rear + 1)

# Check if the deque is empty
def isEmpty():
    return front == -1

# Insert element at the front
def push_front(element):
   global front, rear
   if isFull():
      print("Deque is full")
   if isEmpty():
      front = rear = 0
   else:
      front = (front - 1 + SIZE) % SIZE
   deque[front] = element
   print("Inserted ->", element)

# Display the deque
def display():
    global front, rear
    if isEmpty():
        print("Empty Deque")
    else:
        i = front
        print("Elements ->", end=" ")
        while i != rear:
            print(deque[i], end=" ")
            i = (i + 1) % SIZE
        print(deque[rear])  # Print the last element

# Testing the functions
push_front(1)
push_front(2)
push_front(3)
push_front(4)
push_front(5)
display()