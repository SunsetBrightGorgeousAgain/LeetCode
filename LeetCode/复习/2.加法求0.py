"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：

输入：nums = []
输出：[]

示例 3：

输入：nums = [0]
输出：[]



提示：

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
"""


class Solution:
    def threeSum(self, nums):
        i = 0
        l_lens = len(nums)
        if len(nums) <= 2:
            return []
        nums = sorted(nums)
        l_list = list()
        while i < l_lens - 1:
            k = i + 1
            j = l_lens - 1
            while k < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    x_list = [nums[i], nums[k], nums[j]]
                    l_list.append(x_list)
                    k += 1
                    j -= 1
                    while k<j and nums[k]==nums[k-1]:   # 这里前面加1了...
                        k+=1
                    while j>k and nums[j] == nums[j+1]: # 这里前面减1了...
                        j-=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    k += 1
                else:
                    j -= 1
            while i < l_lens-1:
                if nums[i] != nums[i + 1]:
                    break
                else:
                    i += 1
            i += 1
        return l_list


A = Solution()
# print(A.threeSum([-1, 0, 1, 2, -1, -4]))
print(A.threeSum([-2,0,0,2,2]))
