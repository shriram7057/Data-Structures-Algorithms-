class Node:
    def __init__(self, key):
        self.data = key
        self.degree = 0
        self.child = self.parent = self.sibling = None

def mergeBinomialTrees(b1, b2):
    if b1.data > b2.data:
        b1, b2 = b2, b1
    b2.parent = b1
    b2.sibling = b1.child
    b1.child = b2
    b1.degree += 1
    return b1

def unionBinomialHeap(h1, h2):
    if not h1: return h2
    if not h2: return h1

    dummy = Node(-1)  # Dummy node to track merged heap
    tail = dummy
    curr1, curr2 = h1, h2

    while curr1 and curr2:
        if curr1.degree <= curr2.degree:
            tail.sibling = curr1
            curr1 = curr1.sibling
        else:
            tail.sibling = curr2
            curr2 = curr2.sibling
        tail = tail.sibling

    tail.sibling = curr1 if curr1 else curr2
    return dummy.sibling  # Return merged heap without dummy node

def adjustHeap(head):
    if not head: return None
    prev, curr, next = None, head, head.sibling

    while next:
        if curr.degree != next.degree or (next.sibling and next.sibling.degree == curr.degree):
            prev, curr = curr, next
        else:
            if curr.data <= next.data:
                curr.sibling = next.sibling
                curr = mergeBinomialTrees(curr, next)
            else:
                if prev: prev.sibling = next
                else: head = next
                curr = mergeBinomialTrees(next, curr)
        next = curr.sibling

    return head

def insert(heap, key):
    temp = Node(key)
    return adjustHeap(unionBinomialHeap(heap, temp))

def printTree(h):
    while h:
        print(h.data, end=" ")
        printTree(h.child)
        h = h.sibling

def printHeap(h):
    print("Binomial Heap:")
    while h:
        print("B" + str(h.degree) + ": ", end="")
        printTree(h)
        print()
        h = h.sibling

# Testing the fixed binomial heap
hp = None
hp = insert(hp, 10)
hp = insert(hp, 20)
hp = insert(hp, 30)
hp = insert(hp, 40)
printHeap(hp)