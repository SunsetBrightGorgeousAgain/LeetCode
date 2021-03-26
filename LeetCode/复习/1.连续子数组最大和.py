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
        max_sum = nums[0]
        cur_max = 0
        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(cur_max, max_sum)
        return max_sum


A = Solution()
print(A.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# 一个是包含当前元素的子数组的最大子数组和,一个是到当前元素的最大子数组和.


class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_num = nums[0]
        cur_num = nums[0]

        for num in nums[1:]:
            cur_num = max(cur_num + num, num)
            max_num = max(cur_num, max_num)
        return max_num


A = Solution()
print(A.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
