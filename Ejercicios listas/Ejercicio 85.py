#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos
estudiante=""
notas_ingles=[]
notas_castellano=[]
notas_catalan=[]
nota_introducida=0
seguir_preguntando="s"
media_ingles=0
media_castellano=0
media_catalan=0
mediana_ingles=0
mediana_castellano=0
mediana_catalan=0
while seguir_preguntando=="s":
    estudiantes=input("Introduce el nombre de un estudiante: ")
    nota_ingles=int(input("Introduce la nota de inglés: "))
    notas_ingles.append(nota_ingles)
    nota_castellano=int(input("Introduce la nota de castellano: "))
    notas_castellano.append(nota_castellano)
    nota_catalan=int(input("Introduce la nota de catalán: "))
    notas_catalan.append(nota_catalan)
    seguir_preguntando=input("Deseas introducir otro alumno s/n: ")
notas_ingles.sort()
notas_castellano.sort()
notas_catalan.sort()
print("Las notas de inglés son: ", notas_ingles)
print("Las notas de castellano son: ", notas_castellano)
print("Las notas de catalán son: ", notas_catalan)
print("La media de las notas de inglés es: ", sum(notas_ingles)/len(notas_ingles))
print("La media de las notas de castellano es: ", sum(notas_castellano)/len(notas_castellano))
print("La media de las notas de catalán es: ", sum(notas_catalan)/len(notas_catalan))
#Ahora calculamos la mediana
if len(notas_ingles)%2==0:
    for x in notas_ingles:
        if x==len(notas_ingles)//2:
            mediana_ingles=mediana_ingles + x
if not len(notas_ingles)%2==0:
    mediana_ingles=notas_ingles[len(notas_ingles)//2]
if len(notas_castellano)%2==0:
    for x in notas_castellano:
        if x==len(notas_castellano)//2:
            mediana_castellano=mediana_castellano + x
if not len(notas_castellano)%2==0:
    mediana_castellano=notas_castellano[len(notas_castellano)//2]
if len(notas_catalan)%2==0:
    for x in notas_catalan:
        if x==len(notas_catalan)//2:
            mediana_catalan=mediana_catalan + x
if not len(notas_catalan)%2==0:
    mediana_catalan=notas_catalan[len(notas_catalan)//2]
print("La mediana de las notas de inglés es: ", mediana_ingles)
print("La mediana de las notas de castellano es: ", mediana_castellano)
print("La mediana de las notas de catalán es: ", mediana_catalan)