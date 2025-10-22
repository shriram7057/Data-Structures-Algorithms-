class Node:
   def __init__(self, key):
      self.leftChild = None
      self.rightChild = None
      self.data = key

# Create a function to perform preorder tree traversal
def PostorderTraversal(root):
   if root:
      PostorderTraversal(root.leftChild)
      PostorderTraversal(root.rightChild)
      print(root.data)

# Main class
if __name__ == "__main__":
   root = Node(3)
   root.leftChild = Node(26)
   root.rightChild = Node(42)
   root.leftChild.leftChild = Node(54)
   root.leftChild.rightChild = Node(65)
   root.rightChild.leftChild = Node(12)
   print("Postorder traversal of binary tree is")
   PostorderTraversal(root)