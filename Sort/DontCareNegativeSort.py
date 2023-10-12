'''ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง'''

def buble(L):
    for last in range(len(L)-1, 0, -1):
        for i in range(last):
            swap = False
            count = 0
            while not swap and i + count < len(L):
                if L[i] > L[i+count] and L[i] >= 0  and L[i+count] >= 0:
                    L[i], L[i+count] = L[i+count], L[i] # swap
                    swap = True
                else:
                    count += 1
    return L
        
L = list(map(int,input("Enter Input : ").split(" ")))
print(*buble(L))