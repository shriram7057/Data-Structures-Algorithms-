#Python program for Depth First Traversal
MAX = 5
class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
#stack variables
stack = []
top = -1
#graph variables
#array of vertices
lstVertices = [None] * MAX
#adjacency matrix
adjMatrix = [[0] * MAX for _ in range(MAX)]
#vertex count
vertexCount = 0
#stack functions
def push(item):
    global top
    top += 1
    stack.append(item)
def pop():
    global top
    item = stack[top]
    del stack[top]
    top -= 1
    return item
def peek():
    return stack[top]
def isStackEmpty():
    return top == -1
#graph functions
#add vertex to the vertex list
def addVertex(label):
    global vertexCount
    vertex = Vertex(label)
    lstVertices[vertexCount] = vertex
    vertexCount += 1
#add edge to edge array
def addEdge(start, end):
    adjMatrix[start][end] = 1
    adjMatrix[end][start] = 1
#Display the Vertex
def displayVertex(vertexIndex):
    print(lstVertices[vertexIndex].label, end=' ')
def getAdjUnvisitedVertex(vertexIndex):
    for i in range(vertexCount):
        if adjMatrix[vertexIndex][i] == 1 and not lstVertices[i].visited:
            return i
    return -1
def depthFirstSearch():
    lstVertices[0].visited = True
    displayVertex(0)
    push(0)
    while not isStackEmpty():
        unvisitedVertex = getAdjUnvisitedVertex(peek())
        if unvisitedVertex == -1:
            pop()
        else:
            lstVertices[unvisitedVertex].visited = True
            displayVertex(unvisitedVertex)
            push(unvisitedVertex)
    for i in range(vertexCount):
        lstVertices[i].visited = False
for i in range(MAX):
    for j in range(MAX):
        adjMatrix[i][j] = 0
addVertex('S')   # 0
addVertex('A')   # 1
addVertex('B')   # 2
addVertex('C')   # 3
addVertex('D')   # 4
addEdge(0, 1)    # S - A
addEdge(0, 2)    # S - B
addEdge(0, 3)    # S - C
addEdge(1, 4)    # A - D
addEdge(2, 4)    # B - D
addEdge(3, 4)    # C - D
print("Depth First Search:", end=' ')
depthFirstSearch()