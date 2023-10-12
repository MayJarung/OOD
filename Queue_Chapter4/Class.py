class Queue():
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def __str__(self):
        s = ', '.join(self.items)
        return s