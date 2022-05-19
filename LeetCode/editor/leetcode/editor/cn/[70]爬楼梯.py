# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶 
# 
#  示例 2： 
# 
#  
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics 记忆化搜索 数学 动态规划 👍 2414 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 2
        res = 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(3, n + 1):
                res = n1 + n2
                n1 = n2
                n2 = res
            return res

# leetcode submit region end(Prohibit modification and deletion)
