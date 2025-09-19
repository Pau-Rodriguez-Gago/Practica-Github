#Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
num1= int(input("Introduce el primer número (dividendo): "))
num2= int(input("Introduce el segundo número (divisor): "))
cociente= num1 // num2
resto= num1 % num2
if num1 % 2 == 0:
 paridad= "par"
else:
 paridad= "impar"
print("El cociente es: ",cociente)
print("El resto es: ",resto)
print("El dividendo es un número ",paridad)