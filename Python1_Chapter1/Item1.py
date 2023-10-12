print("*** Rabbit & Turtle ***")
MyList = input("Enter Input : ").split()
MyList = [float(MyList[0]),float(MyList[1]),float(MyList[2]),float(MyList[3])]
NewList = "{:.2f}".format(MyList[0]/(MyList[2]-MyList[1])*MyList[3])
print(NewList)