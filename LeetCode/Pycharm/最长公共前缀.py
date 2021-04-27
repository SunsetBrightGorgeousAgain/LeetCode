"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) ==0:
            return ""
        elif len(strs)==1:
            return strs[0]
        target = strs[0]
        lenx = len(target)
        m = len(strs) - 1
        for i in range(lenx,-1,-1):
            common = target[0:i]
            # print(common)
            n = 0
            for j in strs[1:]:
                if j.startswith(common):
                    n += 1
                else:
                    break
                if n == m:
                    return common
        return ""

A=Solution()
print(A.longestCommonPrefix(["flower","flow","flight"]))