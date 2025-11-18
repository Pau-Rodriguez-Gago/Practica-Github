import random
número=random.randint(1,20)
número_introducido=int(input("Introduce el número que crees: "))
contador=2
while not(número_introducido==número) and not(contador==0):
    print("El número no coincide")
    número_introducido=int(input("Introduce el número que ahora crees que es: "))
    contador=contador-1
if contador==0 and not(número==número_introducido):
    print("Te has quedado sin intentos")
else:
    print("EL NÚMERO ES CORRECTO")