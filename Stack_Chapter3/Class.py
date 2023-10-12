class Stack():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]


    

    