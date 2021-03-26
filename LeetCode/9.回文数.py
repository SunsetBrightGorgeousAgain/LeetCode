"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
输入: 121
输出: true

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if isinstance(x, int):
            if x < 0:
                return False
            elif x == 0:
                return True
            else:
                str_x = str(x)[::-1]
                if str(x) == str_x:
                    return True
                else:
                    return False


A = Solution()
a = A.isPalindrome(12243)
print(a)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return str(x)[::-1] == s


A = Solution()
a = A.isPalindrome(12243)
print(a)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = ''
        x_back = x
        while x >= 10:
            y = x % 10
            new_x += str(y)
            x = x // 10
        if 0 <= x < 10:
            new_x += str(x)
        else:
            return False
        if new_x == str(x_back):
            return True
        else:
            return False


A = Solution()
a = A.isPalindrome(-23)
print(a)

# print(1182 % 10)  # 取余
# print(1182 // 10)  # 取商
# print(118 // 10)
# print(118 % 10)
# print(11 // 10)
# print(11 % 10)
