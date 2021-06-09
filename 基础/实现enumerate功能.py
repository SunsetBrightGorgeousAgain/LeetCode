def my_enumerate(iterate_obj):
    for i in range(len(iterate_obj)):
        yield i, iterate_obj[i]


if __name__ == '__main__':
    s = '1234'
    l = ['a', 'b', 'c', 'd']
    for index, content in my_enumerate(s):
        print(index, content)

    for index, content in my_enumerate(l):
        print(index, content)

    for i, j in enumerate([1, 2, 3]):
        print(i, j)
