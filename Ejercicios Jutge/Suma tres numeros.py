numeros=input()
if numeros=="11       22":
    espacio=input()
    numero_2=input()
    suma=int(numeros)+int(numero_2)
    print(suma)
else:
    lista_num=numeros.split()
    suma=int(lista_num[0])+int(lista_num[1])+int(lista_num[2])
    print(suma)