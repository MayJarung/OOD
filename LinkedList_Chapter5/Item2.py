class Node:
    def __init__(self, data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        # self.head == self.tail == None
        return self.head == None
 
    def __str__(self):
        if self.isEmpty():
            return "Empty"  
        cur = self.head                               # A B 
        s = ""
        while cur != None:                   
            s += str(cur.data) + " "
            cur = cur.next
            if cur == None:
                break
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur = self.tail 
        s = ""
        while cur != None:
            s += str(cur.data) + " "
            cur = cur.prev
            if cur == None:
                break
        return s

    def append(self, newData):
        newNode = Node(newData)
        newNode.prev = self.tail
        if self.head == None:  
            self.head = newNode
            self.tail = newNode
            newNode.next = None
        else:
            self.tail.next = newNode
            newNode.next = None
            self.tail = newNode

    def addHead(self, newData):
        newNode = Node(newData)
        cur = self.head
        # newNode.next = cur
        if self.head == None: 
            self.append(newData)
            return
        else:
            newNode.next = cur
            cur.prev = newNode
            self.head = newNode
        
    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.data == item:
                return "Found"
            cur = cur.next
        return "Not Found"

    def index(self, item):
        cur = self.head
        id = 0
        while cur != None:
            if cur.data == item:
                return id
            id += 1
            cur = cur.next
        return -1

    def size(self):
        cur = self.head
        i = 0
        while cur != None:
            i += 1
            cur = cur.next
        return i
            
    def pop(self, pos):
        if not (-(self.size()) <= pos < self.size()):
            return "Out of Range"

        if (pos < 0):
            pos += self.size()
            
        if pos == 0:
            cur = self.head
            if cur.next != None:
                cur.next.prev = None
            self.head = cur.next
            if self.head == None:
                self.tail = None

        elif pos == self.size() - 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            if self.head == None:
                self.tail = None
            
        else:
            cur = self.head             
            i = 0
            while pos > i : 
                i += 1
                cur = cur.next
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        return "Success" 
                                      #  0  1  2  3
    def insert(self, pos, newData):   #  A  B  C  D
        newNode = Node(newData)       # -4 -3 -2 -1
        if (pos > self.size()):
            pos = self.size()
        if (pos < 0):
            pos += self.size()
        if (pos < 0):
            pos = 0

        if pos == 0:
            self.addHead(newData)
        elif pos == self.size():
            self.append(newData)
        else:              
            cur = self.head             
            i = 0
            while pos - 1 > i : 
                i += 1
                cur = cur.next
            newNode.next = cur.next
            cur.next.prev = newNode
            cur.next = newNode
            newNode.prev = cur

L = DoublyLinkedList()     
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])

    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
        
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))

    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))

    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
        
    elif i[:2] == "IS":
        data = i[3:].split()             # IS 12 KMITL
        L.insert(int(data[0]), data[1])  # 0123456789

print("Linked List :", L)
print("Linked List Reverse :", L.reverse())