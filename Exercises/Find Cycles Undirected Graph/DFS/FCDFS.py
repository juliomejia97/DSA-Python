from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v: int, parent: int, visited: list) -> bool:
        # Mark visited the vertex
        visited[v] = True
        # Get the list of adjacents nodes
        for i in self.graph[v]:
            # If I already visit the node and is different of his father then return True!
            # I have found a cycle!
            if parent != i and visited[i] == True:
                return True
            # If I don't have visited the vertex, then go to it
            elif not visited[i]:
                if(self.dfs(i, v, visited)):
                    return True
        return False

    def haveCycle(self):
        visited = [False for i in range(self.V)]
        for i in range(self.V):
            if not visited[i] and self.dfs(i, -1, visited):
                return True
        return False


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
print(g.haveCycle())
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
print(g1.haveCycle())
