contras=input().split("-")
lista_seguras=[]
lista_debil=[]
lista_inval=[]
len_contra_larga=0
contra_larga=""
for x in contras:
    num_letras=0
    num_num=0
    num_carac=0
    for i in x:
        if i .isalpha():
            num_letras+=1
        elif i .isnumeric():
            num_num+=1
        else:
            num_carac+=1
        if len(x)>len_contra_larga:
            len_contra_larga=len(x)
            contra_larga=x
    if num_carac==0:
        if len(x)>=8 and num_num>0 and num_letras>0:
            lista_seguras.append(x)
        if len(x)<8 or (num_letras>0 and num_num<1) or (num_num>0 and num_letras<1):
            lista_debil.append(x)
    else:
        lista_inval.append(x)
print("Contras seguras: ",lista_seguras)
print("Contras débiles: ",lista_debil)
print("Contras invalidas: ",lista_inval)
print("La contraseña más larga es: ",contra_larga)