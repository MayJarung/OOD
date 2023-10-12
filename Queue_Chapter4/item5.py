class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self, i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def __str__(self):
        S = ', '.join(self.items)
        return S

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

def CheckExplosive(a: Stack):
    if a.size() < 3:
        return 0
    b = a.pop()
    c = a.pop()
    d = a.pop()
    a.push(d)
    a.push(c)
    a.push(b)
    return b == c == d
    
inp = input('Enter Input (Normal, Mirror) : ').split()   
Normal = Queue(list(inp[0]))
Mirror = Queue(list(inp[1])[::-1])
s1 = Stack()
s2 = Stack()
MirrorItem = Queue()
ExplosiveMirror = 0
ExplosiveNormal = 0
FailedInterrupted = 0

while not Mirror.isEmpty():
    s1.push(Mirror.deQueue())
    if CheckExplosive(s1):
        MirrorItem.enQueue(s1.pop())
        s1.pop()
        s1.pop()
        ExplosiveMirror += 1

while not s1.isEmpty():
    Mirror.enQueue(s1.pop())

while not Normal.isEmpty():
    s2.push(Normal.deQueue())
    if CheckExplosive(s2):
        if not MirrorItem.isEmpty():
            a = s2.pop()
            s2.push(MirrorItem.deQueue())
            if CheckExplosive(s2):
                s2.pop()
                s2.pop()
                s2.pop()
                FailedInterrupted += 1
                
            s2.push(a)
        else:
            s2.pop()
            s2.pop()
            s2.pop()
            ExplosiveNormal += 1

while not s2.isEmpty():
    Normal.enQueue(s2.pop())

print("NORMAL :")       
print(Normal.size())
if Normal.isEmpty():
    print("Empty")
else:
    print(''.join(Normal.items))
print(f"{ExplosiveNormal} Explosive(s) ! ! ! (NORMAL)")
if FailedInterrupted != 0:
    print(f"Failed Interrupted {FailedInterrupted} Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(Mirror.size())
if Mirror.isEmpty():
    print("ytpmE")
else:
    print(''.join(Mirror.items))
print(f"(RORRIM) ! ! ! (s)evisolpxE {ExplosiveMirror}")

