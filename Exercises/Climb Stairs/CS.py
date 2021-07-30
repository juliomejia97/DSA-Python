class Solution():
    def climbStairs(self, num: int) -> int:
        return self.climbStairs_Memo(num)

    def climbStairs_BU(self, num):
        M = [-1 for i in range(num+1)]
        M[num] = 1
        M[num-1] = 1
        for i in range(num-2, -1, -1):
            M[i] = M[i+1] + M[i+2]
        return M[0]

    def climbStairs_Memo(self, num) -> int:
        M = [-1 for i in range(num+1)]
        return self.climbStairs_Memo_Aux(num, 0, M)

    def climbStairs_Memo_Aux(self, num, i, M) -> int:
        if M[i] == -1:
            if i == num:
                M[i] = 1
                print(M)
            elif i < num:
                oneStep = self.climbStairs_Memo_Aux(
                    num, i+1, M) if i+1 <= num else 0
                twoStep = self.climbStairs_Memo_Aux(
                    num, i+2, M) if i+2 <= num else 0
                M[i] = oneStep+twoStep
                print(M)
        return M[i]

    def climbStairs_Naive(self, num: int, i: int) -> int:
        if i == num:
            return 1
        elif i < num:
            oneStep = self.climbStairs_Naive(num, i+1) if i+1 <= num else 0
            twoStep = self.climbStairs_Naive(num, i+2) if i+2 <= num else 0
            return oneStep+twoStep


print(Solution().climbStairs(10))
