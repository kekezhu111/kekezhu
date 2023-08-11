from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """判断字符串是否为空"""
        if not strs:
            return ''

        prefix, count = strs[0], len(strs)

        for i in range(1, len(strs)):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2) -> str:
        leigth, index = min(len(str1), len(str2)), 0
        while index < leigth and str1[index] == str2[index]:
            index += 1

        return str1[:index]


a = Solution()
print(a.longestCommonPrefix([]))
print(a.longestCommonPrefix(["flower", "floor", "flow"]))
print(a.longestCommonPrefix(["flower", "flow", "flight"]))

