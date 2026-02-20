lista_palabrasecreta=["gigante","arqueras","mago","cementerio","ballesta","mortero","golem","mosquetera","tronco","esqueleto"]
lista_partida=[]
lista_ahorcado=[]
import random
palabra_escogida=random.choice(lista_palabrasecreta)
for i in palabra_escogida:
    lista_partida.append(str("_"))
print(*lista_partida)
letra_escogida=input("")
lista_partida=[]
palabra_completa="no"
while palabra_completa=="no":
    if letra_escogida in palabra_escogida:
        for i in palabra_escogida:
            if letra_escogida==i:
                lista_partida.append(letra_escogida)
            else:
                lista_partida.append(str("_"))
    else:
        print("La letra no está en la palabra")
    print(*lista_partida)
    letra_escogida=input("No te rindas tio, continua con tu siguiente letra: ")