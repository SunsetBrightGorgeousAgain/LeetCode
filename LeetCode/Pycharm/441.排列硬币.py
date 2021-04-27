"""
441. 排列硬币

你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.

示例 2:

n = 8

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

因为第四行不完整，所以返回3.

class Solution:
    def arrangeCoins(self, n: int) -> int:
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        F0 = 0
        F1 = 0
        i = 0
        while F0 < n:
            i += 1
            F1 = F0
            F0 += i
        if n - F1 == i:
            return i
        else:
            return i - 1


A = Solution()
print(A.arrangeCoins(10))
