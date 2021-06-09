"""
写一个列表里,是否有两个数相加为0的,不存在就直接返回FALSE.存在返回TRUE
"""


def judge_sum(a_list):
    new_dict = dict()
    for i in a_list:
        new_dict[i] = 1 + new_dict.get(i, 0)
    for i, j in new_dict.items():
        if 0 - i in new_dict.keys():
            return True
    return False


A = judge_sum([1, 3, 4, 6, 7, -3, 4])
print(A)


def enumerate_function(a_list):
    for i in range(len(a_list)):
        yield i, a_list[i]


s = '1234'
l = ['a', 'b', 'c', 'd']
for index, content in enumerate_function(s):
    print(index, content)
