# 18.-Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.
num_menores= int(input("Introduce el número de menores de 18 años: "))
num_adultos= int(input("Introduce el número de adultos: "))
precio_entrada= 12
descuento_menores= 0.50
descuento_adultos= 0.10
total_menores= num_menores * (precio_entrada * (1 - descuento_menores))
total_adultos= num_adultos * (precio_entrada * (1 - descuento_adultos))
total_pagar= total_menores + total_adultos
total_pagar= format(total_pagar, '.2f')
print("El total a pagar por los menores es:",total_menores,"euros.")
print("El total a pagar los adultos es:",total_adultos,"euros.")
print("El total a pagar es:",total_pagar,"euros.")