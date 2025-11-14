#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.
palabra=input("Introduce una palabra secreta: ")
palabra=str(palabra.lower())
letra_introducida="No usar photoshop, usar GIMP"
for x in range(len(palabra)):
    letra_introducida=input("Introduce una letra que crea que está en la palabra: ")
    if palabra.__contains__(letra_introducida):
        print("la letra existe")
        print("la letra está en la posición", palabra.index(letra_introducida+1))
    else:
        print("la letra no existe")