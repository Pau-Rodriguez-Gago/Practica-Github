numeros=input()
if numeros=="2":
    numero_2=input()
    suma=int(numeros)+int(numero_2)
    print(suma)
else:
    lista_num=numeros.split()
    suma=int(lista_num[0])+int(lista_num[1])
    print(suma)
#Bien, este fué un ejercicio que hice antes de empezar con los de la clase.
#Antes de que nos explicara la respuesta yo ya lo hube hecho, pero... de una manera alternativa.
#No pensé en comprovar la longitud de el primer imput así que, pensé, hmm si solo va ser cuando ponga un 2,
#hagamos uan excepción para ese caso. Y funcionó para mi agratdo, aún y así este plan no lo usé más 
#pues los ejercicios se van complicando y aparecen pruebas privadas...