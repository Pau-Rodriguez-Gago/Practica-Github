#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random
numero=random.randint(0,1000)
numero_intro=0
intentos_max=0
intentos_max=int(input("Itroduce la cantidad de intentos máximos que puedes llegara tener: "))
intentos_totales=0
while not(numero==numero_intro) and not (intentos_totales>=intentos_max):
    numero_intro=int(input("Introduce el número que crees que es: "))
    if numero_intro==numero:
     print("Número acertado")
    if numero_intro>numero:
     print("El número que has introducido es más grande que el secreto")
    if numero_intro<numero:
     print("El número que has introducido es más pequeño que el secreto")
    intentos_totales=intentos_totales+1
if intentos_totales>=intentos_max:
  print("Perdiste, te has quedado sin intentos")
else:
  print("Acertaste, y has usado",intentos_totales,"intentos")