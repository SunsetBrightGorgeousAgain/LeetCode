# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        else:
            # l_list = [i for i in digits]
            l_list_list = list()
            d_dict = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z'],
            }
            [l_list_list.append(d_dict[i]) for i in digits]
            res = list()
            ll_len = len(l_list_list)
            i = ll_len
            while i >= 1:
                l_list_res = l_list_list[i - 1]
                new_res = []
                for j in l_list_res:
                    if len(res) == 0:
                        new_res = l_list_res
                        break
                    else:
                        for m in res:
                            k = j + m
                            new_res.append(k)
                res = new_res
                i -= 1
            return res


# leetcode submit region end(Prohibit modification and deletion)

