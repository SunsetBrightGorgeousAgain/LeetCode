# 返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。 
# 
#  如果没有和至少为 K 的非空子数组，返回 -1 。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：A = [1], K = 1
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：A = [1,2], K = 4
# 输出：-1
#  
# 
#  示例 3： 
# 
#  输入：A = [2,-1,2], K = 3
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 50000 
#  -10 ^ 5 <= A[i] <= 10 ^ 5 
#  1 <= K <= 10 ^ 9 
#  
#  Related Topics 队列 数组 二分查找 前缀和 滑动窗口 单调队列 堆（优先队列） 
#  👍 282 👎 0
"""
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        sum_res = sum(nums)
        if sum_res < k:
            return -1
        new_nums = nums
        if len(nums) == 1:
            return 1
        while sum(nums) >= k:
            new_nums = nums.copy()

            if nums[0] >= k:
                return 1
            if nums[-1] >= k:
                return 1
            l_len = len(new_nums)
            if l_len % 2 == 0:
                mid = l_len // 2
                mid -= 1
                part1 = new_nums[0:mid + 1]
                part2 = new_nums[mid + 1:]
            else:
                mid = (l_len - 1) // 2
                part1 = new_nums[0:mid + 1]
                part2 = new_nums[mid:]

            if part1 >= part2:
                nums.pop()
            else:
                nums.pop(0)
        print(new_nums)
        result_list = new_nums.copy()
        result = new_nums.copy()
        new_nums.pop()

        if sum(new_nums) >= k:
            return len(new_nums)

        result_list.pop(0)
        if sum(result_list) >= k:
            return len(result_list)
        return len(result)


# leetcode submit region end(Prohibit modification and deletion)
A = Solution()

print(A.shortestSubarray([1, 2, 4, 5, 13, 19, 7, 8, 7, 10, 12, 12, 12, 18], 51))

new_nums = [1, 2, 3]
l_len = len(new_nums)
if l_len % 2 == 0:
    mid = l_len // 2
    mid -= 1
    part1 = new_nums[0:mid + 1]
    part2 = new_nums[mid + 1:]
else:
    mid = (l_len - 1) // 2
    part1 = new_nums[0:mid + 1]
    part2 = new_nums[mid:]

