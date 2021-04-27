"""
152. 乘积最大子数组

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
"""


class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 0:
            return 0
        else:
            max_num = nums[0]
            cur_max = nums[0]
            cur_min = nums[0]
            for i in nums[1:]:
                cur_max1 = max(cur_max*i,cur_min*i,i)
                cur_min1 = min(cur_max*i,cur_min*i,i)
                max_num = max(cur_max1,max_num)
                cur_max = cur_max1
                cur_min = cur_min1
            return max_num

A=Solution()
print(A.maxProduct([-2,0,-1]))
print(A.maxProduct([2,3,-2,4]))
