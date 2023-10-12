# ใช้ 2 paramiter 
def f1(n, i=0):
    if n == i:
        return

    i += 1
    print(i)
    f1(n,i)

inp = int(input("Enter Input : "))
f1(inp)

# ใช้ paramiter เดียว
def f2(n):
    if n == 0:
        return

    f2(n-1)
    print(n)

inp = int(input("Enter Input : "))
f2(inp)

# ex. f(4)
# 1
# 2
# 3
# 4





