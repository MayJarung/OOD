class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = BST.add(self.root, data)
        return self.root
    
    def add(root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = BST.add(root.left, data)
        else:
            root.right = BST.add(root.right, data)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(int(i))
T.printTree(root)