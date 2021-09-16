# 如果一个字符串不含有任何重复字符，我们称这个字符串为 好 字符串。 
# 
#  给你一个字符串 s ，请你返回 s 中长度为 3 的 好子字符串 的数量。 
# 
#  注意，如果相同的好子字符串出现多次，每一次都应该被记入答案之中。 
# 
#  子字符串 是一个字符串中连续的字符序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "xyzzaz"
# 输出：1
# 解释：总共有 4 个长度为 3 的子字符串："xyz"，"yzz"，"zza" 和 "zaz" 。
# 唯一的长度为 3 的好子字符串是 "xyz" 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aababcabc"
# 输出：4
# 解释：总共有 7 个长度为 3 的子字符串："aab"，"aba"，"bab"，"abc"，"bca"，"cab" 和 "abc" 。
# 好子字符串包括 "abc"，"bca"，"cab" 和 "abc" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 只包含小写英文字母。 
#  
#  Related Topics 哈希表 字符串 计数 滑动窗口 
#  👍 3 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        new_dict = dict()
        for i, j in enumerate(s):
            new_dict[i] = j
        if len(s) <= 2:
            return 0
        else:
            result = 0
            for m in range(0, len(s) - 2):
                if (new_dict.get(m) != new_dict.get(m + 1)) \
                        and (new_dict.get(m + 1) != new_dict.get(m + 2)) \
                        and (new_dict.get(m) != new_dict.get(m + 2)):
                    result += 1
            return result


# leetcode submit region end(Prohibit modification and deletion)
A = Solution()
print(A.countGoodSubstrings('aababcabc'))

