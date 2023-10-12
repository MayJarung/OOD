Mylist = [int(x) for x in input("Enter Your List : ").split()]  # if input มา 8 ตัว = -25 -10 -7 -3 2 4 8 10
newList = []  
if len(Mylist) < 3:
    print("Array Input Length Must More Than 2")
    exit()
                 
for i in range(0,len(Mylist)-2):   # range index ที่ (0,5) 0 1 2 3 4   [-25 -10 -7 -32- 2]
    for j in range(i+1,len(Mylist)-1):  # range index ที่ (1,6) 1 2 3 4 5   [-10 -7 -3 2 4]
        for k in range(j+1,len(Mylist)):      # range index ที่ (2,7)  2 3 4 5 6   [-7 -3 2 4 8 10]
            if Mylist[i]+Mylist[j]+Mylist[k]==5:   # ถ้าเลข 3 ตัว ในลิสต์บวกกัน = 5
                arr=[]
                arr.append(Mylist[i])   
                arr.append(Mylist[j])
                arr.append(Mylist[k])
                arr.sort()
                if arr not in newList:  # ถ้าเลข 3 ชุดนั้นยังไม่มีใน newList
                    newList.append(arr)   # ให้เพิ่มลิสต์นั้นเข้าไปใน newList 
print(newList)