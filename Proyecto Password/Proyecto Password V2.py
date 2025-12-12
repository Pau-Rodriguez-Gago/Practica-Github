print("INSTRUCCIONES PARA REALIZAR TU CONTRASEÑA PERFECTA")
print("1.Debe contener un número entre el 0 y el 3")
print("2.Debe contener un número entre el 4 y el 6")
print("3.Debe contener un número entre el 7 y el 9")
print("4.Debe contener como mínimo dos letras mayúsculas y una minúscula.")
print("5.Debe contener un mínimo de 2 símbolos a excepción de una coma, un punto o un espacio.")
print("6.No debe contener dos letras, números o símbolos, seguidos.")
print("7.Debe contener un mínimo de 12 caracteres")
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
while otro_password=="s" and not (passwords_restantes==0):
    password=input("Introduce una contraseña: ")
    if len(password)<12:
        print("Error, su contraseña tiene un total de",len(password),"caracteres y no llega a los 12 requeridos.")
    for x in password:
        if x.isnumeric():
            numero_seguido=numero_seguido+1
            if int(x)>=0 and int(x)<=3:
                contador_cero_tres=contador_cero_tres+1
            if int(x)>=4 and int(x)<=6:
                contador_cuatro_seis=contador_cuatro_seis+1
            if int(x)>=7 and int(x)<=9:
                contador_siete_nueve=contador_siete_nueve+1
        if x.isalpha():
            letra_seguida=letra_seguida+1    
            if str(x).isupper():
                contador_letras_mayus=contador_letras_mayus+1
            if str(x).islower():
                contador_letras_minus=contador_letras_minus+1
        if not(x.isalnum()) and not(x==" " or x=="." or x==","):
            contador_simbolos=contador_simbolos+1
            simbolo_seguido=simbolo_seguido+1
        if numero_seguido==2:
            veces_que_hay_numero_seguido=veces_que_hay_numero_seguido+1
            numero_seguido=0
        if letra_seguida==2:
            veces_que_hay_letra_seguida=veces_que_hay_letra_seguida+1
            letra_seguida=0
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
        print("La contraseña debe incluir un mínimo de dos símbolos que no sean ni una coma ni un punto ni un espacio")
        password_perfecto="no"
    if not(veces_que_hay_letra_seguida==0):
        print("La contrseña no debe tener dos letras seguidas, usted ha introducido dos letras seguidas en:",veces_que_hay_letra_seguida,"ocasiones.")
        password_perfecto="no"
    if not(veces_que_hay_numero_seguido==0):
        print("La contrseña no debe tener dos números seguidos, usted ha introducido dos números seguidos en:",veces_que_hay_numero_seguido,"ocasiones.")
        password_perfecto="no"
    if not(veces_que_hay_simbolo_seguido==0):
        print("La contrseña no debe tener dos símbolos seguidos, usted ha introducido dos símbolos seguidos en:",veces_que_hay_simbolo_seguido,"ocasiones.")
        password_perfecto="no"
    if password_perfecto=="sí":
        print("Tu contraseña es correcta!")
        passwords_correctos=passwords_correctos+1
    else:
        passwords_incorrectos=passwords_incorrectos+1
    passwords_restantes=passwords_restantes-1
    otro_password=input("Quieres añadir otra contraseña? s/n: ")
    veces_que_hay_numero_seguido=0
    veces_que_hay_letra_seguida=0
    veces_que_hay_simbolo_seguido=0
    numero_seguido=0
    letra_seguida=0
    simbolo_seguido=0
if passwords_restantes==0 and otro_password=="s":
    print("lo siento, pero aunque quieras seguir, te has quedado sin intentos.")
print("Has introducido",passwords_correctos,"contraseñas correctas.")
print("Y has introducido",passwords_incorrectos,"contraseñas incorrectas.")
#Pau del futuro, haz que se reinicien las variables de letras seguidas y eso, si pones otra cosa.