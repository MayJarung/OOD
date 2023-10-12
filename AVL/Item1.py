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
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return "*"
        else:
            t = self.root
            S = ""
            while True:
                if data <= t.data:
                    if t.left == None:
                        t.left = newNode
                        S += "L*"
                        return S
                    else:
                        t = t.left
                        S += "L"
                else:
                    if t.right == None:
                        t.right = newNode
                        S += "R*"
                        return S
                    else:
                        t=t.right
                        S += "R"
                    
T = BST()
inp = [int(i)for i in input("Enter Input : ").split()]
for i in inp:
    print(T.insert(i))