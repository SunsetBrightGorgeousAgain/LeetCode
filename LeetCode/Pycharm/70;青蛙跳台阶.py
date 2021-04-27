"""
剑指 Offer 10- II. 青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2

示例 2：

输入：n = 7
输出：21

示例 3：

输入：n = 0
输出：1

提示：

    0 <= n <= 100

注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/
"""


class Solution:
    def numWays(self, n: int) -> int:
        f_dict = dict()
        f_dict[0] = 1
        f_dict[1] = 1
        f_dict[2] = 2
        # f(n) = f(n-1)+f(n-2)
        for i in range(3, n + 1):
            f_dict[i] = f_dict[i - 1] + f_dict[i - 2]
        return f_dict[n] % 1000000007


A = Solution()
print(A.numWays(0))


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        d1 = 1
        d2 = 2
        # f(n) = f(n-1)+f(n-2)
        di = 0
        for i in range(3, n + 1):
            di = d1+d2
            d1 = d2
            d2 = di
        return di % 1000000007


A = Solution()
print(A.numWays(0))
