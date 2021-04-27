"""
题目描述
评论 (663)
题解(608)
提交记录
119. 杨辉三角 II

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
"""


class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            return_dict = dict()
            ll_1 = [1]
            ll_2 = [1,1]
            return_dict[0]=ll_1
            return_dict[1]=ll_2
            for i in range(2,rowIndex+1):
                new_list = list()
                new_list.append(1)
                list_i_1 = return_dict[i-1]
                for j in range(len(list_i_1)-1):
                    new_list.append(list_i_1[j]+list_i_1[j+1])
                new_list.append(1)
                return_dict[i] = new_list

        return return_dict[rowIndex]


A=Solution()
print(A.getRow(33))