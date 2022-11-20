
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                dp += 1
            else:
                dp = 0
            res = max(dp, res)
        return res

# leetcode submit region end(Prohibit modification and deletion)
