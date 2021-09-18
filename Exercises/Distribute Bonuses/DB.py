def getBonuses(performance):
    start = 0
    end = len(performance)-1
    bonuses = [1]*len(performance)
    for i in range(1, len(performance)-1):
        if performance[i] > performance[i-1] and performance[i] > performance[i+1]:
            bonuses[i] += 2
        elif performance[i] > performance[i-1] or performance[i] > performance[i+1]:
            bonuses[i] += 1
    if performance[start] > performance[start+1]:
        bonuses[i] += 1
    if performance[end] > performance[end-1]:
        bonuses[i] += 1
    return bonuses


print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
