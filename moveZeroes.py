from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        a, b = 0, 0
        for i in range(len(nums)):
            if nums[a] == 0 and nums[b] != 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b += 1
            elif nums[a] == 0 and nums[b] == 0:
                b += 1
            else:
                a += 1
                b += 1
        return nums


num = Solution()
print(num.moveZeroes([0, 1, 0]))
print(num.moveZeroes([1, 0, 0, 2, 3, 0, 5]))
print(num.moveZeroes([0, 0, 1, 5, 2]))
print(num.moveZeroes([]))

