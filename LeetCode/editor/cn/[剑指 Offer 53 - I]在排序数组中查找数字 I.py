# 统计一个数字在排序数组中出现的次数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2 
# 
#  示例 2: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  
# 
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/ 
#  Related Topics 数组 二分查找 👍 207 👎 0
"""
    def search(self, nums: List[int], target: int) -> int:
        result_dict = dict()
        for i in nums:
            result_dict[i] = result_dict.get(i, 0) + 1
        return result_dict.get(target, 0)
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result_dict = dict()
        for i in nums:
            result_dict[i] = result_dict.get(i, 0) + 1
        return result_dict.get(target, 0)
# leetcode submit region end(Prohibit modification and deletion)
