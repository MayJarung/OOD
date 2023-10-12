def sum(n):
    if n == 0:
        return 0

    
    return n + sum(n-1)

inp = int(input("Enter input : "))
print(sum(inp))


# ex. sum(5) = 5+4+3+2+1 = 15