from ast import Param
from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, i: int, visited: list) -> bool:
        # Have the root or parent of the node
        parent = [-1 for j in range(self.V)]
        dq = deque()
        # Visit the node i
        visited[i] = True
        dq.append(i)
        while len(dq) > 0:
            # Pop from the queue the current node
            currentNode = dq.pop()
            # Get the adj list of the current Node
            for v in self.graph[currentNode]:
                # If is not visited, then visit and put to the queue (pending)
                if visited[v] == False:
                    visited[v] = True
                    dq.append(v)
                    # The parent of the node v of the adj list of the current node
                    parent[v] = currentNode
                # If the parent of the current node is different from the current then
                # We have found a cycle
                elif parent[currentNode] != v:
                    return True

    def haveCycle(self):
        visited = [False for i in range(self.V)]
        for i in range(self.V):
            if not visited[i] and self.bfs(i, visited):
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
