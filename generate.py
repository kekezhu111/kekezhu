from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """创建并初始化dp数组"""
        dp = [[0] * numRow for numRow in range(1, numRows + 1)]
        for i in range(numRows):
            dp[i][0], dp[i][-1] = 1, 1

        cur = 2
        while cur < numRows:  # 判断条件
            for i in range(1, cur):
                # 递推公式
                dp[cur][i] = dp[cur - 1][i - 1] + dp[cur - 1][i]
            cur += 1

        return dp


a = Solution()
print(a.generate(3))
print(a.generate(6))
print(a.generate(8))

