#Operaciones básicas con dos números:
#para mostrar un número con dos decimales se usa format y (la variable y, ".2f")
num1= int(input("Introduce el primer número: "))
num2= int(input("Introduce el segundo número: "))
#El int es para que lo tome como número entero, y el float es para que lo tome como número decimal, el input es para que el usuario introduzca el valor
#en python los nombres de las variables no pueden llevar espacios
#las operaciones son: + - * / ** // %
#** es potencia
#// es cociente
#% es resto
suma= num1 + num2
resta= num1 - num2
multiplicacion= num1 * num2
division= num1 / num2
division_2decimales= format(division, '.2f')
exponente= num1 ** num2
cociente= num1 // num2
resto= num1 % num2
#para redondear un número se usa round(variable, número de decimales)
resto_2decimales= round(resto, 2)

#CONDICIONALES
#El if es para hacer una condición, si se cumple lo que hay después del if se ejecuta lo que hay debajo, si no se cumple no se ejecuta
if num1 > num2:
 print("El primer número es mayor que el segundo")
  #EL elif es para hacer una condición intermedia entre el if y el else, si se cumple lo que hay después del elif se ejecuta lo que hay debajo de si mismo
elif num1 == num2:
#El else es para hacer una condición contraria al if, si no se cumple lo que hay después del if se ejecuta lo que hay debajo del else
#else:
  print("El segundo número es mayor que el primero")
  #para que esté dentro del if, elif o else hay que ponerle una sangría (tabulador o 4 espacios)
#Math
 #Importar el math nos perimite usar la función math.pi para el valor de π y la raíz cuadrada con math.sqrt()
import math
raiz_cuadrada_num1= math.sqrt(num1)
raiz_cuadrada_num2= math.sqrt(num2)
#Con el if, los operadores son: > < >= <= == !=
#El == es para comparar si dos valores son iguales
#El != es para comparar si dos valores son diferentes

#los operadres lógicos son: and, or, not
#El and es para que se cumplan dos condiciones a la vez
#El or es para que se cumpla una de las dos condiciones
#El not es para que no se cumpla una condición
#Por ejemplo:
if num1 > 0 and num2 > 0:
    print("Los dos números son positivos")
if num1 > 0 or num2 > 0:
    print("Al menos uno de los dos números es positivo")
if not num1 > 0:
    print("El primer número no es positivo")

#El .isuper() es para saber si una letra es mayúscula
#Y el .islower() es para saber si una letra es minúscula
#El .isnumeric() es para saber si lo introducido es un número
#El .isalpha() es para saber si lo introducido es una letra
#El .isalnum() es para saber si lo introducido es una letra o un número
#El .isspace() es para saber si lo introducido es un espacio
#El .istitle() es para saber si lo introducido es una frase con la primera letra en mayúscula