# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。 
# 
#  请你找到并返回这个整数 
# 
#  
# 
#  示例： 
# 
#  
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^4 
#  0 <= arr[i] <= 10^5 
#  
#  Related Topics 数组 👍 46 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        lens = len(arr)
        # 有序.如果是超过了25%那么这个数字加25%一定还是这个数字.
        jiange = lens // 4
        for i in range(0, len(arr)):
            if arr[i] == arr[i + jiange]:
                return arr[i]


# leetcode submit region end(Prohibit modification and deletion)

"""
        r_dict = dict()
        lens = len(arr)
        for i in arr:
            r_dict[i] = r_dict.get(i, 0) + 1
        for m, n in r_dict.items():
            if n > lens / 4:
                return m
"""
