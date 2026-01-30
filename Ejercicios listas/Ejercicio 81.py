#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la 
#lista al azar. 
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
import random
valor_azar=random.choice(lista)
print("El valor seleccionado al azar de la lista es: ",valor_azar)
#random.choice() sirve para seleccionar un valor al azar de una lista.