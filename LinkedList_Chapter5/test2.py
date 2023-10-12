# ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้
# 1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
# 2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
# 3. reverse     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่ท้ายไปจนหัวมีตัวอะไรบ้าง
# 4. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
# 5. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
# 6. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
# 7. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
# 8. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
# 9. size           คืนค่าเป็นขนาดของ Linked List
# 10. pop         นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
# 11. insert       เป็นการนำ Item ไปแทรกใน Linked List ตามตำแหน่ง pos ไม่มีการคืนค่า

class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.mext = next

class DoublyLinkedlist:
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
            # if cur == None:
            #     break
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur  = self.tail
        s = ""
        while cur != None:
            s += str(cur.data) + " "
            cur = cur.prev
            if cur == None:
                break
        return s

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            newNode.next = None
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = None

    def addHead(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.append(data)
            return
        else:
            cur = self.head
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
        i = 0
        while cur != None:
            if cur.data == item:
                return i
            i += 1
            cur = cur.next
        return -1

    def size(self):
        cur = self.head
        i = 0
        while cur != None:
            i += 1
            cur = cur.next
        return i

    def insert(self, pos, data):       #  0  1  2  3
                                       #  1  2  3  4
                                       # -4 -3 -2 -1
        newNode = Node(data)
        # if pos < self.size()

        if self.isEmpty():
            self.append(data)
        elif pos == 0:
            self.addHead(data)
        else:
            cur = self.head 
            i = 0
            while pos -1 > i:
                i += 1
                cur = cur.next
            newNode.next = cur.next
            cur.next.prev = newNode
            newNode.prev = cur
            cur.next = newNode
            
    def pop(self, pos):
        if not (-(self.size() <= pos < self.size())):
            return "Out Of Range"

        if pos < 0:
            pos += self.size()

        if pos == 0:
            cur = self.head
            if cur.next != None:
                cur.next.prev = None
            self.head = cur.next
            if self.head == None:
                self.tail = None 

        elif pos == self.size()-1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            if self.tail == None:
                self.head = None
            
        else:
            cur = self.head
            i = 0
            while pos > i:
                i += 1
                cur = cur.next
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        
        return "Success"

inp = input("Enter Input : ").split(",")
L = DoublyLinkedlist()

# Enter Input : AP I,AP Love,AP KMITL,AP 2020
# Linked List : I Love KMITL 2020 
# Linked List Reverse : 2020 KMITL Love I 

for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print(f"{L.search(i[3:])} {i[3:]} in {L}")
    elif i[:2] == "SI":
        print(f"Linked List size = {L.size()} : {L}")
    elif i[:2] == "ID":
        print(f"Index ({i[3:]}) = {L.index(i[3:])} : {L}")
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])

print(f"Linked List : {L}")
print(f"Linked List Reverse : {L.reverse()}")