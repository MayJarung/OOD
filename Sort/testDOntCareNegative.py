






def dontCareNegative(L):
    for outerLoop in range(len(L)-1,0,-1):
        for i in range(outerLoop):
            swap = False
            count = 0
            while swap is False and i + count < len(L):
                if L[i] > L[i+count] and L[i] >= 0 and L[i+count] >= 0:
                    L[i],L[i+count] = L[i+count],L[i]
                    swap = True
                else:
                    count += 1
    return L

inp = list(map(int,input("Enter Inputr : ").split()))
print(*dontCareNegative(inp))