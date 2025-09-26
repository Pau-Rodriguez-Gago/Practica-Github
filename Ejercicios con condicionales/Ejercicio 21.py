#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a= int(input("Introduce el valor de a: "))
b= int(input("Introduce el valor de b: "))
c= int(input("Introduce el valor de c: "))
número_del_cual_sacamos_raíz= b**2 - 4*a*c
if número_del_cual_sacamos_raíz<0:
    print("La ecuación no tiene solución real")
else:
    raiz1= (-b + math.sqrt(número_del_cual_sacamos_raíz)) / (2*a)
    raiz2= (-b - math.sqrt(número_del_cual_sacamos_raíz)) / (2*a)
    print("Las soluciones son:",raiz1,"y",raiz2)

