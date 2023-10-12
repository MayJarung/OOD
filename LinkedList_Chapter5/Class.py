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

    def indexOf(self, data):
        cur = self.head
        id = 0
        while cur != None:
            if cur.data == data:
                return id
            id += 1
            cur = cur.next
        return -1

    def nodeAt(self, pos):
        cur = self.head             
        for i in range(0, pos):
            cur = cur.next
            if cur.next == None:
                break
        return cur
    
    def insertAt(self, pos, newData):
        newNode = Node(newData)
        cur = self.nodeAt(pos)
        newNode.next = cur.next
        cur.next = newNode

    def append(self, newData):
        newNode = Node(newData)
        if self.isEmpty():  
            self.head = newNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode