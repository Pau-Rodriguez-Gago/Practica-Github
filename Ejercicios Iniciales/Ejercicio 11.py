#Realiza un programa que introduciendo el valor del lado de un cuadrado nos devuelva por pantalla en el área y el perímetro.
lado= float(input("Introduce el valor del lado del cuadrado: "))
area= lado * lado
perimetro= lado * 4
#Máximo dos decimales en el área y el perímetro
area= format(area, '.2f')
perimetro= format(perimetro, '.2f')
print("El área del cuadrado es: ",area)
print("El perímetro del cuadrado es: ",perimetro)