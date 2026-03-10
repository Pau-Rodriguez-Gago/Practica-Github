var1=input()
lista1=var1.split("-")
listaproductos=[]
listaprecio=[]
listastock=[]
for x in lista1:
    lista2=x.split(":")
    listaproductos.append(lista2[0])
    listaprecio.append(lista2[1])
    listastock.append(lista2[2])
listaprecio=[int(x) for x in listaprecio]
listastock=[int(x) for x in listastock]
for j in range (len(listaprecio)):
    precio_total=precio_total+(listaprecio[j] * listastock[j])
print(precio_total)
mascaro=max(listaprecio)
posicion=listaprecio.index(mascaro)
print("El producto más caro es: ", listaproductos[posicion])
#stock 0
posicion=listastock.index(0)
print("el producto con stock a cero es: ",listaproductos[posicion])
listaprecio.pop(posicion)
listastock.pop(posicion)
listaproductos.pop(posicion)
print(listaproductos)