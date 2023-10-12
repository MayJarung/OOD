class Queue:
    def __init__(self):
            self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == 0

    def size(self):
        return len(self.items)

def encodemsg(q1,q2):
    nq = Queue()    
    while q1.size() > 0:
        for i in range(q1.size()):
            y = q1.deQueue()    
            x = q2.deQueue()    
            if 'a' <= y <= 'z':
                if ((ord(y)-ord('a')) + x) > 25:
                    nq.enQueue(chr((((ord(y)-ord('a')) + x) % 26) + ord('a'))) 
                    q2.enQueue(x)
                else:
                    nq.enQueue(chr((ord(y)-ord('a')) + x + ord('a')))
                    q2.enQueue(x)
            else:
                if ((ord(y)-ord('A')) + x)  > 25:
                    nq.enQueue(chr((((ord(y)-ord('A')) + x) % 26) + ord('A')))
                    q2.enQueue(x) 
                else:
                    nq.enQueue(chr((ord(y)-ord('A'))+ x + ord('A')))
                    q2.enQueue(x)
    q1 = nq
    
    return q1.items

def decodemsg(q3, q4):
    nq = Queue()    
    while q3.size() > 0:
        for i in range(q3.size()):
            y = q3.deQueue()    
            x = q4.deQueue()    
            if 'a' <= y <= 'z':
                if ((ord(y)-ord('a')) - x) < 0:
                    nq.enQueue(chr((((ord(y)-ord('a')) - x) % 26) + ord('a'))) 
                    q4.enQueue(x)
                else:
                    nq.enQueue(chr((ord(y)-ord('a')) - x + ord('a')))
                    q4.enQueue(x)
            else:
                if ((ord(y)-ord('A')) - x)  < 0:
                    nq.enQueue(chr((((ord(y)-ord('A')) - x) % 26) + ord('A')))
                    q4.enQueue(x) 
                else:
                    nq.enQueue(chr((ord(y)-ord('A'))- x + ord('A')))
                    q4.enQueue(x)
    q3 = nq

    return q3.items

q1 = Queue()
q2 = Queue()
q3 = Queue()
q4 = Queue()

inp = input('Enter String and Code : ').split(',')          # KMITL,2

for i in range(len(inp[0])):
    if inp[0][i] != ' ':
        q1.enQueue(inp[0][i])
for i in range(len(inp[1])):
    q2.enQueue(int(inp[1][i]))

q1.items = encodemsg(q1, q2)
print("Encode message is : ",q1.items)

for i in range(q1.size()):
    if q1.items != ' ':
        q3.enQueue(q1.deQueue())
for i in range(len(inp[1])):
    q4.enQueue(int(inp[1][i]))

q3.items = decodemsg(q3,q4)
print("Decode message is : ",q3.items)


