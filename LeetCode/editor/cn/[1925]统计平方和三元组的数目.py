# 一个 平方和三元组 (a,b,c) 指的是满足 a2 + b2 = c2 的 整数 三元组 a，b 和 c 。 
# 
#  给你一个整数 n ，请你返回满足 1 <= a, b, c <= n 的 平方和三元组 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 5
# 输出：2
# 解释：平方和三元组为 (3,4,5) 和 (4,3,5) 。
#  
# 
#  示例 2： 
# 
#  输入：n = 10
# 输出：4
# 解释：平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 250 
#  
#  Related Topics 数学 枚举 
#  👍 5 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countTriples(self, n: int) -> int:
        # 感觉可以当做垂直三角形来解答
        # 一定是三个不同的数字
        l_list = list()
        l_dict = dict()
        for i in range(n + 1):
            l_dict[i**2] = 1

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if (i ** 2 + j ** 2) in l_dict:
                    f = (i, j)
                    l_list.append(f)
        return len(l_list) * 2


# leetcode submit region end(Prohibit modification and deletion)

A = Solution()
print(A.countTriples(177))
