inicio=0
fin=0
incremento=0
incio=int(input("Introduce el inicio: "))
fin=int(input("Introduce el fin: "))
incremento=int(input("Introduce un incremento: "))
for i in range(incio,fin,incremento):
    if not(i/4==i//4) and not(i/6==i//6):
        print(i,",")
    elif i/6==i//6:
        print("*",i,"*")
    