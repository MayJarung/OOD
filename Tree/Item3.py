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

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(root: Node, item):
    if root.data == item:
        print("None Because {0} is Root".format(item))
    if not item in data[0]:
        print("Not Found Data")
    if root != None:
        if root.right != None:
            if root.right.data == item:
                print(root.data)
                return
            else:
                father(root.right, item)
        if root.left != None:
            if root.left.data == item:
                print(root.data)
                return
            else:
                father(root.left, item)
        
        
    # if root is None:
    #     return None
    # if item < root.data:
    #     temp = father(root.left, item)
    # elif item > root.data:
    #     temp = father(root.right, item)
    # else:
    #     return root
    
    # if temp is None:
    #     return None
    # if temp.data == item:
    #     return root
    # else:
    #     return temp
    
tree = BST()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)

if data[1] not in data[0]:
    print("Not Found Data")
else:
    father(tree.root,data[1])
