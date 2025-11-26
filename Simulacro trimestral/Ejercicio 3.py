numero_de_cifras=0
numero_introducido=0
longitud_numero=0
producto=1
total_de_pares=0
numero_de_cifras=int(input("Introduce cuantas cifras quieres que tenga tu número: "))
numero_introducido=int((input("Introduce el número: ")))
longitud_numero=len(str(numero_introducido))
if longitud_numero==numero_de_cifras:
    for x in str(numero_introducido):
        producto=producto*int(x)
        if int(x)%2==0:
            total_de_pares=total_de_pares+1
    print("Producto de cifras: ",producto)
    print("Cifras pares: ", total_de_pares)
else:
    print("Longitud incorrecta")