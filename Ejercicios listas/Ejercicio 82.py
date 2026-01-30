#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra 
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
valor_adivinado=""
import random
valor_azar=random.choice(lista)
while not valor_adivinado==valor_azar:
    valor_adivinado=input("Adivina la palabra que crees que es la seleccionada al azar de la lista: ")
    if valor_adivinado==valor_azar:
        print("¡Enhorabuena! Has adivinado la palabra.")
    else:
        print("La palabra no es correcta, inténtalo de nuevo.")
