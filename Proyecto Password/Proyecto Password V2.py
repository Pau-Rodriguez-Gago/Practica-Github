print("INSTRUCCIONES PARA REALIZAR TU CONTRASEÑA PERFECTA")
print("1.Debe contener un número entre el 0 y el 3")
print("2.Debe contener un número entre el 4 y el 6")
print("3.Debe contener un número entre el 7 y el 9")
print("4.Debe contener como mínimo dos letras mayúsculas y una minúscula.")
print("5.Debe contener un mínimo de 2 símbolos de entre estos /,!,¿,?,¡,+,-,@")
print("6.No debe contener dos letras, números o símbolos, seguidos.")
print("7.Debe contener un mínimo de 12 caracteres")
#Aquí simplemente muestro las instrucciones para el usuario
#He decidio dividir los rangos de números del 0 al 9 de forma equitativa más o menos, 0-3,4-6,7-9.
#Para aplicar las mayúsculas y minúsculas, con 3 letras ya he considerado suficiente pero, puestos a escoger, 
#considero que las mayúsculas al ser usadas en menor medida, pues es mejor ponerlas más veces que las minúsculas.
#Intenté respecto a los símbolos, que se pudiera escribir cualquiera con if not(x.isnumeric() and not(x.isalpha()),
#Pero por algun motivo no fucnionaba correctamente, así que puse una lista con los símbolos permitidos.
#Respecto a la norma 6; esta no venía demandada en el propio docuemnto pero pensé que esto haría la contraseña mucho más segura al
#ser poco común a pesar de reducir la facilidad con la que una la puede recordar. Aun y así, sobretodo, decidí
#intentar hacerlo como un reto personal para ver si era capaz de programarlo.
#Y, por último, la longitud mínima de 12 caracteres, ya que cuanto más larga es una contraseña, y como estándar una contraseña
#suele tener almenos 8 caracteres pero con 12, es mucho más segura.
password="inicializada"
contador_cero_tres=0
contador_cuatro_seis=0
contador_siete_nueve=0
contador_letras_mayus=0
contador_letras_minus=0
contador_simbolos=0
numero_seguido=0
veces_que_hay_numero_seguido=0
letra_seguida=0
veces_que_hay_letra_seguida=0
simbolo_seguido=0
veces_que_hay_simbolo_seguido=0
password_perfecto="sí"
otro_password="s"
passwords_restantes=3
passwords_correctos=0
passwords_incorrectos=0
#Inicializo las variables que van a ser utilizadas.
while otro_password=="s" and not (passwords_restantes==0):
    #Con este while busco que el usuario pueda introducir las contraseñas que quiera hasta un máximo de 3.
    password=input("Introduce una contraseña: ")
    password_perfecto="sí"
    contador_cero_tres=0
    contador_cuatro_seis=0
    contador_siete_nueve=0
    contador_letras_mayus=0
    contador_letras_minus=0
    contador_simbolos=0
    numero_seguido=0
    veces_que_hay_numero_seguido=0
    letra_seguida=0
    veces_que_hay_letra_seguida=0
    simbolo_seguido=0
    veces_que_hay_simbolo_seguido=0
    #Esto es muy importante y me costó darme cuenta, aquí, vuelvo a inicializar todas las variables excepto los intentos restantes
    #y las contraseñas correctas e incorrectas, así, evito que se acumulen los de una contraseña con la siguiente.
    #Hasta que no me dí cuenta, ya poniendo los resultados, si primero ponía una contraseña y luego una distinta,
    #no se comprovaba bien y directamete me preguntaba ya si quería introducir otra contraseña.
    if len(password)<12:
        print("Error, su contraseña tiene un total de",len(password),"caracteres y no llega a los 12 requeridos.")
        password_perfecto="no"
    #Aquí no añado un else porque quiero que, aunque la contraseña no tenga la longitud mínima, el usuario pueda saber si
    #tiene algo más mal. Porque odio que me digan solo que debo escribir más para luego volverme ha decir que otra cosa está mal.
    for x in password:
        if x.isdigit():
            numero_seguido=numero_seguido+1
            letra_seguida=0
            simbolo_seguido=0
            if int(x)>=0 and int(x)<=3:
                contador_cero_tres=contador_cero_tres+1
            if int(x)>=4 and int(x)<=6:
                contador_cuatro_seis=contador_cuatro_seis+1
            if int(x)>=7 and int(x)<=9:
                contador_siete_nueve=contador_siete_nueve+1
        if x.isupper():
            letra_seguida=letra_seguida+1
            numero_seguido=0
            simbolo_seguido=0 
            contador_letras_mayus=contador_letras_mayus+1
        if x.islower():
                contador_letras_minus=contador_letras_minus+1
                letra_seguida=letra_seguida+1
                numero_seguido=0
                simbolo_seguido=0 
        if x in ["/","!","¿","?","¡","+","-","@"]:
            simbolo_seguido=simbolo_seguido+1
            letra_seguida=0
            numero_seguido=0
            contador_simbolos=contador_simbolos+1
        if numero_seguido==2:
            veces_que_hay_numero_seguido=veces_que_hay_numero_seguido+1
            numero_seguido=0
        if letra_seguida==2:
            veces_que_hay_letra_seguida=veces_que_hay_letra_seguida+1
            letra_seguida=0
        if simbolo_seguido==2:
            veces_que_hay_simbolo_seguido=veces_que_hay_simbolo_seguido+1
            simbolo_seguido=0
            #Con todo esto, si hay algun carácter repetido, se reinicia el contador y se suma 1 a las veces que hay repetidos.
    if not(contador_cero_tres>=1):
        print("La contraseña necesita al menos un número entre el 0 y el 3.")
        password_perfecto="no"
    if not(contador_cuatro_seis>=1):
        print("La contraseña necesita al menos un número entre el 4 y el 6.")
        password_perfecto="no"
    if not(contador_siete_nueve>=1):
        print("La contraseña necesita al menos un número entre el 7 y el 9.")
        password_perfecto="no"
    if not(contador_letras_mayus>=2):
        print("La contraseña debe incluir un mínimo de dos letras mayúsculas.")
        password_perfecto="no"
    if not(contador_letras_minus>=1):
        print("La contraseña debe incluir al menos una letra minúscula.")
        password_perfecto="no"
    if not(contador_simbolos>=2):
        print("La contraseña debe incluir un mínimo de dos símbolos de entre estos /,!,¿,?,¡,+,-,@")
        password_perfecto="no"
    if not(veces_que_hay_letra_seguida==0):
        print("La contraseña no debe tener dos letras seguidas, usted ha introducido dos letras seguidas en:",veces_que_hay_letra_seguida,"ocasiones.")
        password_perfecto="no"
    if not(veces_que_hay_numero_seguido==0):
        print("La contraseña no debe tener dos números seguidos, usted ha introducido dos números seguidos en:",veces_que_hay_numero_seguido,"ocasiones.")
        password_perfecto="no"
    if not(veces_que_hay_simbolo_seguido==0):
        print("La contraseña no debe tener dos símbolos seguidos, usted ha introducido dos símbolos seguidos en:",veces_que_hay_simbolo_seguido,"ocasiones.")
        password_perfecto="no"
        #Con todo esto, si las variables me dicen que alguna de las condiciones no se cumple, muestro el error que hay
        #cómo mejorarlo y, además, hago que el programa sepa que la contraseña actual ya no es correcta.
    if password_perfecto=="sí":
        print("Tu contraseña es correcta!")
        passwords_correctos=passwords_correctos+1
        #Aquí simplemente muestro el mensaje de contraseña correcta y sumo 1 a las contraseñas correctas.
    else:
        passwords_incorrectos=passwords_incorrectos+1
    passwords_restantes=passwords_restantes-1
    otro_password=input("Quieres añadir otra contraseña? s/n: ")
