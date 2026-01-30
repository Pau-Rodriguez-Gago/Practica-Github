#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
numero=input("Introduce un número: ")
lista_numero=list(numero)
es_decimal="n"
for x in lista_numero:
    if "." in lista_numero or "," in lista_numero:
        es_decimal="s"
if es_decimal=="s":
    print("El número es decimal.")
else:
    print("El número no es decimal.")   
