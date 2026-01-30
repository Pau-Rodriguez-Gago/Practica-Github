#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente. 
# 
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar        . PISTA.. ¿existe
#algún método que permita sumar el contenido de una lista? 
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
import random
valor_adivinado=""
puntos_ganados=0
puntos_totales=0
num_intento=0
partida_nueva="si"
media=0
partidas_jugadas=0
while partida_nueva=="si":
    import random
    valor_azar=random.choice(lista)
    while not valor_adivinado==valor_azar:
        valor_adivinado=input("Adivina la palabra que crees que es la seleccionada al azar de la lista: ")
        num_intento=num_intento+1
        if valor_adivinado==valor_azar:
            print("¡Enhorabuena! Has adivinado la palabra.")
            puntos_ganados=8 - (num_intento - 1)
            puntos_totales=puntos_totales + puntos_ganados
            partidas_jugadas=partidas_jugadas + 1
            partida_nueva=input("¿Quieres jugar otra partida? (si/no): ")
        else:
            print("La palabra no es correcta, inténtalo de nuevo.")
media=puntos_totales/partidas_jugadas
print("Ganaste un total de", puntos_totales, "puntos")
if media > 4:
    print("La suerte te acompaña con una media de:", media)
else:
    print("Mejor no te dediques a los juegos de azar, tu media es de:", media)