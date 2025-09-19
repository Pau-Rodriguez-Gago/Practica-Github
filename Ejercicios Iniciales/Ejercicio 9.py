#Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos= int(input("Introduce un número de segundos: "))
minutos= segundos / 60
horas= minutos / 60
minutos_2decimales= format(minutos, '.2f')
horas_2decimales= format(horas, '.2f')
print("Son",segundos,"segubdos o",minutos_2decimales," minutos o ",horas_2decimales," horas.")
#también se podría hacer con round(variable, número de decimales)
