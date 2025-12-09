#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos.
import random
import time
valor_dado=0
veces_que_sale_el_uno=0
veces_que_sale_el_dos=0
veces_que_sale_el_tres=0
veces_que_sale_el_cuatro=0
veces_que_sale_el_cinco=0
veces_que_sale_el_seis=0
veces_que_se_ha_tirado_el_dado=1
tiempo=time.time()
while time.time()-tiempo<3:
    #Con esto vemos que si restamos este time.time(), que es un cronómetro
    #menos el valor del tiempo, si es menor a tres, se cumpla el while, por
    #lo que al pasar tres egundos se deja de cumplir y ya no se ejecuta el while
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
print("Tiempo:",time.time()-tiempo)
print("Uno:",veces_que_sale_el_uno)
print("Dos:",veces_que_sale_el_dos)
print("Tres:",veces_que_sale_el_tres)
print("Cuatro:",veces_que_sale_el_cuatro)
print("Cinco:",veces_que_sale_el_cinco)
print("Seis:",veces_que_sale_el_seis)