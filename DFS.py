import copy
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
route=(('A','B'),('A','D'),('B','C'),('B','E'),('E','C'),('E','F'),('D','G'),('D','H'),('G','H'))

g=Graph(route)
#################### DFS ##########################
def dfs(graph, start, end ,path=[]): 
    stack = []
    stack.insert(0,[start])

    while stack:
        path = stack.pop(0)
        node= path[-1]

        if node == end:
            return path
        child= []
        
        if node in graph:
            child= graph[node]

        for val in child:
            new_path= copy.deepcopy(path)
            new_path.append(val)
            stack.insert(0,new_path)
        # print(child)


graph=g.printGraph()
print(dfs(graph,'A','G'))


