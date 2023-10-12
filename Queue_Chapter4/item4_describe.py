from locale import getlocale


class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self, i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def __str__(self):
        S = ', '.join(self.items)
        return S
    def getmyActmyLoc(self):
        S = ''
        actOrder = ['Eat','Game', 'Learn', 'Movie']
        locOrder = ['Res.','ClassR.', 'SuperM.', 'Home']
        myActivity = Queue()
        for i in self.items: # while !self.isEmpty()
            do, dowhere = i.split(':') # do, dowhere = self.MyQ().split(':')
            myActivity.enQueue(actOrder[int(do)]+':'+locOrder[int(dowhere)])
        S = ', '.join(myActivity.items)
        return S

        # for i in range(myAct.size()):
        #     a = myAct.deQueue()
        #     b = myLoc.deQueue()
        #     if not myAct.isEmpty() and not myLoc.isEmpty():    # ถ้า myAct and myLoc มีสมาชิกใน Queue 
        #     myActmyLoc.enQueue(actOrder[int(a)]+':'+locOrder[int(b)])
        #     myActmyLoc.enQueue(actOrder[int(a)])
        # S = ', '.join(myAct.items)
    def getYourActYourLoc(self):
        S = ''
        actOrder = ['Eat','Game', 'Learn', 'Movie']
        locOrder = ['Res.','ClassR.', 'SuperM.', 'Home']
        myActivity = Queue()
        for i in self.items: # while !self.isEmpty()
            do, dowhere = i.split(':') # do, dowhere = self.MyQ().split(':')
            myActivity.enQueue(actOrder[int(do)]+':'+locOrder[int(dowhere)])
        S = ', '.join(myActivity.items)
        return S
        

inp = input('------------------------------------------Enter Input : ').split(',')  
# inp = 0:1 2:3,3:2 3:2 
print(f"inp = {inp}")
MeInEachDay = Queue()
YouInEachDay = Queue()
myAct = Queue()
myLoc = Queue()
yourAct = Queue()
yourLoc = Queue()
myActmyLoc = Queue()
Score = 0

for i in range(len(inp)):
    a, b = inp[i].split(" ")
    MeInEachDay.enQueue(a)
    YouInEachDay.enQueue(b)
    # MeInEachDay (คิว) = 0:1, 3:2      Me in each day
    # YouInEachDay (คิว) = 2:3, 3:2      You in each day
print(f"My   Queue = {MeInEachDay}")
print(f"Your Queue = {YouInEachDay}")

for i in range(MeInEachDay.size()):
    a = MeInEachDay.deQueue()
    c,d = a.split(":")
    myAct.enQueue(c)
    myLoc.enQueue(d)
    MeInEachDay.enQueue(a)
    # My Act (คิว) = 0, 3          My Act in each day
    # My Location (คิว) = 1, 2     My Loc in each day
print(f"My Act = {myAct}")
print(f"My Location = {myLoc}")
print(f"------------------------------------------My   Queue = {MeInEachDay}")

for i in range(YouInEachDay.size()):
    a = YouInEachDay.deQueue()
    c,d = a.split(":")
    yourAct.enQueue(c)
    yourLoc.enQueue(d)
    YouInEachDay.enQueue(a)
    # yourAct (คิว) = 2, 3         My Act in each day
    # yourLoc (คิว) = 3, 2         My Loc in each day
print(f"Your Act = {yourAct}")
print(f"Your Location = {yourLoc}")
print(f"------------------------------------------Your   Queue = {YouInEachDay}")
print("------------------------------------------My   Activity:Location = "+ MeInEachDay.getmyActmyLoc())
print("------------------------------------------Your   Activity:Location = "+ YouInEachDay.getYourActYourLoc())

for i in range(myAct.size()):  
    a = myAct.deQueue()  
    b = yourAct.deQueue()
    c = myLoc.deQueue()
    d = yourLoc.deQueue()    
    if a == b and c != d:
        Score += 1
    elif a != b and c == d:
        Score += 2
    elif a == b and c == d:
        Score += 4
    else:
        Score -= 5

if Score >= 7:
    print("Yes! You're my love! : Score is "+ str(Score)+".") 
elif Score > 0:  
    print("Umm.. It's complicated relationship! : Score is "+ str(Score)+".")   
else:
    print("No! We're just friends. : Score is "+ str(Score)+".")   
