"""
LCP 18. 早餐组合

小扣在秋日市集选择了一家早餐摊位，一维整型数组 staple 中记录了每种主食的价格，一维整型数组 drinks 中记录了每种饮料的价格。小扣的计划选择一份主食和一款饮料，且花费不超过 x 元。请返回小扣共有多少种购买方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
"""


class Solution:
    def breakfastNumber(self, staple, drinks, x: int) -> int:
        staple = sorted(staple)
        drinks = sorted(drinks)
        staple_lens = len(staple)
        drink_lens = len(drinks)
        i = 0
        result = 0
        while i < staple_lens:
            j = 0
            if staple[i] >= x:
                break
            if drinks[j] >= x:
                i += 1
                j = drink_lens
            while j < drink_lens:
                if staple[i] + drinks[j] <= x:
                    j += 1
                    result += 1
                    if j == drink_lens:
                        i += 1
                else:
                    i += 1
                    j = drink_lens
        result = result % 1000000007
        return result


A = Solution()
print(A.breakfastNumber(staple=[2,1,1], drinks=[8,9,5,1], x=9))
# [2,1,1]
# [8,9,5,1]