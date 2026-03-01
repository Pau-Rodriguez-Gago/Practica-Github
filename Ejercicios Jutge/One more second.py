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
        if horas_fin==24:
            horas_fin=0
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
#Este ejercicio me sacó de quicio bastante. Tuve dos problemas principales.
#El funcionamiento en si fue sencillo, los problemas llegaron a la hora del print.
#La primera complicación fue que me pedía que se mostrara un cero antes de la unidad si no era mayor a nueve.
#Decidí usar un if para cada caso, lo cual alarga muchisimo el código pues son muchas posibilidades.
#Después, una prueva privada fallaba hasta que descubrío que se trataba de que si las horas llegaban a 24, se debián
#reiniciar también, pero que etsuve un buen rato intentando comprender porque el Jutge lo consideraba incorrecto
#de todas formas, al enterarme lo arreglé sencillamente.
#Y para colmo, cuando mi compañero lo acaba le pregunto y veo que existe una fu8nción quer hace lo de los ceros de manera
#mucho mas sencilla hasta pudiendo escoger cuantas cifras, pero bueno el código me funcionó y estoy orgulloso.