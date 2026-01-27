#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
lista=[]
respuesta="s"
letra=""
while respuesta=="s":
    letra=input("Introduce una letra: ")
    if letra not in lista:
        lista.append(letra)
    respuesta=input("Quieres introducir más letras? s/n: ")
print("Tu lista final de letras es:",lista)