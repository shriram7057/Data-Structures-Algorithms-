#Python code for Graph Data Struture
V = 5
#Maximum number of vertices in th graph
#Declaring vertices
class Vertex:
    def __init__(self, end):
        self.end = end
        self.next = None
#Declaring Edges
class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
#Declaring graph data structure
class Graph:
    def __init__(self):
        self.point = [None] * V
def create_graph(edges, x):
    graph = Graph()
    for i in range(V):
        graph.point[i] = None
    for i in range(x):
        start = edges[i].start
        end = edges[i].end
        v = Vertex(end)
        v.next = graph.point[start]
        graph.point[start] = v
    return graph
edges = [Edge(0, 1), Edge(0, 2), Edge(0, 3), Edge(1, 2), Edge(1, 4), Edge(2, 4), Edge(2, 3), Edge(3, 1)]
n = len(edges)
graph = create_graph(edges, n)
#Range
print("The graph created is: ")
for i in range(V):
    ptr = graph.point[i]
    while ptr is not None:
        print("({} -> {})".format(i, ptr.end), end="\t")
        ptr = ptr.next
    print()