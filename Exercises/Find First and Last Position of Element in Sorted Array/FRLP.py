import math


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = Solution().searchFirstOcurrence(nums, target)
        end = Solution().searchLastOcurrence(nums, target)
        return [start, end]

    def searchFirstOcurrence(self, nums: list[int], target: int):
        res = -1
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = (start+end)//2
            if (target < nums[mid]):
                end = mid - 1
            elif (target > nums[mid]):
                start = mid + 1
            else:
                res = mid
                end = mid - 1
        return res

    def searchLastOcurrence(self, nums: list[int], target: int):
        res = -1
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = (start+end)//2
            if (target < nums[mid]):
                end = mid - 1
            elif (target > nums[mid]):
                start = mid + 1
            if (target == nums[mid]):
                res = mid
                start = mid + 1
        return res


nums = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
target = 6
result = Solution().searchRange(nums, target)
print(result)
