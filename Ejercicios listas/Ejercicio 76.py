#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
letras=[]
numeros=[]
orden_letras="caca"
orden_num="pipi"
for x in lista1:
    if x.isdigit():
        numeros.append(x)
    if x.isalpha():
        letras.append(x)
letras.sort()
numeros.sort()
orden_num=input("Quieres mostrar los números en orden ascendente, (a), o descendente, (d)? ")
if orden_num=="a":
    numeros.sort()
    print(numeros)
else:
    numeros.reverse()
    print(numeros)
orden_letras=input("Quieres mostrar las letras en orden ascendente, (a), o descendente, (d)? ")
if orden_letras=="a":
    letras.sort()
    print(letras)
else:
    letras.reverse()
    print(letras)