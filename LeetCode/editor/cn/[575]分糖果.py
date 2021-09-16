# 给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，
# 每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。
# 返回妹妹可以获得的最大糖果的种类数。
# 
#  示例 1: 
# 
#  
# 输入: candies = [1,1,2,2,3,3]
# 输出: 3
# 解析: 一共有三种种类的糖果，每一种都有两个。
#      最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。
#  
# 
#  示例 2 : 
# 
#  
# 输入: candies = [1,1,2,3]
# 输出: 2
# 解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。
#  
# 
#  注意: 
# 
#  
#  数组的长度为[2, 10,000]，并且确定为偶数。 
#  数组中数字的大小在范围[-100,000, 100,000]内。
#  
#  
#  
#  
#  Related Topics 数组 哈希表 
#  👍 107 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distributeCandies(self, candyType) -> int:
        candy_dict = dict()
        candy_type_list = list()
        for one_candy in candyType:
            candy_dict[one_candy] = candy_dict.get(one_candy, 0) + 1
        for one_candy_type, one_candy_value in candy_dict.items():
            candy_type_list.append(one_candy_type)
        candy_part = len(candyType) // 2  # 每人分配到的.因为输入的一定为偶数
        if len(candy_type_list) >= candy_part:  # 种类大于需要分配的糖果数量
            return candy_part
        else:
            return len(candy_type_list)


# leetcode submit region end(Prohibit modification and deletion)
A = Solution()
print(A.distributeCandies([1, 1, 2, 2, 3, 3]))
print(A.distributeCandies([1, 1, 2, 3]))
