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
        self.root = BST._insert(self.root, data)
        return self.root

    def _insert(root, data):
        if root is None:
            return Node(data)
        if  data < root.data:
            root.left = BST._insert(root.left, data)
        else:
            root.right = BST._insert(root.right, data)
        return root
    
    def bet(self, root):
        Q = [root]
        lst = []
        while len(Q) != 0:
            for _ in range(len(Q)):
                a = Q.pop(0)
                lst.append(str(a.data))
                if a.left is not None:
                    Q.append(a.left)
                if a.right is not None:
                    Q.append(a.right)
        return lst

T = BST()
inp = input("Input : ").split()
for i in inp:
    root = T.insert(int(i))
print("Out : ", end = "")
print(" ".join(T.bet(root)))



