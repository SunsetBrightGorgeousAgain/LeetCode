def swap(input_list, i, j):
    input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list


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


print(sortedlist([1, 2, 3, 4, 8, 6, 7, 9, 12],
                 0, len([1, 2, 3, 4, 8, 6, 7, 9, 12]) - 1))
