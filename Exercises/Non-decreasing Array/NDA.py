class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        cont = 0
        for i in range(1, len(nums)):
            if (nums[i] < nums[i-1]):
                if(i == 1 or nums[i-2] <= nums[i]):
                    nums[i-1] = nums[i]
                    cont += 1
                else:
                    nums[i] = nums[i-1]
                    cont += 1
        return cont <= 1
