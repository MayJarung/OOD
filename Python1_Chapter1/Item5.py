x = int(input("Enter Input : "))

for i in range(x+2):
    s = ""
    for j in range(x-i+1):
        s += "."
    for j in range(i+1):
        s += "#"
    for j in range(x+2):
        if i == 0 or i == x+1:
            s += "+"
        elif j != 0 and j != x+1:
            s += "#"
        else:
            s += "+"
    print(s)

for i in range(x+2):
    s = ""
    for j in range(x+2):
        if i == 0 or i == x+1:
            s += "#"
        elif j != 0 and j != x+1:
            s += "+"
        else:
            s += "#"
    for j in range(x-i+2):
        s += "+"
    for j in range(i):
        s += "."
    print(s)