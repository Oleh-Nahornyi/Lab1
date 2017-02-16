class Iterator:
    def __init__(self, lst=[]):
        self.list = lst
        self.index = -1
        self.last_index = len(self.list) - 1

    def next(self):
        self.index=+1
        return self.index <= self.last_index

    def current(self):
        return self.list[self.index]


a = [4, 5, [6, 7]]
b = Iterator(a)
while b.next():
    print(b.current())