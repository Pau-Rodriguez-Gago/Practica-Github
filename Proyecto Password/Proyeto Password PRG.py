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
#Creo una variable que será el password introduit
password=input("Introduce una palabra clave:")
#Com no em sortía com fer que el programa sapigues si la contrasenya era correcta,
#vaig retornar al meu diagrama de flux i vaig decidir aplicar una nova variable
#amb el valor de quen no hi havia error però si en qualsevol moment sí que n' hi ha,
#aquest cambia i així el programa sap si el password és correcte.
algun_error="no"
#Utilitzo el valor de len(password) per a no haber de crear una nova variable que tingui aquest valor.
if len(password)<6 or len(password)>8:
    print("Error, el password té una longitud de ",len(password)," caràcters i no compleix els requisits")
#Aquí ve el més important, comprovo cadascuna de les condicions en la seva versió oposada,
#de manera que si és correcte el programa segueix però si no ho és, ho mostra per pantalla
#i continua amb la resta.
else:
    if not (password[0].isnumeric()):
        algun_error="si"
        print("Error en el caràcter 1")
    else:
        if not(int(password[0])>=1) or not(int(password[0])<=5):
            algun_error="si"
            print("Error en el caràter 1")
    if not(password[1].islower()):
        algun_error="si"
        print("Error en el caràcter 2")
        #En aquesta condició faig servir en comptes de not (I la condició demanada)
        #el valor contrari, en comtes de si no es majúscula, que miri si, pel contrari,
        #és minúscula. Ja que de les dues maneres funciona i així queda demostrat.
    if password[2].islower():
        algun_error="si"
        print("Error en el caràcter 3")
    if not(password[3]=="*" or password[3]=="_" or password[3]=="@"):
        algun_error="si"
        print("Error en el caràcter 4")
    if not(password[4].islower()):
        algun_error="si"
        print("Error en el carácter 5")
    if not(int(password[5])>=6) or not(int(password[5])<=9):
        algun_error="si"
        print("Error en el caràter 6")
#Aquí també entra en joc una part molt important per al programa,
#comprovo que el password realmemt tingui 7 o més caràcters i després si te 8
#abans de comprovar les condicions d'aquests caràcters ja que si el password
#fòs més curt, i no ho programès així, detectaria errors al caràcter 7 i 8 quan en realitat
#no existeixen.
    if len(password)>=7:
        if not(password[6]=="&" or password[6]=="/" or password[6]=="#"):
            algun_error="si"
            print("Error en el caràcter 7")
    if len(password)==8:
        if not(int(password[7])<=5):
            algun_error="si"
            print("Error en el caràcter 8")
#Aquí faig servir de nou la variable que vaig crear perquè el programa detecti si el
#password te errors i acabi o si no en té, digui que aquest es correcte.
    if algun_error=="no":
        print("El format del PASSWORD és correcte")
#Com a extra, vaig adonarme de que en els caràcters on el programa demana que siguin
#numérics, si en realitat són lletres, el programa falla. Vaig poder fer que detectés
#si no ho era i mostrès que ho havia un error, però, el programa acababa allà i no
#seguía amb la resta de condicions. I si em posava a pràcticament introduir tota la
#resta de comprovacions sota cadascuna de les comprovacions numériques, el programa
#es feia massa llarg i complexe and diversos errors. Per sort però vaig llegir
#tota la taula i en cap valor hi havia lletres on han d' anar números així que no
#influieix en el que vosté comprovarà.