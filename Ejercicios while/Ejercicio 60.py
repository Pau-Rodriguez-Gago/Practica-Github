#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while
numero=int(input("Introduce un número del que quieras ver su tabla de multiplicar: "))
numero_a_multiplicar=1
while not (numero_a_multiplicar>10):
    numero=numero*numero_a_multiplicar
    print(round(numero))
    numero=numero/numero_a_multiplicar
    numero_a_multiplicar=numero_a_multiplicar+1