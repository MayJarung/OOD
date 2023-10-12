class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BST:
    def __init__(self): 
        self.root = None

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

    def delete(self, data):
        self.root = BST._delete(self.root, data)
        return self.root
    
    def _delete(root, data):
        if root == None:
            print("Error! Not Found DATA")
            return None
        if data < root.data:
            root.left = BST._delete(root.left, data)
        elif data > root.data:
            root.right = BST._delete(root.right, data)
        else:
            if root.left is not None and root.right is not None:
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                cur.data, root.data = root.data, cur.data
                root.right = BST._delete(root.right, data)

            elif root.right is not None:
                return root.right
            elif root.left is not None:
                return root.left
            else:
                return None
        return root
          
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BST()
data = input("Enter Input : ").split(",")
for i in data:
    if i[0] == "i":
        print(f"insert {i[2:]}")
        root = tree.insert(int(i[2:]))
        printTree90(root)
    elif i[0] == "d":
        print(f"delete {i[2:]}")
        root = tree.delete(int(i[2:]))
        printTree90(root)

