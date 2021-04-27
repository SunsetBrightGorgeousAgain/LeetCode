"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
"""


class Solution:
    def twoSum(self, nums, target):
        for index, value in enumerate(nums):
            if target - value in nums and nums.index(target - value) != index:
                return [index, nums.index(target - value)]


A = Solution()
result = A.twoSum([1, 2, 3, 5, 6, 8, 4], 6)
print(result)


class Solution:
    def twoSum(self, nums, target):
        hash_dict = dict()
        for index, value in enumerate(nums):
            hash_dict[value] = index
        for index, value in enumerate(nums):
            if hash_dict.get(target - value):
                if hash_dict.get(target - value) != index:
                    return [index, hash_dict[target - value]]


c = {1: 2, 3: 4}
print(c.get(1))

V = Solution()
C = V.twoSum([1, 2, 5, 6, 8, 3, 6], 10)
print(C)


class Solution:
    def twoSum(self, nums, target):
        for index, value in enumerate(nums):
            if target - value in nums[index:] and nums.index(target - value) != index:
                return [index, nums.index(target - value)]


A = Solution()
result = A.twoSum([1, 2, 3, 5, 6, 8, 4], 6)
print(result)

V = Solution()
C = V.twoSum([3, 2, 4], 6)
print(C)
