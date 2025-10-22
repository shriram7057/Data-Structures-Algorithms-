#Python program for Breadth First Search
# defining MAX 5
MAX = 5
class Vertex:
   def __init__(self, label):
      self.label = label
      self.visited = False
# queue variables
queue = [0] * MAX
rear = -1
front = 0
queueItemCount = 0
# graph variables
#array of vertices
lstVertices = [None] * MAX
#adjacency matrix
adjMatrix = [[0] * MAX for _ in range(MAX)]
#vertex count
vertexCount = 0
# queue functions
def insert(data):
   global rear, queueItemCount
   rear += 1
   queue[rear] = data
   queueItemCount += 1
def removeData():
   global front, queueItemCount
   queueItemCount -= 1
   data = queue[front]
   front += 1
   return data
def isQueueEmpty():
   return queueItemCount == 0
# graph functions
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
#Display the vertex
def displayVertex(vertexIndex):
   print(lstVertices[vertexIndex].label, end=" ")
#Get the adjacent unvisited vertex
def getAdjUnvisitedVertex(vertexIndex):
   for i in range(vertexCount):
      if adjMatrix[vertexIndex][i] == 1 and not lstVertices[i].visited:
         return i
   return -1
def breadthFirstSearch():
    #mark first node as visited
   lstVertices[0].visited = True
   #Display the vertex
   displayVertex(0)
   #insert vertex index in queue
   insert(0)
   while not isQueueEmpty():
    #get the unvisited vertex of vertex which is at front of the queue
      tempVertex = removeData()     
      #no adjacent vertex found
      unvisitedVertex = getAdjUnvisitedVertex(tempVertex)
      while unvisitedVertex != -1:
         lstVertices[unvisitedVertex].visited = True
         displayVertex(unvisitedVertex)
         insert(unvisitedVertex)
         unvisitedVertex = getAdjUnvisitedVertex(tempVertex)     
    #queue is empty, search is complete, reset the visited flag 
   for i in range(vertexCount):
      lstVertices[i].visited = False
# main function
if __name__ == "__main__":
    #set adjacency
   for i in range(MAX):
       #matrix to 0
       for j in range(MAX):
         adjMatrix[i][j] = 0
   addVertex('S')
   addVertex('A')
   addVertex('B')
   addVertex('C')
   addVertex('D')
   addEdge(0, 1)
   addEdge(0, 2)
   addEdge(0, 3)
   addEdge(1, 4)
   addEdge(2, 4)
   addEdge(3, 4)
   print("Breadth First Search: ", end="")
   breadthFirstSearch()