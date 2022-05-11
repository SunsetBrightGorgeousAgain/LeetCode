# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 
# 
#  
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
# 
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/ 
#  Related Topics 哈希表 数学 动态规划 堆（优先队列） 👍 331 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1] * n
        a = 0
        b = 0
        c = 0
        for i in range(1, n):
            r2, r3, r5 = res[a] * 2, res[b] * 3, res[c] * 5
            res[i] = min(r2, r3, r5)
            if res[i] == r2:
                a += 1
            if res[i] == r3:
                b += 1
            if res[i] == r5:
                c += 1
        return res[-1]

# leetcode submit region end(Prohibit modification and deletion)
