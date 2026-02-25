print("Bienvenido a la nueva edición de AHORCADO")
print("El único juego relacionado con el suicido que pueden jugar menores.")
print("En esta nueva edición de ahorcado, los errores se irán mostrando en forma de texto, y, cuando se complete la palabra ahorcado, te habrás quedado sin intentos.")
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
lista_ahorcado=["A","H","O","R","C","A","D","O"]
for i in palabra_escogida:
    if letra_escogida==i:
        lista_partida.append(letra_escogida)
    else:
        lista_partida.append(str("_"))
while"_" in lista_partida and contador_errores<8:
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
        contador_errores+=1
        if contador_errores<=8:
            print("Uy uy uy, un error más, observa cuanto te queda hasta que se llene la palabra ahorcado... El fin se acerca...")
            if contador_errores==1:
                print(lista_ahorcado[0])
                print(*lista_partida)
                letra_escogida=input("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ")            
            elif contador_errores==2:
                print(lista_ahorcado[0],lista_ahorcado[1])
                print(*lista_partida)
                letra_escogida=input("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ")
            elif contador_errores==3:
                print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2])
                print(*lista_partida)
                letra_escogida=input("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ")    
            elif contador_errores==4:
                print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3])
                print(*lista_partida)
                letra_escogida=input("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ")
            elif contador_errores==5:
                print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3],lista_ahorcado[4])
                print(*lista_partida)
                letra_escogida=input("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ")            
            elif contador_errores==6:
                print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3],lista_ahorcado[4],lista_ahorcado[5])
                print(*lista_partida)
                letra_escogida=input("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ")
            elif contador_errores==7:
                print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3],lista_ahorcado[4],lista_ahorcado[5],lista_ahorcado[6])
                print(*lista_partida)
                letra_escogida=input("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ")
            elif contador_errores==8:
                print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3],lista_ahorcado[4],lista_ahorcado[5],lista_ahorcado[6],lista_ahorcado[7])
                print("¡Has perdido! La palabra era",palabra_escogida)