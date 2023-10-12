def calculate(L):
    lst = []
    lst.append(L[0])
    lst.append({'points': (int(L[1])*3)+(int(L[3]))})
    lst.append({'gd': (int(L[4]))-(int(L[5]))})
    return lst

def sort(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if more(L[j],L[i]):
                L[j],L[i] = L[i],L[j]
    return L

def more(x,y):
    if x[1]["points"] > y[1]["points"]:
        return True
    if x[1]["points"] == y[1]["points"]:
        return x[2]["gd"] > y[2]["gd"]
    return False

inp = input("Enter Input : ").split("/")
list1,Ans = [],[]
for i in inp:
    list1.append(i.split(","))
for i in list1:
    Ans.append(calculate(i))
sort(Ans)
print("== results ==")
print(*Ans,sep ='\n')


# Ans = ['Manchester United', {'points': 95}, {'gd': 68}]
