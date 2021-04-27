"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        return_list = []
        return_dict = dict()
        return_dict[1] = [1]
        return_dict[2] = [1, 1]
        return_list.append(return_dict[1])
        return_list.append(return_dict[2])
        if numRows <= 2:
            return return_list

        for j in range(3, numRows + 1):
            new_list = list()
            new_list.append(1)
            list_j_1 = return_dict[j - 1]
            list_lens = len(list_j_1)
            for i in range(list_lens - 1):
                need_num = list_j_1[i] + list_j_1[i + 1]
                new_list.append(need_num)
            new_list.append(1)
            return_dict[j]=new_list
            return_list.append(new_list)

        return return_list

A=Solution()
print(A.generate(10))


class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        return_list = []
        ll1 = [1]
        ll2 = [1, 1]
        return_list.append(ll1)
        return_list.append(ll2)
        if numRows <= 2:
            return return_list

        for j in range(3, numRows + 1):
            new_list = list()
            new_list.append(1)
            list_j_1 = return_list[j - 2]
            list_lens = len(list_j_1)
            for i in range(list_lens - 1):
                need_num = list_j_1[i] + list_j_1[i + 1]
                new_list.append(need_num)
            new_list.append(1)
            return_list.append(new_list)

        return return_list

A=Solution()
print(A.generate(10))