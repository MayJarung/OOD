




def greaterValue(lst,data):
    for i in lst:
        if i > data:
            return i
    return "No First Greater Value"

inp = input("Enter Input : ").split("/")
arr,k = list(map(int,inp[0].split())),inp[1]

for i in k.split():
    print(greaterValue(sorted(arr),int(i)))




