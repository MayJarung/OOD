'''รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

- หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

- หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"

- หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง'''

# น้อยไปมาก return True ก็ต่อเมื่อไม่มีเลยที่ตัวซ้ายจะมากกว่าตัวขวา
def lessTomore(L):            
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

# มากไปน้อย return True ก็ต่อเมื่อไม่มีเลยที่ตัวซ้ายจะน้อยกว่าตัวขวา
def moreToless(L):
    for i in range(len(L)-1):
        if L[i] < L[i+1]:
            return False
    return True

# return True ก็ต่อเมื่อมีตัวใดตัวนึงเท่ากัน
def someSame(L):
    for i in range(len(L)-1):
        if L[i] == L[i+1]:
            return True
    return False

# return True ก็ต่อเมื่อไม่มีตัวใดเลยที่ไม่เท่ากัน
def allSame(L):
    for i in range(len(L)-1):
        if L[i] != L[i+1]:
            return False
    return True

def somethingDrome(L):
    if allSame(L):
        return "Repdrome"
    elif lessTomore(L):
        if someSame(L):
            return "Plaindrome"
        return "Metadrome"
    elif moreToless(L):
        if someSame(L):
            return "Nialpdrome"
        return "Katadrome"
    else:
        return "Nondrome"

inp = [int (i) for i in input("Enter Input : ")]
print(somethingDrome(inp))
