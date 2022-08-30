# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        right = len(arr) - 1
        left = 0
        while left < right:
            if arr[left] < arr[left + 1]:
                left += 1
            else:
                break
        while left < right:
            if arr[right] < arr[right - 1]:
                right -= 1
            else:
                break
        if left == right and left != len(arr) - 1 and right != 0:
            return True
        else:
            return False


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
