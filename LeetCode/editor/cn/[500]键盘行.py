# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。 
# 
#  美式键盘 中： 
# 
#  
#  第一行由字符 "qwertyuiop" 组成。 
#  第二行由字符 "asdfghjkl" 组成。 
#  第三行由字符 "zxcvbnm" 组成。 
#  
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["Hello","Alaska","Dad","Peace"]
# 输出：["Alaska","Dad"]
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["omk"]
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：words = ["adsdf","sfd"]
# 输出：["adsdf","sfd"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 20 
#  1 <= words[i].length <= 100 
#  words[i] 由英文字母（小写和大写字母）组成 
#  
#  Related Topics 数组 哈希表 字符串 
#  👍 134 👎 0
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, words):
        s1 = "qwertyuiop"
        s2 = "asdfghjkl"
        s3 = "zxcvbnm"
        s1_dict = dict()
        s2_dict = dict()
        s3_dict = dict()
        for i in s1:
            s1_dict[i] = 1
        for i in s2:
            s2_dict[i] = 1
        for i in s3:
            s3_dict[i] = 1
        return_list = []
        for one_word_yuan in words:
            one_word = one_word_yuan.lower()
            first_num = one_word[0]
            if first_num in s1_dict:
                target = s1_dict
            elif first_num in s2_dict:
                target = s2_dict
            else:
                target = s3_dict
            i = 1
            for one_num in one_word[1:]:
                if one_num in target.keys():
                    i += 1
                else:
                    break
            if len(one_word_yuan) == i:
                return_list.append(one_word_yuan)
        return return_list


# leetcode submit region end(Prohibit modification and deletion)
A = Solution()
print(A.findWords(words=["adsdf", "sfd"]))
