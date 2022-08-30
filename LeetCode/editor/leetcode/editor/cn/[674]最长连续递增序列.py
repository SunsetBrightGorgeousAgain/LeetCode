# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_num = 1
        for i, j in enumerate(nums):
            res_num = 1
            m = i
            while m <= len(nums) - 1:
                if m == 0:
                    pass
                else:
                    if nums[m] > nums[m - 1]:
                        res_num += 1
                    else:
                        break
                m += 1
            max_num = max(res_num, max_num)
        return max_num
"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1
        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)



A = Solution()
print(A.findLengthOfLCIS([2, 2, 1]))
