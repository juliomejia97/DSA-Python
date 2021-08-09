# https://leetcode.com/problems/longest-common-subsequence/
def printM(M):
    print("-----------------")
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end="\t")
        print("")
    print("-----------------")


def LCS(s1: str, s2: str) -> str:
    return LCS_Memo(s1, s2)


def LCS_Memo(s1: str, s2: str) -> str:
    M = [[-1 for _ in range(len(s2))]for _ in range(len(s1))]
    return LCS_Memo_AUX(s1, s2, len(s1)-1, len(s2)-1, M)


def LCS_Memo_AUX(s1: str, s2: str, i: int, j: int, M):
    if i < 0 or j < 0:
        return 0
    if M[i][j] == -1:
        if s1[i] == s2[j]:
            M[i][j] = 1 + LCS_Memo_AUX(s1, s2, i-1, j-1, M)
            printM(M)
        else:
            p = LCS_Memo_AUX(s1, s2, i-1, j, M)
            q = LCS_Memo_AUX(s1, s2, i, j-1, M)
            M[i][j] = max(p, q)
    return M[i][j]


def LCS_AUX(s1: str, s2: str, i: int, j: int) -> int:
    if i < 0 or j < 0:
        return 0
    elif s1[i] == s2[j]:
        return 1 + LCS_AUX(s1, s2, i-1, j-1)
    else:
        p = LCS_AUX(s1, s2, i-1, j)
        q = LCS_AUX(s1, s2, i, j-1)
        return max(p, q)


print(LCS("abcde", "ace"))
