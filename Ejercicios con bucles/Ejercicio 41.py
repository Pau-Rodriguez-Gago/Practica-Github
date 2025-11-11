#41. Imprime el siguiente patrón utilizando for:
patron="54321"
contador=0
for x in range(len(patron)):
    if contador==0:
        print(patron)
    if contador==1:
        print(4321)
    if contador==2:
        print(321)
    if contador==3:
        print(21)
    if contador==4:
        print(1)
    contador=contador+1
