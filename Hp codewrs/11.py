map = input().split(' ')
total = 0
comprovacion=0
for i in map:
    comprovacion+=1
    if comprovacion>1 and comprovacion < len(map):
        if int(i) > int(map[comprovacion-2]) and int(i) > int(map[comprovacion]):
            total += 1
if total == 0:
    print('There are no peaks!')
else:
    print(total)