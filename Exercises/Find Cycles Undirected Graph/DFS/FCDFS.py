from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

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


g = Graph(20)
g.addEdge(0, 10)
g.addEdge(3, 18)
g.addEdge(5, 5)
g.addEdge(6, 11)
g.addEdge(11, 14)
g.addEdge(13, 1)
g.addEdge(15, 1)
g.addEdge(17, 4)
print(g.haveCycle())
