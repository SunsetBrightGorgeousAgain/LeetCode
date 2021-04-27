"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target: int) -> int:
        if len(nums) == 0:
            return 0
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        if target > nums[-1]:
            return len(nums)

        # list_lens = len(nums)
        new_nums = nums
        middle = math.floor(len(new_nums) / 2)
        while True:
            print(new_nums)
            new_lens = len(new_nums)
            print('--middle--')

            print(middle)
            if nums[middle] == target:
                print('****')
                return middle
            elif nums[middle] > target:
                print('------')
                print(new_nums)
                print(math.floor(len(new_nums) / 2))
                new_nums = nums[middle - math.floor(len(new_nums) / 2):middle]
                middle -= math.floor(len(new_nums) / 2)
                print(middle)
                print(new_nums)
                if len(new_nums) == 0:
                    return middle
                if target <= new_nums[0]:
                    return middle
                if target >= new_nums[-1]:
                    return middle + 1
            else:
                print('++++')
                new_nums = nums[middle + 1:middle + math.floor(len(new_nums))]
                middle += math.floor(len(new_nums) / 2)
                print(new_nums)
                if len(new_nums) == 0:
                    return middle
                if target <= new_nums[0]:
                    return middle + 1
                if target >= new_nums[-1]:
                    return middle + math.floor(len(new_nums) / 2)


class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target: int) -> int:
        if len(nums) == 0:
            return 0

        if target <= nums[0]:
            return 0

        if target == nums[-1]:
            return len(nums) - 1

        if target > nums[-1]:
            return len(nums)

        if target == nums[0] and len(nums) == 1:
            return 0
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            if nums[i] < target and nums[i + 1] > target:
                return i + 1


A = Solution()
print(A.searchInsert([1, 2, 3, 5, 6], 5))


class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target: int) -> int:
        if len(nums) == 0:
            return 0

        if target <= nums[0]:
            return 0

        if target == nums[-1]:
            return len(nums) - 1

        if target > nums[-1]:
            return len(nums)

        if target == nums[0] and len(nums) == 1:
            return 0
        r = 0
        l = len(nums) - 1
        while r <= l:
            middle = (r + l) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                r = middle+1
            else:
                l = middle -1
        return r


A = Solution()
print(A.searchInsert([1, 2, 3, 5, 6], 5))
