#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota= float(input("Introduce la nota: "))
if nota<0 or nota>10:
    print("La nota no es válida")
elif nota>=0 and nota<5:
    print("Has sacado un",nota,"que es un insuficiente")
elif nota>=5 and nota<6.5:
    print("Has sacado un",nota,"que es un satisfactorio")
elif nota>=6.5 and nota<8.5:
    print("Has sacado un",nota,"que es un Notable")
else:
    print("Has sacado un",nota,"que es un Excelente")
    