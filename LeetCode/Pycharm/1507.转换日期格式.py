"""
给你一个字符串 date ，它的格式为 Day Month Year ，其中：

    Day 是集合 {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"} 中的一个元素。
    Month 是集合 {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"} 中的一个元素。
    Year 的范围在 ​[1900, 2100] 之间。

请你将字符串转变为 YYYY-MM-DD 的格式，其中：

    YYYY 表示 4 位的年份。
    MM 表示 2 位的月份。
    DD 表示 2 位的天数。



示例 1：

输入：date = "20th Oct 2052"
输出："2052-10-20"

示例 2：

输入：date = "6th Jun 1933"
输出："1933-06-06"

示例 3：

输入：date = "26th May 1960"
输出："1960-05-26"



提示：

    给定日期保证是合法的，所以不需要处理异常输入。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reformat-date
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def reformatDate(self, date: str) -> str:
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        month_str = '{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}'
        month_str = month_str.strip('{').strip('}')
        month_list = month_str.split(",")
        month_list = [i.strip('"').strip(' "') for i in month_list]
        date_list = date.split(' ')
        result = ""
        result += date_list[2]
        result += '-'
        month = month_list.index(date_list[1]) + 1
        month = str(month).zfill(2)
        result += month
        result += '-'
        result += date_list[0][:-2].zfill(2)
        return result


A = Solution()
v = A.reformatDate("20th Oct 2052")
print(v)
