#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.
núm_pedidos=0
pedidinho_bocadilio=0
pedidinho_segundinho=0
pedidinho_bedidinho=0
total_pagar=float(0)
total_iva=float(0)
total_con_el_descuento=float(0)
repetir="s"
print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print(" ")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print(" ")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")
while repetir=="s":
    pedidinho_bocadilio=int(input("Introduce el número del primer plato que quieras pedir: "))
    pedidinho_segundinho=int(input("Introduce el número del acompañante que quieras pedir: "))
    pedidinho_bedidinho=int(input("Introduce el número de la bebida que quieras pedir: "))
    núm_pedidos=núm_pedidos+1
    if pedidinho_bocadilio==1:
        total_pagar=float(total_pagar+9)
    if pedidinho_bocadilio==2:
        total_pagar=float(total_pagar+4.5)
    if pedidinho_bocadilio==3:
        total_pagar=float(total_pagar+2.5)
    if pedidinho_segundinho==1:
        total_pagar=float(total_pagar+1.5)
    if pedidinho_segundinho==2:
        total_pagar=float(total_pagar+1.75)
    if pedidinho_segundinho==3:
        total_pagar=float(total_pagar+3)
    if pedidinho_bedidinho==1:
        total_pagar=float(total_pagar+2)
    if pedidinho_bedidinho==2:
        total_pagar=float(total_pagar+1.5)
    if pedidinho_bedidinho==3:
        total_pagar=float(total_pagar+1)
    repetir=input("¿Quieres pedir otro set de menú? s/n: ")
print("Número de pedidos:", núm_pedidos)
print("Total a pagar:", total_pagar)
total_iva=total_pagar*10
total_iva=total_iva/100
total_iva=total_pagar+total_iva
print("Total con IVA:", total_iva)
if total_pagar>=20 and total_pagar<=30:
    total_con_el_descuento=float(total_iva*5)
    total_con_el_descuento=float(total_con_el_descuento/100)
    total_con_el_descuento=float(total_iva-total_con_el_descuento)
    print("Total con descuento del 5%:",float(total_con_el_descuento))
if total_pagar>30:
    total_con_el_descuento=float(total_iva*15)
    total_con_el_descuento=float(total_con_el_descuento/100)
    total_con_el_descuento=float(total_iva-total_con_el_descuento)
    print("Total con descuento del 15%:",float(total_con_el_descuento))