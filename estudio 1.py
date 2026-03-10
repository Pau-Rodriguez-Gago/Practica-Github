valores=input().split(",")
num=[int(x) for x in valores]
print(valores)
num.remove(max(num))
num.remove(min(num))
print(num)
media=round(sum(num)/len(num),2)
if media<5:
    print("Rendimiento bajo")
if media >=5 and media <=10:
    print("Rendimiento medio")
if media >10:
    print("Rendimiento alto")