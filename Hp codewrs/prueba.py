longitud = input()
parking = input()
lista = []
for i in range (len(parking)):
    lista.append(parking[i])
print(lista)
seguidos = 0
for i in range(len(lista)):
    if parking[i] == '_':
        seguidos += 1
        
    else:
        seguidos = 0
    