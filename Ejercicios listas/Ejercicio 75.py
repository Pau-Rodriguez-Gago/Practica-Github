#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
cantidad_total=len(lista1)
cantidad_num=0
cantidad_let=0
cantidad_mayus=0
suma=0

for x in lista1:
    if x.isdigit():
        cantidad_num=cantidad_num+1
        suma=suma+int(x)
    if x.isalpha():
        cantidad_let=cantidad_let+1
        if x.isupper():
            cantidad_mayus=cantidad_mayus+1
print("La longitud es: ",cantidad_total)
print("La cantidad de números es: ",cantidad_num)
print("La cantidad de letras es: ",cantidad_let)
print("La cantidad de msyúsculas es: ",cantidad_mayus)
print("La suma de todos los números da: ",suma)