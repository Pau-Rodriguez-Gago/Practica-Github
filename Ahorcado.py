import time
import sys
import winsound
import os
musica="s"
hay_guardado="Guardado ahorcado.txt"
winsound.Beep(787,300)
winsound.Beep(787,300)
winsound.Beep(1375,500)
winsound.Beep(1080,300)
winsound.Beep(984,300)
winsound.Beep(898,350)
winsound.Beep(787,300)
winsound.Beep(730,300)
winsound.Beep(787,300)
winsound.Beep(984,300)
def escribir_lento(texto, retraso=0.05):
    for x in texto:
        sys.stdout.write(x)
        winsound.Beep(500,20)
        sys.stdout.flush()  
        time.sleep(retraso)
def input_lento(texto, retraso=0.05):
    import time
    for x in texto:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(retraso)
    return ""
escribir_lento("Bienvenido a la nueva edición de AHORCADO", retraso=0.0275)
print()
cronómetro_s_n="n"
escribir_lento("El único juego relacionado con el suicido que pueden jugar menores", retraso=0.0275)
print()
escribir_lento("En esta nueva edición de ahorcado, los errores se irán mostrando en forma de texto, y, cuando se complete la palabra ahorcado, te habrás quedado sin intentos.", retraso=0.0275)
print()
escribir_lento("Además consta de una nueva característica ideal para los speedrunners y amantes de los records, un cronómetro.", retraso=0.0275)
print()
escribir_lento("Si activas la opción del cronómetro, al empezar una de tus partidas, este se activará y al final de esta, podrás ver el tiempo que te ha tomado.", retraso=0.0275)
print()
cronómetro_s_n=input(input_lento("¿Quieres usar el modo cronómetro? S/N: ", retraso=0.0275))
if cronómetro_s_n in ["S","s","Sí","Si","sí","si","SI","SÍ"]:
     cronómetro=time.time()
