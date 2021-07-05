# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[3, 2, 1]
# 输出：1
# 解释：第三大的数是 1 。 
# 
#  示例 2： 
# 
#  
# 输入：[1, 2]
# 输出：2
# 解释：第三大的数不存在, 所以返回最大的数 2 。
#  
# 
#  示例 3： 
# 
#  
# 输入：[2, 2, 3, 1]
# 输出：1
# 解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
# 此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 104 
#  -231 <= nums[i] <= 231 - 1 
#  
# 
#  
# 
#  进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？ 
#  Related Topics 数组 排序 
#  👍 230 👎 0
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:


class Solution:
    def thirdMax(self, nums) -> int:
        if len(nums) <= 1:
            return nums[0]
        else:
            if nums[1] > nums[0]:
                first = nums[1]
                second = nums[0]
            elif nums[1] == nums[0]:
                first = nums[1]
                second = nums[0]
            else:
                first = nums[0]
                second = nums[1]
            if len(nums) == 2:
                return first
            else:
                third = nums[2]
                for i in nums[2:]:
                    if i == first:
                        third = first
                    elif i == second:
                        third = first
                    else:
                        if i > first:
                            first, second, third = i, first, second
                        elif i > second:
                            first, second, third = first, i, second
                        elif i > third:
                            first, second, third = first, second, i
                        else:
                            pass
                if first == second or first == third or second == third:
                    return first
                return third
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def thirdMax(self, nums) -> int:
        return_dict = dict()
        for num in nums:
            return_dict[num] = return_dict.get(num, 0) + 1
        keys_list = list()
        for i in return_dict.keys():
            keys_list.append(i)
        keys_len = len(keys_list)
        if keys_len == 1:
            return keys_list[0]
        elif keys_len == 2:
            return max(keys_list[0], keys_list[1])
        else:
            n1 = max(keys_list[0], keys_list[1], keys_list[2])
            n3 = min(keys_list[0], keys_list[1], keys_list[2])
            n2 = keys_list[0] + keys_list[1] + keys_list[2] - n1 - n3
            for num in keys_list[3:]:
                if num > n1:
                    n1, n2, n3 = num, n1, n2
                elif num > n2:
                    n1, n2, n3 = n1, num, n2
                elif num > n3:
                    n1, n2, n3 = n1, n2, num
                else:
                    n1, n2, n3 = n1, n2, n3
            return n3


# leetcode submit region end(Prohibit modification and deletion)

A = Solution()
print(A.thirdMax([5, 2, 4, 1, 3, 6, 0]))
