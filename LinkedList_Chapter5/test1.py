class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedlist:
    def __init__(self):
        self.head = None
        self.next = None

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        cur = self.head
        s = ""
        while cur != None:
            s += str(cur.data)
            cur = cur.next
            if cur == None:
                break
            s += "->"
        return s

    def append(self, newData):
        newNode = Node(newData)
        if self.isEmpty():
            self.head = newNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode

    def insert(self, index, newData):
        newNode = Node(newData)
        if (index < 0) or (index > self.lenn()):
            return "Data cannot be added"
        elif self.isEmpty():
            self.append(newData)
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            cur = self.head
            i = 0
            while index-1 > i:
                i += 1
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
        return "index = " + str(index) + " and data = " + str(data)

    def lenn(self):
        cur = self.head
        i = 0
        while cur != None:
            i += 1
            cur = cur.next
            if cur == None:
                break
        return i

inp = input("Enter Input : ").split(",")
L = SinglyLinkedlist()

# Enter Input : 0 1 2, -1:3, 10:10
# link list : 0->1->2
# Data cannot be added
# link list : 0->1->2
# Data cannot be added
# link list : 0->1->2

list1 = inp[0].split(" ")
for i in list1:
    L.append(i)
    
if L.isEmpty():
    print("List is empty")
else:
    print(f"link list : {L}" )

for i in inp[1:]:
    id, data = i.split(":")
    id, data = int(id), int(data)
    print(L.insert(id, data))
    print(L)

