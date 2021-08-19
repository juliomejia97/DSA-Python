from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, v, u):
        self.graph[v].append(u)

    def topologicalSort(self):
        res = []
        visited, cycle = set(), set()
        for i in range(self.V):
            if not self.dfs(i, visited, res, cycle):
                return []
        return res

    def dfs(self, v, visited, res, cycle):
        if v in cycle:
            return False
        if v in visited:
            return True
        cycle.add(v)
        for i in self.graph[v]:
            if not self.dfs(i, visited, res, cycle):
                return False
        cycle.remove(v)
        visited.add(v)
        res.append(v)

    def topologicalSort2(self):
        edges = [0]*(self.V)
        res = []
        d = deque()
        for x in range(self.V):
            if edges[x] == 0:
                d.append(x)
        while len(d) != 0:
            node = d.popleft()
            res.append(node)
            for v in self.graph[node]:
                edges[v] -= 1
                if edges[v] == 0:
                    d.append(v)
        return res[::-1] if len(res) == self.V else []


g = Graph(20)
g.addEdge(0, 10)
g.addEdge(3, 18)
g.addEdge(5, 5)
g.addEdge(6, 11)
g.addEdge(11, 14)
g.addEdge(13, 1)
g.addEdge(15, 1)
g.addEdge(17, 4)
print(g.topologicalSort2())
