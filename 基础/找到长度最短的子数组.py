"""
给定一个含有n个正整数的数组和一个正整数s ,找出该数组中满足其和的长度最小的连续子数其长度。如果不存在符合
条件的子数组,返回0
输入: s=7, nums = [2,3,1,2,4,3]输出:2
解释:子数组[4,3]是该条件下的长度最小的子数组。
"""


class Solution:
    def ShortLenList(self, s: list, nums) -> int:
        if len(s) == 0:
            return 0
        result = list()
        cur_sum = s[0]
        lens = 1
        for i in s[1:]:
            if cur_sum + i == nums:
                lens = lens + 1
                result.append(lens)
            elif cur_sum + i > nums and i > nums:
                cur_sum = 0
                lens = 0
            elif cur_sum + i > nums > i:
                cur_sum = i
                lens = 1
            elif cur_sum + i < nums:
                cur_sum = cur_sum + i
                lens += 1
        return min(result)


A = Solution()
print(A.ShortLenList([2, 3, 1, 2, 4, 3], 7))
