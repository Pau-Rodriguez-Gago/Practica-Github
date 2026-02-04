numeros=input()
if numeros=="2":
    numero_2=input()
    suma=int(numeros)+int(numero_2)
    print(suma)
else:
    lista_num=numeros.split()
    suma=int(lista_num[0])+int(lista_num[1])
    print(suma)