class Stack():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def isEmpty(self):
        return self.size() == 0
    def size(self):
        return len(self.items)
    def push(self, ele):
        self.items.append(ele)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def __str__(self): 
        return ''.join(self.items)


def checkParen():
    s =  Stack()
    op = "({["
    cl = ")}]"
    for i in inp:
        if i in op:
            s.push(i)
        elif i in cl:
            if s.is_empty():
                return inp + " close paren excess"
            else:
                if op.index(s.peek()) == cl.index(i):
                    s.pop()
                else: 
                    return inp + " Unmatch open-close"
    if s.is_empty():
        return inp + " MATCH"
    else:
        return f"{inp} open paren excess   {str(s.size())} : {str(s)}"
        
inp = (input("Enter expresion : "))
s =  Stack()
print(checkParen())
