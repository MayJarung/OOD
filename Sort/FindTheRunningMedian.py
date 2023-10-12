'''เขียนโปรแกรมที่ทำการรับข้อมูลเป็น list เพื่อหาค่ามัธยฐานของข้อมูลใน list โดยจะเริ่มต้นจากข้อมูลใน list เพียง 1 ตัวจากนั้นค่อยๆเพิ่มไปเรื่อยๆจนครบ โดยในการหาค่ามัธยฐานเราต้องจัดเรียงข้อมูลตามลำดับจากน้อยไปหามากเสียก่อน จากนั้นแสดงผลตามตัวอย่าง

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    #code here
'''

def sort(L):
    newList = L.copy()
    a = []
    while newList:
        a.append(newList.pop(minIndex(newList)))
    return a

def minIndex(L):
    index = 0
    for i in range(len(L)):
        if L[i] < L[index]:
            index = i
    return index

def median(L):
    List = sort(L)
    x = len(List) // 2
    y = x
    if len(List) % 2 == 0:
        y = x-1
    return (List[x] + List[y]) / 2

inp = [e for e in input("Enter Input : ").split()]

if inp[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l = list(map(int, inp))
    Ans = []
    for i in l:
        Ans.append(i)
        print(f"list = {Ans} : median = {median(Ans)}")


