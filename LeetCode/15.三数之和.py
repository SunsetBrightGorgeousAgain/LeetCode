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
        nums = sorted(nums)
        result = list()
        # 类似于快排的解法.
        nums_len = len(nums)
        if len(nums) < 3:
            return result
        # for i in range(nums_len - 1):
        i = 0
        while i < nums_len - 1:
            j = i + 1
            k = nums_len - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    result_list = list()
                    result_list.append(nums[i])
                    result_list.append(nums[j])
                    result_list.append(nums[k])
                    """
                    if result_list in result:
                        pass
                    else:
                        result.append(result_list)
                    """
                    result.append(result_list)
                    j += 1
                    k -= 1
                    # 需要去掉重复元素
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                elif sums < 0:
                    j += 1
                else:
                    k -= 1

            while i < nums_len - 1:
                if nums[i] != nums[i + 1]:
                    break
                else:
                    i += 1
            i += 1
        return result


A = Solution()
print(A.threeSum([-1, 0, 1, 2, -1, -4]))
