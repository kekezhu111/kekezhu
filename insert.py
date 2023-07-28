from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lst = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if lst == [] or i[0] > lst[-1][1]:
                lst.append(i)

            else:
                lst[-1][1] = max(lst[-1][1], i[1])
        return lst


a = Solution()
print(a.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(a.insert([[1, 3], [6, 9]], [2, 5]))

