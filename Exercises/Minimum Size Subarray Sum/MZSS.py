import math


class Solution:
    def minSubArrayLen(self, nums, s):
        res = math.inf
        sumN = 0
        j = 0
        for i in range(len(nums)):
            sumN += nums[i]
            while sumN >= s:
                res = min(res, i+1-j)
                sumN -= nums[j]
                j += 1
        return res if res != math.inf else 0


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
