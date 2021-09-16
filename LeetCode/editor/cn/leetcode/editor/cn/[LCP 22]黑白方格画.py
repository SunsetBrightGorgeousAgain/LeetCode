# 小扣注意到秋日市集上有一个创作黑白方格画的摊位。摊主给每个顾客提供一个固定在墙上的白色画板，画板不能转动。
# 画板上有 `n * n` 的网格。绘画规则为，小扣
# 可以选择任意多行以及任意多列的格子涂成黑色（选择的整行、整列均需涂成黑色），所选行数、列数均可为 0。
# 
# 小扣希望最终的成品上需要有 `k` 个黑色格子，请返回小扣共有多少种涂色方案。
# 
# 注意：两个方案中任意一个相同位置的格子颜色不同，就视为不同的方案。
# 
# **示例 1：**
# >输入：`n = 2, k = 2`
# >
# >输出：`4`
# > 
# >解释：一共有四种不同的方案：
# >第一种方案：涂第一列；
# >第二种方案：涂第二列；
# >第三种方案：涂第一行；
# >第四种方案：涂第二行。
# 
# **示例 2：**
# >输入：`n = 2, k = 1`
# > 
# >输出：`0`
# > 
# >解释：不可行，因为第一次涂色至少会涂两个黑格。
# 
# **示例 3：**
# >输入：`n = 2, k = 4`
# > 
# >输出：`1`
# >
# >解释：共有 2*2=4 个格子，仅有一种涂色方案。
# 
# **限制：**
# - `1 <= n <= 6`
# - `0 <= k <= n * n`
# 
# 
#  Related Topics 数学 
#  👍 57 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        # j横,l竖
        j = 0

        if k < n:
            return 0
        elif k == n*n:
            return 1
        else:
            # 横竖最大也就是为N，有一个最大也是N-1
            # 0< j < n-1
            result = 0
            while 0<=j<=n:
                for i in range(0,n):
                    if j*n+i*n-i*j == k:
                        result += 1
                        break
                j += 1

            return result*2


# leetcode submit region end(Prohibit modification and deletion)
