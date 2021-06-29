# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。 
# 
#  对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。 
# 
#  你可以返回任何满足上述条件的数组作为答案。 
# 
#  
# 
#  示例： 
# 
#  输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 20000 
#  A.length % 2 == 0 
#  0 <= A[i] <= 1000 
#  
# 
#  
#  Related Topics 数组 双指针 排序 
#  👍 212 👎 0
"""
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArrayByParityII(self, nums):
            oushu_list = list()
            jishu_list = list()
            for num in nums:
                if num % 2 == 0:
                    oushu_list.append(num)
                else:
                    jishu_list.append(num)
            result = list()
            lens = len(nums)
            for i in range((lens//2)):
                result.append(oushu_list[i])
                result.append(jishu_list[i])
            return result
# leetcode submit region end(Prohibit modification and deletion)
A=Solution()
print(A.sortArrayByParityII([4,2,5,7]))
print(4//2)
for i in range(0,2):
    print(i)