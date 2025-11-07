#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.
cantidad_notas=int(input("Introduce la cantidad de notas que quieres introducir: "))
nota_en_estado_de_comprovación="tonto quien lo lea"
for x in range(cantidad_notas):
    nota_en_estado_de_comprovación=float(input("Introduce tu nota: "))
    if float(nota_en_estado_de_comprovación)<5:
        print("Asignatura suspendida")
    else:
        print("Asignatura aprovada")