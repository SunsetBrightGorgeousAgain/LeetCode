"""
283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:

    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0

        for i, j in enumerate(nums):
            if j == 0:
                n += 1
                nums.remove(j)

        # lens = len(nums)
        #
        # for j in range(lens - 1, -1, -1):
        #     if nums[j] == 0:
        #         n += 1
        #         nums.remove(nums[j])
        #     else:
        #         pass
        for i in range(n):
            nums.append(0)
#         return nums
# A = Solution()
# print(A.moveZeroes([0, 0, 1]))


nums = [0, 0, 1]
n = 0
# 动态删除会造成nums发生变化.
for i in nums:
    i = i-n
    if nums[i] == 0:
        n += 1
        nums.remove(nums[i])
print(n)
print(nums)
