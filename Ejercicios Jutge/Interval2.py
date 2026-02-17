intervalos=input()
intervalos=intervalos.split()
num1_int1=int(intervalos[0])
num2_int2=int(intervalos[1])
num1_int2=int(intervalos[2])
num2_int2=int(intervalos[3])
if num1_int1==num1_int2 and num2_int2==num2_int2:
    print("=")
elif num1_int1>=num1_int2 and num2_int2<=num2_int2:
    print("1")
elif num1_int2>=num1_int1 and num2_int2<=num2_int2:
    print("2")
else:
    print("?")
#Aquí hago los numeros en una variable por separados con el .split y les doy valor a las variables por posición
#pasandolos a numeros y no un string. Luego los comparo para ver si se cumplen las condiciones del enunciado