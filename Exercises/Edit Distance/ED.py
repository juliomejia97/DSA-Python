import math


def printM(M):
    print("-----------------")
    for j in range(len(M[0])):
        for i in range(len(M)):
            print(M[i][j], end=" ")
        print("")
    print("-----------------")
# end def


def distance(s1, s2):
    return distance_BU(s1, s2)


def distance_BU(s1, s2):
    M = [[math.inf for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1)+1):
        M[i][0] = i
    for j in range(len(s2)+1):
        M[0][j] = j

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] != s2[j-1]:
                insert = M[i-1][j]
                delete = M[i][j-1]
                change = M[i-1][j-1]
                M[i][j] = min(insert, delete, change)+1
            else:
                M[i][j] = M[i-1][j-1]
    return M[i][j]


def distance_Memo(s1, s2):
    M = [[math.inf for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    return distance_Memo_Aux(s1, s2, len(s1), len(s2), M)


def distance_Memo_Aux(s1, s2, i, j, M):
    if M[i][j] == math.inf:
        if i == 0 and j == 0:
            M[i][j] = 0
            printM(M)
        elif i != 0 and j == 0:
            M[i][j] = i
            printM(M)
        elif i == 0 and j != 0:
            M[i][j] = j
            printM(M)
        elif s1[i-1] != s2[j-1]:
            insert = distance_Memo_Aux(s1, s2, i-1, j, M)
            delete = distance_Memo_Aux(s1, s2, i, j-1, M)
            change = distance_Memo_Aux(s1, s2, i-1, j-1, M)
            M[i][j] = min(insert, delete, change)+1
            printM(M)
        else:
            M[i][j] = distance_Memo_Aux(s1, s2, i-1, j-1, M)
            printM(M)
    return M[i][j]


def distance_aux(s1, s2, i, j):
    if i == 0 and j == 0:
        return 0
    if i != 0 and j == 0:
        return i
    if i == 0 and j != 0:
        return j
    if s1[i-1] != s2[j-1]:
        insert = distance_aux(s1, s2, i-1, j)
        delete = distance_aux(s1, s2, i, j-1)
        change = distance_aux(s1, s2, i-1, j-1)
        return min(insert, delete, change)+1
    return distance_aux(s1, s2, i-1, j-1)


print(distance("horse", "ros"))
