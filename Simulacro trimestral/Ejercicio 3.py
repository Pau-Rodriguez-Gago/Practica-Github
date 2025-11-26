numero_de_cifras=0
numero_introducido=0
producto=1
total_de_pares=0
numero_de_cifras=int(input("Introduce cuantas cifras quieres que tenga tu número: "))
numero_introducido=str((input("Introduce el número: ")))
if len(numero_introducido)==numero_de_cifras:
    for x in range(0,numero_de_cifras):
        producto=producto*numero_introducido[x]
        if numero_introducido[x]/2==numero_introducido//2:
            total_de_pares=total_de_pares+1
    print("Producto de cifras: ",producto)
    print("Cifras pares: ", total_de_pares)
else:
    print("Longitud incorrecta")