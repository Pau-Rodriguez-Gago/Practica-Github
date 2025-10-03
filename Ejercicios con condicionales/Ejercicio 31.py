#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.
frase="A quién madruga Dios ayuda"
palabra=input("Introduce una palabra: ")

palabra1="A"
palabra2="Dios"
palabra3="quién"
palabra4="madruga"
palabra5="ayuda"
if palabra==palabra1 or palabra2 or palabra3 or palabra4 or palabra5:
    print("La palabra está en la frase y su posición es: ",frase.index(palabra))
else:
    print("La palabra no está en la frase")