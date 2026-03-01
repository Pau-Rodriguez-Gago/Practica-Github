num1_int1, num2_int1, num1_int2, num2_int2 = map(int, input().split())

mayor = max(num1_int1, num1_int2)
menor = min(num2_int1, num2_int2)

if mayor <= menor:
    print("[" + str(mayor) + "," + str(menor) + "]")
else:
    print("[]")
#Este ejercicio la verdad me costaba mucho sacarlo así que busqué en internet por soluciones.
#vi que se podía usar el map para saltarse el poner cada apartado de la lista en una variable en una sola línea
#Y, además con el max y min me ahorraba comprobar cual era el mayor y cual el menor y ver si un intervalo está contenido en otro.