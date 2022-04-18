from queue import Queue
import queue
from traceback import print_tb

class Graph:
    def __init__(self,routes) -> None:
        self.routes=routes
        self.graph={}
        for start,end in self.routes:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]

    def Add_vertice(self,u,v):
        self.graph[u]=[v]
            
    def printGraph(self):
        return self.graph

routes = (('A','B'),('B','A'),('A','D'),('D','A'),('B','C'),('C','B'),('B','E'),('E','B'),('E','C'),('C','E'),('E','F'),('F','E'),
('D','G'),('G','D'),('D','H'),('H','D'),('G','H'),('H','G'))

# routes=(('A','B'),('A','D'),('B','C'),('B','E'),('E','C'),('E','F'),('D','G'),('D','H'),('G','H'))
g=Graph(routes)


######### BFS ##########
def BFS(graph,source,dest):
    # print(graph)
    visited = {}
    parent = {}
    level={}
    bfs_travers = []
    path = []
    queue = Queue()
    #initial value
    for i in graph.keys():
        visited[i] = False
        parent[i] = 0
        level[i] = -1
    
    visited[source] = True
    level[source] = 0
    queue.put(source)
    while  not queue.empty():
        u =queue.get()
        bfs_travers.append(u)
        for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v]=u
                    level[v]=level[u]+1
                    queue.put(v)
    
    while dest is not None:
        if dest != 0:
            # print(dest)
            path.append(dest)
            dest = parent[dest]
            # print(path)
        else:
            break

    path.reverse()
    print(path)
    # print(pare)
    # print(path.reverse())
    # print(level['G'])
    # print(bfs_travers)
BFS(g.printGraph(),'A','F')

    



# print("gggg",graphs)
