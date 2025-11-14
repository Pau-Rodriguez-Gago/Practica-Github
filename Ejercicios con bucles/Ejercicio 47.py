#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida
primer_numero= int(input("Introduce el primer número del intervalo: "))
segundo_numero= int(input("Introduce el segundo número del intervalo: "))
if primer_numero < segundo_numero:
    numeros = list(range(primer_numero, segundo_numero + 1))
else:
    numeros = list(range(primer_numero, segundo_numero - 1, -1))
print("-".join(map(str, numeros)))
#con list haces una lista en la que una misma variable tiene múltiples valores.
#ponemos más uno o menos uno para que aí el programa tenga en cuenta el último valor de la lista.