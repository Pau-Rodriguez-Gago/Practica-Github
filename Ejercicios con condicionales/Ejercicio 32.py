#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas
frase="A quién madruga Dios ayuda"
palabra=input("Introduce una palabra: ")
frase=frase.lower()
palabra=palabra.lower()
palabra1="a"
palabra2="dios"
palabra3="quién"
palabra4="madruga"
palabra5="ayuda"
if palabra==palabra1 or palabra2 or palabra3 or palabra4 or palabra5:
    print("La palabra está en la frase y su posición es: ",frase.index(palabra))
else:
    print("La palabra no está en la frase")