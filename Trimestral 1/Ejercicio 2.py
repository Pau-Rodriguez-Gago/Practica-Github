numero=0
total_positivos=0
total_negativos=0
#Inicializo las variables una para el numero introducido y otras dos para la suma
#total de los números pares e impares por separado todas ellas con valores numéricos
for x in range(6):
    #Aquí utilizo el in range (6) aunque también serviría, in range(0,6)
    #Esto sirve para que así se pida el numero un total de 6 veces
    numero=int(input("Introduce un numero: "))
    if numero>0:
        #Así, si el número es mayor que cero, es positivo, y se suma al total
        total_positivos=total_positivos+numero
    else:
        #Y, para ver si es negativo podemos usar un else, pues, si no es positivo
        #será negativo
        total_negativos=total_negativos+numero
print("Suma de números positivos:",total_positivos)
print("Suma de números negativos:",total_negativos)
#Finalmente lo muestro por pantalla
#Además, como añadido explicatorio, el 0 en este programa no se tiene en cuenta
#pero no afectaría en nada pues al ser 0, no añadiría ni restaría valor a la suma total