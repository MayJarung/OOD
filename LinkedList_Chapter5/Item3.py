# Enter Input (L1,L2) : 1->2->3 4->5
# L1    : 1 2 3 
# L2    : 4 5 
# Merge : 1 2 3 5 4

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
        return self.head == None
 
    def __str__(self):
        if self.isEmpty():
            return "Empty"  
        cur = self.head                               
        s = ""
        while cur != None:                   
            s += str(cur.data) + " "
            cur = cur.next
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

    def size(self):
        cur = self.head
        i = 0
        while cur != None:
            i += 1
            cur = cur.next
        return i

    def pop(self):
        out = self.tail.data
        self.tail = self.tail.prev
        if self.tail == None:
            self.head = None
        else:
            self.tail.next = None
        return out

    # def pop(self):
    #     out = self.tail.data
    #     self.tail = self.tail.prev
    #     if self.tail == None:
    #         self.head = None
    #     else:
    #         self.tail.next = None
    #     return out
    
L1 = DoublyLinkedList()     
L2 = DoublyLinkedList()    
inp = input("Enter Input (L1,L2) : ").split()

# 1->2->3 4->5

a = inp[0].split("->")
b = inp[1].split("->")

for i in range(len(a)):
    L1.append(a[i])
for i in range(len(b)):
    L2.append(b[i])

print("L1    :", L1)
print("L2    :", L2)

while not L2.isEmpty():
    L1.append(L2.pop())

print("Merge :", L1)







