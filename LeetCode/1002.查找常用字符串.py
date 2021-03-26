"""
1002. 查找常用字符

给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。



示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]

示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]



提示：

    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] 是小写字母

    class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
"""


class Solution:
    def commonChars(self, A):
        result_list = list()
        if len(A) == 0:
            return result_list
        if len(A) == 1:
            for i in A[0]:
                result_list.append(i)
            return result_list
        first_list = list()
        for i in A[0]:
            if i not in first_list:
                first_list.append(i)
        min_time_dict = dict()
        for i in first_list:
            min_time = A[0].count(i)
            for j in A:
                min_time = min(min_time, j.count(i))
            if min_time >= 1:
                min_time_dict[i] = min_time

        for i, j in min_time_dict.items():
            for n in range(j):
                result_list.append(i)
        return result_list


A = Solution()
print(A.commonChars([]))


class Solution:
    def commonChars(self, A):
        result_list = list()
        if len(A) == 0:
            return result_list
        if len(A) == 1:
            for i in A[0]:
                result_list.append(i)
            return result_list
        first_list = list()
        for i in A[0]:
            if i not in first_list:
                first_list.append(i)
        min_time_dict = dict()
        for i in first_list:
            min_time = 0
            for k in A[0]:
                if i == k:
                    min_time += 1
            for j in A:
                current_time = 0
                for m in j:
                    if i == m:
                        current_time += 1

                min_time = min(min_time, current_time)
            if min_time >= 1:
                min_time_dict[i] = min_time

        for i, j in min_time_dict.items():
            for n in range(j):
                result_list.append(i)
        return result_list


A = Solution()
print(A.commonChars(['abc','anc','amc']))
