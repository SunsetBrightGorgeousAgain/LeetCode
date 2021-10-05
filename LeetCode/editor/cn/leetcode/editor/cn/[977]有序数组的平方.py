# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 已按 非递减顺序 排序 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  请你设计时间复杂度为 O(n) 的算法解决本问题 
#  
#  Related Topics 数组 双指针 排序 👍 313 👎 0

"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = list()
        for i in nums:
            new_list.append(i ** 2)
        if len(new_list) == 1:
            return new_list
        else:
            return self.quick_sorted(new_list, 0, len(new_list) - 1)

    def swap(self, a_list, i, j):
        a_list[i], a_list[j] = a_list[j], a_list[i]
        return a_list

    def quick_sorted(self, a_list, start, end):
        if start < end:
            i = start
            j = end
            target = a_list[i]
            while i < j:
                while i < j and a_list[j] >= target:
                    j -= 1
                self.swap(a_list, i, j)

                while i < j and a_list[i] <= target:
                    i += 1
                self.swap(a_list, i, j)

                self.quick_sorted(a_list, start, i - 1)
                self.quick_sorted(a_list, j + 1, end)
            return a_list
"""
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = list()
        if len(nums) == 1:
            new_list.append(nums[0] ** 2)
            return new_list
        else:
            left = 0
            right = len(nums) - 1
            while left <= right:
                if abs(nums[left]) >= abs(nums[right]):
                    new_list.append(nums[left] ** 2)
                    left += 1
                else:
                    new_list.append(nums[right] ** 2)
                    right -= 1
            result_list = list()
            for i in new_list[::-1]:
                result_list.append(i)
            return result_list

# leetcode submit region end(Prohibit modification and deletion)
