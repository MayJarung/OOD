class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

    def insert(root, data):
        if root is None:
            return Node(data)
        if data < root.data :
            root.left = Node.insert(root.left, data)
        if data > root.data :
            root.right = Node.insert(root.right, data)
        
        root.updateHeight()
        balance = root.getBalance()

        if balance > 1 and root.left.getBalance() > 0:
            return root.rightRotate()
        elif balance > 1 and root.left.getBalance() < 0:
            root.left = root.left.leftRotate()
            return root.rightRotate()
        elif balance < -1 and root.right.getBalance() < 0:
            return root.leftRotate()
        elif balance < -1 and root.right.getBalance() > 0:
            root.right = root.right.rightRotate()
            return root.leftRotate()
        return root

    def getHeight(self):
        if self is None:
            return 0
        return self.height

    def updateHeight(self):
        self.height = 1 + max(Node.getHeight(self.left), Node.getHeight(self.right))

    def getBalance(self):
        if self is None:
            return 0
        return Node.getHeight(self.left) - Node.getHeight(self.right)

#       y           right Rotate            x
#      / \          ----------->           / \
#     x   C                               A   y
#    / \            <-----------             / \
#   A   B           left Rotate             B   C

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

    def printTree90(node, level = 0):
        if node != None:
            Node.printTree90(node.right, level + 1)
            print('     ' * level, node)
            Node.printTree90(node.left, level + 1)

class AVL(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = Node.insert(self.root, data)
        return self.root

MyAVLTree = AVL()
data = input("Enter Input :").split()
for e in data:
    print("insert :",e)
    root = MyAVLTree.insert(int(e))
    root.printTree90()
    print("===============")