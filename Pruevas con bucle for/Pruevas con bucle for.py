#FOR
#cuando sabemos la cantidad de veces que se debe repetir
total=0
repeticiones=int(input("introduce un número de veces: "))
for j in range(repeticiones):
    print(j,"hola")
    total=total+j
print(total)
password="h1l4 que t4l"
total=0
repeticiones=int(input("introduce un número de veces: "))
for j in range(len(password)):
    print(password[j])
    if password[j].isnumeric():
        print("es un número")
    else:
        print("no es un número")
print(total)
#for j in string:
password= "h1l4"
num_vocales=0
total=0
for i in password:
    if i.isnumeric():
        total=total+int(i)
    if i in 'aeiouAEIOU':
        num_vocales=num_vocales+1
print(total)
print(num_vocales)
#for j in ranje (0,10,2):
#[El tercer número es para ver cada cuanto salta por egemplo de dos en dos]

#WHILE
#cuando queremos que se detenga por una condición