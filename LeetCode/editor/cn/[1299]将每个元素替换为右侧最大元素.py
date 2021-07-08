# 给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。 
# 
#  完成所有替换操作后，请你返回这个数组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [17,18,5,4,6,1]
# 输出：[18,6,6,6,1,-1]
# 解释：
# - 下标 0 的元素 --> 右侧最大元素是下标 1 的元素 (18)
# - 下标 1 的元素 --> 右侧最大元素是下标 4 的元素 (6)
# - 下标 2 的元素 --> 右侧最大元素是下标 4 的元素 (6)
# - 下标 3 的元素 --> 右侧最大元素是下标 4 的元素 (6)
# - 下标 4 的元素 --> 右侧最大元素是下标 5 的元素 (1)
# - 下标 5 的元素 --> 右侧没有其他元素，替换为 -1
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [400]
# 输出：[-1]
# 解释：下标 0 的元素右侧没有其他元素。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 104 
#  1 <= arr[i] <= 105 
#  
#  Related Topics 数组 
#  👍 63 👎 0
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceElements(self, arr):
        """
        这里,如果可以认为从右到左,这样就是求最大值了.复杂度会低下来,最后循环遍历也可以
        """
        new_list = []
        if len(arr) == 1:
            new_list.append(-1)
            return new_list
        else:
            new_list.append(-1)
            max_num = arr[-1]
            for i in arr[::-1]:
                max_num = max(max_num, i)
                new_list.append(max_num)
            new_list.pop()
            new_list = [i for i in new_list[::-1]]
            return new_list


# leetcode submit region end(Prohibit modification and deletion)
A = Solution()
print(A.replaceElements(arr=[17, 18, 5, 4, 6, 1]))
print(A.replaceElements(arr=[400]))
# arr = [17, 18, 5, 4, 6, 1]
# for i in arr[::-1]:
#     print(i)
