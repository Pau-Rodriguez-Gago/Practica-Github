#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.
numero=int(input("Introduce un número del que quieras ver su tabla de multiplicar: "))
numero_a_multiplicar=1
while not (numero_a_multiplicar>10) and not(numero*numero_a_multiplicar>=40):
    numero=numero*numero_a_multiplicar
    print(round(numero))
    numero=numero/numero_a_multiplicar
    numero_a_multiplicar=numero_a_multiplicar+1
print(round(numero*numero_a_multiplicar))
print("Fin del programa")