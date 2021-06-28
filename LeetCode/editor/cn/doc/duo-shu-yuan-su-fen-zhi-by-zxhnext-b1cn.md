## 题解
如果数 a 是数组 nums 的众数，如果我们将 nums 分成两部分，那么 a 必定是至少一部分的众数。

#### 1. 题解思路
1. 分：将数组分成左右两部分随后
2. 解：分别求出左半部分的众数 a1 以及右半部分的众数 a2
3. 合：在 a1 和 a2 中选出正确的众数

#### 2. 代码实现
```js
var majorityElement = function(nums) {
    function majorityElementRec(nums, lo, hi) {
        if (lo === hi) {
            return nums[lo];
        }

        const mid = Math.floor((hi - lo) / 2) + lo;
        const left = majorityElementRec(nums, lo, mid);
        const right = majorityElementRec(nums, mid + 1, hi);

        if (left === right) {
            return left;
        }

        const leftCount = countInRange(nums, left, lo, hi);
        const rightCount = countInRange(nums, right, lo, hi);

        return leftCount > rightCount ? left : right;
    }

    function countInRange (nums, num, lo, hi) {
        let count = 0;
        for (let i = lo; i <= hi; i++) {
            if (nums[i] == num) {
                count++;
            }
        }
        return count;
    }

    return majorityElementRec(nums, 0, nums.length - 1);
};
```

### 3. 复杂度分析
时间复杂度：O(nlogn)，空间复杂度：O(logn)