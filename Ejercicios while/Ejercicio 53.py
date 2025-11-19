#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
número_1=0
número_2=0
repetir="s"
suma=número_1+número_2
contador_repetir=0
contador_sumas=0
while repetir=="s":
    número_1=int(input("Introduce el primer número que quieres que se sume: "))
    número_2=int(input("Introduce el segundo número que quieres que se sume: "))
    contador_repetir=contador_repetir+1
    suma=número_1+número_2
    contador_sumas=contador_sumas+suma
    print("La suma de los números es:",suma)
    repetir=input("Deseas repetir la operación s/n: ")
print("Programa finalizado")
print("El número total de repeticiones que has hecho es de:",contador_repetir,"veces")
print("La suma total de todas las sumas da:",contador_sumas)