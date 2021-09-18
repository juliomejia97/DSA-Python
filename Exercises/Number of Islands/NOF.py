def numIslands(grid: list[list[str]]) -> int:
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    cont = 0
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if grid[i][j] == "0":
                visited[i][j] = True
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if not visited[i][j]:
                dfs(i, j, visited)
                cont += 1
    return cont


def dfs(i: int, j: int, visited: list[list[str]]):
    if i >= len(visited) or j >= len(visited[0]) or i < 0 or j < 0:
        return
    if visited[i][j] == True:
        return
    visited[i][j] = True
    return dfs(i+1, j, visited), dfs(i, j+1, visited), dfs(i-1, j, visited), dfs(i, j-1, visited)


t1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

t2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

t3 = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]

print(numIslands(t1))
print(numIslands(t2))
print(numIslands(t3))
