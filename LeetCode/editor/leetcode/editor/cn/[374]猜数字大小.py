
# leetcode submit region begin(Prohibit modification and deletion)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        right = 1
        left = n
        middle = 0
        while right <= left:
            middle = (right+left)//2
            res = guess(middle)
            if res == 0:
                return middle
            elif res == -1:
                left = middle-1
            else:
                right = middle+1
        return middle

        
# leetcode submit region end(Prohibit modification and deletion)
