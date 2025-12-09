#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
num_intr=1
num_intr=int(input("Introduce un número"))
mayor=num_intr
menor=num_intr
while not(num_intr==-99):
    num_intr=int(input("Introduce un número: "))
    if num_intr>mayor:
        mayor=num_intr
    if num_intr<menor:
        menor=num_intr
print("El mayor es",mayor)
print("El menor es",menor)