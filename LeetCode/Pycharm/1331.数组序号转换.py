"""
331. 数组序号转换

给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：

    序号从 1 开始编号。
    一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
    每个数字的序号都应该尽可能地小。



示例 1：

输入：arr = [40,10,20,30]
输出：[4,1,2,3]
解释：40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。

示例 2：

输入：arr = [100,100,100]
输出：[1,1,1]
解释：所有元素有相同的序号。

示例 3：

输入：arr = [37,12,28,9,100,56,80,5,12]
输出：[5,3,4,2,8,6,7,1,3]
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
"""


class Solution:
    def arrayRankTransform(self, arr: list) -> list:
        if len(arr) == 0:
            return []
        set_list = list(set(arr))
        sorted_list = sorted(set_list)
        new_list = list()
        for i in arr:
            new_list.append((sorted_list.index(i) + 1))
        return new_list


arr = [100, 100, 100]
A = Solution()
print(A.arrayRankTransform(arr))



class Solution:
    def arrayRankTransform(self, arr: list) -> list:
        if len(arr) == 0:
            return []
        set_list = list(set(arr))
        sorted_list = sorted(set_list)
        new_dict = dict()
        for i,j in enumerate(sorted_list):
            new_dict[j] = i+1   # 从1开始
        result_list = [new_dict[j] for j in arr]
        return result_list


arr = [37,12,28,9,100,56,80,5,12]
A = Solution()
print(A.arrayRankTransform(arr))
