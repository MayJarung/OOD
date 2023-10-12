print("*** TorKham HanSaa ***")
array = [x.split() for x in input("Enter Input : ").split(",")]
newArray = []
first = True
i = 0

for ele in array:
    if(ele[0]=="P"):   # ถ้า ele ตัวแรก (index 0) คือ "P"
        myLastTwo = ele[1][-2] + ele[1][-1]   # 2 ตัวท้ายของคำ = ele index 1 (คำที่ต่อคำแรก) ตำแหน่งที่ -2 + ำle index 1(คำที่ต่อคำแรก) ตำแหน่งที่ -1
        if(array[i+1][0]!="X" and array[i+1][0]!="R"):  # index ที่ 1 ตำแหน่งที่ 0 (ตัวแรกของ index 1) ไม่เท่ากับ X และ R
            nextTwoFirst = array[i+1][1][0] + array[i+1][1][1]  # 2 ตัวแรกของคำถัดไป = ตัวอักษรของคำใน array ที่ index ที่ 1 ของ array ทั้งหมด แต่ index ที่ 0 ของ index ก่อนหน้า + ตัวอักษรของคำใน array ที่ index ที่ 1 ของ array ทั้งหมด แต่ index ที่ 1 ของ index ก่อนหน้า
        if(first):
            newArray.append(ele[1])
            first = False
        print("'" + ele[1]+"' -> ", end = '')
        print(newArray)
        if(array[i+1][0]!="X" and array[i+1][0]!="R"):
            if(myLastTwo.lower()==nextTwoFirst.lower()):
                newArray.append(array[i+1][1])
            else:
                print("'" + array[i+1][1]+"' -> game over")
                break
    elif(ele[0]=="R"):
        print("game restarted")
        newArray= []
        first = True
    elif(ele[0]=="X"):
        break
    else:
        print("'" + ele[0] + " " + ele[1]+"' is Invalid Input !!!")
        break
    i = i + 1
    myLastTwo = ""
    nextTwoFirst = ""