from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def root(self, id, p):
        if(id[p] == p):
            return p
        return self.root(id, id[p])

    def union(self, id, sz, p, q):
        i = self.root(id, p)
        j = self.root(id, q)
        # If the have the same parent, then do nothing, is balanced
        if (i == j):
            return
        # Paste the smallest tree to the greater
        if(sz[i] < sz[j]):
            id[i] = j
            sz[j] += sz[i]
        else:
            id[j] = i
            sz[i] += sz[j]

    def haveCycle(self):
        # Memory to the ids and sz
        id = [i for i in range(self.V)]
        sz = [1 for i in range(self.V)]
        visited = [False for i in range(self.V)]
        for i in self.graph:
            for j in self.graph[i]:
                if not visited[j]:
                    x = self.root(id, i)
                    y = self.root(id, j)
                    if x == y:
                        return True
                    self.union(id, sz, i, j)
                    visited[i] = True
        return False


g = Graph(4)
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
print(g.graph)
print(g.haveCycle())
