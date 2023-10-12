def newRange(a): 
    b=[]
    if len(a)==1:         
        s=0.0
        while s<a[-1]:    
            b.append(s)
            s+=1           
    elif len(a)==2:
        s=a[0]
        while s<a[1]:
            b.append(s)
            s+=1
    else:
        s=a[0]
        while s<a[1]:
            b.append(s)
            s+=a[2]
    return b

print("*** New Range ***")
a = [float(i) for i in input("Enter Input : ").split()]
l = newRange(a)

for i in range(len(l)):
    l[i]=float("{:.3f}".format(l[i]))
print(tuple(l))