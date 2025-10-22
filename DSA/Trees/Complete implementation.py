class Node:
   def __init__(self, data):
     self.left = None
     self.right = None
     self.data = data

# Insert method to create nodes
   def insert(self, data):
     if self.data:
       if data < self.data:
         if self.left is None:
            self.left = Node(data)
         else:
            self.left.insert(data)
       elif data > self.data:
         if self.right is None:
            self.right = Node(data)
         else:
            self.right.insert(data)
       else:
         self.data = data

# search method to compare the value with nodes
   def search(self, key):
     if key < self.data:
       if self.left is None:
         return str(key)+ " Not Found"
       return self.left.search(key)
     elif key > self.data:
       if self.right is None:
         return str(key)+" Not Found"
       return self.right.search(key)
     else:
       print(str(self.data) + ' is found')

# Print the tree
   def Inorder(self):
     if self.left:
       self.left.Inorder()
     print(self.data , " ->", end = " ")
     if self.right:
       self.right.Inorder()

# Print the tree
   def Preorder(self):
     print(self.data, " ->", end = " ")
     if self.left:
       self.left.Preorder()
     if self.right:
       self.right.Preorder()

# Print the tree
   def Postorder(self):
     if self.left:
       self.left.Postorder()
     if self.right:
       self.right.Postorder()
     print(self.data, " ->", end = " ")

root = Node(54)
root.insert(34)
root.insert(46)
root.insert(12)
root.insert(23)
root.insert(5)
print("Insertion Done")
print("Preorder Traversal: ")
root.Preorder()
print("\nInorder Traversal: ")
root.Inorder()
print("\nPostorder Traversal: ")
root.Postorder()
ele = 17
print("\nElement to be searched: ", ele)
print(root.search(ele))