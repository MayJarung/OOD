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

# inp = [i for i in input("Enter data to stack : ").split()]
inp = input('Enter Input : ').split(',')
qEs = Queue()
qEn = Queue()

for x in inp:                                       # EN 1,EN 2,D,D,D,EN 3,D          2 1 Empty 3
    if x[0] == 'E':                                 # EN 1,ES 2,D,D,D,EN 3,D          2 1 Empty 3
        if x[1] == 'N':                             # EN 1,ES 2,ES 99,D,D,D,EN 3,D    2 99 1 3
            qEn.enQueue(int(x[3:]))
        else:
            qEs.enQueue(int(x[3:]))
    else:
        if qEs.isEmpty() and qEn.isEmpty():
            print("Empty")
        elif qEs.size() > 0 :
            print(qEs.deQueue())
        else:
            print(qEn.deQueue())

            
