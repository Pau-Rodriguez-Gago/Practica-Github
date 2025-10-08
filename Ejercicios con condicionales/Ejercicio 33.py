#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años
frase="No hay mal que dure cien años"
frase=frase.lower()
vocales=["a","e","i","o","u"]
for vocal in vocales:
    print("La vocal",vocal,"aparece",frase.count(vocal),"veces")