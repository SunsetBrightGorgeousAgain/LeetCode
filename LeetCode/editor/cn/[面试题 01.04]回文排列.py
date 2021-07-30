# 给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。 
# 
#  回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。 
# 
#  回文串不一定是字典当中的单词。 
# 
#  
# 
#  示例1： 
# 
#  输入："tactcoa"
# 输出：true（排列有"tacocat"、"atcocta"，等等）
#  
# 
#  
#  Related Topics 位运算 哈希表 字符串 
#  👍 54 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        str_dict = dict()
        for i in s:
            str_dict[i] = str_dict.get(i,0)+1
        times = 0
        for i in str_dict.values():
            if i % 2 == 1:
                times += 1
                if times >= 2:
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
A=Solution()
print(A.canPermutePalindrome('tactcoa'))