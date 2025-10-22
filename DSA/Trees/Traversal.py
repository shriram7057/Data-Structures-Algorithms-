class Node:
   def __init__(self, key):
      self.leftChild = None
      self.rightChild = None
      self.data = key

# Create a function to perform inorder tree traversal
def InorderTraversal(root):
   if root:
      InorderTraversal(root.leftChild)
      print(root.data)
      InorderTraversal(root.rightChild)

# Main class
if __name__ == "__main__":
   root = Node(3)
   root.leftChild = Node(26)
   root.rightChild = Node(42)
   root.leftChild.leftChild = Node(54)
   root.leftChild.rightChild = Node(65)
   root.rightChild.leftChild = Node(12)

   # Function call
   print("Inorder traversal of binary tree is")
   InorderTraversal(root)