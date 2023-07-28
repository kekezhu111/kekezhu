from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits.insert(0, 1)
        return digits


a = Solution()
print(a.plusOne([1, 2, 3]))
print(a.plusOne([1, 5, 0, 9]))
print(a.plusOne([9, 9, 9]))

