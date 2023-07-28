from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            if height[right] > height[left]:
                area = max(area, height[left] * (right - left))
                left += 1
            else:
                area = max(area, height[right] * (right - left))
                right -= 1
        return area


a = Solution()
print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(a.maxArea([1, 1]))

