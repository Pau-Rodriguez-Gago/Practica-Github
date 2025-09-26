#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10
num1 =int(input("Introduce el primer número (entre 0 y 10): "))
num2=int(input("Introduce el segundo número (entre 0 y 10): "))
if num1<0 or num1>10 or num2<0 or num2>10:
    print("uno o los dos números no están entre 0 y 10")
elif num1>num2:
    print("El número",num1,"es mayor que",num2)
elif num1<num2:
        print("El número",num1,"es menor que",num2)
else:
        print("Los números son iguales")