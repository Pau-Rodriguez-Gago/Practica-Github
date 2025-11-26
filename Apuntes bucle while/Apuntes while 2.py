edad=int(input("Introduce tu edad: "))

while edad<18 or edad<=0:
    print("Edad incorrecta")
    edad=int(input("vuelve a introducir la edad: "))
print("Tu edad es correcta")
#while True PROHIBIDO