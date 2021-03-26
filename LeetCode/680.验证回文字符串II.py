"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True

示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。

注意:

    字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def check_str(s_new, m, n):
            while m < n:
                if s_new[m] == s_new[n]:
                    m += 1
                    n -= 1
                else:
                    return False
            return True

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if check_str(s[i + 1:j + 1], 0, len(s[i + 1:j + 1]) - 1) \
                        or check_str(s[i:j], 0, len(s[i:j]) - 1):
                    return True
                else:
                    return False
        return True


A = Solution()
print(A.validPalindrome('abvva'))

# print('abcdef'[2:4])
