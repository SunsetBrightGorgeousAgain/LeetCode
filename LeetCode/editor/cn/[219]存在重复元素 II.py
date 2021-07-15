# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
# 使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值
#  至多为 k。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,2,3,1], k = 3
# 输出: true 
# 
#  示例 2: 
# 
#  输入: nums = [1,0,1,1], k = 1
# 输出: true 
# 
#  示例 3: 
# 
#  输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false 
#  Related Topics 数组 哈希表 滑动窗口 
#  👍 285 👎 0
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if len(nums) == 0:
            return False
        else:
            res_dict = dict()
            for i, j in enumerate(nums):
                if res_dict.get(j, 'm') != 'm':
                    if i - res_dict.get(j) <= k:
                        return True
                res_dict[j] = i
            return False
# leetcode submit region end(Prohibit modification and deletion)
