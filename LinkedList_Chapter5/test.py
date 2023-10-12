class SinglyLinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.dummy = self.Node(None, None)
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return 'Empty'
        s = ''
        p = self.dummy.next
        while p != None:
            s += str(p.data) + '->'
            p = p.next
        return s[:-2]

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, data):
        q = self.dummy.next
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, i):
        p = self.dummy
        for j in range(-1, i):
            p = p.next
            if p.next == None:
                break
        return p

    def append(self, data):
        return self.insertAfter(len(self), data)

    def insertAfter(self, i, data):
        p = self.nodeAt(i-1)
        p.next = self.Node(data, p.next)
        self.size += 1

    def deleteAfter(self, i):
        if self.size > 0:
            p = self.nodeAt(i)
            p.next = p.next.next
            self.size -= 1

    def delete(self, i):  # ลบข้อมูลที่ index นั้นเลย
        self.deleteAfter(i-1)

    def removeData(self, data):
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data)-1)


L = SinglyLinkedList()
inp = input('Enter input : ').split(',')
isLoop = False

for x in inp:
    if x[0] == 'A':
        L.append(int(x[2:]))
        print(L)

    elif x[0] == 'S':
        index1, index2 = x[2:].split(':')
        index1, index2 = int(index1), int(index2)
        if L.isEmpty():
            print('Error! {list is empty}')
        elif index1 >= L.size or index1 < 0:
            print(f'Error! {{index not in length}}: {index1}')
        elif index2 >= L.size or index2 < 0:
            print(f'index not in length, append : {index2}')
            L.append(index2)
        else: 
            n1 = L.nodeAt(index1)
            n2 = L.nodeAt(index2)
            n1.next = n2
            print(f'Set node.next complete!, index:value = {index1}:{n1.data} -> {index2}:{n2.data}')
            if index1 > index2 or index1 == index2:
                isLoop = True

if isLoop:
    print('Found Loop')
else:
    print('No Loop')
    print(L)