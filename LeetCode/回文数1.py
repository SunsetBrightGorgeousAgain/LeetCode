# 都是整数.
# 是否能不转化为字符串进行处理

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str_folder = str(x)[::-1]
        x_str = str(x)
        if x_str_folder == x_str:
            return True
        else:
            return False


A = Solution()
print(A.isPalindrome(101))

# 不转化数字


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        result = 0
        result_list = []
        old_x = x
        while x >= 10:
            y = x % 10
            x = x // 10
            result_list.append(y)
        result_list.append(x)
        lens = len(result_list)
        for i, j in enumerate(result_list):
            result += j * (10**(lens - i - 1))
        if result == old_x:
            return True
        else:
            return False


A = Solution()
print(A.isPalindrome(6446))
