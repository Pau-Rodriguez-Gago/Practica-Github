#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.
cantidad_números=int(input("Introduce la cantidad de números que quieres introducir: "))
número_en_estado_de_comprovación="tonto quien lo lea"
total_positivos=0
total_negativos=0
total_ceros=0
for x in range(cantidad_números):
    número_en_estado_de_comprovación=float(input("Introduce un número: "))
    if float(número_en_estado_de_comprovación)>0:
        total_positivos=total_positivos+1
    if float(número_en_estado_de_comprovación)<0:
        total_negativos=total_negativos+1
    if float(número_en_estado_de_comprovación)==0:
        total_ceros=total_ceros+1
print("La cantidad de números positivos es: ",total_positivos)
print("La cantidad de números negativos es: ",total_negativos)
print("La cantidad de números ceros es: ",total_ceros)