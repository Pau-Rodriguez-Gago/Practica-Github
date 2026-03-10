longitud = int(input())
parking = input()
lista = parking.split('X')
lista_def = []
parking_si_no="no"
puede = 0
while parking_si_no=="no":
    for i in lista:
        if len(i) == longitud and parking_si_no == 'no':
            puede = 1
            asteriscos = ''
            parking_si_no="si"
            for x in range(len(i)):
                asteriscos = asteriscos + '*'
            idx = lista.index(i)
            lista.pop(idx)
            lista.insert(idx, asteriscos)
if puede == 0:
    print(parking)
else:
    if parking[0]=="X":
        parking_final="X"
    else:
        parking_final=""

    for n in range(len(lista)):
        if parking[0]=="X":
            parking_final+=lista[n] + "X"
        else:
            parking_final+=lista[n] + "X"
    for i in range(len(parking_final)):
        lista_def.append(parking_final[i])
    lista_def.pop(len(lista_def) - 1)
    if parking_final[0] == 'X':
        lista_def.pop(0)
    salida = ''
    for i in range(len(lista_def)):
        salida += lista_def[i]

    print(salida)