

def mergeSort(L):
    if len(L) > 1:
        left_L = L[:len(L)//2]
        right_L = L[len(L)//2:]

        # recursion
        mergeSort(left_L)
        mergeSort(right_L)

        # merge
        i = 0 # left_L index
        j = 0 # right_L index 
        k = 0 # merge L idx
        while i < len(left_L) and j < len(right_L):
            if left_L[i] < right_L[j]:
                L[k] = left_L[i]
                i += 1
            else:
                L[k] = right_L[j]
                j += 1
            k += 1

        while i < len(left_L):
            L[k] = left_L[i]
            i += 1
            k += 1

        while j < len(right_L):
            L[k] = right_L[j]
            j += 1
            k += 1
    return L

inp = list(map(int,input("Enter Input : ").split()))
print(*mergeSort(inp))
