class Node:
   def __init__(self, val = 0):
      self.val = val
      self.next = None
def sublist_search(sub_ptr, list_ptr):
   if not sub_ptr and not list_ptr:
      return True
   if not sub_ptr or not list_ptr:
      return False
   ptr1 = sub_ptr
   ptr2 = list_ptr
   while ptr2:
      ptr2 = list_ptr
      while ptr1:
         if not ptr2:
            return False
         elif ptr1.val == ptr2.val:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
         else:
            break
      if not ptr1:
         return True
      ptr1 = sub_ptr
      list_ptr = list_ptr.next
   return False
node_sublist = Node(3)
node_sublist.next = Node(3)
node_sublist.next.next = Node(6)
node_list = Node(2)
node_list.next = Node(5)
node_list.next.next = Node(3)
node_list.next.next.next = Node(3)
node_list.next.next.next.next = Node(6)
node_list.next.next.next.next.next = Node(7)
node_list.next.next.next.next.next.next = Node(0)
res = sublist_search(node_sublist, node_list)
if res == True:
   print("Is the sublist present in the list? ", res)