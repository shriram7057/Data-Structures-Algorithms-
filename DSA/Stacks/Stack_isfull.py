#python code for stack(IsFull)
MAXSIZE = 8
stack = [None] * MAXSIZE
top = -1
#Check if the stack is empty 
def isfull():
    if top == MAXSIZE - 1:
        return True
    else:
        return False
#main function
print("Stack full:", isfull())