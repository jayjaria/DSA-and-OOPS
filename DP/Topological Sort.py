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

        return stack[::-1]
    

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort of the given graph is:")
print(g.topoSort())
        
        