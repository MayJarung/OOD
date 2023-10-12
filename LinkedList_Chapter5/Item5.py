class Node:
    def __init__(self, data = None):
        if data == None:
            self.data = None
        else:
            self.data = data
        self.next = None
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None

    def __str__(self):
        return str(self.data)

def createLL(LL):
    head = None
    tail = None
    for x in LL:
        if head is None:
            head = Node(x)
            tail = head
        else:
            tail.next = Node(x)
            tail = tail.next
    return head

def printLL(head: Node):
    s = ""
    cur = head
    while cur is not None:
        s += str(cur.data) + " "
        cur = cur.next
    return s

def SIZE(head: Node):
    i = 0
    while head is not None:
        i += 1
        head = head.next
    return i

def nodeAt(head: Node, pos):
    i = 0
    cur = head
    while pos > i:
        i += 1
        cur = cur.next
    return cur
    # cur = head             
    # for i in range(0, pos):
    #     cur = cur.next
    #     if cur.next == None:
    #         break
    # return cur

def splitLL(head: Node, pos):
    beforeLL = nodeAt(head, pos-1)
    afterLL = beforeLL.next
    beforeLL.next = None
    return afterLL

def appendNode(head: Node, n: Node):
    if head is None:
        return n
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = n
    return head
    
def buttomUp(head: Node, pos, size):
    if pos == 0 or pos == size:
        return head
    tail = nodeAt(head, size-1)
    newHead = splitLL(head, pos)
    tail.next = head
    return newHead

def Riffle(head: Node, pos):
    second = splitLL(head, pos)
    newNode = None
    while head is not None or second is not None:
        if head is not None:
            a = splitLL(head, 1)
            head, a = a, head
            newNode = appendNode(newNode, a)
        if second is not None:
            b = splitLL(second, 1)
            second, b = b, second
            newNode = appendNode(newNode, b)
    return newNode
            
def DeRiffle(head: Node, pos, size):
    firstNode = None
    secondNode = None
    while head is not None:
        if SIZE(firstNode) < pos:
            a = splitLL(head, 1)
            head, a = a, head
            firstNode = appendNode(firstNode, a)
        if SIZE(secondNode) < size-pos:
            b = splitLL(head, 1)
            head, b = b, head
            secondNode = appendNode(secondNode, b)
    tail = nodeAt(firstNode, pos-1)
    tail.next = secondNode
    return firstNode

def scarmble(head: Node, b, r, size):
    buttom = int((b*size)/100)
    riffle = int((r*size)/100)
    head = buttomUp(head, buttom, size)
    print(f"BottomUp {b:.3f} % : {printLL(head)}")
    head = Riffle(head, riffle)
    print(f"Riffle {r:.3f} % : {printLL(head)}")
    head = DeRiffle(head, riffle, size)
    print(f"Deriffle {r:.3f} % : {printLL(head)}")
    head = buttomUp(head, size-buttom, size)
    print(f"Debottomup {b:.3f} % : {printLL(head)}")

inp1, inp2 = input('Enter Input : ').split('/') # 1 2 3 4 5 6 7 8 9 10/B 30,R 60|B 50,R 50

print('-' * 50)
h = createLL(inp1.split())

for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)