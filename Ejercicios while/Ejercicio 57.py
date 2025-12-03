#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
numero=random.randint(1,5)
numero_intro=0
while not(numero==numero_intro):
    numero_intro=int(input("Introduce el número que crees que es: "))
    if numero_intro==numero:
     print("Número acertado")
    else:
       print("Número no acertado")