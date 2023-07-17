from typing import List


class Solution:
    def two_list(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        for i in range(len(nums1) + len(nums2)):
            if nums1:
                a = nums1.pop(0)
                nums3.append(a)
            if nums2:
                b = nums2.pop(0)
                nums3.append(b)
        return nums3


num = Solution()
print(num.two_list(
    [1, 2, 3, 4, 5, 6, 7, 8, 16, 20],
    [11, 12, 13, 14, 15, 16, 9]))

