num1_int1, num2_int1, num1_int2, num2_int2 = map(int, input().split())
if num1_int1 == num1_int2 and num2_int1 == num2_int2:
    relacion = '='
elif num1_int1 >= num1_int2 and num2_int1 <= num2_int2:
    relacion = '1'
elif num1_int2 >= num1_int1 and num2_int2 <= num2_int1:
    relacion = '2'
else:
    relacion = '?'
inicio_inter = max(num1_int1, num1_int2)
fin_inter = min(num2_int1, num2_int2)
if inicio_inter > fin_inter:
    interseccion = "[]"
else:
    interseccion = f"[{inicio_inter},{fin_inter}]"

print(relacion, ",", interseccion)
#Aquí también me costó y lo hice despues de buscar así que también apliqué el map, y el print tuve que usar f [] para 
#que no salieran más espacios de los deseados.
