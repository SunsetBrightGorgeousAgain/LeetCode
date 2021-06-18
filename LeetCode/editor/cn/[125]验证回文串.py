# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串 
#  👍 388 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for i in s:
            if i.isalnum() or i.isalpha():
                new_s += i

        s_str = new_s[::-1]
        if s_str == new_s:
            return True
        else:
            return False


A = Solution()
print(A.isPalindrome("A man, a plan, a canal: Panama"))
# leetcode submit region end(Prohibit modification and deletion)
