# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = 0
        left = math.floor(math.sqrt(c)) + 1
        while right <= left:
            if right ** 2 + left ** 2 == c:
                return True
            elif right ** 2 + left ** 2 > c:
                left -= 1
            else:
                right += 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
