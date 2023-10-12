



def bubbleSort(L):
    step = 0
    for outerLoop in range(len(L)-1,0,-1):
        swap = False
        move = None
        for i in range(outerLoop):
            if L[i] > L[i+1]:
                move = L[i]
                L[i],L[i+1] = L[i+1],L[i]
                swap = True
        if swap is True and outerLoop == 1:
            print(f"last step : {L} move[{move}]")
        elif swap is True and outerLoop > 1:
            step += 1
            print(f"{step} step : {L} move[{move}]")
        if swap is False:
            print(f"last step : {L} move[{move}]")
            break 
                

inp = list(map(int,input("Enter Input : ").split()))
bubbleSort(inp)






