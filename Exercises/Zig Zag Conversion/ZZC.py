from collections import defaultdict


def convert(s: str, numRows: int) -> str:
    rows = [[] for i in range(numRows)]
    currentRow = 0
    if currentRow == numRows - 1:
        return s
    goingDown = True
    for c in s:
        rows[currentRow].append(c)
        if currentRow == 0:
            goingDown = True
        elif currentRow == numRows-1:
            goingDown = False
        currentRow = currentRow + 1 if goingDown else currentRow - 1
    res = ""
    for l in rows:
        for c in l:
            res += c
    return res


s = "PAYPALISHIRING"
print(convert(s, 3))
