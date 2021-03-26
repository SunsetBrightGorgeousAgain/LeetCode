a = [1, 3, 6, 5, 6, 8, 8]


def find_value(input_list, z):
    for i in input_list:
        print(i)
        x = i
        y = z - x
        if y in input_list:
            return True
    else:
        return False


print(find_value(a, 16))
