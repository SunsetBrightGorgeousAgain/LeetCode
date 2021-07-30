# A 和 B 在一个 3 x 3 的网格上玩井字棋。 
# 
#  井字棋游戏的规则如下： 
# 
#  
#  玩家轮流将棋子放在空方格 (" ") 上。 
#  第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。 
#  "X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。 
#  只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。 
#  如果所有方块都放满棋子（不为空），游戏也会结束。 
#  游戏结束后，棋子无法再进行任何移动。 
#  
# 
#  给你一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），
#  它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各
# 自的棋子位置。 
# 
#  如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；
#  如果仍会有行动（游戏未结束），则返回 "Pending"
# 。 
# 
#  你可以假设 moves 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。 
# 
#  
# 
#  示例 1： 
# 
#  输入：moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# 输出："A"
# 解释："A" 获胜，他总是先走。
# "X  "    "X  "    "X  "    "X  "    "X  "
# "   " -> "   " -> " X " -> " X " -> " X "
# "   "    "O  "    "O  "    "OO "    "OOX"
#  
# 
#  示例 2： 
# 
#  输入：moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# 输出："B"
# 解释："B" 获胜。
# "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
# "   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
# "   "    "   "    "   "    "   "    "   "    "O  "
#  
# 
#  示例 3： 
# 
#  输入：moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# 输出："Draw"
# 输出：由于没有办法再行动，游戏以平局结束。
# "XXO"
# "OOX"
# "XOX"
#  
# 
#  示例 4： 
# 
#  输入：moves = [[0,0],[1,1]]
# 输出："Pending"
# 解释：游戏还没有结束。
# "X  "
# " O "
# "   "
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= moves.length <= 9 
#  moves[i].length == 2 
#  0 <= moves[i][j] <= 2 
#  moves 里没有重复的元素。 
#  moves 遵循井字棋的规则。 
#  
#  Related Topics 数组 哈希表 矩阵 模拟 
#  👍 39 👎 0

"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tictactoe(self, moves) -> str:
        n = 3
        m_list = [i for i in range(n * n)]
        for i, one_move in enumerate(moves):
            if i % 2 == 0:
                m = 'x'
                l = n * one_move[0] + one_move[1]
                m_list[l] = m
            else:
                m = 'o'
                l = n * one_move[0] + one_move[1]
                m_list[l] = m
        print(m_list)
        for i in range(n):
            times1 = 0
            x = m_list[i]
            for j in range(n):
                if x == m_list[j*n]:
                    times1 += 1
                    if times1 == n:
                        if x == 'x':
                            return "A"
                        else:
                            return "B"
                else:
                    break

        for i in range(n):
            x = m_list[i*n]
            times2 = 0
            for j in range(n):
                if x == m_list[i*n+j]:
                    times2 += 1
                    if times2 == n:
                        if x == 'x':
                            return "A"
                        else:
                            return "B"
                else:
                    break

        # 斜对角.考虑
        target = m_list[0]
        times3 = 0
        for j in range(n):
            if target == m_list[j * n + j]:
                times3 += 1
                if times3 == n:
                    if target == 'x':
                        return "A"
                    else:
                        return "B"
            else:
                break

        target2 = m_list[n-1]
        times4 = 0
        for j in range(n):
            if target2 == m_list[(j+1)*n - j]:
                times4 += 1
                if times4 == n:
                    if target2 == 'x':
                        return "A"
                    else:
                        return "B"
            else:
                break

        if len(moves) == n*n:
            return "Draw"
        else:
            return "Pending"

# leetcode submit region end(Prohibit modification and deletion)
"""

# print(A.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(A.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(A.tictactoe([[0,0],[1,1]]))
print(A.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
"""
A = Solution()
# print(A.tictactoe([[2,2],[0,2],[1,0],[0,1],[2,0],[0,0]]))
# print(A.tictactoe([[1,0],[0,1],[0,0],[2,0],[1,1],[2,1],[1,2]]))
print(A.tictactoe([[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]))