"""
剑指 Offer 61. 扑克牌中的顺子

从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
"""


class Solution:
    def isStraight(self, nums) -> bool:
        value_dict = dict()
        new_list = list()
        for i in nums:
            value_dict[i] = value_dict.get(i, 0) + 1
            if i != 0:
                new_list.append(i)
        min_num = min(new_list)
        max_num = max(new_list)
        result = value_dict.get(0, 0)
        if result == 0:
            if max_num - min_num == 4:
                for i in range(min_num, max_num + 1):
                    if value_dict.get(i, 0) == 1:
                        pass
                    elif value_dict.get(i, 0) > 1:
                        return False
                    else:
                        return False
                return True
            else:
                return False

        if result >= 1:
            times = 0
            if max_num - min_num <= 4:
                for i in range(min_num, max_num + 1):
                    if value_dict.get(i, 0) == 1:
                        pass
                    elif value_dict.get(i, 0) > 1:
                        return False
                    else:
                        times += 1
                        if times >= result+1:
                            return False
                return True
            else:
                return False



A = Solution()
print(A.isStraight([0,12,11,11,0]
))
