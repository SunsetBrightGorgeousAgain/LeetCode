# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 667 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法
        res1 = math.floor(x / 2)
        res2 = math.ceil(x / 2)
        y = x
        if res1 ** 2 == x:
            return res1
        if res2 ** 2 == x:
            return res2
        while (res2 ** 2 < x and res1 ** 2 < x) or (res2 ** 2 > x and res1 ** 2 > x):
            if res1 ** 2 > x:
                y = res1
                res1 = math.floor(res1 / 2)
                res2 = math.ceil(res2 / 2)
            else:
                res1 = math.floor((res1 + y) / 2)
                res2 = math.ceil((res2 + y) / 2)

        if res2 ** 2 > x:
            return res1
        else:
            return res2


# leetcode submit region end(Prohibit modification and deletion)

A = Solution()
print(A.mySqrt(8))
