def witnesses(heights):
    # Fill this in.
    if (len(heights) == 0):
        return 0
    mostTall = heights[len(heights)-1]
    res = 1
    for i in range(len(heights)-2, -1, -1):
        if heights[i] > mostTall:
            mostTall = heights[i]
            res += 1
    return res


print(witnesses([3, 6, 3, 4, 1]))
# 3
