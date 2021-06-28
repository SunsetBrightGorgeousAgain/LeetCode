# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[3,2,3]
# 输出：3 
# 
#  示例 2： 
# 
#  
# 输入：[2,2,1,1,1,2,2]
# 输出：2
#  
# 
#  
# 
#  进阶： 
# 
#  
#  尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。 
#  
#  Related Topics 位运算 数组 分治算法 
#  👍 1027 👎 0
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums) -> int:
        new_dict = dict()
        for i in nums:
            new_dict[i] = new_dict.get(i, 0) + 1
        # key_name = max(new_dict, key=new_dict.get)

        key_value = 0
        key_name = nums[0]
        for i, j in new_dict.items():
            if key_value < j:
                key_name = i
                key_value = j
        return key_name


# leetcode submit region end(Prohibit modification and deletion)

my_dict = {
    1: 4,
    2: 5,
    5: 6,
    7: 4
}
key_name = max(my_dict, key=my_dict.get)
print(my_dict.get)
print(key_name)
