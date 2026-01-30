#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la
#palabra secreta.  El usuario tendrá 3 oportunidades para adivinar la palabra.
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
intentos=0
palabra_introducida=""
palabra_correcta="n"
import random
palabra_azar=random.choice(lista)
letras=list(palabra_azar)
random.shuffle(letras)
palabra_desordenada="".join(letras)
print("La palabra desordenada es: ",palabra_desordenada)
while intentos<3 and palabra_correcta=="n":
    palabra_introducida=input("Adivina la palabra: ")
    intentos=intentos+1
    if palabra_introducida==palabra_azar:
        print("¡Enhorabuena! Has adivinado la palabra.")
        intentos=intentos+1
        palabra_correcta="s"
    else:
        print("Esa no es la palabra correcta.")
        intentos=intentos+1
if intentos==3:
    print("Has agotado tus intentos. La palabra correcta era:", palabra_azar)