segundos_intro=int(input(""))
horas=segundos_intro//3600
minutos=(segundos_intro%3600)//60
segundos=(segundos_intro%3600)%60
print(horas,minutos,segundos)