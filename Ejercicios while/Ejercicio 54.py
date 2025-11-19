#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While
número_1=0
número_2=0
suma=número_1+número_2
contador_repetir=0
contador_sumas=0
while contador_sumas<=50:
    número_1=int(input("Introduce el primer número que quieres que se sume: "))
    número_2=int(input("Introduce el segundo número que quieres que se sume: "))
    contador_repetir=contador_repetir+1
    suma=número_1+número_2
    contador_sumas=contador_sumas+suma
    print("La suma de los números es:",suma)
    print("El total acumulado es:",contador_sumas,"y llevas",contador_repetir,"operaciones realizadas")
print("Fin del programa")