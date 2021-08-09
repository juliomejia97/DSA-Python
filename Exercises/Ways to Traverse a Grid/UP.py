import math


def printM(M):
    print("-----------------")
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end="\t")
        print("")
    print("-----------------")


def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if(i == n-1 or j == m-1):
                dp[i][j] = 1
    for j in range(m-2, -1, -1):
        for i in range(n-2, -1, -1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]
    return dp[0][0]


def uniquePaths_Memo(m: int, n: int) -> int:
    M = [[math.inf for _ in range(m)] for _ in range(n)]
    return uniquePaths_Memo_Aux(0, 0, m, n, M)


def uniquePaths_Memo_Aux(i: int, j: int, m: int, n: int, M):
    if i > n-1 or j > m-1:
        return 0
    if M[i][j] == math.inf:
        if i == n-1 and j == m-1:
            M[i][j] = 1
            printM(M)
        else:
            M[i][j] = uniquePaths_Memo_Aux(
                i+1, j, m, n, M) + uniquePaths_Memo_Aux(i, j+1, m, n, M)
            printM(M)
    return M[i][j]


def uniquePaths_Naive(i: int, j: int, m: int, n: int):
    if i == n-1 and j == m-1:
        return 1
    if i > n-1 or j > m+1:
        return 0
    return uniquePaths_Naive(i+1, j, m, n) + uniquePaths_Naive(i, j+1, m, n)


print(uniquePaths(7, 3))
