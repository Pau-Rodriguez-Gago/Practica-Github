numeros=input()
numeros_espeiales=numeros.split()
if len(numeros_espeiales)==2:
    novia_pq_no_hay=input()
    tercer_numero_especial=input()
    suma=int(numeros_espeiales[0])+int(numeros_espeiales[1])+int(tercer_numero_especial)
    print(suma)
else:
    lista_num=numeros.split()
    suma=int(lista_num[0])+int(lista_num[1])+int(lista_num[2])
    print(suma)