class Queue():

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def isEmpty(self):
        return self.size() == 0
    def size(self):
        return len(self.items)
    def enQueue(self, ele):
        self.items.append(ele)
    def deQueue(self):
        return self.items.pop(0)
    def peak(self):
        return self.items[-1]
    def buttom(self):
        return self.items[0]
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        return ' '.join(self.items)

inp = input("Enter Input : ").split(",")   # E 10,E 20,E 30,E 40,D,D
q = Queue()

for i in inp:
    if i[0] == "E":
        q.enQueue(i[2:])
        print(q.size())
    else:
        if q.size() > 0:
            print(f"{q.deQueue()} 0")
        else: 
            print(-1)
print(q)




