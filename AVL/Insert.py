class Node(object): 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)

    def insert(root, data):
        # ถ้าไม่มีอะไรใน AVL Tree เลย
        if root is None:
            return Node(data)
        # ถ้า data ที่จะ insert น้อยกว่า root.data
        if data < root.data:
            root.left = Node.insert(root.left, data)
        # ถ้า data ที่จะ insert มากกว่า root.data
        else:
            root.right = Node.insert(root.right, data)

        # update ความสูงของ root หลังจาก insert
        root.updateHeight()
        balance = root.getBalance()

        # LeftLeft
        if balance > 1 and root.left.getBalance() > 0:
            return root.rightRotate()
        # LeftRight
        elif balance > 1 and root.left.getBalance() < 0:
            root.left = root.left.leftRotate()
            return root.rightRotate()
        # RightRight
        elif balance < -1 and root.right.getBalance() < 0:
            return root.leftRotate()
        # RightLeft
        elif balance < -1 and root.right.getBalance() > 0:
            root.right = root.right.rightRotate()
            return root.leftRotate()
        # Already Balance
        return root

    def printTree90(node, level = 0):
        if node != None:
            Node.printTree90(node.right, level + 1)
            print('     ' * level, node)
            Node.printTree90(node.left, level + 1)

    def getHeight(self):
        # ถ้าไม่มีอะไรใน AVL Tree เลย
        if self is None:
            return 0
        # มีข้อมูลใน AVL Tree 
        return self.height

    def updateHeight(self):
        # อัพเดทความสูง โดยเอาความสูงของ root (กำหนดเป็น 1) + ค่าความสูงที่มากที่สุดของลูกทั้ง 2 ฝั่ง 
        self.height = 1 + max(Node.getHeight(self.left), Node.getHeight(self.right))

    def getBalance(self):
        # ถ้าไม่มีอะไรใน AVL Tree เลย
        if self is None:
            return 0
        # มีข้อมูลใน AVL Tree 
        # return ค่า Balance โดยเอาความสูงของลูกฝั่งซ้าย - ความสูงของลูกฝั่งขวา
        return Node.getHeight(self.left) - Node.getHeight(self.right)

    #              LeftRotate                                 RightRotate
    #       x                        y                 x                        A
    #      / \                      / \               / \                      / \
    #     A   y      ------>       x   C             A   y      ------>       B   x
    #        / \                  / \               / \                          / \
    #       B   C                A   B             B   C                        C   y

    #       y                            x
    #      / \     Right Rotation       / \
    #     x   C    - - - - - - - >     A   y
    #    / \       < - - - - - - -        / \
    #   A   B      Left Rotation         B   C

    def leftRotate(px):
        py = px.right
        px.right, py.left = py.left, px
        px.updateHeight()
        py.updateHeight()
        return py

    def rightRotate(py):
        px = py.left
        py.left, px.right = px.right, py
        py.updateHeight()
        px.updateHeight()
        return px
    
class AVL_Tree(object): 
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = Node.insert(self.root, data)
        return self.root

myTree = AVL_Tree() 
data = input("Enter Input : ").split()

for e in data:
    print("insert :",e)
    root = myTree.insert(int(e))
    root.printTree90()
    print("===============")