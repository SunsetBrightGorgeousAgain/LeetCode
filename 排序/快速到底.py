def swap(input_list, i, j):
    input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list


def sortedlist(input_list, start, end):
    if start < end:
        lens = len(input_list)
        if lens <= 1:
            return input_list
        i = start
        j = end
        target = input_list[i]
        while i < j:
            while i < j and input_list[j] <= target:
                j -= 1
            swap(input_list, i, j)

            while i < j and input_list[i] >= target:
                i += 1
            swap(input_list, i, j)

            sortedlist(input_list, j + 1, end)
            sortedlist(input_list, start, i - 1)

    return input_list


print(sortedlist([1, 2, 3, 4, 8, 6, 7, 9, 12, 1],
                 0, len([1, 2, 3, 4, 8, 6, 7, 9, 12, 1]) - 1))
a = [1, 2, 6, 3, 1, 454, 65, 1, 9]
print(sortedlist(a, 0, len(a) - 1))
