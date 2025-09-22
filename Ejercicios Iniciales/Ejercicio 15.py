#15.- Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio= float(input("Introduce el valor del radio del cilindro: "))
altura= float(input("Introduce el valor de la altura del cilindro: "))
area= 2 * math.pi * radio * (radio + altura)
volumen= math.pi * (radio ** 2) * altura
#Máximo dos decimales en el área y el volumen
area= format(area, '.2f')
volumen= format(volumen, '.2f')
print("El área del cilindro es: ",area)
print("El volumen del cilindro es: ",volumen)