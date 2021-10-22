class Solution:
    def reverse(self, x):
        res = 0
        # TODO: Analizar si es positivo o negativo
        negativeFlag = False
        if x < 0:
            negativeFlag = True
            x = x*-1

        while x > 0:
            val = x % 10
            res = res*10 + val
            x = x//10
        if negativeFlag:
            res = res*-1
            flag = -2**31
            if res < flag:
                return 0
        else:
            flag = 2**31-1
            if res > flag:
                return 0
        return res


print(Solution().reverse(-123))
# 321
print(Solution().reverse(2**31))
# 0
