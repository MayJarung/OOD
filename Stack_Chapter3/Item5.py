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

    def peak(self):
        return self.items[-1]
        
    def highCheck(self):
        if self.size() > 0:      # ถ้าใน stack (s) มีขนาด > 0
            return self.peak()   # เรียกดูค่าล่าสุด (top) ของ s
        else:
            return 0

inp = input('Enter Input : ').split(',')      # สมมุติ input = A 4,A 3,B,S,B,A 5,A 8,B

s1 = Stack()                                                  # 4 3 / 4 3 5 8
s2 = Stack()       
s3 = Stack()             
a1 = []                                                       # [4 3] / [4 3 5 8] => [3 5 5 8]
a2 = []                                                  

for x in inp:                                                 # i = A 4 (ตัวที่อยู่ในคอมม่า) 
 
    if x[0] == 'S':
        for i in range(len(a1)):
            if a1[i] % 2 == 0:
                a1[i] -= 1
            else:
                a1[i] += 2                                          

    elif x[0] == 'B':                                         # สมมุติ input = A 4,A 3,B,S   4 3 5 8
        countTrees = 0                                        # 1
        maxHeightTree = 0                                     # max = 8
        a2 = a1.copy()                                        # a1 = [4,3] / [4,3,5,8]
        a2.reverse()                                          # a1 = [3,4] / [8,5,3,4] 
        for i in range(len(a2)):                              # a2 = [3,4]                             
            if a2[i]> maxHeightTree:  
                maxHeightTree = a2[i]
                countTrees += 1
        print(countTrees)                                     # 9 4 8 2 7 3 6   6 3 7 2 8 4 9
        

    else:                                                         
        s1.push(int(x[2:])) 
        a1.append(int(x[2:])) 

            
        # สมมุติ input = A 4,A 3,B,S,B,A 5,A 8,B    s1 = 4 3 


        #print(s.size())         
                                          

                                        