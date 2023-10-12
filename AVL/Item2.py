class Node(object): 
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        return str(self.data)

class BST:
    def getHeight(self, root):
        if not root:
            return 0
        else:
            return root.height

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def insert(self, root, data):
        if not root:
            return Node(data)
        if data >= root.data:
            root.right = self.insert(root.right, data)
        else:
            root.left = self.insert(root.left, data)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and root.left.data >= data:
            print("Not Balance, Rebalance!")
            return self.rotateRight(root)
        if balance < -1 and root.right.data < data:
            print("Not Balance, Rebalance!")
            return self.rotateLeft(root)
        if balance < -1 and root.right.data > data:
            print("Not Balance, Rebalance!")
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        if balance > 1 and root.left.data < data:
            print("Not Balance, Rebalance!")
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        return root

    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        z.left = T3
        y.right = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rotateLeft(self, z): 
        y = z.right
        T2 = y.left
        z.right = T2
        y.left = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

T = BST() 
root = None
inp = input("Enter Input : ").split()
for x in inp:
    print("insert :",x)
    root = T.insert(root, int(x))
    printTree90(root)
    print("===============")