lista=input().split(",")
num=[]
dec=[]
#join
for x in lista:
    num.append(int(x))
print(lista)
num.remove(min(num))
num.remove(max(num))
print(num)
for y in num:
    dec.append(float(y))
media=sum(dec)/len(dec)
media=round(media,2)
if media < 5:
    print("Rendimiento bajo")
if media >=5 and media<=10:
    print("Rendimiento medio")
if media > 10:
    print("Rendimiento alto")