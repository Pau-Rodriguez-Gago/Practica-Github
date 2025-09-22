#12.-Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado= float(input("Introduce el valor del lado del trapecio: "))
base_menor= float(input("Introduce el valor de la base menor del trapecio: "))
base_mayor= float(input("Introduce el valor de la base mayor del trapecio: "))
altura= float(input("Introduce el valor de la altura del trapecio: "))
area= ((base_menor + base_mayor) * altura) / 2
perimetro= (2 * lado) + base_menor + base_mayor
#Máximo dos decimales en el área y el perímetro para facilitar el proceso
area= format(area, '.2f')
perimetro= format(perimetro, '.2f')
print("El área del trapecio es: ",area)
print("El perímetro del trapecio es: ",perimetro)
