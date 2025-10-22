class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

# Insert method to create nodes
   def insert(self, data):
      if self.data:
         if data  self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            self.data = data
   def printTree(self, prefex):
       if self is None:
           return
       self.left.printTree(prefex + "") if self.left else None
       print(prefex + "--", str(self.data),"", end = "")
       self.right.printTree(prefex + "") if self.right else None
root = Node(54)
root.insert(34)
root.insert(46)
root.insert(12)
root.insert(23)
root.insert(5)
print("Insertion Done")
print("BST: ")
root.printTree('')