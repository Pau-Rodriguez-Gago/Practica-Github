var_total=50
introducido=1
#Aquí inicio las variables, dándoles su valor correspondiente, pero
#IMPORTANTE, el valor de introducido no puede ser 0 ya que de ser así el while no se ejecutaría.
#por eso, le doy el valor de 1 por egemplo.
while not introducido==0 and not var_total>60:
    introducido=int(input("Introduce un valor: "))
    #Con esto, siempre que se cumplan las condiciones pedidas,
    #se seguirá pidiendo un número
    if introducido%2==0:
        var_total=var_total+introducido
    #Con esto, si el resto de diidir entre 2, es 0, entonces es para y se suma
    else:
        #Y, si no lo es entonces se resta porque será inpar
        var_total=var_total-introducido
    if not introducido==0 and not var_total>60:
        #Aquí importante añadir este condicional para que al introducir un 0 o el valor sea mayor a 60
        #Directamente se muestre fin del programa y no otra vez el valor además de esto.
        print(var_total)
    
print("Fin del programa")
#Y, finalmente muestro por pantalla fin del programa.