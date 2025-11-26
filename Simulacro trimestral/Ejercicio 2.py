numero=0
suma_numeros_positivos=0
suma_numeros_negativo=0
suma_numeros_mayor_a_cien=0
for x in range(0,7):
    numero=int(input("Introduce uno de los 7 números: "))
    if numero<0:
        suma_numeros_negativo=suma_numeros_negativo+numero
    if numero>0:
        suma_numeros_positivos=suma_numeros_positivos+numero
        if numero>100:
            suma_numeros_mayor_a_cien=suma_numeros_mayor_a_cien+1
print("Suma positivos: ",suma_numeros_positivos)
print("Suma negativos: ",suma_numeros_negativo)
print("Mayores de 100: ", suma_numeros_mayor_a_cien)
