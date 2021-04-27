"""
给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-sequence-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSubArray(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            res = nums[0]
            cur_max = nums[0]
            for num in nums[1:]:
                cur_max = max(num, cur_max+num)
                res = max(cur_max, res)
            return res


A = Solution()
print(A.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# 判断当前最大数值,加上当前数据后,是变大还是变小即可..
