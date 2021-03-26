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
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        else:
            min_res = nums[0]
            max_res = nums[0]
            res = nums[0]
            for num in nums[1:]:
                cur_min = min(min_res * num, max_res * num, num)
                cur_max = max(min_res * num, max_res * num, num)
                res = max(cur_max, res)
                min_res = cur_min
                max_res = cur_max
            return res


A = Solution()
print(A.maxProduct([1, 0, -1]))
print(A.maxProduct([2, 3, -2, 4]))
