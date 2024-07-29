class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adjList = [[] for _ in range(vertices)]

    def add_edge(self,u,v):
        self.adjList[u].append(v)

    def topoSort(self):
        def dfs(v, visited, stack):
            visited[v] = True
            for i in self.adjList[v]:
                if not visited[i]:
                    dfs(i, visited, stack)

            stack.append(v)

        
        visited = [False]*self.v
        stack=[]

        for i in range(self.v):
            if not visited[i]:
                dfs(i, visited, stack)

        return stack
    
    def transpose(self):
        g = Graph(self.v)

        for i in range(self.v):
            for j in self.adjList[i]:
                g.add_edge(j,i)

        return g
    
    def dfs_transposed(self, v, visited, component):
        visited[v]=True
        component.append(v)
        for i in self.adjList[v]:
            if not visited[i]:
                self.dfs_transposed(i, visited, component)
        
    def printSCC(self):

        stack = self.topoSort()
        gr = self.transpose()

        visited = [False]*self.v
 
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                gr.dfs_transposed(v, visited, component)

                print(component)

        

g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Strongly Connected Components in the graph are:")
g.printSCC()

