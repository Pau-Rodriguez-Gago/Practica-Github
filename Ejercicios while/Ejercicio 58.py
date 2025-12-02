#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
numero=random.randint(1,5)
numero_intro=0
vidas=3
while not(numero==numero_intro) and not(vidas==0):
    numero_intro=int(input("Introduce el número que crees que es: "))
    if numero_intro==numero:
     print("Número acertado")
    else:
       print("Número no acertado")
    vidas=vidas-1