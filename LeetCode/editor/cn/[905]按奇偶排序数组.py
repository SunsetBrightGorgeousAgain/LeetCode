# 给定一个非负整数数组 A，返回一个数组，在该数组中，
# A 的所有偶数元素之后跟着所有奇数元素。
# 
#  你可以返回满足此条件的任何数组作为答案。 
# 
#  
# 
#  示例： 
# 
#  输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 5000 
#  0 <= A[i] <= 5000 
#  
#  Related Topics 数组 双指针 排序 
#  👍 210 👎 0
"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArrayByParity(self, nums):
        oushu_list = list()
        jishu_list = list()
        for num in nums:
            if num%2==0:
                oushu_list.append(num)
            else:
                jishu_list.append(num)
        oushu_list = oushu_list + jishu_list
        return oushu_list
# leetcode submit region end(Prohibit modification and deletion)