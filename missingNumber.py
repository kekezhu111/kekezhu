from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        index = 0
        for i in range(len(nums)):
            if nums[i] != index:
                return index
            else:
                index += 1
        return len(nums)


lst = Solution()
print(lst.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(lst.missingNumber([0, 1, 3]))
print(lst.missingNumber([0, 1, 2]))
print(lst.missingNumber([1]))
print(lst.missingNumber([0]))
print(lst.missingNumber([1, 2]))

