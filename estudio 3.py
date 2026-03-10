todo_pero_por_producto=input().split("-")
lista_indiv=[]
lista_producto=[]
lista_precio=[]
lista_stock=[]
lista_no_stock=[]
for x in todo_pero_por_producto:
    lista_indiv=x.split(":")
    lista_producto=lista_producto.append(lista_indiv[0])
    lista_precio=lista_precio.append(lista_indiv[1])
    lista_stock=lista_stock.append(lista_indiv[2])
    indice_x=todo_pero_por_producto.index(x)
    precio_total+=lista_precio[indice_x]*lista_stock[indice_x]
    if lista_indiv[2]==0:
        lista_no_stock.append(lista_producto[indice_x])
        
print("El producto más caro es: ",max(lista_precio))
