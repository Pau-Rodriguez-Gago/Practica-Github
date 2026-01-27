#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no
lista1=["casa","mesa","sal","sol"]
lista2=["casa","luz","tres","tren","sol","pan"]
si_repe=[]
no_repe=[]
for x in lista1:
    if x in lista2:
        si_repe.append(x)
    else:
        no_repe.append(x)
print("Las palabras que están repetidas son: ",si_repe)
print("Las palabras que no están repetidas son: ",no_repe)