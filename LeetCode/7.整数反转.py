"""给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverse(self, x: int):
        if -(2 ** 31) < x < 2 ** 31 - 1:
            if x < 0:
                x = str(x)
                y = x[0]
                x_str = x[1:]
                x_str = x_str[::-1]
                y_str = y + x_str
                if -(2 ** 31) < int(y_str) < 2 ** 31 - 1:
                    return int(y_str)
                else:
                    return 0
            elif x == 0:
                return 0
            else:
                x = str(x)
                x_str = x[::-1]
                if -(2 ** 31) < int(x_str) < 2 ** 31 - 1:
                    return int(x_str)
                else:
                    return 0
        else:
            return 0


A = Solution()
a = A.reverse(1534236469)
print(a)
print(-2 ** 31)
print(2 ** 31 - 1)
print(-2147483648<1534236469<2147483647)