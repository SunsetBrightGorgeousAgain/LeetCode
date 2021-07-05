# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。 
# 
#  字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：text = "nlaebolko"
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：text = "loonbalxballpoon"
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：text = "leetcode"
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 10^4 
#  text 全部由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串 计数 
#  👍 51 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        result_dict = dict()
        for one_text in text:
            result_dict[one_text] = result_dict.get(one_text, 0) + 1

        result = result_dict.get('b', 0)
        for i in "balloon":
            n = result_dict.get(i, 0)
            if i == "l" or i == "o":
                n = n // 2
            if n <= result:
                result = n
        return result


# leetcode submit region end(Prohibit modification and deletion)

A = Solution()
print(A.maxNumberOfBalloons("loonbalxballpoon"))
