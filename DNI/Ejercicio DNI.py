dni=0
resto=0
letra="A"
continuar="s"
dni_final=[]
dni_str=""
dni_bienmal=52
errores_long=0
errores_num=0
errores_resto=0
while continuar=="s":
    dni_final=[]
    dni=(input("Introduce los números del DNI: "))
    dni_str=str(dni)
    if not len(dni_str)==8:
        print("El valor introducido no cumple con la longitud correcta.")
        dni_bienmal=0
        errores_long=errores_long+1
    elif not dni.isdigit():
         dni_bienmal=1
         errores_num=errores_num+1
         print("El valor introducido debe ser numérico.")
    else:
        resto=int(dni)%23
        if resto==0:
            letra="T"
        elif resto==1:
            letra="R"
        elif resto==2:
            letra="W"
        elif resto==3:
            letra="A"
        elif resto==4:
            letra="G"
        elif resto==5:
            letra="M"
        elif resto==6:
            letra="Y"
        elif resto==7:
            letra="F"
        elif resto==8:
            letra="P"
        elif resto==9:
            letra="D"
        elif resto==10:
            letra="X"
        elif resto==11:
            letra="B"
        elif resto==12:
            letra="N"
        elif resto==13:
            letra="J"
        elif resto==14:
            letra="Z"
        elif resto==15:
            letra="S"
        elif resto==16:
            letra="Q"
        elif resto==17:
            letra="V"
        elif resto==18:
            letra="H"
        elif resto==19:
            letra="L"
        elif resto==20:
            letra="C"
        elif resto==21:
            letra="K"
        elif resto==22:
            letra="E"
        else:
            dni_bienmal=3
            errores_resto=errores_resto+1
        dni_final.append(dni_str)
        dni_final.append(letra)
        "-".join(dni_final)
        print(dni_final)
    continuar=input("Quieres introducir más DNI? s/n : ")