lista_palabrasecreta=["gigante","arqueras","mago","cementerio","ballesta","mortero","golem","mosquetera","tronco","esqueleto"]
contador_partidas=0
otra_partida="S"
while otra_partida=="S" or otra_partida=="s" or otra_partida=="Si" or otra_partida=="SI" or otra_partida=="si" or otra_partida=="Sí" or otra_partida=="SÍ" or otra_partida=="sí":
    contador_partidas+=1
    ver_guardado_sn=input(input_lento("Antes de continuar con el juego, ¿le gustaría visualizar los datos de la partida que guardó anteriormente? S/N: "))
    if ver_guardado_sn in ["S","s","Sí","Si","sí","si","SI","SÍ"]:
         if os.path.exists(hay_guardado):
            escribir_lento("Bien, a continuación le muestro los datos de su tan preciada última partida guardada.")
            def leer_datos_guardaos():
                   archivo_lectura=open('Guardado ahorcado.txt','r')
                   filas_texto=archivo_lectura.readlines()
                   for x in filas_texto:
                        if x==1:
                            escribir_lento("La partida que guardaste fue jugada durante el "+str(x.strip())+".")
                        if x==2:
                            escribir_lento("Acabaste en esta hora:  "+str(x.strip())+".")
                        if x==3:
                             escribir_lento("La palabra escogida en la partida fue: "+str(x.strip()))
                        if x==4:
                             escribir_lento("Introduciste un total de "+str(x.strip())+" letras diferentes que fueron correctas.")
                        if x==5:
                             escribir_lento("Y, introduciste un total de "+str(x.strip())+" letras diferentes que fueron incorrectas.")
            leer_datos_guardaos()
         else:
            escribir_lento("Oye oye, a mi no me intentes engañar, todavía no has guardado ninguna partida.",retraso=0.0275)
            print()
            escribir_lento("Si tantas ganas tienes de ver algo guardado, no pierdas tiempo y empieza ya a jugar! :D",retraso=0.0275)
            print()
    if contador_partidas>1 and cronómetro_s_n in ["S","s","Sí","Si","sí","si","SI","SÍ"]:
         cronómetro=time.time()
    lista_letras_introducidas=[]
    lista_letras_repetidas=[]
    lista_letras_incorrectas=[]
    lista_letras_correctas=[]
    otra_palabra="n"
    palabra_añadida=""
    if contador_partidas>1:
        escribir_lento("Vaya vaya, así que con ganas de más eh... Por lo que parece, si mis datos no me engañan, esta es tu partida número "+str(contador_partidas)+".", retraso=0.0275)
        print()
        if contador_partidas<5:
            escribir_lento("No lleva ni 5 partidas caballero, le animamos a seguir disfrutando del juego :D.", retraso=0.0275)
            print()
        if contador_partidas>=5 and contador_partidas<10:
            escribir_lento("Bueno, ya es la partida número "+str(contador_partidas)+". Veo, que eres un apasionado del ahorcado! ¡Sigue así :D!", retraso=0.0275)
            print()
        if contador_errores>=10:
            escribir_lento("Emm... No es por ser aguafiestas pero... Deberías ir saliendo, dar tiempo a tus amigos, familía, respirar aire, salir de casa... Bueno, por mí sigue jugando tanto como quieras..", retraso=0.0275)
            print()
    if contador_partidas>1:
        otra_palabra=input(input_lento("¿Quieres añadir una palabra a las que pueden salir en el juego? S/N: ", retraso=0.0275))
        if otra_palabra in ["S","s","Sí","Si","sí","si","SI","SÍ"]:
            palabra_añadida=input(input_lento("Vaya, así que, otra palabra es, entonces, escribela justo aquí: ", retraso=0.0275))
            lista_palabrasecreta.append(palabra_añadida)
    lista_partida=[]
    lista_ahorcado=[]
    contador_errores=0
    otra_partida="S"
    import random
    palabra_escogida=random.choice(lista_palabrasecreta)
    lista_palabrasecreta.remove(palabra_escogida)
    for i in palabra_escogida:
        lista_partida.append(str("_"))
    print(*lista_partida)
    letra_escogida=input(input_lento("Introduce una letra: ", retraso=0.0275))
    while letra_escogida in lista_letras_introducidas:
        escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
        print()
        lista_letras_repetidas.append(letra_escogida)
        letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275))
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
            escribir_lento("La letra está en la palabra", retraso=0.0275)
            print()
            lista_letras_correctas.append(letra_escogida)
            lista_letras_introducidas.append(letra_escogida)
            print(*lista_partida)
            if "_" not in lista_partida:
                escribir_lento("¡Enhorabuena, has ganado!", retraso=0.0275)
                print()
                escribir_lento("En esta partida, introduciste un total de "+str(len(lista_letras_introducidas))+" letras diferentes.", retraso=0.0275)
                print()
                escribir_lento("De las cuales "+str(len(lista_letras_correctas))+" fueron correctas.", retraso=0.0275)
                print()
                escribir_lento("Y "+str(len(lista_letras_incorrectas))+" fueron incorrectas.", retraso=0.0275)
                print()
                escribir_lento("Y repetiste alguna letra en un total de "+str(len(lista_letras_repetidas))+" ocasiones.", retraso=0.0275)
                print()
                if cronómetro_s_n in ["S","s","Sí","Si","sí","si","SI","SÍ"]:
                    cronómetro_final=(round(time.time()-cronómetro,2))
                    min=round(int(cronómetro_final)//60,2)
                    sec=cronómetro_final%60
                    escribir_lento("Y, ha durado "+str(min)+" minuto/s y "+str(sec)+" segundos.", retraso=0.0275)
                    print()
                guardar_datos_sn=input(input_lento("Que gran partida! ¿Te gustaría guardar los datos de esta última partida para poder verlos más tarde? S/N: ",retraso=0.0275))
                print()
                if guardar_datos_sn in ["S","s","Sí","Si","sí","si","SI","SÍ"]:
                    def guardar():
                        archivo=open('Guardado ahorcado.txt','w')
                        archivo.write(str(time.strftime("%Y-%m-%d")+'\n'))
                        archivo.write(str(time.strftime('%H-%M-%S'))+'\n')
                        archivo.write(str(palabra_escogida)+'\n')
                        archivo.write(str(len(lista_letras_correctas))+'\n')
                        archivo.write(str(len(lista_letras_incorrectas))+'\n')
                        archivo.close()
                    guardar()
                otra_partida=input(input_lento("¿Quieres jugar otra partida? (S/N): ", retraso=0.0275))
            else:
                letra_escogida=input(input_lento("Sigue así, introduce tu siguiente letra: ", retraso=0.0275))
                while letra_escogida in lista_letras_introducidas:
                        escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
                        print()
                        lista_letras_repetidas.append(letra_escogida)
                        letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275))
        else:
            escribir_lento("La letra no está en la palabra", retraso=0.0275)
            print()
            lista_letras_incorrectas.append(letra_escogida)
            lista_letras_introducidas.append(letra_escogida)
            contador_errores+=1
            if contador_errores<=8:
                escribir_lento("Uy uy uy, un error más, observa cuanto te queda hasta que se llene la palabra ahorcado... El fin se acerca...", retraso=0.0275)
                print()
                if contador_errores==1:
                    print(lista_ahorcado[0])
                    print(*lista_partida)
                    letra_escogida=input(input_lento("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ", retraso=0.0275))
                    while letra_escogida in lista_letras_introducidas:
                            escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
                            print()
                            lista_letras_repetidas.append(letra_escogida)
                            letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275))            
                elif contador_errores==2:
                    print(lista_ahorcado[0],lista_ahorcado[1])
                    print(*lista_partida)
                    letra_escogida=input(input_lento("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ", retraso=0.0275))
                    while letra_escogida in lista_letras_introducidas:
                        escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
                        print()
                        lista_letras_repetidas.append(letra_escogida)
                        letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275))
                elif contador_errores==3:
                    print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2])
                    print(*lista_partida)
                    letra_escogida=input(input_lento("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ", retraso=0.0275))
                    while letra_escogida in lista_letras_introducidas:
                            escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
                            print()
                            lista_letras_repetidas.append(letra_escogida)
                            letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275))
                elif contador_errores==4:
                    print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3])
                    print(*lista_partida)
                    letra_escogida=input(input_lento("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ", retraso=0.0275))
                    while letra_escogida in lista_letras_introducidas:
                            escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
                            print()
                            lista_letras_repetidas.append(letra_escogida)
                            letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275)) 
                elif contador_errores==5:
                    print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3],lista_ahorcado[4])
                    print(*lista_partida)
                    letra_escogida=input(input_lento("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ", retraso=0.0275))
                    while letra_escogida in lista_letras_introducidas:
                            escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
                            print()
                            lista_letras_repetidas.append(letra_escogida)
                            letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275))
                elif contador_errores==6:
                    print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3],lista_ahorcado[4],lista_ahorcado[5])
                    print(*lista_partida)
                    letra_escogida=input(input_lento("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ", retraso=0.0275))
                    while letra_escogida in lista_letras_introducidas:
                            escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
                            print()
                            lista_letras_repetidas.append(letra_escogida)
                            letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275))
                elif contador_errores==7:
                    print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3],lista_ahorcado[4],lista_ahorcado[5],lista_ahorcado[6])
                    print(*lista_partida)
                    letra_escogida=input(input_lento("No te rindas tio, esa letra no era correcta, continua con tu siguiente letra: ", retraso=0.0275))
                    while letra_escogida in lista_letras_introducidas:
                            escribir_lento("Oye, esa letra que acabas de poner, ya la has intentado antes, ten un poco más de cuidado!",retraso=0.0275)
                            print()
                            lista_letras_repetidas.append(letra_escogida)
                            letra_escogida=input(input_lento("Introduce otra letra, y esta vez, a ser posible, que no esté repetida: ", retraso=0.0275))
                elif contador_errores==8:
                    print(lista_ahorcado[0],lista_ahorcado[1],lista_ahorcado[2],lista_ahorcado[3],lista_ahorcado[4],lista_ahorcado[5],lista_ahorcado[6],lista_ahorcado[7])
                    escribir_lento("¡Has perdido! La palabra era: "+palabra_escogida, retraso=0.0275)
                    print()
                    escribir_lento("En esta partida, introduciste un total de "+str(len(lista_letras_introducidas))+" letras diferentes.", retraso=0.0275)
                    print()
                    escribir_lento("De las cuales "+str(len(lista_letras_correctas))+" fueron correctas.", retraso=0.0275)
                    print()
                    escribir_lento("Y "+str(len(lista_letras_incorrectas))+" fueron incorrectas.", retraso=0.0275)
                    print()
                    escribir_lento("Repetiste alguna letra en un total de "+str(len(lista_letras_repetidas))+" ocasiones.", retraso=0.0275)
                    print()
                    if cronómetro_s_n in ["S","s","Sí","Si","sí","si","SI","SÍ"]:
                        cronómetro_final=(round(time.time()-cronómetro,2))
                        min=round(int(cronómetro_final)//60,2)
                        sec=cronómetro_final%60
                        escribir_lento("Y, ha durado "+str(min)+" minuto/s y "+str(sec)+" segundos.", retraso=0.0275)
                        print()
                        guardar_datos_sn=input(input_lento("Que gran partida! ¿Te gustaría guardar los datos de esta última partida para poder verlos más tarde? S/N: ",retraso=0.0275))
                        print()
                        def guardar():
                            archivo=open('Guardado ahorcado.txt','w')
                            archivo.write(str(time.strftime("%Y-%m-%d")+'\n'))
                            archivo.write(str(time.strftime('%H-%M-%S'))+'\n')
                            archivo.write(str(palabra_escogida)+'\n')
                            archivo.write(str(len(lista_letras_correctas))+'\n')
                            archivo.write(str(len(lista_letras_incorrectas))+'\n')
                            archivo.close()
                        guardar()
                    otra_partida=input(input_lento("¿Quieres jugar otra partida? (S/N): ", retraso=0.0275))
    if contador_errores==8 and not otra_partida in ["S","s","Sí","Si","sí","si","SI","SÍ"]:
        escribir_lento("Que lástima estimado compañero, hasta la próxima... No olvide... EL 99% DE LOS JUGADORES DE AHORCADO SE RINDEN JUSTO ANTES DE SU VICTORIA...", retraso=0.0275)
        print()
        escribir_lento("¿Seguro que no quieres seguiiiiiir?? Anda, anímate...", retraso=0.0275)
        print()
        otra_partida=input(input_lento("Juega... Es tu última oportunidad... (S/N): ", retraso=0.0275))
        if otra_partida not in ["S","s","Si","SI","si","Sí","SÍ","sí"]:
            escribir_lento("Pues nada, tu lo has querido, nos vemos en la próxima :D.", retraso=0.0275)
            print()
if contador_errores<8:
    escribir_lento("Bueno, hasta aquí llegó tu partida, ganador, nos vemos en la próxima.", retraso=0.0275)
    print()