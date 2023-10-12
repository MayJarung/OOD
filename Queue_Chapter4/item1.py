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
q = Queue()

for x in inp:                       # inp = E 10,E 20,E 30,E 40,D,D
    if x[0] == 'E':
        q.enQueue(int(x[2:]))       # q = 10 20 30 40
        print(q.size())
    else: 
        if q.size() > 0: 
            print(f'{q.deQueue()} 0')
        else:
            print(-1)

         
if q.size() > 0:
    for i in range(len(q.items)):     # q = 30 40
        print(q.deQueue(), end =" ")
else:
    print("Empty")



    