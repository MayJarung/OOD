class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)
        
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
        
    def match(self,open, close):
        opens = '{[('
        closes = '}])'
        return opens.index(open) == closes.index(close)

    def parenMatching(self,inp):
        i = 0
        error = 0
        s = Stack()

        while i<len(inp) and error == 0:
            ch = inp[i]
            if ch in '{[(':
                s.push(ch)
            else:
                if ch in '}])':
                    if s.size()>0:   # isEmpty ก็ได้
                        if not self.match(s.pop(),ch):
                            error = 1
                    else:
                        error = 2
            i += 1
        
        if error==0 and s.size()>0:
            error = 3
        return error,ch,i,s

ls = list(input("Enter expresion : "))

stack = Stack()

error,ch,i,s = stack.parenMatching(ls)

ls = ''.join(ls)   # ทำให้ ls กลับไปเป็น str

if error == 1:
    print(ls, 'Unmatch open-close ')
elif error == 2:
    print(ls, 'close paren excess')
elif error == 3:
    print(ls, 'open paren excess  ',s.size(),': ',end='' )
    for ele in s.items:
        print(ele,sep=' ',end='')
    print()
else:
    print(ls,'MATCH')
    

