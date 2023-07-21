from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left * 2 + nums[i] == all:
                print(i)
            else:
                left += nums[i]
        return -1


a = Solution()
a.pivotIndex([1, 2, 3])
a.pivotIndex([2, 1, -1])
a.pivotIndex([1, 7, 3, 6, 5, 6])

