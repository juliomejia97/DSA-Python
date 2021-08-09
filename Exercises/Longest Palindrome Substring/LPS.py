def printM(M):
    print("-----------------")
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], "(", i, " ", j, ")", end="\t")
        print("")
    print("-----------------")


def LPS(s: str) -> str:
    dp = [[0]*len(s) for _ in range(len(s))]
    res = ''
    for i in range(len(s)):
        dp[i][i] = 1
        res = s[i]
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if j-i == 1 or dp[i+1][j-1]:
                    dp[i][j] = 1
                    if len(res) < len(s[i:j+1]):
                        res = s[i:j+1]
    return res


def LPS_Aux(s: str, i: int, j: int) -> str:
    if i == j or isPalindrome(s, i, j):
        return s[i:j+1]
    left = LPS_Aux(s, i+1, j)
    right = LPS_Aux(s, i, j-1)
    middle = LPS_Aux(s, i+1, j-1)
    if len(left) >= len(right) and len(left) >= len(middle):
        return left
    elif len(right) >= len(left) and len(right) >= len(middle):
        return right
    else:
        return middle


def isPalindrome(s: str, i: int, j: int):
    rev = ''.join(reversed(s[i:j+1]))
    return s[i:j+1] == rev


print(LPS("babad"))
