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
pedido_pedido=0
núm_pedidos=0
total_pagar=float(0)
total_con_iva=float(0)
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
    pedido_pedido=int(input("Introduce el pedido que quieras pedir"))
    núm_pedidos=núm_pedidos+1
    if pedido_pedido==1:
        total_pagar=float(total_pagar+12.5)
    if pedido_pedido==2:
        total_pagar=float(total_pagar+7.75)
    if pedido_pedido==3:
        total_pagar=float(total_pagar+5.5)
    repetir=input("Quiere pedir otro menú?, s/n: ")

