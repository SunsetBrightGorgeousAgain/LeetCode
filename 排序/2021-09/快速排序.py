def swap(b_list, a, b):
    b_list[a], b_list[b] = b_list[b], b_list[a]
    return b_list


def quick(a_list, start, end):
    if start < end:
        i = start
        j = end
        target = a_list[i]
        while i < j:
            while i < j and a_list[j] >= target:
                j -= 1
            swap(a_list, i, j)

            while i < j and a_list[i] <= target:
                i += 1
            swap(a_list, i, j)

            quick(a_list, start, i - 1)
            quick(a_list, j + 1, end)
    return a_list


a = [1, 2, 6, 3, 1, 454, 65, 1, 9]
print(quick(a, 0, len(a) - 1))
