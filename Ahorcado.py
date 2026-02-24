lista_palabrasecreta=["gigante","arqueras","mago","cementerio","ballesta","mortero","golem","mosquetera","tronco","esqueleto"]
lista_partida=[]
lista_ahorcado=[]
contador_errores=0
import random
palabra_escogida=random.choice(lista_palabrasecreta)
for i in palabra_escogida:
    lista_partida.append(str("_"))
print(*lista_partida)
letra_escogida=input("Introduce una letra: ")
lista_partida=[]
for i in palabra_escogida:
    if letra_escogida==i:
        lista_partida.append(letra_escogida)
    else:
        lista_partida.append(str("_"))
while"_" in lista_partida:
    if letra_escogida in palabra_escogida:
        for i in range(len(palabra_escogida)):
            if letra_escogida==palabra_escogida[i]:
                lista_partida[i]=letra_escogida
        print("La letra está en la palabra")
        print(*lista_partida)
        if "_" not in lista_partida:
            print("¡Enhorabuena, has ganado!")
        else:
             letra_escogida=input("Sigue así, introduce tu siguiente letra: ")
    else:
        print("La letra no está en la palabra")
        print(*lista_partida)
        letra_escogida=input("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ")