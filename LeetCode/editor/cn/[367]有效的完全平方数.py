# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。 
# 
#  进阶：不要 使用任何内置的库函数，如 sqrt 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num = 16
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：num = 14
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num <= 2^31 - 1 
#  
#  Related Topics 数学 二分查找 
#  👍 226 👎 0
"""
        for i in range(1, num+1):
            if i ** 2 <= num <= (i + 1) ** 2:
                if i ** 2 == num or (i + 1) ** 2 == num:
                    return True
        return False
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return True
        elif num == 1:
            return True
        elif num == 4:
            return True
        elif num < 4:
            return False
        r = (num // 2) + 1
        l = 2
        while l <= r:
            mid = (r + l) // 2
            if mid ** 2 == num:
                return True
            if mid ** 2 < num:
                l = mid + 1
            else:
                r = mid - 1
            print(l,r)
        return False


# leetcode submit region end(Prohibit modification and deletion)

a = Solution()
print(a.isPerfectSquare(16))
