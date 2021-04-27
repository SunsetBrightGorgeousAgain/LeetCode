"""
1184. 公交站间的距离

环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。

环线上的公交车都可以按顺时针和逆时针的方向行驶。

返回乘客从出发点 start 到目的地 destination 之间的最短距离。



示例 1：

输入：distance = [1,2,3,4], start = 0, destination = 1
输出：1
解释：公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。



示例 2：

输入：distance = [1,2,3,4], start = 0, destination = 2
输出：3
解释：公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。



示例 3：

输入：distance = [1,2,3,4], start = 0, destination = 3
输出：4
解释：公交站 0 和 3 之间的距离是 6 或 4，最小值是 4。



提示：

    1 <= n <= 10^4
    distance.length == n
    0 <= start, destination < n
    0 <= distance[i] <= 10^4

通过次数10,213
提交次数17,712

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
"""


class Solution:
    def distanceBetweenBusStops(
            self,
            distance,
            start: int,
            destination: int) -> int:
        # distance
        if start == destination:
            return 0
        else:
            if start > destination:
                start, destination = destination, start
            result1 = 0
            for i in range(start, destination):
                result1 += distance[i]
            new_distance = distance * 2
            result2 = new_distance[destination:start + len(distance)]
            result2 = sum(result2)
            result = min(result2, result1)
            return result


A = Solution()
print(A.distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=2))
print(A.distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=3))
print(A.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
