#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el 
#número de veces que desea que repita la frase Buenos días. Con While
contador=int(input("Introduce elnúmero de veces que qiueres que se repita buenos días: "))
while not(contador==0):
    print("Buenos días")
    contador=contador-1