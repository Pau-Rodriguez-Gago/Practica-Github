#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
valor=input("Introduce un número para eliminar de la lista: ")
if valor.isdigit():
    if valor in lista1:
        lista1.remove(valor)
        print("La lista sin el número es: ",lista1)
    else:
        print("El número que has introducido no se encuentra en la lista.")
else:
    print("El valor introducido no es un número.")