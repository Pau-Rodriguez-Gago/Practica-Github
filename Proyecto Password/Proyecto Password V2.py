print("INSTRUCCIONES")
print("1.Debe contener un número entre el 0 y el 3")
print("2.Debe contener un número entre el 4 y el 6")
print("3.Debe contener un número entre el 7 y el 9")
print("4.Debe contener como mínimo dos letras mayúsculas y una minúscula.")
print("5.Debe contener un mínimo de 2 símbolos a excepción de una coma, un punto o un espacio.")
print("6.No debe contener dos letras,números,símbolos,seguidos.")
print("7.Debe contener un mínimo de 12 caracteres")
password=input("Introduce una contraseña:")
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
if len(password)<12:
    print("Error, el password té una longitud de ",len(password)," caràcters i no arriba als 12 requerits.")
for x in password:
    if int(x)>=0 and x<=3:
        contador_cero_tres=contador_cero_tres+1
        numero_seguido=numero_seguido+1
    if int(x)>=4 and x<=6:
        contador_cuatro_seis=contador_cuatro_seis+1
        numero_seguido=numero_seguido+1
    if int(x)>=7 and x<=9:
        contador_siete_nueve=contador_siete_nueve+1
        numero_seguido=numero_seguido+1
    if str(x).isupper:
        contador_letras_mayus=contador_letras_mayus+1
        letra_seguida=letra_seguida+1
    if str(x).islower:
        contador_letras_minus=contador_letras_minus+1
        letra_seguida=letra_seguida+1
    if not(x.isalnum) and not(x==" " or x=="." or x==","):
        contador_simbolos=contador_simbolos+1
        simbolo_seguido=simbolo_seguido+1
    if numero_seguido==2:
        veces_que_hay_numero_seguido=veces_que_hay_numero_seguido+1
        numero_seguido=0

else:
    if not (password[0].isnumeric()):
        algun_error="si"
        print("Error en el caràcter 1")
    else:
        if not(int(password[0])>=1) or not(int(password[0])<=5):
            algun_error="si"
            print("Error en el caràter 1")
    if not(password[1].islower()):
        algun_error="si"
        print("Error en el caràcter 2")
    if password[2].islower():
        algun_error="si"
        print("Error en el caràcter 3")
    if not(password[3]=="*" or password[3]=="_" or password[3]=="@"):
        algun_error="si"
        print("Error en el caràcter 4")
    if not(password[4].islower()):
        algun_error="si"
        print("Error en el carácter 5")
    if not(int(password[5])>=6) or not(int(password[5])<=9):
        algun_error="si"
        print("Error en el caràter 6")
    if len(password)>=7:
        if not(password[6]=="&" or password[6]=="/" or password[6]=="#"):
            algun_error="si"
            print("Error en el caràcter 7")
    if len(password)==8:
        if not(int(password[7])<=5):
            algun_error="si"
            print("Error en el caràcter 8")
    if algun_error=="no":
        print("El format del PASSWORD és correcte")
