#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10
cantidad_notas=int(input("Introduce la cantidad de notas que quieres introducir: "))
nota_en_estado_de_comprovación="tonto quien lo lea"
for x in range(cantidad_notas):
    nota_en_estado_de_comprovación=float(input("Introduce tu nota: "))
    if float(nota_en_estado_de_comprovación)<10 and float(nota_en_estado_de_comprovación)>1:
        if float(nota_en_estado_de_comprovación)<5:
            print("Asignatura suspendida")
        else:
            print("Asignatura aprovada")
    else:
        print("Has introducido una nota equivocada")