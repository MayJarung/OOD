class Stack:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peak(self):
        return self.items[-1]
    def highCheck(self):
        if self.size() > 0:
            return self.peak()
        else:
            return 0

s = Stack()

inp = input('Enter Input : ').split(',')

for i in inp:
    if i[0] == 'A':
        while int(i[2:]) >= s.highCheck() and s.size() > 0:
            s.pop()
        s.push(int(i[2:]))
    else:
        print(s.size())
        
