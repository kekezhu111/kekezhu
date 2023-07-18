from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in nums:
            if i >= target:
                return index
            index += 1
        else:
            return len(nums)


b = Solution()
print(b.searchInsert([1, 3, 5, 6], 5))
print(b.searchInsert([1, 3, 5, 6], 2))
print(b.searchInsert([1, 3, 5, 6], 7))
print(b.searchInsert([2, 3, 5, 6], 1))

