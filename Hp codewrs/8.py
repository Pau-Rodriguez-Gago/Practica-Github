numeros = input()
lista = numeros.split(' ')
lista.sort()
lista_def = []
total = 0
for i in range(int(lista[len(lista) - 1]) - int(lista[0])):
    numero = int(lista[0]) + (i)
    lista_def.append(numero)
lista_def.remove(lista_def[0])
for i in lista_def:
    if not (str(i) in lista):
        total += i
print(total)