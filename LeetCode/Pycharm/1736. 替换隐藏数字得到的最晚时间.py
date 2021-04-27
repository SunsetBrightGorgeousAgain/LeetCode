"""
1736. 替换隐藏数字得到的最晚时间

给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。

有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。

替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。



示例 1：

输入：time = "2?:?0"
输出："23:50"
解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。

示例 2：

输入：time = "0?:3?"
输出："09:39"

示例 3：

输入：time = "1?:22"
输出："19:22"



提示：

    time 的格式为 hh:mm
    题目数据保证你可以由输入的字符串生成有效的时间
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        # 1,2,3,4
        time = time.replace(":", '')
        time_lens = len(time)
        for i in range(time_lens - 1, -1, -1):
            if i == 3:
                if time[i] == "?":
                    time = time[0:3] + '9'
            if i == 2:
                if time[i] == "?":
                    time = time[0:2] + '5' + time[3]
            if i == 1:
                pass
            if i == 0:
                if time[i] == "?":
                    if time[1] == "?":
                        time = '2' + '3' + time[2:]
                    else:
                        if time[1] == '0' or time[1] == '1' or time[1] == '2' or time[1] == '3':
                            time = '2' + time[1:]
                        else:
                            time = '1' + time[1:]
                else:
                    if time[i] == '0' or time[i] == '1':
                        if time[1] == "?":
                            time = time[i] + '9' + time[2:]
                        else:
                            time = time[i] + time[1:]
                    else:
                        if time[1] == "?":
                            time = time[i] + '3' + time[2:]
                        else:
                            if time[1] == '0' or time[1] == '1' or time[1] == '2' or time[1] == '3':
                                time = '2' + time[1:]

        time = time[0:2] + ":" + time[2:]
        return time


A = Solution()
print(A.maximumTime('??:15'))
