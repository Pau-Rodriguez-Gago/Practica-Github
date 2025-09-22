#13.- Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.
lado= float(input("Introduce el valor del lado del cubo: "))
area= 6 * (lado ** 2)
volumen= lado ** 3
#Máximo dos decimales en el área y el volumen
area= format(area, '.2f')
volumen= format(volumen, '.2f')
print("El área del cubo es: ",area)
print("El volumen del cubo es: ",volumen)