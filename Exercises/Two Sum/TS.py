from typing import Sized


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictN = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in dictN:
                return [dictN[target-nums[i]], i]
            else:
                dictN[nums[i]] = i
        return res


l = [3, 3]
print(Solution().twoSum(l, 6))
