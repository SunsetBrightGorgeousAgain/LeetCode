# 给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。 
# 
#  请你计算并返回该式的最大值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,4,5,2]
# 输出：12 
# 解释：如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) =
#  3*4 = 12 。 
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,5,4,5]
# 输出：16
# 解释：选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [3,7]
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 500 
#  1 <= nums[i] <= 10^3 
#  
#  Related Topics 数组 排序 堆（优先队列） 👍 23 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result_list = self.quicksorted(nums, 0, len(nums) - 1)
        print(result_list)
        m, n = result_list[-1], result_list[-2]
        return (m - 1) * (n - 1)

    def swap(self, input_list, i, j):
        input_list[i], input_list[j] = input_list[j], input_list[i]
        return input_list

    def quicksorted(self, input_list, start, end):
        if start < end:
            i = start
            j = end
            target = input_list[i]
            while i < j:
                while i < j and input_list[j] >= target:
                    j -= 1
                self.swap(input_list, i, j)

                while i < j and input_list[i] <= target:
                    i += 1
                self.swap(input_list, i, j)
            self.quicksorted(input_list, start, i - 1)
            self.quicksorted(input_list, j + 1, end)
        return input_list


# leetcode submit region end(Prohibit modification and deletion)

A = Solution()
print(A.maxProduct([1, 5, 4, 5]))
