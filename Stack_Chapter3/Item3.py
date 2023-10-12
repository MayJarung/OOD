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

ls = input('Enter Input : ').split()
s1 = Stack()
combo = 0

for i in range(len(ls)):
    if s1.size() < 2:
        s1.push(ls[i])
    else:
        ele2 = s1.pop()
        ele1 = s1.pop()
        if ele1 == ele2 == ls[i]:
            combo += 1
        else:
            s1.push(ele1)
            s1.push(ele2)
            s1.push(ls[i])

print(s1.size())

s2 = Stack()

for i in range(s1.size()):
    s2.push(s1.pop())

if s2.isEmpty():
    print('Empty') 
else:
    print(''.join(s2.items))

if combo > 1:
    print(f'Combo : {combo} ! ! !')
