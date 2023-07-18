from typing import List


class Solution:
    def pivotIndex(self, nums1: List[int], nums2: List[int]) -> bool:
        a = b = d = 0
        nums3 = []
        while b < (len(nums2)):
            if nums1[a] == nums2[b]:
                nums3.append(nums2[b])
                if nums3 == nums1:
                    return True
                a += 1
                b += 1
            else:
                a = 0
                d += 1
                b = d
                nums3 = []
        else:
            return False


c = Solution()
print(c.pivotIndex([4, 1, 3, 5, 6], [1, 3, 2, 4, 1, 3, 5, 6]))
print(c.pivotIndex([2, 4], [1, 3, 2, 4, 1, 3, 5]))
print(c.pivotIndex([1, 3, 3], [1, 3, 2, 4, 1, 3, 5]))
print(c.pivotIndex([1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 7, 8, 9]))
