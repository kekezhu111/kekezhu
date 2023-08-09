class Solution:
    def climbStairs(self, n: int) -> int:
        """排除Corner Case"""
        if n <= 3:
            return n

        # 创建 dp table
        dp = [0] * (n + 1)

        # 初始化 dp 数组
        dp[1] = 1
        dp[2] = 2

        # 遍历顺序：从前往后，因为后面要用到前面的状态
        for i in range(3, n + 1):
            # 确定递推公式/状态转移公式
            dp[i] = dp[i - 1] + dp[i - 2]

        # 返回值
        return dp[n]


a = Solution()
print(a.climbStairs(2))
print(a.climbStairs(3))
print(a.climbStairs(4))


class Solution:
    """第二种解法"""

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        dp = [1, 2]

        for i in range(3, n + 1):
            total = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], total

        return dp[1]


a = Solution()
print(a.climbStairs(2))
print(a.climbStairs(3))
print(a.climbStairs(4))
print(a.climbStairs(5))

