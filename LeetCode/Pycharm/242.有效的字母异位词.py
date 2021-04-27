"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true

示例 2:

输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t)==0:
            return True
        s_dict = dict()
        t_dict = dict()
        for i in s:
            if i not in s_dict.keys():
                s_dict[i] = 1
            else:
                s_dict[i]+=1

        for i in t:
            if i not in t_dict.keys():
                t_dict[i] = 1
            else:
                t_dict[i]+=1

        if s_dict == t_dict:
            return True
        else:
            return False
