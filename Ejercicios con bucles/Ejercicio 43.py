#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra
palabra=input("introduce una palabra: ")
for j in range(len(palabra)):
    print("En la posición",j,"está la ",palabra[j])
  