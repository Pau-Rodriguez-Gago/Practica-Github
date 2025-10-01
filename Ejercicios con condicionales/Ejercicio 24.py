#24.Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
var1=float(input("Introduce el peso: "))
var2=float(input("Introduce la altura: "))
var_imc=var1 / var2**2
print("Si pesas",var1,"kilos y mides",var2,"tu IMC es:",var_imc)
if var_imc>25:
 print("Hay sobrepeso")
elif var_imc<18.5:
 print("Estás por debajo de los parámetros normales")
else:
    print("Estás dentro de los parámetros normales")