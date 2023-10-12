class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if self.isEmpty():
            return "Empty"  
        cur = self.head                               
        s = ""
        while cur != None:                   
            s += str(cur.data)
            cur = cur.next
            if cur == None:
                break
            s += "->"
        return s

    def size(self):
        cur = self.head
        i = 0
        while cur != None:
            i += 1
            cur = cur.next
        return i

    def nodeAt(self, pos):
        cur = self.head             
        for i in range(0, pos):
            cur = cur.next
            if cur.next == None:
                break
        return cur

    def append(self, newData):
        newNode = Node(newData)
        if self.isEmpty():  
            self.head = newNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode
    
L = SinglyLinkedList()  
inp = input("Enter input : ").split(",")          # A 0,A 3,A 5,A 7,A 9,S 2:0
isLoop = False                                    # 0->3->5->7->9

for i in inp:
    if i[0] == "A":
        L.append(int(i[2:]))
        print(L)

    if i[0] == "S":
        id1, id2 = i[2:].split(":")    
        id1, id2 = int(id1), int(id2)
        if L.isEmpty():
            print("Error! {list is empty}")
        elif (id1 >= L.size() or id1 < 0):
            print("Error! {index not in length}:",id1)
        elif (id2 >= L.size() or id2 < 0):
            print("index not in length, append :",id2)
            L.append(id2)
        else:
            n1 = L.nodeAt(id1)
            n2 = L.nodeAt(id2)
            n1.next = n2
            print(f"Set node.next complete!, index:value = {id1}:{n1.data} -> {id2}:{n2.data}")
            if id1 > id2 or id1 == id2:
                isLoop = True

if isLoop:
    print('Found Loop')
else:
    print('No Loop')
    print(L)
    