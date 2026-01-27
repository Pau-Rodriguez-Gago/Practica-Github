#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.lista1=["casa","mesa","sal","sol"]
lista1=["casa","mesa","sal","sol"]
lista2=["casa","luz","tres","tren","sol","pan"]
si_repe=[]
no_repe=[]
for x in lista1:
    if x in lista2:
        si_repe.append(x)
    if x not in lista2:
        no_repe.append(x)
for y in lista2:
    if y not in lista1:
        no_repe.append(y)
print("Las palabras que están repetidas son: ",si_repe)
print("Las palabras que no están repetidas son: ",no_repe)