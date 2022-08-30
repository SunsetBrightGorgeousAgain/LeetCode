
# leetcode submit region begin(Prohibit modification and deletion)
class MyHashSet:

    def __init__(self):
        self.list_dict = []


    def add(self, key: int) -> None:
        if key not in self.list_dict:
            self.list_dict.append(key)


    def remove(self, key: int) -> None:
        if key in self.list_dict:
            key_index = self.list_dict.index(key)
            self.list_dict.pop(key_index)

    def contains(self, key: int) -> bool:
        if key in self.list_dict:
            return True
        else:
            return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# leetcode submit region end(Prohibit modification and deletion)
