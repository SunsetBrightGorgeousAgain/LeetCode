"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return Solution.climbStairs(self, n - 1) + Solution.climbStairs(self, n - 2)


A = Solution()
print(A.climbStairs(5))


class Solution:
    def climbStairs(self, n: int) -> int:
        result_dict = dict()
        result_dict[1] = 1
        result_dict[2] = 2
        for i in range(3, n+1):
            result_dict[i] = result_dict[i - 1] + result_dict[i - 2]
        return result_dict[n]


A = Solution()
print(A.climbStairs(1003))
