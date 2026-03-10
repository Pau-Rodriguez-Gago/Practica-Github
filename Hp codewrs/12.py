import math
veces = int(input())
soluciones = []
for i in range(veces):
    a = input().split(' ')
    if a[0] == 'rectangle':
        area = float(a[1]) * float(a[2])
        soluciones.append(format(area, '.6f'))
    if a[0] == 'circle':
        area = math.pi * (float(a[1]) ** 2)
        soluciones.append(format(area, '.6f'))
for i in soluciones:
    print(i)
