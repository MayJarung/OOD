

def selectionSort(L):
    for i in range(0, len(L)-1):
        cur_min_index = i
        for j in range(i+1, len(L)):
            if L[cur_min_index] > L[j]:
                cur_min_index = j
        
        L[i],L[cur_min_index] = L[cur_min_index],L[i]

    return L

inp = list(map(int,input("Enter Input : ").split()))
print(*selectionSort(inp))


'''
inp = 2 6 5 1 3 4

for loop ให้ i เป็นได้ถึงตัวก่อนสุดท้าย เพราะมันต้องใช้ i+1 เดะเกิน
    ให้ Index ของ ตัวน้อยสุด = i
    for loop ให้ j เป็นได้ตั้งแต่ i+1 ถึงตัวสุดท้าย
        if L[i] > L[j]:
            สลับที่กัน ให้่ j ไปซ้าย i ไปขวา
return L
'''