dni=0
resto=0
letra="PEPINILLO"
continuar="s"
dni_final=[]
dni_str=""
lista_letras="TRWAGMYFPDXBNJZSQVHLCKE"
dni_bienmal=52
errores_long=0
errores_num=0
errores_resto=0
dni_totales=0
dni_correctos=0
dni_incorrectos=0
danis_correctos_ordenados=[]
danis_incorrectos_ordenados=[]
menu=0
while continuar=="s" or continuar=="S":
    dni_final=[]
    dni=(input("Introduce los números del DNI: "))
    dni_str=str(dni)
    dni_totales=dni_totales+1
    if not len(dni_str)==8:
        print("El valor introducido no cumple con la longitud correcta.")
        dni_bienmal=0
        errores_long=errores_long+1
        dni_incorrectos=dni_incorrectos+1
        danis_incorrectos_ordenados.append(dni)
    elif not dni.isdigit():
         dni_bienmal=1
         errores_num=errores_num+1
         dni_incorrectos=dni_incorrectos+1
         print("El valor introducido debe ser numérico.")
         danis_incorrectos_ordenados.append(dni)
    else:
        resto=int(dni)%23
        letra=lista_letras[resto]
        if not (resto>-1 or resto<23): 
            dni_bienmal=3
            errores_resto=errores_resto+1
            dni_incorrectos=dni_incorrectos+1
            danis_incorrectos_ordenados.append(dni)
        else:
            dni_final.append(dni_str)
            dni_final.append(letra)
            dni_correctos=dni_correctos+1
            danis_correctos_ordenados.append(dni_final)
            print(dni,"-",letra)
    continuar=input("Quieres introducir más DNI? s/n : ")
danis_correctos_ordenados.sort()
danis_incorrectos_ordenados.sort()
print("A continuación puede seleccionar como quiere ver los resultados recogidos por el programa: ")
print("1. Listar DNI correctos ordenados de menor a mayor.")
print("2. Listar DNI incorrectos ordenados de menor a mayor.")
print("3. Número total de errores")
print("4. Número total de DNIs correctos.")
print("5. Porcentaje de DNI correctos, incorrectos, errores de longitud, errores de número, no existentes.")
print("6. Salir s/n.")
while not (menu==6):
    menu=int(input("Introduzca el número de la opción que desee ver: "))
    if menu==1:
        print(danis_correctos_ordenados)
    elif menu==2:
        print(danis_incorrectos_ordenados)
    elif menu==3:
        print("Su número total de errores es de:",errores_long+errores_num+errores_resto)
    elif menu==4:
        print("Su número total de DNI correctos es de:",dni_correctos)
    elif menu==5:
        print("Porcentaje de DNIs correctos: ",round((dni_correctos/dni_totales)*100,1),"%")
        print("Porcentaje de DNIs incorrectos: ",round((dni_incorrectos/dni_totales)*100,1),"%")
        print("Porcentaje de errores de longitud: ",round((errores_long/dni_totales)*100,1),"%")
        print("Porcentaje de errores de número: ",round((errores_num/dni_totales)*100,1),"%")
        print("Porcentaje de errores de resto/no existentes: ",round((errores_resto/dni_totales)*100,1),"%")
    else:
        if not (menu==6):
            print("No ha introducido un valor permitido. Por favor, introduce uno de nuevo.")
print("Programa finalizado")
#Me ahorrro tener que poner if menu==6: gracias a que nunca va a poder escapar del while si no ha puesto un 6, por lo tanto,
#Eso significa que ya quiere que se acabe el programa.
#He decidido redondear los porcentajes a una cifra decimal para que no salgan todos esos decimales.