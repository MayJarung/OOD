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
        if data < root.data:
            root.left = BST._insert(root.left, data)
        else:
            root.right = BST._insert(root.right, data)
        return root

    def delete(self, data):
        self.root = BST._delete(self.root, data)
        return self.root
    
    def _delete(root, data):
        if root is None:
            print("Error! Not Found DATA")
            return None
        if data < root.data:
            root.left = BST._delete(root.left, data)
        elif data > root.data:
            root.right = BST._delete(root.right, data)
        else: # เจอข้อมูลที่ต้องการลบละ
            if root.right is not None and root.left is not None:
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                root.data, cur.data = cur.data, root.data
                # data ที่จะลบอยู่ที่ใบเรียบร้อย 
                root.right = BST._delete(root.right, data) 
                # ทำอันนี้ ยังไง data ที่จะลบก็จะอยู่ที่ใบอยู่แล้ว จะไม่เข้า if นี้อีกแน่นอน
            elif root.left is not None:
                return root.left
            elif root.right is not None:
                return root.right
            else:
                return None
            
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

T = BST()
data = input("Enter Input : ").split(",")
for i in data:
    if i[0] == "i":
        print(f"insert {i[2:]}")
        root = T.insert(int(i[2:]))
        printTree90(root)
    elif i[0] == "d":
        print(f"delete {i[2:]}")
        root = T.delete(int(i[2:]))
        printTree90(root)
