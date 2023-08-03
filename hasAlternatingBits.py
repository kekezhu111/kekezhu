class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = f"{n : b}"
        slow, fast = 0, 1
        while fast < len(n):
            if n[fast] != n[slow]:
                slow += 1
                fast += 1
            else:
                return False

        return True


a = Solution()
print(a.hasAlternatingBits(5))
print(a.hasAlternatingBits(7))
print(a.hasAlternatingBits(11))

