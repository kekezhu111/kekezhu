from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = []
        for i in nums1:
            res = self.nextLess(i, nums2)
            count.append(res)

        return count

    def nextLess(self, i: int, nums: List[int]) -> int:
        slow = nums.index(i)
        while slow < len(nums) - 1:
            slow += 1
            if nums[slow] > i:
                return nums[slow]

        return -1


a = Solution()
print(a.nextGreaterElement([2, 4], [1, 2, 3, 4]))
print(a.nextGreaterElement([4, 1, 2], [1, 2, 4, 3]))
print(a.nextGreaterElement([3, 2, 4], [1, 2, 3, 4]))

