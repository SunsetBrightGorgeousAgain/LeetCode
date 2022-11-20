# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        elif -2 ** 31 <= dividend <= 2 ** 31 - 1:
            dividend = dividend - divisor
            Solution.divide(self, dividend, divisor)
        else:
            return 2 ** 31 - 1
# leetcode submit region end(Prohibit modification and deletion)

A = Solution()
print(A.divide(10, 3))
