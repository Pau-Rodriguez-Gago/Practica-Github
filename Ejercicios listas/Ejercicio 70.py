#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.
numero_palabras=int(input("Cuantos números quieres introducir: "))
lista=[]
for x in range(numero_palabras):
    palabra=(int(input("Introduce una palabra: ")))
    lista.append(numeros)
    lista.sort()
print(lista)