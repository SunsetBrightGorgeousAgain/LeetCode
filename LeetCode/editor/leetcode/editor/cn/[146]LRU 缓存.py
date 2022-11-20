import collections
# leetcode submit region begin(Prohibit modification and deletion)
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = collections.OrderedDict()
        self.num = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        m = self.dict.pop(key)
        self.dict[key] = m
        return m


    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            self.dict.pop(key)
        else:
            if self.num > 0:
                self.num -= 1
            else:
                self.dict.popitem(last=False)
        self.dict[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
