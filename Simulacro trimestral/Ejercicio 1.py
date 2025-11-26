concatenar=""
inicio=0
fin=0
incremento=0
incio=int(input("Introduce el inicio: "))
fin=int(input("Introduce el fin: "))
incremento=int(input("Introduce un incremento: "))
for i in range(incio,fin,incremento):
    if not i%4==0:
        if i%6==0:
            concatenar=concatenar+"*" + str(i)+ "*" ","
        else:
            concatenar=concatenar+ str(i) + ","
print(concatenar[:-1])
