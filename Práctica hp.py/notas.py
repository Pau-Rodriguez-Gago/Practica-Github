notas=input().split()
redondo=input()
notas=[float(x) for x in notas]
red_notas=[round(notas,redondo) for nota in notas]
print("".join(map(str,red_notas)))