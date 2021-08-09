class Solution(object):
    def pushDominoes(self, dominoes):
        N = len(dominoes)
        res = ['']*len(dominoes)
        force = [0]*len(dominoes)
        f = 0
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f
        f = 0
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = min(f-1, 0)
            force[i] -= f
        for i in range(len(dominoes)):
            if force == 0:
                res[i] = '.'
            elif force[i] < 0:
                res[i] = 'L'
            else:
                res[i] = 'R'
        return ''.join(res)


print(Solution().pushDominoes('LR'))
# ..RR.LL..RR
