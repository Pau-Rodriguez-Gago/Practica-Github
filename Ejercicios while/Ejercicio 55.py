#55.Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
número_1=0
número_2=0
suma=número_1+número_2
contador_repetir=0
contador_sumas=0
while contador_sumas<=50 or float(contador_sumas/2==contador_sumas//2):
    número_1=int(input("Introduce el primer número que quieres que se sume: "))
    número_2=int(input("Introduce el segundo número que quieres que se sume: "))
    contador_repetir=contador_repetir+1
    suma=número_1+número_2
    contador_sumas=contador_sumas+suma
    print("La suma de los números es:",suma)
    print("El total acumulado es:",contador_sumas,"y llevas",contador_repetir,"operaciones realizadas")
print("Fin del programa")