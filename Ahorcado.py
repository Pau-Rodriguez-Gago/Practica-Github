import time
import sys
def escribir_lento(texto, retraso=0.05):
    for x in texto:
        sys.stdout.write(x)
        sys.stdout.flush()          
        time.sleep(retraso)
escribir_lento("Bienvenido a la nueva edición de AHORCADO", retraso=0.0275)
print()
escribir_lento("El único juego relacionado con el suicido que pueden jugar menores", retraso=0.0275)
print()
escribir_lento("En esta nueva edición de ahorcado, los errores se irán mostrando en forma de texto, y, cuando se complete la palabra ahorcado, te habrás quedado sin intentos.", retraso=0.0275)
print()
contador_partidas=0
otra_partida="S"
while otra_partida=="S" or otra_partida=="s" or otra_partida=="Si" or otra_partida=="SI" or otra_partida=="si" or otra_partida=="Sí" or otra_partida=="SÍ" or otra_partida=="sí":
    contador_partidas+=1
    if contador_partidas>1:
        print("Vaya vaya, así que con ganas de más eh... Por lo que parece, si mis datos no me engañan, esta es tu partida número",contador_partidas,".")
        if contador_partidas<5:
            print("No lleva ni 5 partidas caballero, le animamos a seguir disfrutando del juego :D.")
        if contador_partidas>=5 and contador_partidas<10:
            print("Bueno, ya es la partida número",contador_partidas,". Veo, que eres un apasionado del ahorcado! ¡Sigue así :D!")
        if contador_errores>=10:
            print("Emm... No es por ser aguafiestas pero... Deberías ir saliendo, dar tiempo a tus amigos, familía, respirar aire, salir de casa... Bueno, por mí sigue jugando tanto cuanto quieras.")
    lista_palabrasecreta=["gigante","arqueras","mago","cementerio","ballesta","mortero","golem","mosquetera","tronco","esqueleto"]
    lista_partida=[]
    lista_ahorcado=[]
    contador_errores=0
    otra_partida="S"
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
                otra_partida=input("¿Quieres jugar otra partida? (S/N): ")
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
                    print("¡Has perdido! La palabra era",palabra_escogida,".")
                    otra_partida=input("¿Quieres jugar otra partida? (S/N): ")
    if contador_errores==8:
        print("Que lástima estimado compañero, hasta la próxima... No olvide... EL 99% DE LOS JUGADORES DE AHORCADO SE RINDEN JUSTO ANTES DE SU VICTORIA...")
        print("¿Seguro que no quieres seguiiiiiir?? Anda, anímate...")
        otra_partida=input("Juega... Es tu última oportunidad... (S/N): ")
    if otra_partida not in ["S","s","Si","SI","si","Sí","SÍ","sí"]:
        print("Pues nada, tu lo has querido, nos vemos en la próxima :D.")
if contador_errores<8:
    print("Bueno, hasta aquí llegó tu partida, ganador, nos vemos en la próxima.")