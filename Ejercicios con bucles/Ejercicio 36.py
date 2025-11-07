#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
primeros_números_naturales=int(input("Introduce la cantidad de los primeros números números naturales que quieres sumar entre sí: "))
número_natural_por_el_que_vamos=1
total=0
for x in range(primeros_números_naturales):
    total=total+número_natural_por_el_que_vamos
    número_natural_por_el_que_vamos=número_natural_por_el_que_vamos+1
print("La suma de los primeros",primeros_números_naturales,"números naturales da:",total)