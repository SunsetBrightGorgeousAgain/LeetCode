# 在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。 
# 
#  如果小镇的法官真的存在，那么： 
# 
#  
#  小镇的法官不相信任何人。 
#  每个人（除了小镇法官外）都信任小镇的法官。 
#  只有一个人同时满足属性 1 和属性 2 。 
#  
# 
#  给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。 
# 
#  如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：N = 2, trust = [[1,2]]
# 输出：2
#  
# 
#  示例 2： 
# 
#  输入：N = 3, trust = [[1,3],[2,3]]
# 输出：3
#  
# 
#  示例 3： 
# 
#  输入：N = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1
#  
# 
#  示例 4： 
# 
#  输入：N = 3, trust = [[1,2],[2,3]]
# 输出：-1
#  
# 
#  示例 5： 
# 
#  输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 输出：3 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 1000 
#  trust.length <= 10000 
#  trust[i] 是完全不同的 
#  trust[i][0] != trust[i][1] 
#  1 <= trust[i][0], trust[i][1] <= N 
#  
#  Related Topics 图 数组 哈希表 
#  👍 126 👎 0
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findJudge(self, n: int, trust):
        # 前面的信任后面的.如果有法官.那么一定有一个只出现在后面而不出现在前面,且出现在后面的次数就是人数-1
        first_dictionary = dict()
        second_dictionary = dict()
        total_info = list()
        if n == 1:
            return 1
        for i in trust:
            second_dictionary[i[1]] = second_dictionary.get(i[1], 0) + 1
            first_dictionary[i[0]] = first_dictionary.get(i[0], 0) + 1
            if i[0] not in total_info:
                total_info.append(i[0])
            if i[1] not in total_info:
                total_info.append(i[1])
        for one_member in total_info:
            if second_dictionary.get(one_member,0) == (n-1) and first_dictionary.get(one_member,0) == 0:
                return one_member
        return -1
# leetcode submit region end(Prohibit modification and deletion)

A=Solution()
print(A.findJudge(1,[]))