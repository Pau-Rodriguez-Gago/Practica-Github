#34. Corrige los  errores o añade el código que necesites para que el siguiente programa se 
#ejecute correctamente 
#inicializo valores a cada variable 
var_numero = 6734
var_suma = 0
var_longitud = 0

# convierto a string para poder obtener la longitud y acceder a cada dígito
var_str = str(var_numero)
# obtengo su longitud
var_longitud = len(var_str)

# sumo cada dígito (porque así me sirve para cualquier longitud)
#el ch es cada carácter de la cadena
for ch in var_str:
    if ch.isdigit():
        var_suma += int(ch)

# utilizo una condición y el operador aritmético % para saber si el resto da 0 y ver si es par
if var_suma % 2 == 0:
    print("El valor de la suma de los dígitos es", var_suma, "y es par")
else:
    print("El valor de la suma de los dígitos es", var_suma, "y es impar")