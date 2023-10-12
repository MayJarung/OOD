class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self, i):
        self.items.append(i)
        #self.size += 1
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    
print(" *** Stack implement by Python list***")

ls = [i for i in input("Enter data to stack : ").split()]

s = Stack()

for i in ls:

    s.push(i)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)

