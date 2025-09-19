#7.-Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
número_1= int(input("Introduce el primer operando: "))
número_2= int(input("Introduce el segundo operando: "))
Suma=número_1 + número_2
Resta=número_1 - número_2
Multiplicacion=número_1 * número_2
Division=número_1 / número_2
#format y (la variable y, ".2f") para que muestre 2 decimales
Division_2decimales= format(Division, '.2f')
#otra forma de hacerlo es con round(variable, número de decimales) pero redondea el número
Division_2decimales_redondeada= round(Division, 2)
Exponente=número_1 ** número_2
Cociente=número_1 // número_2
Resto=número_1 % número_2
print("El resultado de la suma es: ",Suma)
print("El resultado de la resta es: ",Resta)
print("El resultado de la multiplicación es: ",Multiplicacion)
print("El resultado de la división truncada a dos decimales es: ",Division_2decimales)
print("El resultado de la división redondeada a dos decimales es: ",Division_2decimales_redondeada)
print("El exponente es: ",Exponente)
print("El cociente es: ",Cociente)
print("El resto es: ",Resto)