# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 
# 不重复 的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  
# 
#  注意：本题与主站 15 题相同：https://leetcode-cn.com/problems/3sum/ 
#  Related Topics 数组 双指针 排序 👍 58 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []

        nums.sort()
        res_list = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i], nums[j], nums[k]] not in res_list:
                        res_list.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return res_list
# leetcode submit region end(Prohibit modification and deletion)
