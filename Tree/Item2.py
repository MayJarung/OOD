class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self, root = None):
        self.root = root
    
    def insert(self, data):
        self.root = BST._insert(self.root, data)
        return self.root

    def _insert(root, data):
        if root == None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._insert(root.left, data)
            else:
                root.right = BST._insert(root.right, data)
        return root

    def findMin(self):
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return "Min : " + str(cur.data)

    def findMax(self):
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return "Max : " + str(cur.data)

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
print("-"*50)
print(T.findMin())
print(T.findMax())
