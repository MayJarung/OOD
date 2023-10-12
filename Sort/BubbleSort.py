''' 
รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่าง

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import*** 
'''

def buble(L):
    step = 0
    for last in range(len(L)-1, 0, -1): # ทำเพิ้อให้ ขอบเขตน้อยลงที่ละ 1
        move = None
        swap = False
        for i in range(last):
            if L[i] > L[i+1]:
                move = L[i]
                L[i], L[i+1] = L[i+1], L[i] # swap
                swap = True
        if swap is True and last > 1:
            step += 1
            print(f"{step} step : {L} move[{move}]")
        elif swap is True and last == 1:
            print(f"last step : {L} move[{move}]")

        if swap is False:
            print(f"last step : {L} move[None]")
            break

L = list(map(int,input("Enter Input : ").split(" ")))
buble(L)