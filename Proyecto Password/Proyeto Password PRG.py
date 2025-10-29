print("INSTRUCCIONS")
print("1.La longitud del password té que tenir entre 6 i 8 caracters")
print("2.Forçar els següents valors segons la posició indicada:")
print("Posició 1 Un número major o igual 1 i menor o igual que 5")
print("Posició 2 Una lletra minúscula")
print("Posició 3 Una lletra majúscula")
print("Posició 4 Un dels següents simbols *,_, @")
print("Posició 5 Una lletra minúscula")
print("Posició 6 Un número major o igual 6 i menor o igual que 9")
print("Posició 7 Un dels següents simbols &,/,#)")
print("Posició 8 Un número menor o igual que 5")
password=input("Introduce una palabra clave:")
#Utilitzo el valor de len(password) per a no haber de crear una nova variable que tingui elaquest valor.
if len(password)<6 or len(password)>8:
    print("Error, el password té una longitud de ",len(password)," caràcters i no compleix els requisits")
else:
    #A continuación, compruevo si el carácter 1 es un número 
    #aunque no salga en las entrradas propuestas pues si no lo hiciera,
    #si el usuario introduce una letra en el primer carácter, falla el programa.
    if password[0].isnumeric():   
        if not(int(password[0])>=1 or int(password[0])<=5):
            print("Error en el caràter 1")
    else:
        print("Error en el caràter 1")
    if not(password[1].islower):
        print("Error en el caràcter 2")
    if not(password[2].isupper):
         print("Error en el caràcter 3")
    if not(password[3]=="*" or password[3]=="_" or password[3]=="@"):
        print("Error en el caràcter 4")
    if not(password[4].islower):
        print("Error en el carácter 5")
    if password[5].isnumeric():   
        if not(int(password[0])>=1 or int(password[0])<=5):
            print("Error en el caràter 6")
    else:
        print("Error en el caràter 1")