if passwords_restantes==0 and otro_password=="s":
    print("Lo siento, pero aunque quieras seguir, te has quedado sin intentos.")
print("Has introducido",passwords_correctos,"contraseñas correctas.")
print("Y has introducido",passwords_incorrectos,"contraseñas incorrectas.")
#Pruebas:
#Entrada:                                         Salida:
#1A5B8c/7B@c9K+                                   Tu contraseña es correcta!
#3l6P7h@G0+d5                                     Tu contraseña es correcta!
#E¿3f-6G!7H@4                                     Tu contraseña es correcta!
#M!2q@5Z?8R+1                                     Tu contraseña es correcta!
#H¡0x?4P+7N/5                                     Tu contraseña es correcta!
#4a9D2f/1J@3                                      Error, su contraseña tiene un total de 11 caracteres y no llega a los 12 requeridos.
#1234abcABC!?                                     La contraseña necesita al menos un número entre el 7 y el 9.
#                                                 La contraseña no debe tener dos letras seguidas, usted ha introducido dos letras seguidas en: 3 ocasiones.
#                                                 La contraseña no debe tener dos números seguidos, usted ha introducido dos números seguidos en: 2 ocasiones.
#                                                 La contraseña no debe tener dos símbolos seguidos, usted ha introducido dos símbolos seguidos en: 1 ocasiones.
#M!2q@5ZZ?8R+1                                    La contraseña no debe tener dos letras seguidas, usted ha introducido dos letras seguidas en: 1 ocasiones.
#Q?2M/5Z?7P+3                                     La contraseña debe incluir al menos una letra minúscula.
#0t5/9@3+1-6!                                     La contraseña debe incluir un mínimo de dos letras mayúsculas.
#03@b/Y4S9+8Q                                     La contraseña no debe tener dos números seguidos, usted ha introducido dos números seguidos en: 1 ocasiones.

#EXTRA:
#Se que es un código bastante largo, y con muchas condicones, pero he querido dificultarmelo, y aunque por egemplo
#lo de los números seguidos no venía en el enunciado, le he puesto tiempo y logré que funcionase.