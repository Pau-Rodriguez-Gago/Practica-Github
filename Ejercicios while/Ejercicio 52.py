#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
número_1=0
número_2=0
repetir="s"
suma=número_1+número_2
while repetir=="s":
    número_1=int(input("Introduce el primer número que quieres que se sume: "))
    número_2=int(input("Introduce el segundo número que quieres que se sume: "))
    suma=número_1+número_2
    print("La suma de los números es:",suma)
    repetir=input("Deseas repetir la operación s/n: ")
print("Programa finalizado")