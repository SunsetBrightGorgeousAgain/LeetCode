class ccc:
    def __init__(self):
        self.value1 = 2

    def func(self):
        self.value2 = 3
        return self.value2


a = ccc()
print(a.func())
