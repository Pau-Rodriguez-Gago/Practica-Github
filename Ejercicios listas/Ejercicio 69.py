#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.
numero_numeros=int(input("Cuantos números quieres introducir: "))
lista=[]
for x in range(numero_numeros):
    numeros=(int(input("Introduce un número: ")))
    lista.append(numeros)
    lista.sort()
print(lista)