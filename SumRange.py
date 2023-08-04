from typing import List


class NumArray:
    """
    前缀和方法
    SumRange(i, j) = sums[j + 1] - suma[i]
    """

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        _sums = self.sums
        return _sums[right + 1] - _sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


a = NumArray([-2, 0, 3, -5, 2, -1])
print(a.sumRange(0, 2))
print(a.sumRange(2, 5))
print(a.sumRange(0, 5))

