n = int(input())
lista = []
for i in range(n):
    a = int(input())
    lista.append(a)
lista.sort()
intervalo = lista[len(lista) - 1] - lista[0]
if intervalo in lista:
    print(':)')
else:
    print(':(')