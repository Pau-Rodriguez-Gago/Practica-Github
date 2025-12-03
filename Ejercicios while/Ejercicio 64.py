#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
total_de_pares=0
total_de_impares=0
total_de_números_positivos=0
total_de_números_negativos=0
total_de_ceros=0
total_de_la_suma=0
numero_introducido=0
while not(numero_introducido==-99):
    numero_introducido=int(input("Introduce un número: "))
    if numero_introducido%2==0:
        total_de_pares=total_de_pares+1
        if numero_introducido>0:
            total_de_números_positivos=total_de_números_positivos+1
        if not(numero_introducido>0):
            total_de_números_negattivos=total_de_números_negativos+1
        if numero_introducido==0:
            total_de_ceros=total_de_ceros+1
        total_de_la_suma=total_de_la_suma+numero_introducido
    else:
        total_de_impares=total_de_impares+1
        if numero_introducido>0:
            total_de_números_positivos=total_de_números_positivos+1
        if not(numero_introducido>0):
            total_de_números_negattivos=total_de_números_negativos+1
        if numero_introducido==0:
            total_de_ceros=total_de_ceros+1
        total_de_la_suma=total_de_la_suma+numero_introducido
print("El número de pares es de:")