# Base-Case
def countdown(n):
    # Base-Case
    if n == 0:
        return
    print(n)
    countdown(n-1)

inp = int(input("Enter Input : "))
countdown(inp)

# ex. countdown(4)
# 4
# 3
# 2
# 1
# 0