class Stack:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self, ele):
        self.items.append(ele)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size() == 0
    def buttom(self):
        return self.items[0]
    def peak(self):
        return self.items[-1]
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        return "".join(self.items)

inp = input('Enter Input : ').split()    # G H H H H P

s1 = Stack()
s2 = Stack()
combo = 0

for i in inp:
    if s1.size() < 2:
        s1.push(i)
    else:
        ele2 = s1.pop()
        ele1 = s1.pop()
        if ele1 == ele2 == i:
            combo += 1
        else:
            s1.push(ele1)
            s1.push(ele2)
            s1.push(i)

for i in range(len(s1.items)):
    s2.push(s1.pop())

print(s2.size())
print(s2)

if combo >= 2:
    print(f"Combo : {combo} ! ! !")
