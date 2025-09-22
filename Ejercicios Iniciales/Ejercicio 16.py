#-16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división).
import math
num= float(input("Introduce un número para calcular su raíz cuadrada: "))
raiz_cuadrada= math.sqrt(num)
division_entero= raiz_cuadrada // 2
print("La raíz cuadrada de",num,"es:",format(raiz_cuadrada, '.2f'))
print("La división entera de la raíz cuadrada entre 2 es:",int(division_entero))