numeros=input()
numeros=numeros.split()
if int(numeros[0])>int(numeros[1]) and int(numeros[0])>int(numeros[2]):
    print(numeros[0])
if int(numeros[1])>int(numeros[0]) and int(numeros[1])>int(numeros[2]):
    print(numeros[1])
if int(numeros[2])>int(numeros[0]) and int(numeros[2])>int(numeros[1]):
    print(numeros[2])
if int(numeros[0])==int(numeros[1]) and int(numeros[0])==int(numeros[2]):
    print(numeros[0])
if int(numeros[0])==int(numeros[1]) and int(numeros[0])>int(numeros[2]):
    print(numeros[0])
if int(numeros[0])==int(numeros[2]) and int(numeros[0])>int(numeros[1]):
    print(numeros[0])
if int(numeros[1])==int(numeros[2]) and int(numeros[1])>int(numeros[0]):
    print(numeros[1])