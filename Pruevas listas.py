#Ejercicio guido 3, no estuve el día de los otros:
sinduplicados=[]
milista=[1,1,2,3,2,1,6,7,1]
sinduplicados=list(set(milista))
print(sinduplicados)
#Ejercicio 4
listanumeros=[]
listanonumeros=[]
listatodo=[]
frase=input("Introduce valores separados por un guión: ")
print(listatodo)
listatodo=frase.split("-")
print(listatodo)
for x in range(len(listatodo)):
    if listatodo[x].isnumeric():
        listanumeros.append(int(listatodo[x]))
    else:
        listanonumeros.append(listatodo[x])
print(listanumeros)
print(listanonumeros)