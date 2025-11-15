#40. Crea un programa que cuente todos los números pares hasta el número 50
total_pares=0
total_inpares=0
for x in range(0,50,2):
    total_pares=total_pares+1
for x in range(1,50,2):
    total_inpares=total_inpares+1
print("El total de pares es: ",total_pares)
print("El total de inpares es: ",total_inpares)
