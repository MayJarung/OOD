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

inp = input("Enter Input : ").split(",")
qEn = Queue()
qEs = Queue()

for x in inp:
    if x[0] == "E":
        if x[1] == "N":
            qEn.enQueue(x[3:])
        else:
            qEs.enQueue(x[3:])
    else:
        if qEn.isEmpty() and qEs.isEmpty():
            print("Empty")
        elif qEs.size() > 0:
            print(qEs.deQueue())
        elif qEn.size() > 0:
            print(qEn.deQueue())
            