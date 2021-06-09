"""
就是对比.
拿一个作为基准.要将左边和右边的,一边全大于/小于基准,另一边则相反
"""


def swap(normal_list, start, end):
    normal_list[start], normal_list[end] = normal_list[end], normal_list[start]
    return normal_list


def sortedlist(input_list, start, end):
    if start < end:
        i = start
        j = end
        target = input_list[i]
        while i < j and input_list[j] >= target:
            j -= 1
        swap(input_list, i, j)

        while i < j and input_list[i] <= target:
            i += 1
        swap(input_list, i, j)
        sortedlist(input_list, start, i - 1)
        sortedlist(input_list, j + 1, end)
    return input_list


print(sortedlist([1, 2, 3, 4, 8, 6, 7, 9, 9, 12],
                 0, len([1, 2, 3, 4, 8, 6, 7, 9, 9, 12]) - 1))


def sortedlist2(a_list, start, end):
    if start < end:
        i = start
        j = end
        target = a_list[i]
        while i < j and a_list[j] >= target:
            j -= 1
        swap(a_list, i, j)
        while i < j and a_list[i] <= target:
            i += 1
        swap(a_list, i, j)

        sortedlist(a_list, j + 1, end)
        sortedlist2(a_list, start, i - 1)
    return a_list


print(sortedlist2([1, 2, 3, 4, 8, 6, 7, 9, 9, 12],
                  0, len([1, 2, 3, 4, 8, 6, 7, 9, 9, 12]) - 1))


def sortedlist3(b_list):
    if len(b_list) >= 2:
        mid = b_list[len(b_list) // 2]
        left = []
        right = []
        b_list.remove(mid)
        for i in b_list:
            if i >= mid:
                left.append(i)
            else:
                right.append(i)
        return sortedlist3(left) + [mid] + sortedlist3(right)
    else:
        return b_list


print(sortedlist3([1, 2, 3, 4, 8, 7, 7, 9, 9, 12]))


def quick_sort(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data) // 2]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


a = [1, 2, 3, 4, 8, 7, 7, 9, 9, 12]
a.remove(7)


def sortedlist4(c_list, start, end):
    if start < end:
        i = start
        j = end
        target = c_list[i]
        while i < j and c_list[j] >= target:
            j -= 1
        swap(c_list, i, j)

        while i < j and c_list[i] <= target:
            i += 1
        swap(c_list, i, j)

        sortedlist4(c_list, start, i - 1)
        sortedlist4(c_list, j + 1, end)
    return c_list


print(sortedlist4([1, 2, 3, 4, 8, 7, 7, 9, 9, 12], 0, len([1, 2, 3, 4, 8, 7, 7, 9, 9, 12]) - 1))
