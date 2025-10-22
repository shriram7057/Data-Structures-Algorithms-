class Node(object):
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      self.height = 1
class AVLTree(object):
   def insert(self, root, key):
      if not root:
         return Node(key)
      elif key < root.data:
         root.left = self.insert(root.left, key)
      else:
         root.right = self.insert(root.right, key)
      root.h = 1 + max(self.getHeight(root.left),
         self.getHeight(root.right))
      b = self.getBalance(root)
      if b > 1 and key < root.left.data:
         return self.rightRotate(root)
      if b < -1 and key > root.right.data:
         return self.leftRotate(root)
      if b > 1 and key > root.left.data:
         root.left = self.lefttRotate(root.left)
         return self.rightRotate(root)
      if b < -1 and key < root.right.data:
         root.right = self.rightRotate(root.right)
         return self.leftRotate(root)
      return root
   def leftRotate(self, z):
      y = z.right
      T2 = y.left
      y.left = z
      z.right = T2
      z.height = 1 + max(self.getHeight(z.left),
         self.getHeight(z.right))
      y.height = 1 + max(self.getHeight(y.left),
         self.getHeight(y.right))
      return y
   def rightRotate(self, z):
      y = z.left
      T3 = y.right
      y.right = z
      z.left = T3
      z.height = 1 + max(self.getHeight(z.left),
         self.getHeight(z.right))
      y.height = 1 + max(self.getHeight(y.left),
         self.getHeight(y.right))
      return y
   def getHeight(self, root):
      if not root:
         return 0
      return root.height
   def getBalance(self, root):
      if not root:
         return 0
      return self.getHeight(root.left) - self.getHeight(root.right)
   def Inorder(self, root):
      if root.left:
         self.Inorder(root.left)
      print(root.data)
      if root.right:
         self.Inorder(root.right)
Tree = AVLTree()
root = None

root = Tree.insert(root, 10)
root = Tree.insert(root, 13)
root = Tree.insert(root, 11)
root = Tree.insert(root, 14)
root = Tree.insert(root, 12)
root = Tree.insert(root, 15)

# Inorder Traversal
print("Inorder traversal of the AVL tree is")
Tree.Inorder(root)