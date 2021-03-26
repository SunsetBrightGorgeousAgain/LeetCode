def swap(input_list, i, j):
    input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list


def quick_sorted(input_list, start, end):
    if start < end:
        i = start
        j = end
        base = input_list[i]

        while i < j:
            while i < j and input_list[j] >= base:
                j -= 1
            swap(input_list, i, j)

            while i < j and input_list[i] <= base:
                i += 1
            swap(input_list, i, j)

        quick_sorted(input_list, j + 1, end)
        quick_sorted(input_list, start, i - 1)

    return input_list


if __name__ == '__main__':
    unsort_list = [1, 3, 4, 6, 8, 7, 5, 9, 6, 2]
    list_len = len(unsort_list)
    if list_len == 1:
        sort_list = unsort_list
    else:
        start_len = 0
        end_len = list_len - 1
        sort_list = quick_sorted(unsort_list, start_len, end_len)
        print(sort_list)