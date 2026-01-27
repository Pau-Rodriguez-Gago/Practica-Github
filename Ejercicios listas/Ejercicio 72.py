#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista
lista=[]
respuesta="s"
letra=""
vocales=['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
while respuesta=="s":
    letra=input("Introduce una letra: ")
    if letra not in lista and not letra in vocales:
        lista.append(letra)
    respuesta=input("Quieres introducir más letras? s/n: ")
print("Tu lista final de letras es:",lista)