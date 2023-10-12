class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        S = ''
        t = self.head
        while t.next != None or t != None:
            S += str(t.data)
            t = t.next
            if t == None:
                break
            S += '->'
        return S

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        newNode = node(data)
        if self.isEmpty():  
            self.head = newNode
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = newNode
        self.size += 1

        # Inserts a new element at the given position
    def insert(self, index, data):
        newNode = node(data)
        if (index < 0) or (index > x.size):
            print("Data cannot be added")
            return
        elif self.isEmpty():  
            self.head = newNode
        elif (index == 0):
            newNode.next = self.head
            self.head = newNode
        else:     # index > 0 
            t = self.head
            i = 0
            while index - 1 > i:
                i += 1
                t = t.next
            newNode.next = t.next
            t.next = newNode
        print("index = " + str(index) + " and data = " + str(data))
        self.size += 1

inp = input("Enter Input : ").split(',')
list1 = inp[0].split(' ')
x = LinkedList()

for i in list1:
    if(i == ''):
        break
    x.append(int(i))

if x.isEmpty():
    print("List is empty")
else:
    print("link list : "+ (x.__str__()))

for i in inp[1:]:
    id, data = [int(j) for j in i.split(":")]
    x.insert(id, data)
    if x.isEmpty():
        print("List is empty")
    else:
        print("link list : "+ (str(x)))
