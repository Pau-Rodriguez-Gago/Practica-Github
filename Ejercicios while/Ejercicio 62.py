#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. UTILIZA FOR. Contempla si primer valor es superior al segundo
var_min=0
var_max=0
var_intervalo=0
concatenar=""
var_min=int(input("Introduce un inicio: "))
var_max=int(input("Introduce un final: "))
if var_min<var_max:
    for x in range(var_min,var_max+1):
        concatenar=concatenar+str(x)+","
if var_min>var_max:
     for x in range(var_max,var_min-1):
        concatenar=concatenar+str(x)+","

print(concatenar[:-1])