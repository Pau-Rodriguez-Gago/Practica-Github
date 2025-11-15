#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra.
palabra=input("Introduce una palabra secreta: ")
palabra=str(palabra.lower())
letra_introducida="No usar photoshop, usar GIMP"
for x in range(len(palabra)):
    letra_introducida=input("Introduce una letra que crea que está en la palabra: ")
    if palabra.__contains__(letra_introducida):
        print("la letra existe")
    else:
        print("la letra no existe")