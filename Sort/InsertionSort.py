






def insertion(L):
    for i in range(1, len(L)):
        while L[i] < L[i-1] and i > 0:
            L[i-1], L[i] = L[i], L[i-1]
            i -=1
    return L

inp = list(map(int,input("Enter Input : ").split()))
print(*insertion(inp))

'''
L = 2 6 5 1 3 4
ให้เริ่ม for loop index 1
    แล้วเช็คว่า ค่าของ index i < index i-1
    while ถ้าค่าของ index i < index i-1 และ i > 0 ก็คือ i น้อยสุดได้แค่ 1 เพราะเราต้องใช้ index i-1 ด้วย
        ถ้าน้อยกว่าให้สลับค่ากัน ค่าน้อยจะไปอยู่หน้า
        แล้ว i -= 1 เพื่อเช็คของคู่ก่อนหน้าเราอีกรอบ
return L
'''