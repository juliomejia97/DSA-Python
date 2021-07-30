class Solution:
    def sortColors(self, nums: list[int]) -> None:
        dictN = {0: 0, 1: 0, 2: 0}
        for i in range(len(nums)):
            dictN[nums[i]] += 1
        position = 0
        for key in dictN:
            nums[position:position + dictN[key]
                 ] = [key for k in range(dictN[key])]
            position += dictN[key]


l = [2, 0, 2, 1, 1, 0]
Solution().sortColors(l)
