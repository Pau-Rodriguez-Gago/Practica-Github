#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
import random
valor_dado=0
veces_que_sale_el_uno=0
veces_que_sale_el_dos=0
veces_que_sale_el_tres=0
veces_que_sale_el_cuatro=0
veces_que_sale_el_cinco=0
veces_que_sale_el_seis=0
veces_que_se_ha_tirado_el_dado=1
while not(veces_que_se_ha_tirado_el_dado>100):
    valor_dado=random.randint(1,6)
    if valor_dado==1:
        veces_que_sale_el_uno=veces_que_sale_el_uno+1
    if valor_dado==2:
        veces_que_sale_el_dos=veces_que_sale_el_dos+1
    if valor_dado==3:
        veces_que_sale_el_tres=veces_que_sale_el_tres+1
    if valor_dado==4:
        veces_que_sale_el_cuatro=veces_que_sale_el_cuatro+1
    if valor_dado==5:
        veces_que_sale_el_cinco=veces_que_sale_el_cinco+1
    if valor_dado==6:
        veces_que_sale_el_seis=veces_que_sale_el_seis+1
    veces_que_se_ha_tirado_el_dado=veces_que_se_ha_tirado_el_dado+1
print("Uno:",veces_que_sale_el_uno)
print("Dos:",veces_que_sale_el_dos)
print("Tres:",veces_que_sale_el_tres)
print("Cuatro:",veces_que_sale_el_cuatro)
print("Cinco:",veces_que_sale_el_cinco)
print("Seis:",veces_que_sale_el_seis)