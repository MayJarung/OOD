def bin(dec, start, size):
    if start < size-1:
        bin(dec//2, start+1, size)
    print(dec%2, end='')

def numinbinary(min, size, max):
    if(min < max):
        bin(min, 0, size)
        print("")
        numinbinary(min+1, size, max)

inp = input("Enter Number : ")
inp = int(inp)

if(inp < 0):
    print("Only Positive & Zero Number ! ! !")
elif(inp == 0):
    print("0")
else:
    numinbinary(0, inp, 2**inp)