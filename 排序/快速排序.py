def swap(unsorted, i, j):
    unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
    return unsorted


def quick_sorted(unsorted_list, start, end):
    if start < end:
        lens = len(unsorted_list)
        if lens <= 1:
            return unsorted_list
        i = start
        j = end
        base = unsorted_list[i]
        # 从小到大排序的
        while i < j:
            while i < j and unsorted_list[j] >= base:
                j -= 1
            swap(unsorted_list, i, j)

            while i < j and unsorted_list[i] <= base:
                i += 1
            swap(unsorted_list, i, j)

        quick_sorted(unsorted_list, start, i - 1)
        quick_sorted(unsorted_list, j + 1, end)
        return unsorted_list


alist = [1, 43, 2, 5, 7, 8, 4]
sorted_list = quick_sorted(alist, 0, len(alist) - 1)
print(sorted_list)
