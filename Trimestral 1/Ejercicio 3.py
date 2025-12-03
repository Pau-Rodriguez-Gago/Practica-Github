numero=0
numero_cifras=0
numero_cifras=int(input("Introduce un número de cifras: "))
suma_cifras=0
numero=int(input("Introduce un número con esa cantidad de cifras: "))
#Inicializo ls variables y pido que se introduzcan por teclado las que así lo requieren
if len(str(numero))==numero_cifras:
    #Aquí entra en juego una parte crucuial para el programa pues comparo
    #la longitud del numero con la de las cifras que quermos que haya
    #pero esto no es tan sencillo pues debemos acordarnos de que la variable
    #numero no está como un string, sino como un valor numérico.
    #Y, si queremos que el comando leng() funcione adecuadamente debemos
    #pasar numero a: str(numero)
    for x in str(numero):
        #Aquí sucede lo mismo, y es que, para que el for pueda i pasando por 
        #las cifras del número, esta variable debe ser un string
        suma_cifras=suma_cifras+int(x)
        #Y, por último para asegurarme de que se sume adecuadamente
        #convierto el valor de x que en este caso tendrá el numero que
        #se encuentra en la posición que se esté comprovando gracias al for
        # en un valor numérico con: int(x)
    print("Resultado:",suma_cifras)
    #también es importante que el print se encuentre dentro del if pero fuera del for
    #con esto logramos que el resultado se muestre pero no cada vez que introducimos
    #un número.
else:
    print("Error, no coincide el número de cifras")
    #Y, finalmente muestro por pantalla. si el numero no coincide con la cantidad
    #de cifras