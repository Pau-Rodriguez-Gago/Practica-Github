valor=100
numero=51
while numero>0 and valor>=50 and valor<=150:
    numero=int(input("Pon un número: "))
    if numero/2==numero//2 and not(numero/3==numero//3):
       valor=valor/2
       print(valor)
    if numero/2==numero//2 and numero/3==numero//3:
        valor=valor/2
        valor=valor-5
        print(valor)
    if not(numero/2==numero//2) and not(numero/3==numero//3):
       valor=valor+numero
       print(valor)
    if not(numero/2==numero//2) and numero/3==numero//3:
        valor=valor+numero
        valor=valor-5
        print(valor) 