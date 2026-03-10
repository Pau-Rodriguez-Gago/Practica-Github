lista_contraseña=input().split("-")
lista_seg=[]
lista_deb=[]
lista_inval=[]
len_cont_larga=0
cont_buena_larga=""
for x in lista_contraseña:
    numletras=0
    numnum=0
    numcaract=0
    for j in x:
        if len(x)>len_cont_larga:
            len_cont_larga=len(x)
            cont_buena_larga=x
        if j.isnumeric():
            numnum+=1
        elif j.isalpha():
            numletras+=1
        else:
            numcaract+=1
if numcaract==0 and len(x)>=8: 
    if numnum>=1 and numletras:
        lista_seg.append(x)
if len(x)<8 or (numcaract==0 and numnum==0) or (numcaract==0 and numletras==0):
    lista_deb.append(x)
if numcaract>0:
    lista_inval.append(x)
print("Las contraseñas seguras son:",lista_seg)
print("Las contraseñas débiles son:",lista_deb)
print("Las contraseñas inválidas son:",lista_inval)
print("La contraeña más larga es: ",cont_buena_larga)
