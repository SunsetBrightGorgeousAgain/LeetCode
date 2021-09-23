# 给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。 
# 
#  你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。 
# 
#  请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-3,2,-3,4,2]
# 输出：5
# 解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。
#                 累加求和
#                 startValue = 4 | startValue = 5 | nums
#                   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#                   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#                   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#                   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#                   (4 +2 ) = 6  | (5 +2 ) = 7    |   2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2]
# 输出：1
# 解释：最小的 startValue 需要是正数。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,-2,-3]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  -100 <= nums[i] <= 100 
#  
#  Related Topics 数组 前缀和 👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result = 0
        result_list = list()
        for i in nums:
            result += i
            result_list.append(result)
        if len(result_list) == 1:
            min_num = result_list[0]
        else:
            min_num = self.quicksorted(result_list, 0, len(result_list) - 1)
            min_num = min_num[0]
        result_num = 1 - min_num
        if result_num <= 1:
            result_num = 1
        return result_num
        # 排序

    def swap(self, a_list, a, b):
        a_list[a], a_list[b] = a_list[b], a_list[a]
        return a_list

    def quicksorted(self, a_list, start, end):
        if start < end:
            i = start
            j = end
            target = a_list[i]
            while i < j:
                while i < j and a_list[j] >= target:
                    j -= 1
                self.swap(a_list, i, j)

                while i < j and a_list[i] < target:
                    i += 1
                self.swap(a_list, i, j)

            self.quicksorted(a_list, start, i - 1)
            self.quicksorted(a_list, j + 1, end)
            return a_list


# leetcode submit region end(Prohibit modification and deletion)

A = Solution()
# print(A.minStartValue([-3, 2, -3, 4, 2]))
# print(A.minStartValue([1, 2]))
print(A.minStartValue([1, 5, 4, 5]))
