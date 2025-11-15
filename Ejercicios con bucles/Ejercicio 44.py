#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
#de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’
numeros = list(range(0, 100, 3))
resultado = ",".join(map(str, numeros))
print(resultado)
