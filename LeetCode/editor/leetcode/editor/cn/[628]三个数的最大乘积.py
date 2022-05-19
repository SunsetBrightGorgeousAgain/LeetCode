# 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：24
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [-1,-2,-3]
# 输出：-6
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  
#  Related Topics 数组 数学 排序 👍 377 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a, b, c = nums[0], nums[1], nums[-1]
        x, y, z = nums[-1], nums[-2], nums[-3]
        if a * b * c >= x * y * z:
            return a * b * c
        else:
            return x * y * z


# leetcode submit region end(Prohibit modification and deletion)

"""
        # 3 <= nums.length <= 10⁴
        min_num = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            temp = nums[i]
            res_min = min(min_num * temp, max_num * temp, temp)
            res_max = max(min_num * temp, max_num * temp, temp)
            min_num = res_min
            max_num = res_max
        return max_num
"""
