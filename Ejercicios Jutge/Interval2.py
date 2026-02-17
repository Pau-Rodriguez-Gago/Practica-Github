intervalos=input()
intervalos=intervalos.split()
a1=int(intervalos[0])
b1=int(intervalos[1])
a2=int(intervalos[2])
b2=int(intervalos[3])
if a1==a2 and b1==b2:
    print("=")
elif a1>=a2 and b1<=b2:
    print("1")
elif a2>=a1 and b2<=b1:
    print("2")
else:
    print("?")
