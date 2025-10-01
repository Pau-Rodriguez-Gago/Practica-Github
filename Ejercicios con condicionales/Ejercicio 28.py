#Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra= input("Introduce una letra: ")
if letra.isupper():
    print("La letra es mayúscula")
elif letra.islower():
    print("La letra es minúscula")
elif letra.isnumeric():
    print("No has introducido una letra")
elif not letra.isalnum():
    print("Has introducido un símbolo")