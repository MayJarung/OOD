class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    
    # def getData(self):
    #     return self.data

    # def getLeft(self):
    #     return self.left

    # def getRight(self):
    #     return self.right
    
    # def setData(self, data):
    #     self.data = data

    # def setLeft(self, left):
    #     self.left = left
    
    # def setRight(self, right):
    #     self.right = right

class BST:
    def __init__(self, root = None):
        self.root = root
    
    def insert(self, data):
        self.root = BST._add(self.root, data)
        return self.root

    def _add(root, data):
        if root == None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
        return root

#         Enter Input : 10 4 20 1 5
#       20
#  10
#            5
#       4
#            1

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
