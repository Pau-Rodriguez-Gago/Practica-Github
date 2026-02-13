tiempo=input("").split()
horas=(tiempo[0])
minutos=(tiempo[1])
segundos=(tiempo[2])
horas_fin=int(horas)
minutos_fin=int(minutos)
segundos_fin=int(segundos)+1
if segundos_fin==60:
    segundos_fin=0 
    minutos_fin=minutos_fin+1
    if minutos_fin==60:
        minutos_fin=0 
        horas_fin=horas_fin+1
if horas_fin<10 and minutos_fin<10 and segundos_fin<10:
    print(str(0)+str(horas_fin)+":"+str(0)+str(minutos_fin)+":"+str(0)+str(segundos_fin))
elif horas_fin<10 and minutos_fin<10 and not (segundos_fin<10): 
    print(str(0)+str(horas_fin)+":"+str(0)+str(minutos_fin)+":"+str(segundos_fin)) 
elif horas_fin<10 and not (minutos_fin<10) and segundos_fin<10: 
    print(str(0)+str(horas_fin)+":"+str(minutos_fin)+":"+str(0)+str(segundos_fin)) 
elif not (horas_fin<10) and minutos_fin<10 and segundos_fin<10: 
    print(str(horas_fin)+":"+str(0)+str(minutos_fin)+":"+str(0)+str(segundos_fin)) 
elif horas_fin<10 and not (minutos_fin<10) and not (segundos_fin<10): 
    print(str(0)+str(horas_fin)+":"+str(minutos_fin)+":"+str(segundos_fin)) 
elif not (horas_fin<10) and minutos_fin<10 and not (segundos_fin<10): 
    print(str(horas_fin)+":"+str(0)+str(minutos_fin)+":"+str(segundos_fin)) 
elif not (horas_fin<10) and not (minutos_fin<10) and segundos_fin<10: 
    print(str(horas_fin)+":"+str(minutos_fin)+":"+str(0)+str(segundos_fin)) 
else: 
    print(str(horas_fin)+":"+str(minutos_fin)+":"+str(segundos_fin))